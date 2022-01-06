# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dplus20201216 import models as dplus_20201216_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('dplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def ae_predict_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AePredictCategory',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.AePredictCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def ae_predict_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ae_predict_category_with_options(request, runtime)

    def ae_predict_category_advance(self, request, runtime):
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
            product='dplus',
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
        ae_predict_category_req = dplus_20201216_models.AePredictCategoryRequest()
        OpenApiUtilClient.convert(request, ae_predict_category_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            ae_predict_category_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        ae_predict_category_resp = self.ae_predict_category_with_options(ae_predict_category_req, runtime)
        return ae_predict_category_resp

    def ae_prop_rec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AePropRec',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.AePropRecResponse(),
            self.call_api(params, req, runtime)
        )

    def ae_prop_rec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ae_prop_rec_with_options(request, runtime)

    def ae_prop_rec_advance(self, request, runtime):
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
            product='dplus',
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
        ae_prop_rec_req = dplus_20201216_models.AePropRecRequest()
        OpenApiUtilClient.convert(request, ae_prop_rec_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            ae_prop_rec_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        ae_prop_rec_resp = self.ae_prop_rec_with_options(ae_prop_rec_req, runtime)
        return ae_prop_rec_resp

    def alivision_imgdup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_height):
            body['ImageHeight'] = request.image_height
        if not UtilClient.is_unset(request.image_width):
            body['ImageWidth'] = request.image_width
        if not UtilClient.is_unset(request.output_image_num):
            body['OutputImageNum'] = request.output_image_num
        if not UtilClient.is_unset(request.pic_num):
            body['PicNum'] = request.pic_num
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AlivisionImgdup',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.AlivisionImgdupResponse(),
            self.call_api(params, req, runtime)
        )

    def alivision_imgdup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.alivision_imgdup_with_options(request, runtime)

    def alivision_imgdup_advance(self, request, runtime):
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
            product='dplus',
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
        alivision_imgdup_req = dplus_20201216_models.AlivisionImgdupRequest()
        OpenApiUtilClient.convert(request, alivision_imgdup_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            alivision_imgdup_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        alivision_imgdup_resp = self.alivision_imgdup_with_options(alivision_imgdup_req, runtime)
        return alivision_imgdup_resp

    def create_image_amazon_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dplus_20201216_models.CreateImageAmazonTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.img_url_list):
            request.img_url_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.img_url_list, 'ImgUrlList', 'json')
        if not UtilClient.is_unset(tmp_req.text_list):
            request.text_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_list, 'TextList', 'json')
        query = {}
        if not UtilClient.is_unset(request.gif):
            query['Gif'] = request.gif
        if not UtilClient.is_unset(request.img_url_list_shrink):
            query['ImgUrlList'] = request.img_url_list_shrink
        if not UtilClient.is_unset(request.template_mode):
            query['TemplateMode'] = request.template_mode
        if not UtilClient.is_unset(request.text_list_shrink):
            query['TextList'] = request.text_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageAmazonTask',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.CreateImageAmazonTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_amazon_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_amazon_task_with_options(request, runtime)

    def faceshifter_twith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.race):
            body['Race'] = request.race
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceshifterT',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.FaceshifterTResponse(),
            self.call_api(params, req, runtime)
        )

    def faceshifter_t(self, request):
        runtime = util_models.RuntimeOptions()
        return self.faceshifter_twith_options(request, runtime)

    def faceshifter_tadvance(self, request, runtime):
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
            product='dplus',
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
        faceshifter_treq = dplus_20201216_models.FaceshifterTRequest()
        OpenApiUtilClient.convert(request, faceshifter_treq)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            faceshifter_treq.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        faceshifter_tresp = self.faceshifter_twith_options(faceshifter_treq, runtime)
        return faceshifter_tresp

    def get_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskResult',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_result_with_options(request, runtime)

    def get_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    def kuajing_seg_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.return_pic_format):
            body['ReturnPicFormat'] = request.return_pic_format
        if not UtilClient.is_unset(request.return_pic_type):
            body['ReturnPicType'] = request.return_pic_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KuajingSeg',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.KuajingSegResponse(),
            self.call_api(params, req, runtime)
        )

    def kuajing_seg(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kuajing_seg_with_options(request, runtime)

    def kuajing_seg_advance(self, request, runtime):
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
            product='dplus',
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
        kuajing_seg_req = dplus_20201216_models.KuajingSegRequest()
        OpenApiUtilClient.convert(request, kuajing_seg_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            kuajing_seg_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        kuajing_seg_resp = self.kuajing_seg_with_options(kuajing_seg_req, runtime)
        return kuajing_seg_resp

    def remove_words_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveWords',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.RemoveWordsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_words(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_words_with_options(request, runtime)

    def remove_words_advance(self, request, runtime):
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
            product='dplus',
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
        remove_words_req = dplus_20201216_models.RemoveWordsRequest()
        OpenApiUtilClient.convert(request, remove_words_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            remove_words_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        remove_words_resp = self.remove_words_with_options(remove_words_req, runtime)
        return remove_words_resp

    def replace_background_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.background_id):
            query['BackgroundId'] = request.background_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.pic_background_url):
            query['PicBackgroundUrl'] = request.pic_background_url
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceBackground',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.ReplaceBackgroundResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_background(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_background_with_options(request, runtime)

    def replace_background_advance(self, request, runtime):
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
            product='dplus',
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
        replace_background_req = dplus_20201216_models.ReplaceBackgroundRequest()
        OpenApiUtilClient.convert(request, replace_background_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            replace_background_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        replace_background_resp = self.replace_background_with_options(replace_background_req, runtime)
        return replace_background_resp

    def tb_predict_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TbPredictCategory',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.TbPredictCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def tb_predict_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tb_predict_category_with_options(request, runtime)

    def tb_predict_category_advance(self, request, runtime):
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
            product='dplus',
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
        tb_predict_category_req = dplus_20201216_models.TbPredictCategoryRequest()
        OpenApiUtilClient.convert(request, tb_predict_category_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            tb_predict_category_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        tb_predict_category_resp = self.tb_predict_category_with_options(tb_predict_category_req, runtime)
        return tb_predict_category_resp

    def tb_prop_rec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TbPropRec',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.TbPropRecResponse(),
            self.call_api(params, req, runtime)
        )

    def tb_prop_rec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tb_prop_rec_with_options(request, runtime)

    def tb_prop_rec_advance(self, request, runtime):
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
            product='dplus',
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
        tb_prop_rec_req = dplus_20201216_models.TbPropRecRequest()
        OpenApiUtilClient.convert(request, tb_prop_rec_req)
        if not UtilClient.is_unset(request.pic_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_url_object,
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
            tb_prop_rec_req.pic_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        tb_prop_rec_resp = self.tb_prop_rec_with_options(tb_prop_rec_req, runtime)
        return tb_prop_rec_resp
