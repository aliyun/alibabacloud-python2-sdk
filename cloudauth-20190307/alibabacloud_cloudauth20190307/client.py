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
from RPC import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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

    def verify_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.do_rpcrequest('VerifyMaterial', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_material_with_options(request, runtime)

    def describe_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            self.do_rpcrequest('DescribeWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_with_options(request, runtime)

    def update_app_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            self.do_rpcrequest('UpdateAppPackage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_package_with_options(request, runtime)

    def describe_verify_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.do_rpcrequest('DescribeVerifyToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    def describe_rpsdkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            self.do_rpcrequest('DescribeRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rpsdk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rpsdkwith_options(request, runtime)

    def describe_face_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            self.do_rpcrequest('DescribeFaceUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_usage_with_options(request, runtime)

    def describe_verify_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            self.do_rpcrequest('DescribeVerifyUsage', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_usage_with_options(request, runtime)

    def describe_update_package_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            self.do_rpcrequest('DescribeUpdatePackageResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_update_package_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result_with_options(request, runtime)

    def create_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            self.do_rpcrequest('CreateWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist_with_options(request, runtime)

    def delete_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            self.do_rpcrequest('DeleteWhitelist', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist_with_options(request, runtime)

    def create_auth_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.do_rpcrequest('CreateAuthKey', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auth_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key_with_options(request, runtime)

    def describe_upload_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            self.do_rpcrequest('DescribeUploadInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upload_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info_with_options(request, runtime)

    def describe_verify_setting_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            self.do_rpcrequest('DescribeVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_setting(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting_with_options(runtime)

    def describe_verify_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            self.do_rpcrequest('DescribeVerifyRecords', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_records_with_options(request, runtime)

    def describe_whitelist_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistSettingResponse(),
            self.do_rpcrequest('DescribeWhitelistSetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_whitelist_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_setting_with_options(request, runtime)

    def create_rpsdkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            self.do_rpcrequest('CreateRPSDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rpsdk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rpsdkwith_options(request, runtime)

    def update_face_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            self.do_rpcrequest('UpdateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_config_with_options(request, runtime)

    def describe_face_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            self.do_rpcrequest('DescribeFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_config_with_options(request, runtime)

    def liveness_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.do_rpcrequest('LivenessFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def liveness_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify_with_options(request, runtime)

    def describe_app_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            self.do_rpcrequest('DescribeAppInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info_with_options(request, runtime)

    def modify_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.do_rpcrequest('ModifyDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info_with_options(request, runtime)

    def contrast_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.do_rpcrequest('ContrastFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def verify_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            self.do_rpcrequest('VerifyDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_device_with_options(request, runtime)

    def compare_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.do_rpcrequest('CompareFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify_with_options(request, runtime)

    def describe_verify_sdkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.do_rpcrequest('DescribeVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_sdk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdkwith_options(request, runtime)

    def describe_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.do_rpcrequest('DescribeDeviceInfo', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    def describe_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.do_rpcrequest('DescribeFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify_with_options(request, runtime)

    def describe_oss_upload_token_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.do_rpcrequest('DescribeOssUploadToken', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_upload_token(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    def detect_face_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.do_rpcrequest('DetectFaceAttributes', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_face_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    def describe_sdk_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            self.do_rpcrequest('DescribeSdkUrl', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdk_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url_with_options(request, runtime)

    def delete_whitelist_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistSettingResponse(),
            self.do_rpcrequest('DeleteWhitelistSetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_whitelist_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist_setting_with_options(request, runtime)

    def update_verify_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            self.do_rpcrequest('UpdateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_verify_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_verify_setting_with_options(request, runtime)

    def describe_verify_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.do_rpcrequest('DescribeVerifyResult', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    def compare_faces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.do_rpcrequest('CompareFaces', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def compare_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    def create_face_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            self.do_rpcrequest('CreateFaceConfig', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_face_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_face_config_with_options(request, runtime)

    def create_verify_sdkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            self.do_rpcrequest('CreateVerifySDK', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_sdk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_sdkwith_options(request, runtime)

    def init_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            self.do_rpcrequest('InitDevice', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_device_with_options(request, runtime)

    def create_whitelist_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistSettingResponse(),
            self.do_rpcrequest('CreateWhitelistSetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_whitelist_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist_setting_with_options(request, runtime)

    def describe_user_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            self.do_rpcrequest('DescribeUserStatus', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(runtime)

    def create_verify_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.do_rpcrequest('CreateVerifySetting', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting_with_options(request, runtime)

    def init_face_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.do_rpcrequest('InitFaceVerify', '2019-03-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_face_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)
