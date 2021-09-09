# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from RPC.client import Client as RPCClient
from RPC import models as rpc_models
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_whitelist_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistSettingResponse(),
            self.do_request('DescribeWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_whitelist_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_setting(request, runtime)

    def delete_whitelist_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistSettingResponse(),
            self.do_request('DeleteWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_whitelist_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist_setting(request, runtime)

    def create_whitelist_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistSettingResponse(),
            self.do_request('CreateWhitelistSetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_whitelist_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist_setting(request, runtime)

    def describe_whitelist(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeWhitelistResponse(),
            self.do_request('DescribeWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_whitelist_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist(request, runtime)

    def delete_whitelist(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteWhitelistResponse(),
            self.do_request('DeleteWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_whitelist_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_whitelist(request, runtime)

    def create_whitelist(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateWhitelistResponse(),
            self.do_request('CreateWhitelist', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_whitelist_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_whitelist(request, runtime)

    def describe_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceConfigResponse(),
            self.do_request('DescribeFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_config(request, runtime)

    def update_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateFaceConfigResponse(),
            self.do_request('UpdateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_config(request, runtime)

    def create_face_config(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateFaceConfigResponse(),
            self.do_request('CreateFaceConfig', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_face_config_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_face_config(request, runtime)

    def liveness_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.do_request('LivenessFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def liveness_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify(request, runtime)

    def compare_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.do_request('CompareFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def compare_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify(request, runtime)

    def describe_sdk_url(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSdkUrlResponse(),
            self.do_request('DescribeSdkUrl', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sdk_url_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url(request, runtime)

    def describe_update_package_result(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUpdatePackageResultResponse(),
            self.do_request('DescribeUpdatePackageResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_update_package_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result(request, runtime)

    def update_app_package(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateAppPackageResponse(),
            self.do_request('UpdateAppPackage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_app_package_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_package(request, runtime)

    def describe_app_info(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeAppInfoResponse(),
            self.do_request('DescribeAppInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_app_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info(request, runtime)

    def contrast_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.do_request('ContrastFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def contrast_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify(request, runtime)

    def contrast_face_verify_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
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
        RPCUtilClient.convert(runtime, oss_runtime)
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        RPCUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        contrast_face_verify_resp = self.contrast_face_verify(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def init_device(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitDeviceResponse(),
            self.do_request('InitDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def init_device_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_device(request, runtime)

    def init_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.do_request('InitFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def init_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify(request, runtime)

    def describe_face_verify(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.do_request('DescribeFaceVerify', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_verify_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify(request, runtime)

    def verify_device(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyDeviceResponse(),
            self.do_request('VerifyDevice', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def verify_device_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_device(request, runtime)

    def modify_device_info(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.do_request('ModifyDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_device_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info(request, runtime)

    def describe_verify_sdk(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.do_request('DescribeVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_sdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdk(request, runtime)

    def describe_device_info(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.do_request('DescribeDeviceInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_device_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info(request, runtime)

    def create_verify_sdk(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySDKResponse(),
            self.do_request('CreateVerifySDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_verify_sdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_sdk(request, runtime)

    def create_auth_key(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.do_request('CreateAuthKey', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_auth_key_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key(request, runtime)

    def detect_face_attributes(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.do_request('DetectFaceAttributes', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detect_face_attributes_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes(request, runtime)

    def compare_faces(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.do_request('CompareFaces', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def compare_faces_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_faces(request, runtime)

    def describe_face_usage(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceUsageResponse(),
            self.do_request('DescribeFaceUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_face_usage_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_face_usage(request, runtime)

    def describe_verify_records(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyRecordsResponse(),
            self.do_request('DescribeVerifyRecords', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_records_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_records(request, runtime)

    def update_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.UpdateVerifySettingResponse(),
            self.do_request('UpdateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_verify_setting(request, runtime)

    def create_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.do_request('CreateVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting(request, runtime)

    def describe_verify_setting(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySettingResponse(),
            self.do_request('DescribeVerifySetting', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_setting_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_setting(request, runtime)

    def describe_verify_usage(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyUsageResponse(),
            self.do_request('DescribeVerifyUsage', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_usage_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_usage(request, runtime)

    def describe_user_status(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUserStatusResponse(),
            self.do_request('DescribeUserStatus', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_user_status_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status(request, runtime)

    def describe_upload_info(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeUploadInfoResponse(),
            self.do_request('DescribeUploadInfo', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_upload_info_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info(request, runtime)

    def describe_rpsdk(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeRPSDKResponse(),
            self.do_request('DescribeRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_rpsdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rpsdk(request, runtime)

    def create_rpsdk(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateRPSDKResponse(),
            self.do_request('CreateRPSDK', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rpsdksimply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rpsdk(request, runtime)

    def verify_material(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.do_request('VerifyMaterial', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def verify_material_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_material(request, runtime)

    def describe_verify_result(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.do_request('DescribeVerifyResult', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result(request, runtime)

    def describe_oss_upload_token(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.do_request('DescribeOssUploadToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_oss_upload_token_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token(request, runtime)

    def describe_verify_token(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.do_request('DescribeVerifyToken', 'HTTPS', 'POST', '2019-03-07', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_verify_token_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
