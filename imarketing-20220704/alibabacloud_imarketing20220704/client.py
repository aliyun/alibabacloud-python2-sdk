# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imarketing20220704 import models as imarketing_20220704_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('imarketing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.CreateDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra_map):
            request.extra_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra_map, 'ExtraMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.device_model_number):
            body['DeviceModelNumber'] = request.device_model_number
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.district):
            body['District'] = request.district
        if not UtilClient.is_unset(request.extra_map_shrink):
            body['ExtraMap'] = request.extra_map_shrink
        if not UtilClient.is_unset(request.first_scene):
            body['FirstScene'] = request.first_scene
        if not UtilClient.is_unset(request.floor):
            body['Floor'] = request.floor
        if not UtilClient.is_unset(request.location_name):
            body['LocationName'] = request.location_name
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.outer_code):
            body['OuterCode'] = request.outer_code
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.second_scene):
            body['SecondScene'] = request.second_scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def delete_creative_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCreativeInfo',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.DeleteCreativeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_creative_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_creative_info_with_options(request, runtime)

    def get_brand_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        if not UtilClient.is_unset(request.main_name):
            query['MainName'] = request.main_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBrandPage',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetBrandPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_brand_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_brand_page_with_options(request, runtime)

    def get_business_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessId',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetBusinessIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_id_with_options(request, runtime)

    def get_creative_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreativeInfo',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetCreativeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_creative_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_creative_info_with_options(request, runtime)

    def get_leads_list_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.content_id):
            query['ContentId'] = request.content_id
        if not UtilClient.is_unset(request.creative_id):
            query['CreativeId'] = request.creative_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLeadsListPage',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetLeadsListPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_leads_list_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_leads_list_page_with_options(request, runtime)

    def get_main_part_list_by_user_id_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMainPartListByUserId',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetMainPartListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_main_part_list_by_user_id(self):
        runtime = util_models.RuntimeOptions()
        return self.get_main_part_list_by_user_id_with_options(runtime)

    def get_main_part_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        if not UtilClient.is_unset(request.main_name):
            query['MainName'] = request.main_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainPartPage',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetMainPartPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_main_part_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_main_part_page_with_options(request, runtime)

    def get_oss_upload_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUploadSignature',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetOssUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_upload_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_upload_signature_with_options(request, runtime)

    def get_related_by_creative_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRelatedByCreativeId',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetRelatedByCreativeIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_related_by_creative_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_related_by_creative_id_with_options(request, runtime)

    def get_user_finished_ad_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserFinishedAd',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.GetUserFinishedAdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_finished_ad(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_finished_ad_with_options(request, runtime)

    def list_advertising_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imarketing_20220704_models.ListAdvertisingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.app), 'App', 'json')
        if not UtilClient.is_unset(tmp_req.device):
            request.device_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.device), 'Device', 'json')
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'Ext', 'json')
        if not UtilClient.is_unset(tmp_req.imp):
            request.imp_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.imp, 'Imp', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvertising',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.ListAdvertisingResponse(),
            self.call_api(params, req, runtime)
        )

    def list_advertising(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_advertising_with_options(request, runtime)

    def query_audit_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dsp_id):
            query['DspId'] = request.dsp_id
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuditResult',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.QueryAuditResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_audit_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_audit_result_with_options(request, runtime)

    def send_sms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.now_stamp):
            query['NowStamp'] = request.now_stamp
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.sign_key):
            query['SignKey'] = request.sign_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.SendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    def send_sms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    def sync_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.chain_value):
            query['ChainValue'] = request.chain_value
        if not UtilClient.is_unset(request.component_id_list):
            query['ComponentIdList'] = request.component_id_list
        if not UtilClient.is_unset(request.create_user):
            query['CreateUser'] = request.create_user
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.main_id):
            query['MainId'] = request.main_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_chain_value):
            query['NextChainValue'] = request.next_chain_value
        if not UtilClient.is_unset(request.oss_file_url):
            query['OssFileUrl'] = request.oss_file_url
        if not UtilClient.is_unset(request.page_id):
            query['PageId'] = request.page_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.url_type):
            query['UrlType'] = request.url_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncInfo',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.SyncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_info_with_options(request, runtime)

    def update_adx_creative_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad):
            query['Ad'] = request.ad
        if not UtilClient.is_unset(request.dsp_id):
            query['DspId'] = request.dsp_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdxCreativeContent',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.UpdateAdxCreativeContentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_adx_creative_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_adx_creative_content_with_options(request, runtime)

    def verify_sms_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.now_stamp):
            query['NowStamp'] = request.now_stamp
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.sign_key):
            query['SignKey'] = request.sign_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySmsCode',
            version='2022-07-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imarketing_20220704_models.VerifySmsCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_sms_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_sms_code_with_options(request, runtime)
