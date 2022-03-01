# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ivpd20190625 import models as ivpd_20190625_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ivpd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_image_size_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeImageSize',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.ChangeImageSizeResponse(),
            self.call_api(params, req, runtime)
        )

    def change_image_size(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_image_size_with_options(request, runtime)

    def create_segment_body_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_list):
            body['DataList'] = request.data_list
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.time_to_live):
            body['TimeToLive'] = request.time_to_live
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSegmentBodyJob',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.CreateSegmentBodyJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_segment_body_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_segment_body_job_with_options(request, runtime)

    def detect_image_elements_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectImageElements',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.DetectImageElementsResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_elements(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_elements_with_options(request, runtime)

    def erase_logo_in_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.boxes):
            body['Boxes'] = request.boxes
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EraseLogoInVideo',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.EraseLogoInVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def erase_logo_in_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.erase_logo_in_video_with_options(request, runtime)

    def extend_image_style_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.major_url):
            body['MajorUrl'] = request.major_url
        if not UtilClient.is_unset(request.style_url):
            body['StyleUrl'] = request.style_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendImageStyle',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.ExtendImageStyleResponse(),
            self.call_api(params, req, runtime)
        )

    def extend_image_style(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extend_image_style_with_options(request, runtime)

    def get_async_job_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_job_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    def get_async_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncResult',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.GetAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    def get_job_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobResult',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.GetJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_result_with_options(request, runtime)

    def get_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    def get_user_bucket_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserBucketConfig',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.GetUserBucketConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_bucket_config(self):
        runtime = util_models.RuntimeOptions()
        return self.get_user_bucket_config_with_options(runtime)

    def highlight_game_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async):
            body['Async'] = request.async
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HighlightGameVideo',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.HighlightGameVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def highlight_game_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.highlight_game_video_with_options(request, runtime)

    def highlight_game_video_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='ivpd',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        highlight_game_video_req = ivpd_20190625_models.HighlightGameVideoRequest()
        OpenApiUtilClient.convert(request, highlight_game_video_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.video_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            highlight_game_video_req.video_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        highlight_game_video_resp = self.highlight_game_video_with_options(highlight_game_video_req, runtime)
        return highlight_game_video_resp

    def list_package_design_model_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListPackageDesignModelTypes',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.ListPackageDesignModelTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_package_design_model_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_package_design_model_types_with_options(runtime)

    def list_user_buckets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserBuckets',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.ListUserBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_buckets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_buckets_with_options(request, runtime)

    def make_super_resolution_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MakeSuperResolutionImage',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.MakeSuperResolutionImageResponse(),
            self.call_api(params, req, runtime)
        )

    def make_super_resolution_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.make_super_resolution_image_with_options(request, runtime)

    def recognize_image_color_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeImageColor',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.RecognizeImageColorResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_image_color(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_color_with_options(request, runtime)

    def recognize_image_style_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeImageStyle',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.RecognizeImageStyleResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_image_style(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_style_with_options(request, runtime)

    def recolor_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.color_count):
            body['ColorCount'] = request.color_count
        if not UtilClient.is_unset(request.color_template):
            body['ColorTemplate'] = request.color_template
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecolorImage',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.RecolorImageResponse(),
            self.call_api(params, req, runtime)
        )

    def recolor_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recolor_image_with_options(request, runtime)

    def segment_body_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SegmentBody',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.SegmentBodyResponse(),
            self.call_api(params, req, runtime)
        )

    def segment_body(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_body_with_options(request, runtime)

    def segment_commodity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SegmentCommodity',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.SegmentCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    def segment_commodity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_commodity_with_options(request, runtime)

    def segment_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SegmentImage',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.SegmentImageResponse(),
            self.call_api(params, req, runtime)
        )

    def segment_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_image_with_options(request, runtime)

    def update_user_bucket_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserBucketConfig',
            version='2019-06-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ivpd_20190625_models.UpdateUserBucketConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_bucket_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_bucket_config_with_options(request, runtime)
