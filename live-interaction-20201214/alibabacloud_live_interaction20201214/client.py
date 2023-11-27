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

    def add_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_members_with_options(request, runtime)

    def add_group_silence_blacklist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def add_group_silence_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_blacklist_with_options(request, runtime)

    def add_group_silence_whitelist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def add_group_silence_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_whitelist_with_options(request, runtime)

    def bind_interconnection_cid_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: BindInterconnectionCidRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BindInterconnectionCidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionCidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionCid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionCidResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_interconnection_cid(self, request):
        """
        @deprecated
        

        @param request: BindInterconnectionCidRequest

        @return: BindInterconnectionCidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_interconnection_cid_with_options(request, runtime)

    def bind_interconnection_uid_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: BindInterconnectionUidRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionUidResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_interconnection_uid(self, request):
        """
        @deprecated
        

        @param request: BindInterconnectionUidRequest

        @return: BindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_interconnection_uid_with_options(request, runtime)

    def cancel_silence_all_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CancelSilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelSilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_silence_all_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_silence_all_group_members_with_options(request, runtime)

    def create_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CreateGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_room_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateRoomRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRoomResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def create_room(self, request):
        """
        @deprecated
        

        @param request: CreateRoomRequest

        @return: CreateRoomResponse
        Deprecated
        """
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
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def destroy_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def destroy_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_room_with_options(request, runtime)

    def dismiss_group_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: DismissGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DismissGroupResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DismissGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def dismiss_group(self, request):
        """
        @deprecated
        

        @param request: DismissGroupRequest

        @return: DismissGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.dismiss_group_with_options(request, runtime)

    def get_common_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCommonConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_common_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_common_config_with_options(request, runtime)

    def get_group_by_id_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_by_id_with_options(request, runtime)

    def get_group_member_by_ids_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: GetGroupMemberByIdsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupMemberByIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_member_by_ids(self, request):
        """
        @deprecated
        

        @param request: GetGroupMemberByIdsRequest

        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_group_member_by_ids_with_options(request, runtime)

    def get_imconfig_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetIMConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetIMConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIMConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_imconfig(self, request):
        """
        @deprecated
        

        @param request: GetIMConfigRequest

        @return: GetIMConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_imconfig_with_options(request, runtime)

    def get_login_token_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_login_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    def get_media_upload_url_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUploadUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUploadUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_upload_url_with_options(request, runtime)

    def get_media_url_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_url_with_options(request, runtime)

    def get_message_by_id_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMessageByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_by_id_with_options(request, runtime)

    def get_room_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoomStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_room_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_room_statistics_with_options(request, runtime)

    def get_user_mute_setting_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: GetUserMuteSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetUserMuteSettingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserMuteSetting',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_mute_setting(self, request):
        """
        @deprecated
        

        @param request: GetUserMuteSettingRequest

        @return: GetUserMuteSettingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_mute_setting_with_options(request, runtime)

    def import_group_chat_conversation_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            self.call_api(params, req, runtime)
        )

    def import_group_chat_conversation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_conversation_with_options(request, runtime)

    def import_group_chat_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatMember',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def import_group_chat_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_member_with_options(request, runtime)

    def import_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def import_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_message_with_options(request, runtime)

    def import_single_conversation_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportSingleConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSingleConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            self.call_api(params, req, runtime)
        )

    def import_single_conversation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_single_conversation_with_options(request, runtime)

    def init_tenant_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: InitTenantRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InitTenantResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitTenant',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def init_tenant(self, request):
        """
        @deprecated
        

        @param request: InitTenantRequest

        @return: InitTenantResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.init_tenant_with_options(request, runtime)

    def kick_off_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.KickOffShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickOff',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            self.call_api(params, req, runtime)
        )

    def kick_off(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kick_off_with_options(request, runtime)

    def list_app_infos_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: ListAppInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAppInfosResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInfos',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_infos(self, request):
        """
        @deprecated
        

        @param request: ListAppInfosRequest

        @return: ListAppInfosResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_infos_with_options(request, runtime)

    def list_callback_api_ids_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCallbackApiIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_callback_api_ids(self):
        runtime = util_models.RuntimeOptions()
        return self.list_callback_api_ids_with_options(runtime)

    def list_detail_report_statistics_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListDetailReportStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDetailReportStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_detail_report_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_detail_report_statistics_with_options(request, runtime)

    def list_group_all_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupAllMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupAllMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_all_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_all_members_with_options(request, runtime)

    def list_group_silence_members_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: ListGroupSilenceMembersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupSilenceMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_silence_members(self, request):
        """
        @deprecated
        

        @param request: ListGroupSilenceMembersRequest

        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_group_silence_members_with_options(request, runtime)

    def list_room_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomMessages',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_room_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_messages_with_options(request, runtime)

    def list_room_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_room_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_users_with_options(request, runtime)

    def mute_users_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: MuteUsersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MuteUsersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MuteUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def mute_users(self, request):
        """
        @deprecated
        

        @param request: MuteUsersRequest

        @return: MuteUsersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.mute_users_with_options(request, runtime)

    def query_interconnection_cid_mapping_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: QueryInterconnectionCidMappingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.QueryInterconnectionCidMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInterconnectionCidMapping',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.QueryInterconnectionCidMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def query_interconnection_cid_mapping(self, request):
        """
        @deprecated
        

        @param request: QueryInterconnectionCidMappingRequest

        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.query_interconnection_cid_mapping_with_options(request, runtime)

    def recall_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RecallMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def recall_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recall_message_with_options(request, runtime)

    def remove_group_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_group_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_extension_by_keys_with_options(request, runtime)

    def remove_group_member_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_group_member_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_member_extension_by_keys_with_options(request, runtime)

    def remove_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_members_with_options(request, runtime)

    def remove_group_silence_blacklist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_group_silence_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_blacklist_with_options(request, runtime)

    def remove_group_silence_whitelist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_group_silence_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_whitelist_with_options(request, runtime)

    def remove_message_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_message_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_message_extension_by_keys_with_options(request, runtime)

    def remove_single_chat_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_single_chat_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_single_chat_extension_by_keys_with_options(request, runtime)

    def remove_user_conversation_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_conversation_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_conversation_extension_by_keys_with_options(request, runtime)

    def send_custom_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_custom_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_with_options(request, runtime)

    def send_custom_message_to_room_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.receivers):
            body_flat['Receivers'] = request.receivers
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def send_custom_message_to_room_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_room_users_with_options(request, runtime)

    def send_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    def set_group_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def set_group_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_extension_by_keys_with_options(request, runtime)

    def set_group_member_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def set_group_member_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_member_extension_by_keys_with_options(request, runtime)

    def set_group_owner_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupOwnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupOwner',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def set_group_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_owner_with_options(request, runtime)

    def set_message_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def set_message_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_message_extension_by_keys_with_options(request, runtime)

    def set_message_read_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageReadShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageRead',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            self.call_api(params, req, runtime)
        )

    def set_message_read(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_message_read_with_options(request, runtime)

    def set_single_chat_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def set_single_chat_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_single_chat_extension_by_keys_with_options(request, runtime)

    def set_user_conversation_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_conversation_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_conversation_extension_by_keys_with_options(request, runtime)

    def silence_all_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def silence_all_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.silence_all_group_members_with_options(request, runtime)

    def unbind_interconnection_uid_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: UnbindInterconnectionUidRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UnbindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UnbindInterconnectionUidResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_interconnection_uid(self, request):
        """
        @deprecated
        

        @param request: UnbindInterconnectionUidRequest

        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_interconnection_uid_with_options(request, runtime)

    def update_app_name_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_name_with_options(request, runtime)

    def update_app_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_status_with_options(request, runtime)

    def update_callback_config_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: UpdateCallbackConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCallbackConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_callback_config(self, request):
        """
        @deprecated
        

        @param request: UpdateCallbackConfigRequest

        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_callback_config_with_options(request, runtime)

    def update_group_icon_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupIconShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupIcon',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_icon(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_icon_with_options(request, runtime)

    def update_group_members_role_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupMembersRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMembersRole',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_members_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_members_role_with_options(request, runtime)

    def update_group_title_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupTitleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupTitle',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_title(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_title_with_options(request, runtime)

    def update_msg_recall_interval_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateMsgRecallIntervalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMsgRecallInterval',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            self.call_api(params, req, runtime)
        )

    def update_msg_recall_interval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_msg_recall_interval_with_options(request, runtime)

    def update_tenant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenantStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_tenant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_tenant_status_with_options(request, runtime)
