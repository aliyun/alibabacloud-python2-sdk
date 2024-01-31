# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20220302 import models as green_20220302_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_file_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFileModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeFileModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_file_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_file_moderation_result_with_options(request, runtime)

    def describe_image_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_moderation_result_with_options(request, runtime)

    def describe_image_result_ext_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.info_type):
            body['InfoType'] = request.info_type
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImageResultExt',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageResultExtResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_result_ext(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_result_ext_with_options(request, runtime)

    def describe_upload_token_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUploadToken',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_upload_token(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_token_with_options(runtime)

    def describe_url_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUrlModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUrlModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_url_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_url_moderation_result_with_options(request, runtime)

    def file_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.FileModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def file_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.file_moderation_with_options(request, runtime)

    def image_async_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def image_async_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.image_async_moderation_with_options(request, runtime)

    def image_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def image_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.image_moderation_with_options(request, runtime)

    def text_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def text_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.text_moderation_with_options(request, runtime)

    def text_moderation_plus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModerationPlus',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationPlusResponse(),
            self.call_api(params, req, runtime)
        )

    def text_moderation_plus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.text_moderation_plus_with_options(request, runtime)

    def url_async_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UrlAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.UrlAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def url_async_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.url_async_moderation_with_options(request, runtime)

    def video_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def video_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_with_options(request, runtime)

    def video_moderation_cancel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    def video_moderation_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_cancel_with_options(request, runtime)

    def video_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def video_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_result_with_options(request, runtime)

    def voice_moderation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResponse(),
            self.call_api(params, req, runtime)
        )

    def voice_moderation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_with_options(request, runtime)

    def voice_moderation_cancel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    def voice_moderation_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_cancel_with_options(request, runtime)

    def voice_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def voice_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_result_with_options(request, runtime)
