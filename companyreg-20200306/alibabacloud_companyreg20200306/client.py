# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_companyreg20200306 import models as companyreg_20200306_models
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
            'ap-northeast-1': 'companyreg.aliyuncs.com',
            'ap-northeast-2-pop': 'companyreg.aliyuncs.com',
            'ap-south-1': 'companyreg.aliyuncs.com',
            'ap-southeast-1': 'companyreg.aliyuncs.com',
            'ap-southeast-2': 'companyreg.aliyuncs.com',
            'ap-southeast-3': 'companyreg.aliyuncs.com',
            'ap-southeast-5': 'companyreg.aliyuncs.com',
            'cn-beijing': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-1': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-pop': 'companyreg.aliyuncs.com',
            'cn-beijing-gov-1': 'companyreg.aliyuncs.com',
            'cn-beijing-nu16-b01': 'companyreg.aliyuncs.com',
            'cn-chengdu': 'companyreg.aliyuncs.com',
            'cn-edge-1': 'companyreg.aliyuncs.com',
            'cn-fujian': 'companyreg.aliyuncs.com',
            'cn-haidian-cm12-c01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-finance': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'companyreg.aliyuncs.com',
            'cn-hangzhou-test-306': 'companyreg.aliyuncs.com',
            'cn-hongkong': 'companyreg.aliyuncs.com',
            'cn-hongkong-finance-pop': 'companyreg.aliyuncs.com',
            'cn-huhehaote': 'companyreg.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'companyreg.aliyuncs.com',
            'cn-north-2-gov-1': 'companyreg.aliyuncs.com',
            'cn-qingdao': 'companyreg.aliyuncs.com',
            'cn-qingdao-nebula': 'companyreg.aliyuncs.com',
            'cn-shanghai': 'companyreg.aliyuncs.com',
            'cn-shanghai-et15-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-et2-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-finance-1': 'companyreg.aliyuncs.com',
            'cn-shanghai-inner': 'companyreg.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen': 'companyreg.aliyuncs.com',
            'cn-shenzhen-finance-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen-inner': 'companyreg.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'companyreg.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'companyreg.aliyuncs.com',
            'cn-wuhan': 'companyreg.aliyuncs.com',
            'cn-wulanchabu': 'companyreg.aliyuncs.com',
            'cn-yushanfang': 'companyreg.aliyuncs.com',
            'cn-zhangbei': 'companyreg.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'companyreg.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'companyreg.aliyuncs.com',
            'eu-central-1': 'companyreg.aliyuncs.com',
            'eu-west-1': 'companyreg.aliyuncs.com',
            'eu-west-1-oxs': 'companyreg.aliyuncs.com',
            'me-east-1': 'companyreg.aliyuncs.com',
            'rus-west-1-pop': 'companyreg.aliyuncs.com',
            'us-east-1': 'companyreg.aliyuncs.com',
            'us-west-1': 'companyreg.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('companyreg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_produce_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorized_user_ids):
            body['AuthorizedUserIds'] = request.authorized_user_ids
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindProduceAuthorization',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.BindProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_produce_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_produce_authorization_with_options(request, runtime)

    def close_intention_for_partner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseIntentionForPartner',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.CloseIntentionForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    def close_intention_for_partner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_intention_for_partner_with_options(request, runtime)

    def close_user_intention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseUserIntention',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.CloseUserIntentionResponse(),
            self.call_api(params, req, runtime)
        )

    def close_user_intention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_user_intention_with_options(request, runtime)

    def create_business_opportunity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.vcode):
            query['VCode'] = request.vcode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBusinessOpportunity',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.CreateBusinessOpportunityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_business_opportunity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_business_opportunity_with_options(request, runtime)

    def create_produce_for_partner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduceForPartner',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.CreateProduceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_produce_for_partner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_produce_for_partner_with_options(request, runtime)

    def describe_partner_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.partner_code):
            query['PartnerCode'] = request.partner_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePartnerConfig',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.DescribePartnerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_partner_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_partner_config_with_options(request, runtime)

    def generate_upload_file_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadFilePolicy',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.GenerateUploadFilePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_upload_file_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_file_policy_with_options(request, runtime)

    def get_alipay_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlipayUrl',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.GetAlipayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alipay_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alipay_url_with_options(request, runtime)

    def list_intention_note_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntentionNote',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListIntentionNoteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_intention_note(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_intention_note_with_options(request, runtime)

    def list_produce_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProduceAuthorization',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_produce_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_produce_authorization_with_options(request, runtime)

    def list_user_detail_solutions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDetailSolutions',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListUserDetailSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_detail_solutions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_detail_solutions_with_options(request, runtime)

    def list_user_intention_notes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserIntentionNotes',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListUserIntentionNotesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_intention_notes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_intention_notes_with_options(request, runtime)

    def list_user_intentions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.with_ext_info):
            query['WithExtInfo'] = request.with_ext_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserIntentions',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListUserIntentionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_intentions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_intentions_with_options(request, runtime)

    def list_user_produce_operate_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserProduceOperateLogs',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListUserProduceOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_produce_operate_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_produce_operate_logs_with_options(request, runtime)

    def list_user_solutions_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = companyreg_20200306_models.ListUserSolutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exist_status):
            request.exist_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exist_status, 'ExistStatus', 'json')
        query = {}
        if not UtilClient.is_unset(request.exist_status_shrink):
            query['ExistStatus'] = request.exist_status_shrink
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserSolutions',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ListUserSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_solutions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_solutions_with_options(request, runtime)

    def operate_produce_for_partner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateProduceForPartner',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.OperateProduceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_produce_for_partner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_produce_for_partner_with_options(request, runtime)

    def put_measure_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutMeasureData',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.PutMeasureDataResponse(),
            self.call_api(params, req, runtime)
        )

    def put_measure_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_measure_data_with_options(request, runtime)

    def put_measure_ready_flag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ready_flag):
            query['ReadyFlag'] = request.ready_flag
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMeasureReadyFlag',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.PutMeasureReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    def put_measure_ready_flag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_measure_ready_flag_with_options(request, runtime)

    def query_available_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvailableNumbers',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryAvailableNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_available_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_available_numbers_with_options(request, runtime)

    def query_bag_remaining_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBagRemaining',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryBagRemainingResponse(),
            self.call_api(params, req, runtime)
        )

    def query_bag_remaining(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bag_remaining_with_options(request, runtime)

    def query_commodity_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.query_module):
            query['QueryModule'] = request.query_module
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommodityConfig',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryCommodityConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def query_commodity_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_commodity_config_with_options(request, runtime)

    def query_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstance',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_with_options(request, runtime)

    def query_partner_intention_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPartnerIntentionList',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryPartnerIntentionListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_partner_intention_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_partner_intention_list_with_options(request, runtime)

    def query_partner_produce_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPartnerProduceList',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryPartnerProduceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_partner_produce_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_partner_produce_list_with_options(request, runtime)

    def query_user_need_auth_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUserNeedAuth',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.QueryUserNeedAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_need_auth(self):
        runtime = util_models.RuntimeOptions()
        return self.query_user_need_auth_with_options(runtime)

    def record_post_back_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.contactor):
            query['contactor'] = request.contactor
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        if not UtilClient.is_unset(request.entity_key):
            query['entityKey'] = request.entity_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordPostBack',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.RecordPostBackResponse(),
            self.call_api(params, req, runtime)
        )

    def record_post_back(self, request):
        runtime = util_models.RuntimeOptions()
        return self.record_post_back_with_options(request, runtime)

    def reject_solution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectSolution',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.RejectSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_solution_with_options(request, runtime)

    def reject_user_solution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.solution_biz_id):
            query['SolutionBizId'] = request.solution_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectUserSolution',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.RejectUserSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_user_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_user_solution_with_options(request, runtime)

    def release_produce_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorized_user_id):
            body['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseProduceAuthorization',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.ReleaseProduceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def release_produce_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_produce_authorization_with_options(request, runtime)

    def start_back_to_back_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.call_center_number):
            query['CallCenterNumber'] = request.call_center_number
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.mobile_key):
            query['MobileKey'] = request.mobile_key
        if not UtilClient.is_unset(request.skill_type):
            query['SkillType'] = request.skill_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBackToBackCall',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.StartBackToBackCallResponse(),
            self.call_api(params, req, runtime)
        )

    def start_back_to_back_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_back_to_back_call_with_options(request, runtime)

    def submit_intention_note_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIntentionNote',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.SubmitIntentionNoteResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_intention_note(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_intention_note_with_options(request, runtime)

    def submit_solution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSolution',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.SubmitSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_solution_with_options(request, runtime)

    def transfer_intention_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferIntentionOwner',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.TransferIntentionOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_intention_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_intention_owner_with_options(request, runtime)

    def transfer_produce_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferProduceOwner',
            version='2020-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            companyreg_20200306_models.TransferProduceOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_produce_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_produce_owner_with_options(request, runtime)
