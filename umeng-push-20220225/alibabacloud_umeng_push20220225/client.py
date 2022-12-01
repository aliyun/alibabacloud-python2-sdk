# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_push20220225 import models as umeng_push_20220225_models
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
        self._endpoint = self.get_endpoint('umeng-push', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def send_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_app_with_options(request, headers, runtime)

    def send_by_app_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.android_payload), 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_properties), 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.ios_payload), 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.policy), 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByApp',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/SendByApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def send_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_device_with_options(request, headers, runtime)

    def send_by_device_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.android_payload), 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.channel_properties), 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.ios_payload), 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.policy), 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByDevice',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/SendByDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByDeviceResponse(),
            self.call_api(params, req, runtime)
        )
