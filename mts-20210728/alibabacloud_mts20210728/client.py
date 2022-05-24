# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mts20210728 import models as mts_20210728_models
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
            'ap-northeast-2-pop': 'mts.aliyuncs.com',
            'ap-southeast-2': 'mts.aliyuncs.com',
            'ap-southeast-3': 'mts.aliyuncs.com',
            'cn-beijing-finance-1': 'mts.aliyuncs.com',
            'cn-beijing-finance-pop': 'mts.aliyuncs.com',
            'cn-beijing-gov-1': 'mts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mts.aliyuncs.com',
            'cn-chengdu': 'mts.aliyuncs.com',
            'cn-edge-1': 'mts.aliyuncs.com',
            'cn-fujian': 'mts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mts.aliyuncs.com',
            'cn-hangzhou-finance': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mts.aliyuncs.com',
            'cn-hangzhou-test-306': 'mts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mts.aliyuncs.com',
            'cn-north-2-gov-1': 'mts.aliyuncs.com',
            'cn-qingdao-nebula': 'mts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mts.aliyuncs.com',
            'cn-shanghai-finance-1': 'mts.aliyuncs.com',
            'cn-shanghai-inner': 'mts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mts.aliyuncs.com',
            'cn-shenzhen-inner': 'mts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mts.aliyuncs.com',
            'cn-wuhan': 'mts.aliyuncs.com',
            'cn-wulanchabu': 'mts.aliyuncs.com',
            'cn-yushanfang': 'mts.aliyuncs.com',
            'cn-zhangbei': 'mts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mts.aliyuncs.com',
            'eu-west-1-oxs': 'mts.aliyuncs.com',
            'me-east-1': 'mts.aliyuncs.com',
            'rus-west-1-pop': 'mts.aliyuncs.com',
            'us-east-1': 'mts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def query_copyright(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_copyright_with_options(request, headers, runtime)

    def query_copyright_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCopyright',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/queryCopyrightJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    def query_copyright_extract(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_copyright_extract_with_options(request, headers, runtime)

    def query_copyright_extract_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCopyrightExtract',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/queryCopyrightExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryCopyrightExtractResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trace_ab(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_trace_ab_with_options(request, headers, runtime)

    def query_trace_ab_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTraceAb',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/queryTraceAb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceAbResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trace_extract(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_trace_extract_with_options(request, headers, runtime)

    def query_trace_extract_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTraceExtract',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/queryTraceExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceExtractResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trace_mu(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_trace_mu_with_options(request, headers, runtime)

    def query_trace_mu_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTraceMu',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/queryTraceM3u8',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceMuResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_copyright_extract(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_copyright_extract_with_options(request, headers, runtime)

    def submit_copyright_extract_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCopyrightExtract',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitCopyrightExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitCopyrightExtractResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_copyright_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_copyright_job_with_options(request, headers, runtime)

    def submit_copyright_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_time):
            body['TotalTime'] = request.total_time
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        if not UtilClient.is_unset(request.visible_message):
            body['VisibleMessage'] = request.visible_message
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCopyrightJob',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitCopyrightJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitCopyrightJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_image_copyright(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_image_copyright_with_options(request, headers, runtime)

    def submit_image_copyright_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImageCopyright',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitImageCopyright',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitImageCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_trace_ab(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_trace_ab_with_options(request, headers, runtime)

    def submit_trace_ab_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.cipher_base_64ed):
            body['CipherBase64ed'] = request.cipher_base_64ed
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_time):
            body['TotalTime'] = request.total_time
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTraceAb',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitTraceAb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTraceAbResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_trace_extract(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_trace_extract_with_options(request, headers, runtime)

    def submit_trace_extract_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTraceExtract',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitTraceExtract',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTraceExtractResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_tracemu(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_tracemu_with_options(request, headers, runtime)

    def submit_tracemu_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_uri):
            body['KeyUri'] = request.key_uri
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.trace):
            body['Trace'] = request.trace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTracemu',
            version='2021-07-28',
            protocol='HTTPS',
            pathname='/submitTraceM3u8',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTracemuResponse(),
            self.call_api(params, req, runtime)
        )
