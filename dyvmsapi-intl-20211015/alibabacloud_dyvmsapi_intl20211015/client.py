# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyvmsapi_intl20211015 import models as dyvmsapi_intl_20211015_models
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
        self._endpoint = self.get_endpoint('dyvmsapi-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def backend_call_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.BackendCallGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallGroup',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def backend_call_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.backend_call_group_with_options(request, runtime)

    def backend_call_signal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackendCallSignal',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.BackendCallSignalResponse(),
            self.call_api(params, req, runtime)
        )

    def backend_call_signal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.backend_call_signal_with_options(request, runtime)

    def group_call_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dyvmsapi_intl_20211015_models.GroupCallShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.called_number):
            request.called_number_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.called_number, 'CalledNumber', 'json')
        query = {}
        if not UtilClient.is_unset(request.called_number_shrink):
            query['CalledNumber'] = request.called_number_shrink
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GroupCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.GroupCallResponse(),
            self.call_api(params, req, runtime)
        )

    def group_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.group_call_with_options(request, runtime)

    def signal_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.caller_id_number):
            query['CallerIdNumber'] = request.caller_id_number
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_type):
            query['SendType'] = request.send_type
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.signature_nonce):
            query['SignatureNonce'] = request.signature_nonce
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.timing_start):
            query['TimingStart'] = request.timing_start
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalCall',
            version='2021-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_intl_20211015_models.SignalCallResponse(),
            self.call_api(params, req, runtime)
        )

    def signal_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.signal_call_with_options(request, runtime)
