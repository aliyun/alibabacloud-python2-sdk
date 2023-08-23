# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligeniessp_1_0 import models as ali_geniessp__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_and_remove_favorite_content_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_add_and_remove_favorite_content_request):
            request.open_add_and_remove_favorite_content_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_add_and_remove_favorite_content_request, 'OpenAddAndRemoveFavoriteContentRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_add_and_remove_favorite_content_request_shrink):
            body['OpenAddAndRemoveFavoriteContentRequest'] = request.open_add_and_remove_favorite_content_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAndRemoveFavoriteContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/AddAndRemoveFavoriteContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddAndRemoveFavoriteContentResponse(),
            self.call_api(params, req, runtime)
        )

    def add_and_remove_favorite_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddAndRemoveFavoriteContentHeaders()
        return self.add_and_remove_favorite_content_with_options(request, headers, runtime)

    def add_sub_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AddSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_subscription_info_request):
            request.add_subscription_info_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_subscription_info_request, 'AddSubscriptionInfoRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_subscription_info_request_shrink):
            query['AddSubscriptionInfoRequest'] = request.add_subscription_info_request_shrink
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/addSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AddSubResponse(),
            self.call_api(params, req, runtime)
        )

    def add_sub(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AddSubHeaders()
        return self.add_sub_with_options(request, headers, runtime)

    def auth_login_with_aligenie_user_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encrypted_aligenie_user_identifier):
            body['EncryptedAligenieUserIdentifier'] = request.encrypted_aligenie_user_identifier
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthLoginWithAligenieUserInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/authLoginWithAligenieUserInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AuthLoginWithAligenieUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def auth_login_with_aligenie_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AuthLoginWithAligenieUserInfoHeaders()
        return self.auth_login_with_aligenie_user_info_with_options(request, headers, runtime)

    def auth_login_with_aligenie_user_info_generated_by_phone_number_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/authLoginWithAligenieUserInfoGeneratedByPhoneNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def auth_login_with_aligenie_user_info_generated_by_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders()
        return self.auth_login_with_aligenie_user_info_generated_by_phone_number_with_options(request, headers, runtime)

    def auth_login_with_taobao_user_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encrypted_taobao_user_identifier):
            body['EncryptedTaobaoUserIdentifier'] = request.encrypted_taobao_user_identifier
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthLoginWithTaobaoUserInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/authLoginWithTaobaoUserInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AuthLoginWithTaobaoUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def auth_login_with_taobao_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AuthLoginWithTaobaoUserInfoHeaders()
        return self.auth_login_with_taobao_user_info_with_options(request, headers, runtime)

    def auth_login_with_third_user_info_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.AuthLoginWithThirdUserInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        if not UtilClient.is_unset(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.third_user_identifier):
            body['ThirdUserIdentifier'] = request.third_user_identifier
        if not UtilClient.is_unset(request.third_user_type):
            body['ThirdUserType'] = request.third_user_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthLoginWithThirdUserInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/authLoginWithThirdUserInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.AuthLoginWithThirdUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def auth_login_with_third_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.AuthLoginWithThirdUserInfoHeaders()
        return self.auth_login_with_third_user_info_with_options(request, headers, runtime)

    def check_and_do_voip_call_for_hotel_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CheckAndDoVoipCallForHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_data):
            body['BizData'] = request.biz_data
        if not UtilClient.is_unset(request.callee_nick):
            body['CalleeNick'] = request.callee_nick
        if not UtilClient.is_unset(request.callee_phone_num):
            body['CalleePhoneNum'] = request.callee_phone_num
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckAndDoVoipCallForHotel',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/checkAndDoVoipCallForHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CheckAndDoVoipCallForHotelResponse(),
            self.call_api(params, req, runtime)
        )

    def check_and_do_voip_call_for_hotel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CheckAndDoVoipCallForHotelHeaders()
        return self.check_and_do_voip_call_for_hotel_with_options(request, headers, runtime)

    def check_auth_code_bind_for_ext_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CheckAuthCodeBindForExtShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAuthCodeBindForExt',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/checkAuthCodeBindForExt',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CheckAuthCodeBindForExtResponse(),
            self.call_api(params, req, runtime)
        )

    def check_auth_code_bind_for_ext(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CheckAuthCodeBindForExtHeaders()
        return self.check_auth_code_bind_for_ext_with_options(request, headers, runtime)

    def cloud_player_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CloudPlayerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.song_id_list):
            request.song_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.song_id_list, 'SongIdList', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.cur_play_index):
            query['CurPlayIndex'] = request.cur_play_index
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.play_mode):
            query['PlayMode'] = request.play_mode
        if not UtilClient.is_unset(request.song_id):
            query['SongId'] = request.song_id
        if not UtilClient.is_unset(request.song_id_list_shrink):
            query['SongIdList'] = request.song_id_list_shrink
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloudPlayer',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/cloud/player',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CloudPlayerResponse(),
            self.call_api(params, req, runtime)
        )

    def cloud_player(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CloudPlayerHeaders()
        return self.cloud_player_with_options(request, headers, runtime)

    def create_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/createAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateAlarmHeaders()
        return self.create_alarm_with_options(request, headers, runtime)

    def create_playing_list_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreatePlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/CreatePlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreatePlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    def create_playing_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreatePlayingListHeaders()
        return self.create_playing_list_with_options(request, headers, runtime)

    def create_schedule_task_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.CreateScheduleTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/CreateScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.CreateScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedule_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.CreateScheduleTaskHeaders()
        return self.create_schedule_task_with_options(request, headers, runtime)

    def delete_alarms_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteAlarmsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/deleteAlarms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteAlarmsHeaders()
        return self.delete_alarms_with_options(request, headers, runtime)

    def delete_schedule_task_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeleteScheduleTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/DeleteScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_schedule_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteScheduleTaskHeaders()
        return self.delete_schedule_task_with_options(request, headers, runtime)

    def delete_sub_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/deleteSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeleteSubResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sub(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeleteSubHeaders()
        return self.delete_sub_with_options(request, headers, runtime)

    def device_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.control_request):
            request.control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.control_request, 'ControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.control_request_shrink):
            body['ControlRequest'] = request.control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/control',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    def device_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    def ecology_openness_authenticate_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EcologyOpennessAuthenticate',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ecologyOpennessAuthenticate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.EcologyOpennessAuthenticateResponse(),
            self.call_api(params, req, runtime)
        )

    def ecology_openness_authenticate(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.EcologyOpennessAuthenticateHeaders()
        return self.ecology_openness_authenticate_with_options(request, headers, runtime)

    def ecology_openness_send_verification_code_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EcologyOpennessSendVerificationCode',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ecologyOpennessSendVerificationCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.EcologyOpennessSendVerificationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def ecology_openness_send_verification_code(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.EcologyOpennessSendVerificationCodeHeaders()
        return self.ecology_openness_send_verification_code_with_options(request, headers, runtime)

    def find_userlist_to_auth_login_with_phone_number_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindUserlistToAuthLoginWithPhoneNumber',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/findUserlistToAuthLoginWithPhoneNumber',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.FindUserlistToAuthLoginWithPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def find_userlist_to_auth_login_with_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.FindUserlistToAuthLoginWithPhoneNumberHeaders()
        return self.find_userlist_to_auth_login_with_phone_number_with_options(request, headers, runtime)

    def get_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlarmHeaders()
        return self.get_alarm_with_options(request, headers, runtime)

    def get_album_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    def get_album(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumHeaders()
        return self.get_album_with_options(request, headers, runtime)

    def get_album_detail_by_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.album_id):
            query['AlbumId'] = request.album_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlbumDetailById',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getAlbumDetailById',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAlbumDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_album_detail_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAlbumDetailByIdHeaders()
        return self.get_album_detail_by_id_with_options(request, headers, runtime)

    def get_aligenie_user_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.login_state_access_token):
            query['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAligenieUserInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getAligenieUserInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetAligenieUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aligenie_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetAligenieUserInfoHeaders()
        return self.get_aligenie_user_info_with_options(request, headers, runtime)

    def get_code_enhance_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCodeEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeEnhance',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getCodeEnhance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCodeEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_code_enhance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCodeEnhanceHeaders()
        return self.get_code_enhance_with_options(request, headers, runtime)

    def get_content_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetContentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetContentHeaders()
        return self.get_content_with_options(request, headers, runtime)

    def get_current_playing_item_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCurrentPlayingItem',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetCurrentPlayingItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingItemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_current_playing_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingItemHeaders()
        return self.get_current_playing_item_with_options(request, headers, runtime)

    def get_current_playing_list_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetCurrentPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_query_play_list_request):
            request.open_query_play_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_query_play_list_request, 'OpenQueryPlayListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_query_play_list_request_shrink):
            body['OpenQueryPlayListRequest'] = request.open_query_play_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCurrentPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetCurrentPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetCurrentPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_current_playing_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetCurrentPlayingListHeaders()
        return self.get_current_playing_list_with_options(request, headers, runtime)

    def get_device_basic_info_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_basic_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceBasicInfoHeaders()
        return self.get_device_basic_info_with_options(request, headers, runtime)

    def get_device_id_by_identity_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceIdByIdentity',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceIdByIdentity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_id_by_identity(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders()
        return self.get_device_id_by_identity_with_options(request, headers, runtime)

    def get_device_setting_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceSetting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceSettingHeaders()
        return self.get_device_setting_with_options(request, headers, runtime)

    def get_device_status_detail_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceStatusDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceStatusDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_status_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusDetailHeaders()
        return self.get_device_status_detail_with_options(request, headers, runtime)

    def get_device_status_info_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceStatusInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceStatusInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceStatusInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceStatusInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_status_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceStatusInfoHeaders()
        return self.get_device_status_info_with_options(request, headers, runtime)

    def get_device_tag_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetDeviceTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceTag',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getDeviceTag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_tag(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceTagHeaders()
        return self.get_device_tag_with_options(request, headers, runtime)

    def get_schedule_task_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetScheduleTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScheduleTask',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetScheduleTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetScheduleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_schedule_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetScheduleTaskHeaders()
        return self.get_schedule_task_with_options(request, headers, runtime)

    def get_unread_message_count_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUnreadMessageCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUnreadMessageCount',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getUnreadMessageCount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUnreadMessageCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_unread_message_count(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUnreadMessageCountHeaders()
        return self.get_unread_message_count_with_options(request, headers, runtime)

    def get_user_by_device_id_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetUserByDeviceIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserByDeviceId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/getUserByDeviceId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetUserByDeviceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_by_device_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetUserByDeviceIdHeaders()
        return self.get_user_by_device_id_with_options(request, headers, runtime)

    def get_weather_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.GetWeatherShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeather',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/GetWeather',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetWeatherResponse(),
            self.call_api(params, req, runtime)
        )

    def get_weather(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetWeatherHeaders()
        return self.get_weather_with_options(request, headers, runtime)

    def index_control_playing_list_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.IndexControlPlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_index_control_request):
            request.open_index_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_index_control_request, 'OpenIndexControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_index_control_request_shrink):
            body['OpenIndexControlRequest'] = request.open_index_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IndexControlPlayingList',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/IndexControlPlayingList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.IndexControlPlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    def index_control_playing_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.IndexControlPlayingListHeaders()
        return self.index_control_playing_list_with_options(request, headers, runtime)

    def list_alarms_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlarmsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlarms',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlarmsHeaders()
        return self.list_alarms_with_options(request, headers, runtime)

    def list_album_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlbumDetail',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListAlbumDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def list_album_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumDetailHeaders()
        return self.list_album_detail_with_options(request, headers, runtime)

    def list_album_is_added_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListAlbumIsAddedShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.album_id_list):
            request.album_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.album_id_list, 'AlbumIdList', 'json')
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.album_id_list_shrink):
            query['AlbumIdList'] = request.album_id_list_shrink
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlbumIsAdded',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listAlbumIsAdded',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListAlbumIsAddedResponse(),
            self.call_api(params, req, runtime)
        )

    def list_album_is_added(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListAlbumIsAddedHeaders()
        return self.list_album_is_added_with_options(request, headers, runtime)

    def list_cate_content_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListCateContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCateContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListCateContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateContentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cate_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateContentHeaders()
        return self.list_cate_content_with_options(request, headers, runtime)

    def list_cate_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCateInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListCateInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cate_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCateInfoHeaders()
        return self.list_cate_info_with_options(request, headers, runtime)

    def list_common_cate_first_floor_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommonCateFirstFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListCommonCateFirstFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateFirstFloorResponse(),
            self.call_api(params, req, runtime)
        )

    def list_common_cate_first_floor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateFirstFloorHeaders()
        return self.list_common_cate_first_floor_with_options(request, headers, runtime)

    def list_common_cate_second_floor_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_cate_id):
            query['ParentCateId'] = request.parent_cate_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommonCateSecondFloor',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListCommonCateSecondFloor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListCommonCateSecondFloorResponse(),
            self.call_api(params, req, runtime)
        )

    def list_common_cate_second_floor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListCommonCateSecondFloorHeaders()
        return self.list_common_cate_second_floor_with_options(request, headers, runtime)

    def list_device_basic_info_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_infos):
            request.device_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_infos, 'DeviceInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_infos_shrink):
            query['DeviceInfos'] = request.device_infos_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceBasicInfo',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listDeviceBasicInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_basic_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceBasicInfoHeaders()
        return self.list_device_basic_info_with_options(request, headers, runtime)

    def list_device_by_user_id_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceByUserId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listDeviceByUserId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdHeaders()
        return self.list_device_by_user_id_with_options(request, headers, runtime)

    def list_device_by_user_id_and_chanel_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.channel_info):
            request.channel_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_info, 'ChannelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_info_shrink):
            query['ChannelInfo'] = request.channel_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceByUserIdAndChanel',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listDeviceByUserIdAndChanel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_by_user_id_and_chanel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceByUserIdAndChanelHeaders()
        return self.list_device_by_user_id_and_chanel_with_options(request, headers, runtime)

    def list_device_id_by_identities_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.identity_ids):
            request.identity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.identity_ids, 'IdentityIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_ids_shrink):
            query['IdentityIds'] = request.identity_ids_shrink
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceIdByIdentities',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listDeviceIdByIdentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListDeviceIdByIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_id_by_identities(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListDeviceIdByIdentitiesHeaders()
        return self.list_device_id_by_identities_with_options(request, headers, runtime)

    def list_music_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListMusicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMusic',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListMusicResponse(),
            self.call_api(params, req, runtime)
        )

    def list_music(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListMusicHeaders()
        return self.list_music_with_options(request, headers, runtime)

    def list_play_history_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListPlayHistoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlayHistory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListPlayHistory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListPlayHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_play_history(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListPlayHistoryHeaders()
        return self.list_play_history_with_options(request, headers, runtime)

    def list_recommend_content_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListRecommendContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecommendContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ListRecommendContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListRecommendContentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_recommend_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListRecommendContentHeaders()
        return self.list_recommend_content_with_options(request, headers, runtime)

    def list_sub_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSub',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listSub',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sub(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubHeaders()
        return self.list_sub_with_options(request, headers, runtime)

    def list_sub_album_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListSubAlbumShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.query_subscription_album_request):
            request.query_subscription_album_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_subscription_album_request, 'QuerySubscriptionAlbumRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.query_subscription_album_request_shrink):
            query['QuerySubscriptionAlbumRequest'] = request.query_subscription_album_request_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubAlbum',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listSubAlbum',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubAlbumResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sub_album(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubAlbumHeaders()
        return self.list_sub_album_with_options(request, headers, runtime)

    def list_subscription_album_category_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionAlbumCategory',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listSubscriptionAlbumCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subscription_album_category(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListSubscriptionAlbumCategoryHeaders()
        return self.list_subscription_album_category_with_options(request, headers, runtime)

    def list_user_message_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ListUserMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.before_time):
            query['BeforeTime'] = request.before_time
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/listUserMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ListUserMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ListUserMessageHeaders()
        return self.list_user_message_with_options(request, headers, runtime)

    def play_and_pause_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayAndPauseControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_and_pause_control_param):
            request.open_play_and_pause_control_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_play_and_pause_control_param, 'OpenPlayAndPauseControlParam', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_and_pause_control_param_shrink):
            body['OpenPlayAndPauseControlParam'] = request.open_play_and_pause_control_param_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayAndPauseControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/PlayAndPauseControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayAndPauseControlResponse(),
            self.call_api(params, req, runtime)
        )

    def play_and_pause_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayAndPauseControlHeaders()
        return self.play_and_pause_control_with_options(request, headers, runtime)

    def play_mode_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PlayModeControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_play_mode_control_request):
            request.open_play_mode_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_play_mode_control_request, 'OpenPlayModeControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_play_mode_control_request_shrink):
            body['OpenPlayModeControlRequest'] = request.open_play_mode_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PlayModeControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/PlayModeControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PlayModeControlResponse(),
            self.call_api(params, req, runtime)
        )

    def play_mode_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PlayModeControlHeaders()
        return self.play_mode_control_with_options(request, headers, runtime)

    def previous_and_next_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.PreviousAndNextControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_control_playing_list_request):
            request.open_control_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_control_playing_list_request, 'OpenControlPlayingListRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_control_playing_list_request_shrink):
            body['OpenControlPlayingListRequest'] = request.open_control_playing_list_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreviousAndNextControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/PreviousAndNextControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.PreviousAndNextControlResponse(),
            self.call_api(params, req, runtime)
        )

    def previous_and_next_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.PreviousAndNextControlHeaders()
        return self.previous_and_next_control_with_options(request, headers, runtime)

    def progress_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ProgressControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_progress_control_request):
            request.open_progress_control_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_progress_control_request, 'OpenProgressControlRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_progress_control_request_shrink):
            body['OpenProgressControlRequest'] = request.open_progress_control_request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProgressControl',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/ProgressControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ProgressControlResponse(),
            self.call_api(params, req, runtime)
        )

    def progress_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ProgressControlHeaders()
        return self.progress_control_with_options(request, headers, runtime)

    def query_music_type_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.QueryMusicTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMusicType',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/queryMusicType',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.QueryMusicTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_music_type(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.QueryMusicTypeHeaders()
        return self.query_music_type_with_options(request, headers, runtime)

    def query_user_device_list_by_tme_user_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sp):
            query['Sp'] = request.sp
        if not UtilClient.is_unset(request.tme_user_id):
            query['TmeUserId'] = request.tme_user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDeviceListByTmeUserId',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/queryUserDeviceListByTmeUserId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.QueryUserDeviceListByTmeUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_device_list_by_tme_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.QueryUserDeviceListByTmeUserIdHeaders()
        return self.query_user_device_list_by_tme_user_id_with_options(request, headers, runtime)

    def read_message_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ReadMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/readMessage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ReadMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def read_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ReadMessageHeaders()
        return self.read_message_with_options(request, headers, runtime)

    def scan_code_bind_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ScanCodeBindShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bind_req):
            request.bind_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bind_req, 'BindReq', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.bind_req_shrink):
            body['BindReq'] = request.bind_req_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanCodeBind',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/scanCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ScanCodeBindResponse(),
            self.call_api(params, req, runtime)
        )

    def scan_code_bind(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ScanCodeBindHeaders()
        return self.scan_code_bind_with_options(request, headers, runtime)

    def scg_search_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.ScgSearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scg_filter):
            request.scg_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scg_filter, 'ScgFilter', 'json')
        query = {}
        if not UtilClient.is_unset(request.scg_filter_shrink):
            query['ScgFilter'] = request.scg_filter_shrink
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScgSearch',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/scgSearch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.ScgSearchResponse(),
            self.call_api(params, req, runtime)
        )

    def scg_search(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.ScgSearchHeaders()
        return self.scg_search_with_options(request, headers, runtime)

    def search_content_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SearchContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchContent',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/SearchContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SearchContentResponse(),
            self.call_api(params, req, runtime)
        )

    def search_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SearchContentHeaders()
        return self.search_content_with_options(request, headers, runtime)

    def send_message_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SendMessageHeaders()
        return self.send_message_with_options(request, headers, runtime)

    def set_device_setting_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.SetDeviceSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceSetting',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/setDeviceSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.SetDeviceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.SetDeviceSettingHeaders()
        return self.set_device_setting_with_options(request, headers, runtime)

    def unbind_aligenie_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.login_state_access_token):
            body['LoginStateAccessToken'] = request.login_state_access_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindAligenieUser',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/unbindAligenieUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UnbindAligenieUserResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_aligenie_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UnbindAligenieUserHeaders()
        return self.unbind_aligenie_user_with_options(request, headers, runtime)

    def unbind_device_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UnbindDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindDevice',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/unbindDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UnbindDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UnbindDeviceHeaders()
        return self.unbind_device_with_options(request, headers, runtime)

    def update_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_geniessp__1__0_models.UpdateAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlarm',
            version='ssp_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ssp/updateAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.UpdateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.UpdateAlarmHeaders()
        return self.update_alarm_with_options(request, headers, runtime)
