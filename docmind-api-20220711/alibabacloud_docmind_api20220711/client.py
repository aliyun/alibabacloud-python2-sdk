# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_docmind_api20220711 import models as docmind_api_20220711_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
        self._endpoint_map = {
            'ap-northeast-1': 'docmind-api.aliyuncs.com',
            'ap-northeast-2-pop': 'docmind-api.aliyuncs.com',
            'ap-south-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-2': 'docmind-api.aliyuncs.com',
            'ap-southeast-3': 'docmind-api.aliyuncs.com',
            'ap-southeast-5': 'docmind-api.aliyuncs.com',
            'cn-beijing': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-beijing-gov-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-nu16-b01': 'docmind-api.aliyuncs.com',
            'cn-chengdu': 'docmind-api.aliyuncs.com',
            'cn-edge-1': 'docmind-api.aliyuncs.com',
            'cn-fujian': 'docmind-api.aliyuncs.com',
            'cn-haidian-cm12-c01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-finance': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-test-306': 'docmind-api.aliyuncs.com',
            'cn-hongkong': 'docmind-api.aliyuncs.com',
            'cn-hongkong-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-huhehaote': 'docmind-api.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'docmind-api.aliyuncs.com',
            'cn-north-2-gov-1': 'docmind-api.aliyuncs.com',
            'cn-qingdao': 'docmind-api.aliyuncs.com',
            'cn-qingdao-nebula': 'docmind-api.aliyuncs.com',
            'cn-shanghai': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et15-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et2-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shanghai-inner': 'docmind-api.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-inner': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'docmind-api.aliyuncs.com',
            'cn-wuhan': 'docmind-api.aliyuncs.com',
            'cn-wulanchabu': 'docmind-api.aliyuncs.com',
            'cn-yushanfang': 'docmind-api.aliyuncs.com',
            'cn-zhangbei': 'docmind-api.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'docmind-api.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'docmind-api.aliyuncs.com',
            'eu-central-1': 'docmind-api.aliyuncs.com',
            'eu-west-1': 'docmind-api.aliyuncs.com',
            'eu-west-1-oxs': 'docmind-api.aliyuncs.com',
            'me-east-1': 'docmind-api.aliyuncs.com',
            'rus-west-1-pop': 'docmind-api.aliyuncs.com',
            'us-east-1': 'docmind-api.aliyuncs.com',
            'us-west-1': 'docmind-api.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('docmind-api', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_doc_structure_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocStructureResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocStructureResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doc_structure_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_doc_structure_result_with_options(request, runtime)

    def get_document_compare_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentCompareResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentCompareResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_document_compare_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_document_compare_result_with_options(request, runtime)

    def get_document_convert_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentConvertResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentConvertResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_document_convert_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_document_convert_result_with_options(request, runtime)

    def get_document_extract_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocumentExtractResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetDocumentExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_document_extract_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_document_extract_result_with_options(request, runtime)

    def get_table_understanding_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableUnderstandingResult',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.GetTableUnderstandingResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_understanding_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_table_understanding_result_with_options(request, runtime)

    def submit_convert_image_to_excel_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToExcelJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_image_to_excel_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_excel_job_with_options(request, runtime)

    def submit_convert_image_to_pdf_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToPdfJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToPdfJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToPdfJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_image_to_pdf_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_pdf_job_with_options(request, runtime)

    def submit_convert_image_to_word_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220711_models.SubmitConvertImageToWordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'simple')
        if not UtilClient.is_unset(tmp_req.image_urls):
            request.image_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_urls, 'ImageUrls', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_name_extension):
            query['ImageNameExtension'] = request.image_name_extension
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_urls_shrink):
            query['ImageUrls'] = request.image_urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertImageToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertImageToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_image_to_word_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_image_to_word_job_with_options(request, runtime)

    def submit_convert_pdf_to_excel_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToExcelJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToExcelJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_pdf_to_excel_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_excel_job_with_options(request, runtime)

    def submit_convert_pdf_to_excel_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_convert_pdf_to_excel_job_req = docmind_api_20220711_models.SubmitConvertPdfToExcelJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_excel_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_convert_pdf_to_excel_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_convert_pdf_to_excel_job_resp = self.submit_convert_pdf_to_excel_job_with_options(submit_convert_pdf_to_excel_job_req, runtime)
        return submit_convert_pdf_to_excel_job_resp

    def submit_convert_pdf_to_image_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToImageJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_pdf_to_image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_image_job_with_options(request, runtime)

    def submit_convert_pdf_to_image_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_convert_pdf_to_image_job_req = docmind_api_20220711_models.SubmitConvertPdfToImageJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_image_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_convert_pdf_to_image_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_convert_pdf_to_image_job_resp = self.submit_convert_pdf_to_image_job_with_options(submit_convert_pdf_to_image_job_req, runtime)
        return submit_convert_pdf_to_image_job_resp

    def submit_convert_pdf_to_word_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitConvertPdfToWordJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitConvertPdfToWordJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_convert_pdf_to_word_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_convert_pdf_to_word_job_with_options(request, runtime)

    def submit_convert_pdf_to_word_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_convert_pdf_to_word_job_req = docmind_api_20220711_models.SubmitConvertPdfToWordJobRequest()
        OpenApiUtilClient.convert(request, submit_convert_pdf_to_word_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_convert_pdf_to_word_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_convert_pdf_to_word_job_resp = self.submit_convert_pdf_to_word_job_with_options(submit_convert_pdf_to_word_job_req, runtime)
        return submit_convert_pdf_to_word_job_resp

    def submit_doc_structure_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocStructureJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocStructureJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_doc_structure_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_doc_structure_job_with_options(request, runtime)

    def submit_doc_structure_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_doc_structure_job_req = docmind_api_20220711_models.SubmitDocStructureJobRequest()
        OpenApiUtilClient.convert(request, submit_doc_structure_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_doc_structure_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_doc_structure_job_resp = self.submit_doc_structure_job_with_options(submit_doc_structure_job_req, runtime)
        return submit_doc_structure_job_resp

    def submit_document_compare_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compare_file_name):
            query['CompareFileName'] = request.compare_file_name
        if not UtilClient.is_unset(request.compare_file_url):
            query['CompareFileUrl'] = request.compare_file_url
        if not UtilClient.is_unset(request.origin_file_name):
            query['OriginFileName'] = request.origin_file_name
        if not UtilClient.is_unset(request.origin_file_url):
            query['OriginFileUrl'] = request.origin_file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentCompareJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocumentCompareJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_document_compare_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_document_compare_job_with_options(request, runtime)

    def submit_document_extract_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentExtractJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitDocumentExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_document_extract_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_document_extract_job_with_options(request, runtime)

    def submit_document_extract_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_document_extract_job_req = docmind_api_20220711_models.SubmitDocumentExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_document_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_document_extract_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_document_extract_job_resp = self.submit_document_extract_job_with_options(submit_document_extract_job_req, runtime)
        return submit_document_extract_job_resp

    def submit_table_understanding_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTableUnderstandingJob',
            version='2022-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220711_models.SubmitTableUnderstandingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_table_understanding_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_table_understanding_job_with_options(request, runtime)

    def submit_table_understanding_job_advance(self, request, runtime):
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
        auth_config = open_api_models.Config(
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
            product='docmind-api',
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
        submit_table_understanding_job_req = docmind_api_20220711_models.SubmitTableUnderstandingJobRequest()
        OpenApiUtilClient.convert(request, submit_table_understanding_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_table_understanding_job_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        submit_table_understanding_job_resp = self.submit_table_understanding_job_with_options(submit_table_understanding_job_req, runtime)
        return submit_table_understanding_job_resp
