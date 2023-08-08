# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tingwu20220930 import models as tingwu_20220930_models
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
        self._endpoint = self.get_endpoint('tingwu', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_file_trans_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ability_params):
            body['AbilityParams'] = request.ability_params
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.asr_params):
            body['AsrParams'] = request.asr_params
        if not UtilClient.is_unset(request.audio_language):
            body['AudioLanguage'] = request.audio_language
        if not UtilClient.is_unset(request.audio_oss_bucket):
            body['AudioOssBucket'] = request.audio_oss_bucket
        if not UtilClient.is_unset(request.audio_oss_path):
            body['AudioOssPath'] = request.audio_oss_path
        if not UtilClient.is_unset(request.audio_output_enabled):
            body['AudioOutputEnabled'] = request.audio_output_enabled
        if not UtilClient.is_unset(request.audio_output_oss_bucket):
            body['AudioOutputOssBucket'] = request.audio_output_oss_bucket
        if not UtilClient.is_unset(request.audio_output_oss_path):
            body['AudioOutputOssPath'] = request.audio_output_oss_path
        if not UtilClient.is_unset(request.audio_role_num):
            body['AudioRoleNum'] = request.audio_role_num
        if not UtilClient.is_unset(request.audio_segments_enabled):
            body['AudioSegmentsEnabled'] = request.audio_segments_enabled
        if not UtilClient.is_unset(request.lab_params):
            body['LabParams'] = request.lab_params
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.trans_key):
            body['TransKey'] = request.trans_key
        if not UtilClient.is_unset(request.trans_result_oss_bucket):
            body['TransResultOssBucket'] = request.trans_result_oss_bucket
        if not UtilClient.is_unset(request.trans_result_oss_path):
            body['TransResultOssPath'] = request.trans_result_oss_path
        if not UtilClient.is_unset(request.video_output_enabled):
            body['VideoOutputEnabled'] = request.video_output_enabled
        if not UtilClient.is_unset(request.video_output_oss_bucket):
            body['VideoOutputOssBucket'] = request.video_output_oss_bucket
        if not UtilClient.is_unset(request.video_output_oss_path):
            body['VideoOutputOssPath'] = request.video_output_oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFileTrans',
            version='2022-09-30',
            protocol='HTTPS',
            pathname='/openapi/file-trans',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20220930_models.CreateFileTransResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_trans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_trans_with_options(request, headers, runtime)

    def create_meeting_trans_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ability_params):
            body['AbilityParams'] = request.ability_params
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.asr_params):
            body['AsrParams'] = request.asr_params
        if not UtilClient.is_unset(request.audio_bit_rate):
            body['AudioBitRate'] = request.audio_bit_rate
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.audio_language):
            body['AudioLanguage'] = request.audio_language
        if not UtilClient.is_unset(request.audio_output_enabled):
            body['AudioOutputEnabled'] = request.audio_output_enabled
        if not UtilClient.is_unset(request.audio_output_oss_bucket):
            body['AudioOutputOssBucket'] = request.audio_output_oss_bucket
        if not UtilClient.is_unset(request.audio_output_oss_path):
            body['AudioOutputOssPath'] = request.audio_output_oss_path
        if not UtilClient.is_unset(request.audio_package):
            body['AudioPackage'] = request.audio_package
        if not UtilClient.is_unset(request.audio_sample_rate):
            body['AudioSampleRate'] = request.audio_sample_rate
        if not UtilClient.is_unset(request.audio_segments_enabled):
            body['AudioSegmentsEnabled'] = request.audio_segments_enabled
        if not UtilClient.is_unset(request.doc_result_enabled):
            body['DocResultEnabled'] = request.doc_result_enabled
        if not UtilClient.is_unset(request.lab_params):
            body['LabParams'] = request.lab_params
        if not UtilClient.is_unset(request.meeting_key):
            body['MeetingKey'] = request.meeting_key
        if not UtilClient.is_unset(request.meeting_result_enabled):
            body['MeetingResultEnabled'] = request.meeting_result_enabled
        if not UtilClient.is_unset(request.meeting_result_oss_bucket):
            body['MeetingResultOssBucket'] = request.meeting_result_oss_bucket
        if not UtilClient.is_unset(request.meeting_result_oss_path):
            body['MeetingResultOssPath'] = request.meeting_result_oss_path
        if not UtilClient.is_unset(request.realtime_active_result_level):
            body['RealtimeActiveResultLevel'] = request.realtime_active_result_level
        if not UtilClient.is_unset(request.realtime_result_enabled):
            body['RealtimeResultEnabled'] = request.realtime_result_enabled
        if not UtilClient.is_unset(request.realtime_result_level):
            body['RealtimeResultLevel'] = request.realtime_result_level
        if not UtilClient.is_unset(request.realtime_result_meeting_info_enabled):
            body['RealtimeResultMeetingInfoEnabled'] = request.realtime_result_meeting_info_enabled
        if not UtilClient.is_unset(request.realtime_result_words_enabled):
            body['RealtimeResultWordsEnabled'] = request.realtime_result_words_enabled
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.translate_active_result_level):
            body['TranslateActiveResultLevel'] = request.translate_active_result_level
        if not UtilClient.is_unset(request.translate_languages):
            body['TranslateLanguages'] = request.translate_languages
        if not UtilClient.is_unset(request.translate_result_enabled):
            body['TranslateResultEnabled'] = request.translate_result_enabled
        if not UtilClient.is_unset(request.translate_result_level):
            body['TranslateResultLevel'] = request.translate_result_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMeetingTrans',
            version='2022-09-30',
            protocol='HTTPS',
            pathname='/openapi/meeting-trans',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20220930_models.CreateMeetingTransResponse(),
            self.call_api(params, req, runtime)
        )

    def create_meeting_trans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_meeting_trans_with_options(request, headers, runtime)

    def get_file_trans_with_options(self, trans_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFileTrans',
            version='2022-09-30',
            protocol='HTTPS',
            pathname='/openapi/file-trans/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trans_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20220930_models.GetFileTransResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_trans(self, trans_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_trans_with_options(trans_id, headers, runtime)

    def get_meeting_trans_with_options(self, meeting_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMeetingTrans',
            version='2022-09-30',
            protocol='HTTPS',
            pathname='/openapi/meeting-trans/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(meeting_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20220930_models.GetMeetingTransResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meeting_trans(self, meeting_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_meeting_trans_with_options(meeting_id, headers, runtime)

    def stop_meeting_trans_with_options(self, meeting_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meeting_role_num):
            body['MeetingRoleNum'] = request.meeting_role_num
        if not UtilClient.is_unset(request.only_role_split_result):
            body['OnlyRoleSplitResult'] = request.only_role_split_result
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopMeetingTrans',
            version='2022-09-30',
            protocol='HTTPS',
            pathname='/openapi/meeting-trans/%s/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(meeting_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20220930_models.StopMeetingTransResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_meeting_trans(self, meeting_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_meeting_trans_with_options(meeting_id, request, headers, runtime)
