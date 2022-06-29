# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def compare_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.source_certify_id):
            body['SourceCertifyId'] = request.source_certify_id
        if not UtilClient.is_unset(request.source_face_contrast_picture):
            body['SourceFaceContrastPicture'] = request.source_face_contrast_picture
        if not UtilClient.is_unset(request.source_face_contrast_picture_url):
            body['SourceFaceContrastPictureUrl'] = request.source_face_contrast_picture_url
        if not UtilClient.is_unset(request.source_oss_bucket_name):
            body['SourceOssBucketName'] = request.source_oss_bucket_name
        if not UtilClient.is_unset(request.source_oss_object_name):
            body['SourceOssObjectName'] = request.source_oss_object_name
        if not UtilClient.is_unset(request.target_certify_id):
            body['TargetCertifyId'] = request.target_certify_id
        if not UtilClient.is_unset(request.target_face_contrast_picture):
            body['TargetFaceContrastPicture'] = request.target_face_contrast_picture
        if not UtilClient.is_unset(request.target_face_contrast_picture_url):
            body['TargetFaceContrastPictureUrl'] = request.target_face_contrast_picture_url
        if not UtilClient.is_unset(request.target_oss_bucket_name):
            body['TargetOssBucketName'] = request.target_oss_bucket_name
        if not UtilClient.is_unset(request.target_oss_object_name):
            body['TargetOssObjectName'] = request.target_oss_object_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def compare_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify_with_options(request, runtime)

    def compare_faces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_image_type):
            body['SourceImageType'] = request.source_image_type
        if not UtilClient.is_unset(request.source_image_value):
            body['SourceImageValue'] = request.source_image_value
        if not UtilClient.is_unset(request.target_image_type):
            body['TargetImageType'] = request.target_image_type
        if not UtilClient.is_unset(request.target_image_value):
            body['TargetImageValue'] = request.target_image_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaces',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.call_api(params, req, runtime)
        )

    def compare_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    def contrast_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.encrypt_type):
            body['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_file):
            body['FaceContrastFile'] = request.face_contrast_file
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContrastFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def contrast_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify_with_options(request, runtime)

    def contrast_face_verify_advance(self, request, runtime):
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
            product='Cloudauth',
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
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        contrast_face_verify_resp = self.contrast_face_verify_with_options(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_auth_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_years):
            query['AuthYears'] = request.auth_years
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.test):
            query['Test'] = request.test
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthKey',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auth_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key_with_options(request, runtime)

    def create_verify_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.guide_step):
            query['GuideStep'] = request.guide_step
        if not UtilClient.is_unset(request.privacy_step):
            query['PrivacyStep'] = request.privacy_step
        if not UtilClient.is_unset(request.result_step):
            query['ResultStep'] = request.result_step
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_verify_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting_with_options(request, runtime)

    def describe_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.expired_end_day):
            query['ExpiredEndDay'] = request.expired_end_day
        if not UtilClient.is_unset(request.expired_start_day):
            query['ExpiredStartDay'] = request.expired_start_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    def describe_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.picture_return_type):
            query['PictureReturnType'] = request.picture_return_type
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify_with_options(request, runtime)

    def describe_oss_upload_token_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssUploadToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_upload_token(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    def describe_verify_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_verify_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    def describe_verify_sdkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_verify_sdk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdkwith_options(request, runtime)

    def describe_verify_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.face_retained_image_url):
            query['FaceRetainedImageUrl'] = request.face_retained_image_url
        if not UtilClient.is_unset(request.failed_redirect_url):
            query['FailedRedirectUrl'] = request.failed_redirect_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passed_redirect_url):
            query['PassedRedirectUrl'] = request.passed_redirect_url
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_ip):
            query['UserIp'] = request.user_ip
        if not UtilClient.is_unset(request.user_phone_number):
            query['UserPhoneNumber'] = request.user_phone_number
        if not UtilClient.is_unset(request.user_regist_time):
            query['UserRegistTime'] = request.user_regist_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_verify_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    def detect_face_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.material_value):
            body['MaterialValue'] = request.material_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFaceAttributes',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_face_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    def init_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.certify_url_type):
            query['CertifyUrlType'] = request.certify_url_type
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        body = {}
        if not UtilClient.is_unset(request.auth_id):
            body['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def init_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)

    def liveness_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LivenessFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def liveness_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify_with_options(request, runtime)

    def modify_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info_with_options(request, runtime)

    def verify_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.face_image_url):
            query['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMaterial',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_material_with_options(request, runtime)
