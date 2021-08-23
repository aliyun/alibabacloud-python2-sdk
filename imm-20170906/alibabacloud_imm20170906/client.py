# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20170906 import models as imm_20170906_models
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
            'cn-beijing-gov-1': 'imm-vpc.cn-beijing-gov-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('imm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def compare_image_faces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CompareImageFacesResponse(),
            self.do_rpcrequest('CompareImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_image_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    def convert_office_format_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ConvertOfficeFormatResponse(),
            self.do_rpcrequest('ConvertOfficeFormat', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_office_format(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_office_format_with_options(request, runtime)

    def create_grab_frame_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGrabFrameTaskResponse(),
            self.do_rpcrequest('CreateGrabFrameTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_grab_frame_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_grab_frame_task_with_options(request, runtime)

    def create_group_faces_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGroupFacesJobResponse(),
            self.do_rpcrequest('CreateGroupFacesJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group_faces_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_faces_job_with_options(request, runtime)

    def create_image_process_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateImageProcessTaskResponse(),
            self.do_rpcrequest('CreateImageProcessTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_process_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_process_task_with_options(request, runtime)

    def create_media_complex_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMediaComplexTaskResponse(),
            self.do_rpcrequest('CreateMediaComplexTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_media_complex_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_media_complex_task_with_options(request, runtime)

    def create_merge_face_groups_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMergeFaceGroupsJobResponse(),
            self.do_rpcrequest('CreateMergeFaceGroupsJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_merge_face_groups_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_merge_face_groups_job_with_options(request, runtime)

    def create_office_conversion_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateOfficeConversionTaskResponse(),
            self.do_rpcrequest('CreateOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_office_conversion_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    def create_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateSetResponse(),
            self.do_rpcrequest('CreateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_set_with_options(request, runtime)

    def create_video_abstract_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAbstractTaskResponse(),
            self.do_rpcrequest('CreateVideoAbstractTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_abstract_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_abstract_task_with_options(request, runtime)

    def create_video_analyse_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAnalyseTaskResponse(),
            self.do_rpcrequest('CreateVideoAnalyseTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_analyse_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_analyse_task_with_options(request, runtime)

    def create_video_compress_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoCompressTaskResponse(),
            self.do_rpcrequest('CreateVideoCompressTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_compress_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_compress_task_with_options(request, runtime)

    def create_video_produce_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoProduceTaskResponse(),
            self.do_rpcrequest('CreateVideoProduceTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_produce_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_produce_task_with_options(request, runtime)

    def decode_blind_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DecodeBlindWatermarkResponse(),
            self.do_rpcrequest('DecodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def decode_blind_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decode_blind_watermark_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageResponse(),
            self.do_rpcrequest('DeleteImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_image_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageJobResponse(),
            self.do_rpcrequest('DeleteImageJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_job_with_options(request, runtime)

    def delete_office_conversion_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteOfficeConversionTaskResponse(),
            self.do_rpcrequest('DeleteOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_office_conversion_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_office_conversion_task_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def delete_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteSetResponse(),
            self.do_rpcrequest('DeleteSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_set_with_options(request, runtime)

    def delete_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoResponse(),
            self.do_rpcrequest('DeleteVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    def delete_video_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoTaskResponse(),
            self.do_rpcrequest('DeleteVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_video_task_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            imm_20170906_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def detect_image_bodies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageBodiesResponse(),
            self.do_rpcrequest('DetectImageBodies', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_bodies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    def detect_image_faces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageFacesResponse(),
            self.do_rpcrequest('DetectImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    def detect_image_logos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageLogosResponse(),
            self.do_rpcrequest('DetectImageLogos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_logos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_logos_with_options(request, runtime)

    def detect_image_qrcodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageQRCodesResponse(),
            self.do_rpcrequest('DetectImageQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_qrcodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_qrcodes_with_options(request, runtime)

    def detect_image_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageTagsResponse(),
            self.do_rpcrequest('DetectImageTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_tags_with_options(request, runtime)

    def detect_qrcodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectQRCodesResponse(),
            self.do_rpcrequest('DetectQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_qrcodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_qrcodes_with_options(request, runtime)

    def encode_blind_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.EncodeBlindWatermarkResponse(),
            self.do_rpcrequest('EncodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def encode_blind_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.encode_blind_watermark_with_options(request, runtime)

    def find_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.FindImagesResponse(),
            self.do_rpcrequest('FindImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_images_with_options(request, runtime)

    def find_similar_faces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.FindSimilarFacesResponse(),
            self.do_rpcrequest('FindSimilarFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_similar_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_similar_faces_with_options(request, runtime)

    def get_content_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetContentKeyResponse(),
            self.do_rpcrequest('GetContentKey', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_content_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_content_key_with_options(request, runtime)

    def get_drmlicense_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetDRMLicenseResponse(),
            self.do_rpcrequest('GetDRMLicense', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_drmlicense(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_drmlicense_with_options(request, runtime)

    def get_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageResponse(),
            self.do_rpcrequest('GetImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    def get_image_cropping_suggestions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageCroppingSuggestionsResponse(),
            self.do_rpcrequest('GetImageCroppingSuggestions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_cropping_suggestions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_cropping_suggestions_with_options(request, runtime)

    def get_image_quality_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageQualityResponse(),
            self.do_rpcrequest('GetImageQuality', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_quality(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_quality_with_options(request, runtime)

    def get_media_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetMediaMetaResponse(),
            self.do_rpcrequest('GetMediaMeta', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_meta_with_options(request, runtime)

    def get_office_conversion_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeConversionTaskResponse(),
            self.do_rpcrequest('GetOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_office_conversion_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_office_conversion_task_with_options(request, runtime)

    def get_office_edit_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeEditURLResponse(),
            self.do_rpcrequest('GetOfficeEditURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_office_edit_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_office_edit_urlwith_options(request, runtime)

    def get_office_preview_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficePreviewURLResponse(),
            self.do_rpcrequest('GetOfficePreviewURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_office_preview_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_office_preview_urlwith_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def get_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetSetResponse(),
            self.do_rpcrequest('GetSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_set_with_options(request, runtime)

    def get_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoResponse(),
            self.do_rpcrequest('GetVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_with_options(request, runtime)

    def get_video_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoTaskResponse(),
            self.do_rpcrequest('GetVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_task_with_options(request, runtime)

    def get_weboffice_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.GetWebofficeURLResponse(),
            self.do_rpcrequest('GetWebofficeURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_weboffice_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_weboffice_urlwith_options(request, runtime)

    def index_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexImageResponse(),
            self.do_rpcrequest('IndexImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def index_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.index_image_with_options(request, runtime)

    def index_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexVideoResponse(),
            self.do_rpcrequest('IndexVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def index_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.index_video_with_options(request, runtime)

    def list_face_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListFaceGroupsResponse(),
            self.do_rpcrequest('ListFaceGroups', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_face_groups_with_options(request, runtime)

    def list_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListImagesResponse(),
            self.do_rpcrequest('ListImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    def list_office_conversion_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListOfficeConversionTaskResponse(),
            self.do_rpcrequest('ListOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_office_conversion_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_office_conversion_task_with_options(request, runtime)

    def list_project_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectAPIsResponse(),
            self.do_rpcrequest('ListProjectAPIs', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_apis_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetsResponse(),
            self.do_rpcrequest('ListSets', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sets_with_options(request, runtime)

    def list_set_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetTagsResponse(),
            self.do_rpcrequest('ListSetTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_set_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_set_tags_with_options(request, runtime)

    def list_video_audios_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoAudiosResponse(),
            self.do_rpcrequest('ListVideoAudios', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_video_audios(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_video_audios_with_options(request, runtime)

    def list_video_frames_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoFramesResponse(),
            self.do_rpcrequest('ListVideoFrames', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_video_frames(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_video_frames_with_options(request, runtime)

    def list_videos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideosResponse(),
            self.do_rpcrequest('ListVideos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_videos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_videos_with_options(request, runtime)

    def list_video_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoTasksResponse(),
            self.do_rpcrequest('ListVideoTasks', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_video_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_video_tasks_with_options(request, runtime)

    def open_imm_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.OpenImmServiceResponse(),
            self.do_rpcrequest('OpenImmService', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_imm_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_imm_service_with_options(request, runtime)

    def put_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.PutProjectResponse(),
            self.do_rpcrequest('PutProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_project_with_options(request, runtime)

    def refresh_office_edit_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficeEditTokenResponse(),
            self.do_rpcrequest('RefreshOfficeEditToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_office_edit_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_office_edit_token_with_options(request, runtime)

    def refresh_office_preview_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficePreviewTokenResponse(),
            self.do_rpcrequest('RefreshOfficePreviewToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_office_preview_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_office_preview_token_with_options(request, runtime)

    def refresh_weboffice_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshWebofficeTokenResponse(),
            self.do_rpcrequest('RefreshWebofficeToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_weboffice_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    def update_face_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateFaceGroupResponse(),
            self.do_rpcrequest('UpdateFaceGroup', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_group_with_options(request, runtime)

    def update_image_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20170906_models.UpdateImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateImageResponse(),
            self.do_rpcrequest('UpdateImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def update_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateSetResponse(),
            self.do_rpcrequest('UpdateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_set_with_options(request, runtime)
