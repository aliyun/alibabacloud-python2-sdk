# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lvwangwatermark20210104 import models as lvwang_watermark_20210104_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('lvwangwatermark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_audio_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.AddAudioAsyncResponse().from_map(
            self.do_rpcrequest('AddAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_audio_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_audio_async_with_options(request, runtime)

    def add_image_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.AddImageAsyncResponse().from_map(
            self.do_rpcrequest('AddImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_image_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_image_async_with_options(request, runtime)

    def add_image_sync_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.AddImageSyncResponse().from_map(
            self.do_rpcrequest('AddImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_image_sync(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_image_sync_with_options(request, runtime)

    def add_video_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.AddVideoAsyncResponse().from_map(
            self.do_rpcrequest('AddVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_video_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_video_async_with_options(request, runtime)

    def get_audio_add_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetAudioAddResponse().from_map(
            self.do_rpcrequest('GetAudioAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_add(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audio_add_with_options(request, runtime)

    def get_audio_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetAudioAsyncResponse().from_map(
            self.do_rpcrequest('GetAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audio_async_with_options(request, runtime)

    def get_audio_extract_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetAudioExtractResponse().from_map(
            self.do_rpcrequest('GetAudioExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_extract(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audio_extract_with_options(request, runtime)

    def get_audio_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetAudioTraceResponse().from_map(
            self.do_rpcrequest('GetAudioTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audio_trace_with_options(request, runtime)

    def get_image_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetImageAsyncResponse().from_map(
            self.do_rpcrequest('GetImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_async_with_options(request, runtime)

    def get_image_sync_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetImageSyncResponse().from_map(
            self.do_rpcrequest('GetImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_sync(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_sync_with_options(request, runtime)

    def get_video_add_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetVideoAddResponse().from_map(
            self.do_rpcrequest('GetVideoAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_add(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_add_with_options(request, runtime)

    def get_video_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetVideoAsyncResponse().from_map(
            self.do_rpcrequest('GetVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_async_with_options(request, runtime)

    def get_video_extract_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetVideoExtractResponse().from_map(
            self.do_rpcrequest('GetVideoExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_extract(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_extract_with_options(request, runtime)

    def get_video_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return lvwang_watermark_20210104_models.GetVideoTraceResponse().from_map(
            self.do_rpcrequest('GetVideoTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_trace_with_options(request, runtime)
