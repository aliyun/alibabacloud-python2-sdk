# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieip_1_0 import models as ali_genieip__1__0_models
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

    def add_cartoon_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.start_video_md_5):
            body['StartVideoMd5'] = request.start_video_md_5
        if not UtilClient.is_unset(request.start_video_url):
            body['StartVideoUrl'] = request.start_video_url
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
            action='AddCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cartoon(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCartoonHeaders()
        return self.add_cartoon_with_options(request, headers, runtime)

    def add_custom_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
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
            action='AddCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    def add_custom_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCustomQAHeaders()
        return self.add_custom_qawith_options(request, headers, runtime)

    def add_message_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='AddMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_message_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddMessageTemplateHeaders()
        return self.add_message_template_with_options(request, headers, runtime)

    def add_or_update_dis_play_modes_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateDisPlayModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='AddOrUpdateDisPlayModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addOrUpdateDisPlayModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_or_update_dis_play_modes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateDisPlayModesHeaders()
        return self.add_or_update_dis_play_modes_with_options(request, headers, runtime)

    def add_or_update_hotel_setting_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateHotelSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        if not UtilClient.is_unset(tmp_req.night_mode):
            request.night_mode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.night_mode, 'NightMode', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        if not UtilClient.is_unset(request.night_mode_shrink):
            body['NightMode'] = request.night_mode_shrink
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
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
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addOrUpdateHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def add_or_update_hotel_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateHotelSettingHeaders()
        return self.add_or_update_hotel_setting_with_options(request, headers, runtime)

    def add_or_update_screen_saver_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
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
            action='AddOrUpdateScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addOrUpdateScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse(),
            self.call_api(params, req, runtime)
        )

    def add_or_update_screen_saver(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateScreenSaverHeaders()
        return self.add_or_update_screen_saver_with_options(request, headers, runtime)

    def add_or_update_welcome_text_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_url):
            body['MusicUrl'] = request.music_url
        if not UtilClient.is_unset(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
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
            action='AddOrUpdateWelcomeText',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/addOrUpdateWelcomeText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse(),
            self.call_api(params, req, runtime)
        )

    def add_or_update_welcome_text(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateWelcomeTextHeaders()
        return self.add_or_update_welcome_text_with_options(request, headers, runtime)

    def audit_hotel_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AuditHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.audit_hotel_req):
            request.audit_hotel_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audit_hotel_req, 'AuditHotelReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_hotel_req_shrink):
            query['AuditHotelReq'] = request.audit_hotel_req_shrink
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
            action='AuditHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/auditHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.AuditHotelResponse(),
            self.call_api(params, req, runtime)
        )

    def audit_hotel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AuditHotelHeaders()
        return self.audit_hotel_with_options(request, headers, runtime)

    def batch_add_hotel_room_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchAddHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
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
            action='BatchAddHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/batchAddHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_hotel_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchAddHotelRoomHeaders()
        return self.batch_add_hotel_room_with_options(request, headers, runtime)

    def batch_delete_hotel_room_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchDeleteHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
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
            action='BatchDeleteHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/batchDeleteHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_hotel_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders()
        return self.batch_delete_hotel_room_with_options(request, headers, runtime)

    def checkout_with_akwith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
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
            action='CheckoutWithAK',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/checkoutWithAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CheckoutWithAKResponse(),
            self.call_api(params, req, runtime)
        )

    def checkout_with_ak(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CheckoutWithAKHeaders()
        return self.checkout_with_akwith_options(request, headers, runtime)

    def child_account_auth_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
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
            action='ChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/childAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ChildAccountAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def child_account_auth(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ChildAccountAuthHeaders()
        return self.child_account_auth_with_options(request, headers, runtime)

    def control_room_device_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ControlRoomDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not UtilClient.is_unset(request.cmd):
            body['Cmd'] = request.cmd
        if not UtilClient.is_unset(request.device_index):
            body['DeviceIndex'] = request.device_index
        if not UtilClient.is_unset(request.device_number):
            body['DeviceNumber'] = request.device_number
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
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
            action='ControlRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/controlRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ControlRoomDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def control_room_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ControlRoomDeviceHeaders()
        return self.control_room_device_with_options(request, headers, runtime)

    def create_hotel_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pk):
            body['RelatedPk'] = request.related_pk
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
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
            action='CreateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/createHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CreateHotelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hotel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelHeaders()
        return self.create_hotel_with_options(request, headers, runtime)

    def create_hotel_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_type):
            body['MusicType'] = request.music_type
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
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
            action='CreateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/createHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CreateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hotel_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelAlarmHeaders()
        return self.create_hotel_alarm_with_options(request, headers, runtime)

    def create_rcu_scene_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
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
            action='CreateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/createRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.CreateRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rcu_scene(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateRcuSceneHeaders()
        return self.create_rcu_scene_with_options(request, headers, runtime)

    def delete_cartoon_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='DeleteCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cartoon(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCartoonHeaders()
        return self.delete_cartoon_with_options(request, headers, runtime)

    def delete_custom_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_qaids):
            request.custom_qaids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_qaids, 'CustomQAIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.custom_qaids_shrink):
            body['CustomQAIds'] = request.custom_qaids_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='DeleteCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCustomQAHeaders()
        return self.delete_custom_qawith_options(request, headers, runtime)

    def delete_hotel_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='DeleteHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hotel_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelAlarmHeaders()
        return self.delete_hotel_alarm_with_options(request, headers, runtime)

    def delete_hotel_scene_book_item_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
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
            action='DeleteHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hotel_scene_book_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSceneBookItemHeaders()
        return self.delete_hotel_scene_book_item_with_options(request, headers, runtime)

    def delete_hotel_setting_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
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
            action='DeleteHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hotel_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSettingHeaders()
        return self.delete_hotel_setting_with_options(request, headers, runtime)

    def delete_message_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
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
            action='DeleteMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_message_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteMessageTemplateHeaders()
        return self.delete_message_template_with_options(request, headers, runtime)

    def delete_rcu_scene_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
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
            action='DeleteRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deleteRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeleteRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rcu_scene(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteRcuSceneHeaders()
        return self.delete_rcu_scene_with_options(request, headers, runtime)

    def device_control_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='DeviceControl',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/deviceControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.DeviceControlResponse(),
            self.call_api(params, req, runtime)
        )

    def device_control(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    def get_basic_info_qawith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='GetBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetBasicInfoQAResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_info_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetBasicInfoQAHeaders()
        return self.get_basic_info_qawith_options(request, headers, runtime)

    def get_cartoon_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='GetCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetCartoonResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cartoon(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetCartoonHeaders()
        return self.get_cartoon_with_options(request, headers, runtime)

    def get_hotel_contact_by_genie_device_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByGenieDeviceShrinkRequest()
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
            action='GetHotelContactByGenieDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelContactByGenieDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_contact_by_genie_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByGenieDeviceHeaders()
        return self.get_hotel_contact_by_genie_device_with_options(request, headers, runtime)

    def get_hotel_contact_by_number_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
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
            action='GetHotelContactByNumber',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelContactByNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelContactByNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_contact_by_number(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByNumberHeaders()
        return self.get_hotel_contact_by_number_with_options(request, headers, runtime)

    def get_hotel_contacts_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactsShrinkRequest()
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
            action='GetHotelContacts',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelContacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactsHeaders()
        return self.get_hotel_contacts_with_options(request, headers, runtime)

    def get_hotel_home_back_image_and_modes_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesShrinkRequest()
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
            action='GetHotelHomeBackImageAndModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelHomeBackImageAndModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_home_back_image_and_modes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders()
        return self.get_hotel_home_back_image_and_modes_with_options(request, headers, runtime)

    def get_hotel_notice_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeShrinkRequest()
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
            action='GetHotelNotice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_notice(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeHeaders()
        return self.get_hotel_notice_with_options(request, headers, runtime)

    def get_hotel_notice_v2with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeV2ShrinkRequest()
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
            action='GetHotelNoticeV2',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelNoticeV2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelNoticeV2Response(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_notice_v2(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeV2Headers()
        return self.get_hotel_notice_v2with_options(request, headers, runtime)

    def get_hotel_order_detail_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelOrderDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='GetHotelOrderDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelOrderDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelOrderDetailHeaders()
        return self.get_hotel_order_detail_with_options(request, headers, runtime)

    def get_hotel_room_device_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='GetHotelRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_room_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelRoomDeviceHeaders()
        return self.get_hotel_room_device_with_options(request, headers, runtime)

    def get_hotel_sample_utterances_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelSampleUtterancesShrinkRequest()
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
            action='GetHotelSampleUtterances',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelSampleUtterances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_sample_utterances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders()
        return self.get_hotel_sample_utterances_with_options(request, headers, runtime)

    def get_hotel_scene_item_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
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
            action='GetHotelSceneItemDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelSceneItemDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelSceneItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_scene_item_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSceneItemDetailHeaders()
        return self.get_hotel_scene_item_detail_with_options(request, headers, runtime)

    def get_hotel_screen_saver_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelScreenSaverShrinkRequest()
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
            action='GetHotelScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_screen_saver(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverHeaders()
        return self.get_hotel_screen_saver_with_options(request, headers, runtime)

    def get_hotel_screen_saver_style_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='GetHotelScreenSaverStyle',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelScreenSaverStyle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_screen_saver_style(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverStyleHeaders()
        return self.get_hotel_screen_saver_style_with_options(request, headers, runtime)

    def get_hotel_setting_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
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
            action='GetHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetHotelSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotel_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSettingHeaders()
        return self.get_hotel_setting_with_options(request, headers, runtime)

    def get_relation_product_list_with_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetRelationProductList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getRelationProductList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetRelationProductListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_relation_product_list(self):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetRelationProductListHeaders()
        return self.get_relation_product_list_with_options(headers, runtime)

    def get_union_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.id_type):
            body['IdType'] = request.id_type
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
            action='GetUnionId',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getUnionId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetUnionIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_union_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetUnionIdHeaders()
        return self.get_union_id_with_options(request, headers, runtime)

    def get_welcome_text_and_music_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='GetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    def get_welcome_text_and_music(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetWelcomeTextAndMusicHeaders()
        return self.get_welcome_text_and_music_with_options(request, headers, runtime)

    def hotel_qr_bind_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
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
            action='HotelQrBind',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/hotelQrBind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.HotelQrBindResponse(),
            self.call_api(params, req, runtime)
        )

    def hotel_qr_bind(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.HotelQrBindHeaders()
        return self.hotel_qr_bind_with_options(request, headers, runtime)

    def import_hotel_config_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportHotelConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_hotel_config):
            request.import_hotel_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_hotel_config, 'ImportHotelConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.import_hotel_config_shrink):
            body['ImportHotelConfig'] = request.import_hotel_config_shrink
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
            action='ImportHotelConfig',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/importHotelConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ImportHotelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def import_hotel_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportHotelConfigHeaders()
        return self.import_hotel_config_with_options(request, headers, runtime)

    def import_room_control_devices_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomControlDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.location_devices):
            request.location_devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_infrared_device_import):
            body['EnableInfraredDeviceImport'] = request.enable_infrared_device_import
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
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
            action='ImportRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/importRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_room_control_devices(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomControlDevicesHeaders()
        return self.import_room_control_devices_with_options(request, headers, runtime)

    def import_room_genie_scenes_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomGenieScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_list):
            request.scene_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_list, 'SceneList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.scene_list_shrink):
            body['SceneList'] = request.scene_list_shrink
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
            action='ImportRoomGenieScenes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/importRoomGenieScenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ImportRoomGenieScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_room_genie_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomGenieScenesHeaders()
        return self.import_room_genie_scenes_with_options(request, headers, runtime)

    def insert_hotel_scene_book_item_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.InsertHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_hotel_scene_item_req):
            request.add_hotel_scene_item_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_hotel_scene_item_req, 'AddHotelSceneItemReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_hotel_scene_item_req_shrink):
            query['AddHotelSceneItemReq'] = request.add_hotel_scene_item_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='InsertHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/insertHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.InsertHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_hotel_scene_book_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InsertHotelSceneBookItemHeaders()
        return self.insert_hotel_scene_book_item_with_options(request, headers, runtime)

    def invoke_robot_push_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.push_type):
            body['PushType'] = request.push_type
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
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
            action='InvokeRobotPush',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/invokeRobotPush',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.InvokeRobotPushResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_robot_push(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InvokeRobotPushHeaders()
        return self.invoke_robot_push_with_options(request, headers, runtime)

    def list_all_provinces_with_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListAllProvinces',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listAllProvinces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListAllProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_all_provinces(self):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListAllProvincesHeaders()
        return self.list_all_provinces_with_options(headers, runtime)

    def list_cities_by_province_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
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
            action='ListCitiesByProvince',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listCitiesByProvince',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListCitiesByProvinceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cities_by_province(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCitiesByProvinceHeaders()
        return self.list_cities_by_province_with_options(request, headers, runtime)

    def list_custom_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
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
            action='ListCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCustomQAHeaders()
        return self.list_custom_qawith_options(request, headers, runtime)

    def list_dialogue_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='ListDialogueTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listDialogueTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListDialogueTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dialogue_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListDialogueTemplateHeaders()
        return self.list_dialogue_template_with_options(request, headers, runtime)

    def list_hotel_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
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
            action='ListHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/getHotelAlarmList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelAlarmHeaders()
        return self.list_hotel_alarm_with_options(request, headers, runtime)

    def list_hotel_control_device_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelControlDeviceShrinkRequest()
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
            action='ListHotelControlDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelControlDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_control_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelControlDeviceHeaders()
        return self.list_hotel_control_device_with_options(request, headers, runtime)

    def list_hotel_info_with_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelInfo',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_info(self):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelInfoHeaders()
        return self.list_hotel_info_with_options(headers, runtime)

    def list_hotel_message_template_with_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_message_template(self):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelMessageTemplateHeaders()
        return self.list_hotel_message_template_with_options(headers, runtime)

    def list_hotel_order_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='ListHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelOrderHeaders()
        return self.list_hotel_order_with_options(request, headers, runtime)

    def list_hotel_rooms_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='ListHotelRooms',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelRoomsHeaders()
        return self.list_hotel_rooms_with_options(request, headers, runtime)

    def list_hotel_scene_book_items_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneBookItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
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
            action='ListHotelSceneBookItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelSceneBookItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelSceneBookItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_scene_book_items(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneBookItemsHeaders()
        return self.list_hotel_scene_book_items_with_options(request, headers, runtime)

    def list_hotel_scene_item_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='ListHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelSceneItemResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_scene_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemHeaders()
        return self.list_hotel_scene_item_with_options(request, headers, runtime)

    def list_hotel_scene_items_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_hotel_scene_req):
            request.list_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_hotel_scene_req, 'ListHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.list_hotel_scene_req_shrink):
            query['ListHotelSceneReq'] = request.list_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='ListHotelSceneItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelSceneItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelSceneItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_scene_items(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemsHeaders()
        return self.list_hotel_scene_items_with_options(request, headers, runtime)

    def list_hotel_service_category_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelServiceCategoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='ListHotelServiceCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotelServiceCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotel_service_category(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelServiceCategoryHeaders()
        return self.list_hotel_service_category_with_options(request, headers, runtime)

    def list_hotels_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
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
            action='ListHotels',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listHotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListHotelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotels(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelsHeaders()
        return self.list_hotels_with_options(request, headers, runtime)

    def list_infrared_device_brands_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
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
            action='ListInfraredDeviceBrands',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listInfraredDeviceBrands',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_infrared_device_brands(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredDeviceBrandsHeaders()
        return self.list_infrared_device_brands_with_options(request, headers, runtime)

    def list_infrared_remote_controllers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
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
            action='ListInfraredRemoteControllers',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listInfraredRemoteControllers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListInfraredRemoteControllersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_infrared_remote_controllers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredRemoteControllersHeaders()
        return self.list_infrared_remote_controllers_with_options(request, headers, runtime)

    def list_stbservice_providers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
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
            action='ListSTBServiceProviders',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listSTBServiceProviders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListSTBServiceProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stbservice_providers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSTBServiceProvidersHeaders()
        return self.list_stbservice_providers_with_options(request, headers, runtime)

    def list_scene_category_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
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
            action='ListSceneCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listSceneCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListSceneCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scene_category(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSceneCategoryHeaders()
        return self.list_scene_category_with_options(request, headers, runtime)

    def list_service_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListServiceQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
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
            action='ListServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListServiceQAResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListServiceQAHeaders()
        return self.list_service_qawith_options(request, headers, runtime)

    def list_tickets_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.is_desc):
            body['IsDesc'] = request.is_desc
        if not UtilClient.is_unset(request.is_need_callback):
            body['IsNeedCallback'] = request.is_need_callback
        if not UtilClient.is_unset(request.is_need_charges):
            body['IsNeedCharges'] = request.is_need_charges
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
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
            action='ListTickets',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/listTickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ListTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tickets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListTicketsHeaders()
        return self.list_tickets_with_options(request, headers, runtime)

    def page_get_hotel_room_devices_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
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
            action='PageGetHotelRoomDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/pageGetHotelRoomDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def page_get_hotel_room_devices(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PageGetHotelRoomDevicesHeaders()
        return self.page_get_hotel_room_devices_with_options(request, headers, runtime)

    def push_hotel_message_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushHotelMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.push_hotel_message_req, 'PushHotelMessageReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
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
            action='PushHotelMessage',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/pushHotelMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.PushHotelMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def push_hotel_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushHotelMessageHeaders()
        return self.push_hotel_message_with_options(request, headers, runtime)

    def push_welcome_text_and_music_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushWelcomeTextAndMusicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_variable):
            request.template_variable_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_variable, 'TemplateVariable', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.template_variable_shrink):
            body['TemplateVariable'] = request.template_variable_shrink
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
            action='PushWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/pushWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    def push_welcome_text_and_music(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushWelcomeTextAndMusicHeaders()
        return self.push_welcome_text_and_music_with_options(request, headers, runtime)

    def query_device_status_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryDeviceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='QueryDeviceStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/queryDeviceStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryDeviceStatusHeaders()
        return self.query_device_status_with_options(request, headers, runtime)

    def query_hotel_room_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
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
            action='QueryHotelRoomDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/queryHotelRoomDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryHotelRoomDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_hotel_room_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryHotelRoomDetailHeaders()
        return self.query_hotel_room_detail_with_options(request, headers, runtime)

    def query_room_control_devices_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
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
            action='QueryRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/queryRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_room_control_devices(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesHeaders()
        return self.query_room_control_devices_with_options(request, headers, runtime)

    def query_scene_list_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QuerySceneListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_states):
            request.scene_states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_states, 'SceneStates', 'json')
        if not UtilClient.is_unset(tmp_req.scene_types):
            request.scene_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_types, 'SceneTypes', 'json')
        if not UtilClient.is_unset(tmp_req.template_info_ids):
            request.template_info_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_info_ids, 'TemplateInfoIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_states_shrink):
            body['SceneStates'] = request.scene_states_shrink
        if not UtilClient.is_unset(request.scene_types_shrink):
            body['SceneTypes'] = request.scene_types_shrink
        if not UtilClient.is_unset(request.template_info_ids_shrink):
            body['TemplateInfoIds'] = request.template_info_ids_shrink
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
            action='QuerySceneList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/querySceneList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.QuerySceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QuerySceneListHeaders()
        return self.query_scene_list_with_options(request, headers, runtime)

    def remove_child_account_auth_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.child_account_name):
            body['ChildAccountName'] = request.child_account_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
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
            action='RemoveChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/removeChildAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.RemoveChildAccountAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_child_account_auth(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveChildAccountAuthHeaders()
        return self.remove_child_account_auth_with_options(request, headers, runtime)

    def remove_hotel_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
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
            action='RemoveHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/removeHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.RemoveHotelResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_hotel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveHotelHeaders()
        return self.remove_hotel_with_options(request, headers, runtime)

    def reset_welcome_text_and_music_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='ResetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/resetWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_welcome_text_and_music(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ResetWelcomeTextAndMusicHeaders()
        return self.reset_welcome_text_and_music_with_options(request, headers, runtime)

    def room_check_out_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.RoomCheckOutShrinkRequest()
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
            action='RoomCheckOut',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/roomCheckOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.RoomCheckOutResponse(),
            self.call_api(params, req, runtime)
        )

    def room_check_out(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RoomCheckOutHeaders()
        return self.room_check_out_with_options(request, headers, runtime)

    def submit_hotel_order_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.SubmitHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
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
            action='SubmitHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/submitHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.SubmitHotelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_hotel_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SubmitHotelOrderHeaders()
        return self.submit_hotel_order_with_options(request, headers, runtime)

    def sync_device_status_with_ak_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_cn_name):
            body['CategoryCnName'] = request.category_cn_name
        if not UtilClient.is_unset(request.category_en_name):
            body['CategoryEnName'] = request.category_en_name
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.location_cn_name):
            body['LocationCnName'] = request.location_cn_name
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.switch):
            body['Switch'] = request.switch
        if not UtilClient.is_unset(request.fan_speed):
            body['fanSpeed'] = request.fan_speed
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.room_temperature):
            body['roomTemperature'] = request.room_temperature
        if not UtilClient.is_unset(request.temperature):
            body['temperature'] = request.temperature
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
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
            action='SyncDeviceStatusWithAk',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/syncDeviceStatusWithAk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_device_status_with_ak(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SyncDeviceStatusWithAkHeaders()
        return self.sync_device_status_with_ak_with_options(request, headers, runtime)

    def update_basic_info_qawith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_in_time):
            body['CheckInTime'] = request.check_in_time
        if not UtilClient.is_unset(request.check_out_time):
            body['CheckOutTime'] = request.check_out_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_introduction):
            body['HotelIntroduction'] = request.hotel_introduction
        if not UtilClient.is_unset(request.hotel_member):
            body['HotelMember'] = request.hotel_member
        if not UtilClient.is_unset(request.hotel_service):
            body['HotelService'] = request.hotel_service
        if not UtilClient.is_unset(request.parking_expenses):
            body['ParkingExpenses'] = request.parking_expenses
        if not UtilClient.is_unset(request.parking_position):
            body['ParkingPosition'] = request.parking_position
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.wifi_name):
            body['WifiName'] = request.wifi_name
        if not UtilClient.is_unset(request.wifi_password):
            body['WifiPassword'] = request.wifi_password
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
            action='UpdateBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateBasicInfoQAResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_info_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateBasicInfoQAHeaders()
        return self.update_basic_info_qawith_options(request, headers, runtime)

    def update_custom_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.custom_qaid):
            body['CustomQAId'] = request.custom_qaid
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
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
            action='UpdateCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateCustomQAResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateCustomQAHeaders()
        return self.update_custom_qawith_options(request, headers, runtime)

    def update_hotel_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
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
            action='UpdateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hotel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelHeaders()
        return self.update_hotel_with_options(request, headers, runtime)

    def update_hotel_alarm_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
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
            action='UpdateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hotel_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelAlarmHeaders()
        return self.update_hotel_alarm_with_options(request, headers, runtime)

    def update_hotel_scene_book_item_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_book_req):
            request.update_hotel_scene_book_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_book_req, 'UpdateHotelSceneBookReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_book_req_shrink):
            query['UpdateHotelSceneBookReq'] = request.update_hotel_scene_book_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='UpdateHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hotel_scene_book_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneBookItemHeaders()
        return self.update_hotel_scene_book_item_with_options(request, headers, runtime)

    def update_hotel_scene_item_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_operate_req):
            request.update_hotel_scene_operate_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_operate_req, 'UpdateHotelSceneOperateReq', 'json')
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_req):
            request.update_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_req, 'UpdateHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_operate_req_shrink):
            query['UpdateHotelSceneOperateReq'] = request.update_hotel_scene_operate_req_shrink
        if not UtilClient.is_unset(request.update_hotel_scene_req_shrink):
            query['UpdateHotelSceneReq'] = request.update_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
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
            action='UpdateHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateHotelSceneItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hotel_scene_item(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneItemHeaders()
        return self.update_hotel_scene_item_with_options(request, headers, runtime)

    def update_message_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='UpdateMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateMessageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_message_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateMessageTemplateHeaders()
        return self.update_message_template_with_options(request, headers, runtime)

    def update_rcu_scene_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
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
            action='UpdateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateRcuSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rcu_scene(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateRcuSceneHeaders()
        return self.update_rcu_scene_with_options(request, headers, runtime)

    def update_service_qawith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer):
            body['Answer'] = request.answer
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.service_qaid):
            body['ServiceQAId'] = request.service_qaid
        if not UtilClient.is_unset(request.is_active):
            body['isActive'] = request.is_active
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
            action='UpdateServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateServiceQAResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateServiceQAHeaders()
        return self.update_service_qawith_options(request, headers, runtime)

    def update_ticket_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_key):
            body['GroupKey'] = request.group_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
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
            action='UpdateTicket',
            version='ip_1.0',
            protocol='HTTPS',
            pathname='/v1.0/ip/updateTicket',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieip__1__0_models.UpdateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateTicketHeaders()
        return self.update_ticket_with_options(request, headers, runtime)
