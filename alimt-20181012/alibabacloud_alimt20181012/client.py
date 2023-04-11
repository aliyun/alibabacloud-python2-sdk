# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alimt20181012 import models as alimt_20181012_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'mt.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'mt.aliyuncs.com',
            'ap-northeast-2-pop': 'mt.aliyuncs.com',
            'ap-south-1': 'mt.aliyuncs.com',
            'ap-southeast-1': 'mt.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mt.aliyuncs.com',
            'ap-southeast-3': 'mt.aliyuncs.com',
            'ap-southeast-5': 'mt.aliyuncs.com',
            'cn-beijing': 'mt.aliyuncs.com',
            'cn-beijing-finance-1': 'mt.aliyuncs.com',
            'cn-beijing-finance-pop': 'mt.aliyuncs.com',
            'cn-beijing-gov-1': 'mt.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mt.aliyuncs.com',
            'cn-chengdu': 'mt.aliyuncs.com',
            'cn-edge-1': 'mt.aliyuncs.com',
            'cn-fujian': 'mt.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mt.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mt.aliyuncs.com',
            'cn-hangzhou-finance': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mt.aliyuncs.com',
            'cn-hangzhou-test-306': 'mt.aliyuncs.com',
            'cn-hongkong': 'mt.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mt.aliyuncs.com',
            'cn-huhehaote': 'mt.aliyuncs.com',
            'cn-north-2-gov-1': 'mt.aliyuncs.com',
            'cn-qingdao': 'mt.aliyuncs.com',
            'cn-qingdao-nebula': 'mt.aliyuncs.com',
            'cn-shanghai': 'mt.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mt.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mt.aliyuncs.com',
            'cn-shanghai-finance-1': 'mt.aliyuncs.com',
            'cn-shanghai-inner': 'mt.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mt.aliyuncs.com',
            'cn-shenzhen': 'mt.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mt.aliyuncs.com',
            'cn-shenzhen-inner': 'mt.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mt.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mt.aliyuncs.com',
            'cn-wuhan': 'mt.aliyuncs.com',
            'cn-yushanfang': 'mt.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mt.aliyuncs.com',
            'cn-zhangjiakou': 'mt.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mt.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mt.aliyuncs.com',
            'eu-central-1': 'mt.aliyuncs.com',
            'eu-west-1': 'mt.aliyuncs.com',
            'eu-west-1-oxs': 'mt.aliyuncs.com',
            'me-east-1': 'mt.aliyuncs.com',
            'rus-west-1-pop': 'mt.aliyuncs.com',
            'us-east-1': 'mt.aliyuncs.com',
            'us-west-1': 'mt.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alimt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_doc_translate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_doc_translate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_doc_translate_task_with_options(request, runtime)

    def create_doc_translate_task_advance(self, request, runtime):
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
            product='alimt',
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
        create_doc_translate_task_req = alimt_20181012_models.CreateDocTranslateTaskRequest()
        OpenApiUtilClient.convert(request, create_doc_translate_task_req)
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
            create_doc_translate_task_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        create_doc_translate_task_resp = self.create_doc_translate_task_with_options(create_doc_translate_task_req, runtime)
        return create_doc_translate_task_resp

    def create_image_translate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url_list):
            body['UrlList'] = request.url_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.CreateImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_translate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_translate_task_with_options(request, runtime)

    def get_batch_translate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBatchTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetBatchTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_batch_translate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_batch_translate_with_options(request, runtime)

    def get_detect_language_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectLanguage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDetectLanguageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_detect_language(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_detect_language_with_options(request, runtime)

    def get_doc_translate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDocTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doc_translate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_doc_translate_task_with_options(request, runtime)

    def get_image_diagnose_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_diagnose(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_diagnose_with_options(request, runtime)

    def get_image_translate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_translate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_translate_with_options(request, runtime)

    def get_image_translate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslateTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_translate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_translate_task_with_options(request, runtime)

    def get_title_diagnose_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleDiagnose',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_title_diagnose(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_title_diagnose_with_options(request, runtime)

    def get_title_generate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.hot_words):
            body['HotWords'] = request.hot_words
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleGenerate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_title_generate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_title_generate_with_options(request, runtime)

    def get_title_intelligence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cat_level_three_id):
            body['CatLevelThreeId'] = request.cat_level_three_id
        if not UtilClient.is_unset(request.cat_level_two_id):
            body['CatLevelTwoId'] = request.cat_level_two_id
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTitleIntelligence',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTitleIntelligenceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_title_intelligence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_title_intelligence_with_options(request, runtime)

    def get_translate_image_batch_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTranslateImageBatchResult',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateImageBatchResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_translate_image_batch_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_translate_image_batch_result_with_options(request, runtime)

    def get_translate_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranslateReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.GetTranslateReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_translate_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_translate_report_with_options(request, runtime)

    def open_alimt_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAlimtService',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.OpenAlimtServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_alimt_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_alimt_service_with_options(request, runtime)

    def translate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Translate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateResponse(),
            self.call_api(params, req, runtime)
        )

    def translate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_with_options(request, runtime)

    def translate_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_type):
            body['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.result_type):
            body['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateCertificate',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def translate_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_certificate_with_options(request, runtime)

    def translate_certificate_advance(self, request, runtime):
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
            product='alimt',
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
        translate_certificate_req = alimt_20181012_models.TranslateCertificateRequest()
        OpenApiUtilClient.convert(request, translate_certificate_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            translate_certificate_req.image_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        translate_certificate_resp = self.translate_certificate_with_options(translate_certificate_req, runtime)
        return translate_certificate_resp

    def translate_ecommerce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateECommerceResponse(),
            self.call_api(params, req, runtime)
        )

    def translate_ecommerce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_ecommerce_with_options(request, runtime)

    def translate_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.context):
            query['Context'] = request.context
        body = {}
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.source_text):
            body['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def translate_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_general_with_options(request, runtime)

    def translate_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageResponse(),
            self.call_api(params, req, runtime)
        )

    def translate_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_image_with_options(request, runtime)

    def translate_image_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_task_id):
            body['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateImageBatch',
            version='2018-10-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20181012_models.TranslateImageBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def translate_image_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.translate_image_batch_with_options(request, runtime)
