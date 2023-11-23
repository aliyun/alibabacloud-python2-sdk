# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trademark20180724 import models as trademark_20180724_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('trademark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_partner_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.material):
            query['Material'] = request.material
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptPartnerNotification',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.AcceptPartnerNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    def accept_partner_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_partner_notification_with_options(request, runtime)

    def apply_notary_post_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notary_order_id):
            query['NotaryOrderId'] = request.notary_order_id
        if not UtilClient.is_unset(request.receiver_address):
            query['ReceiverAddress'] = request.receiver_address
        if not UtilClient.is_unset(request.receiver_name):
            query['ReceiverName'] = request.receiver_name
        if not UtilClient.is_unset(request.receiver_phone):
            query['ReceiverPhone'] = request.receiver_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNotaryPost',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ApplyNotaryPostResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_notary_post(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_notary_post_with_options(request, runtime)

    def ask_adjudication_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_county):
            query['ContactCounty'] = request.contact_county
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AskAdjudicationFile',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.AskAdjudicationFileResponse(),
            self.call_api(params, req, runtime)
        )

    def ask_adjudication_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ask_adjudication_file_with_options(request, runtime)

    def bind_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.legal_notice_key):
            query['LegalNoticeKey'] = request.legal_notice_key
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.BindMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_material_with_options(request, runtime)

    def cancel_trade_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTradeOrder',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CancelTradeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_trade_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_trade_order_with_options(request, runtime)

    def check_flsm_fill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.wtr_name):
            query['WtrName'] = request.wtr_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFlsmFill',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckFlsmFillResponse(),
            self.call_api(params, req, runtime)
        )

    def check_flsm_fill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_flsm_fill_with_options(request, runtime)

    def check_if_collected_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id_list):
            query['ItemIdList'] = request.item_id_list
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckIfCollected',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckIfCollectedResponse(),
            self.call_api(params, req, runtime)
        )

    def check_if_collected(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_if_collected_with_options(request, runtime)

    def check_loa_fill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_zipcode):
            query['ContactZipcode'] = request.contact_zipcode
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.wtr_name):
            query['WtrName'] = request.wtr_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLoaFill',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckLoaFillResponse(),
            self.call_api(params, req, runtime)
        )

    def check_loa_fill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_loa_fill_with_options(request, runtime)

    def check_trademark_icon_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_scene_type):
            query['EventSceneType'] = request.event_scene_type
        if not UtilClient.is_unset(request.trademark_icon_oss_key):
            query['TrademarkIconOssKey'] = request.trademark_icon_oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTrademarkIcon',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkIconResponse(),
            self.call_api(params, req, runtime)
        )

    def check_trademark_icon(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_icon_with_options(request, runtime)

    def check_trademark_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_id):
            query['AgreementId'] = request.agreement_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.is_black_icon):
            query['IsBlackIcon'] = request.is_black_icon
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.logo_goods_id):
            query['LogoGoodsId'] = request.logo_goods_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.order_data):
            query['OrderData'] = request.order_data
        if not UtilClient.is_unset(request.partner_code):
            query['PartnerCode'] = request.partner_code
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.real_user_name):
            query['RealUserName'] = request.real_user_name
        if not UtilClient.is_unset(request.register_name):
            query['RegisterName'] = request.register_name
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.renew_info_id):
            query['RenewInfoId'] = request.renew_info_id
        if not UtilClient.is_unset(request.root_code):
            query['RootCode'] = request.root_code
        if not UtilClient.is_unset(request.tm_comment):
            query['TmComment'] = request.tm_comment
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_name_type):
            query['TmNameType'] = request.tm_name_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTrademarkOrder',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def check_trademark_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_order_with_options(request, runtime)

    def combine_loa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not UtilClient.is_unset(request.contact_postcode):
            query['ContactPostcode'] = request.contact_postcode
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.material_name):
            query['MaterialName'] = request.material_name
        if not UtilClient.is_unset(request.nationality):
            query['Nationality'] = request.nationality
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.tm_produce_type):
            query['TmProduceType'] = request.tm_produce_type
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CombineLoa',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CombineLoaResponse(),
            self.call_api(params, req, runtime)
        )

    def combine_loa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.combine_loa_with_options(request, runtime)

    def combine_wtswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.contact):
            query['Contact'] = request.contact
        if not UtilClient.is_unset(request.contact_address_post):
            query['ContactAddressPost'] = request.contact_address_post
        if not UtilClient.is_unset(request.contact_mobile):
            query['ContactMobile'] = request.contact_mobile
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.material_name):
            query['MaterialName'] = request.material_name
        if not UtilClient.is_unset(request.nationality):
            query['Nationality'] = request.nationality
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.tm_num):
            query['TmNum'] = request.tm_num
        if not UtilClient.is_unset(request.tm_produce_type):
            query['TmProduceType'] = request.tm_produce_type
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.wts_type):
            query['WtsType'] = request.wts_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CombineWTS',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CombineWTSResponse(),
            self.call_api(params, req, runtime)
        )

    def combine_wts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.combine_wtswith_options(request, runtime)

    def complement_intention_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.complement_user_id):
            body['ComplementUserId'] = request.complement_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ComplementIntentionUserId',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ComplementIntentionUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def complement_intention_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complement_intention_user_id_with_options(request, runtime)

    def confirm_additional_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmAdditionalMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmAdditionalMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_additional_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_additional_material_with_options(request, runtime)

    def confirm_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmApplicant',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_applicant_with_options(request, runtime)

    def confirm_dissent_original_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_county):
            query['ContactCounty'] = request.contact_county
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmDissentOriginal',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmDissentOriginalResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_dissent_original(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_dissent_original_with_options(request, runtime)

    def convert_image_to_gray_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertImageToGray',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConvertImageToGrayResponse(),
            self.call_api(params, req, runtime)
        )

    def convert_image_to_gray(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_image_to_gray_with_options(request, runtime)

    def copy_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyApplicant',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CopyApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_applicant_with_options(request, runtime)

    def create_intention_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntentionOrder',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_intention_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_with_options(request, runtime)

    def create_intention_order_generating_pay_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.payment_callback):
            query['PaymentCallback'] = request.payment_callback
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntentionOrderGeneratingPay',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse(),
            self.call_api(params, req, runtime)
        )

    def create_intention_order_generating_pay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_generating_pay_with_options(request, runtime)

    def create_trademark_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_id):
            query['AgreementId'] = request.agreement_id
        if not UtilClient.is_unset(request.big_dipper_source):
            query['BigDipperSource'] = request.big_dipper_source
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.is_black_icon):
            query['IsBlackIcon'] = request.is_black_icon
        if not UtilClient.is_unset(request.legal_notice_key):
            query['LegalNoticeKey'] = request.legal_notice_key
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.order_data):
            query['OrderData'] = request.order_data
        if not UtilClient.is_unset(request.partner_code):
            query['PartnerCode'] = request.partner_code
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.real_user_name):
            query['RealUserName'] = request.real_user_name
        if not UtilClient.is_unset(request.register_name):
            query['RegisterName'] = request.register_name
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.renew_info_id):
            query['RenewInfoId'] = request.renew_info_id
        if not UtilClient.is_unset(request.root_code):
            query['RootCode'] = request.root_code
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tm_comment):
            query['TmComment'] = request.tm_comment
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_name_type):
            query['TmNameType'] = request.tm_name_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.ua):
            query['Ua'] = request.ua
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrademarkOrder',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateTrademarkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_trademark_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_trademark_order_with_options(request, runtime)

    def delete_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_material_with_options(request, runtime)

    def delete_tm_monitor_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTmMonitorRule',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTmMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tm_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tm_monitor_rule_with_options(request, runtime)

    def delete_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrademarkApplication',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trademark_application_with_options(request, runtime)

    def deny_supplement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DenySupplement',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.DenySupplementResponse(),
            self.call_api(params, req, runtime)
        )

    def deny_supplement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deny_supplement_with_options(request, runtime)

    def descirbe_combine_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accurate_match):
            query['AccurateMatch'] = request.accurate_match
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_name):
            query['OwnerName'] = request.owner_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.products):
            query['Products'] = request.products
        if not UtilClient.is_unset(request.registration_number):
            query['RegistrationNumber'] = request.registration_number
        if not UtilClient.is_unset(request.similar_groups):
            query['SimilarGroups'] = request.similar_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescirbeCombineTrademark',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.DescirbeCombineTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    def descirbe_combine_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descirbe_combine_trademark_with_options(request, runtime)

    def fill_logistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.logistics):
            query['Logistics'] = request.logistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FillLogistics',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.FillLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def fill_logistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fill_logistics_with_options(request, runtime)

    def filter_unavailable_codes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.FilterUnavailableCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        query = {}
        if not UtilClient.is_unset(request.codes_shrink):
            query['Codes'] = request.codes_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FilterUnavailableCodes',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.FilterUnavailableCodesResponse(),
            self.call_api(params, req, runtime)
        )

    def filter_unavailable_codes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.filter_unavailable_codes_with_options(request, runtime)

    def force_upload_trademark_onsale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.classification_code):
            query['ClassificationCode'] = request.classification_code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.original_price):
            query['OriginalPrice'] = request.original_price
        if not UtilClient.is_unset(request.owner_en_name):
            query['OwnerEnName'] = request.owner_en_name
        if not UtilClient.is_unset(request.owner_name):
            query['OwnerName'] = request.owner_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_ann_date):
            query['RegAnnDate'] = request.reg_ann_date
        if not UtilClient.is_unset(request.secondary_classification):
            query['SecondaryClassification'] = request.secondary_classification
        if not UtilClient.is_unset(request.third_classification):
            query['ThirdClassification'] = request.third_classification
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForceUploadTrademarkOnsale',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ForceUploadTrademarkOnsaleResponse(),
            self.call_api(params, req, runtime)
        )

    def force_upload_trademark_onsale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.force_upload_trademark_onsale_with_options(request, runtime)

    def generate_qr_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field_key):
            query['FieldKey'] = request.field_key
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateQrCode',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateQrCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_qr_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_qr_code_with_options(request, runtime)

    def generate_upload_file_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadFilePolicy',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateUploadFilePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_upload_file_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_file_policy_with_options(request, runtime)

    def get_authorization_letter_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationLetterVersion',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetAuthorizationLetterVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization_letter_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_letter_version_with_options(request, runtime)

    def get_default_principal_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultPrincipal',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_principal(self):
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_with_options(runtime)

    def get_default_principal_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultPrincipalName',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalNameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_principal_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_name_with_options(request, runtime)

    def get_notary_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notary_order_id):
            query['NotaryOrderId'] = request.notary_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNotaryOrder',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetNotaryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_notary_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_notary_order_with_options(request, runtime)

    def get_support_principal_name_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSupportPrincipalName',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetSupportPrincipalNameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_support_principal_name(self):
        runtime = util_models.RuntimeOptions()
        return self.get_support_principal_name_with_options(runtime)

    def insert_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_county):
            query['ContactCounty'] = request.contact_county
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        if not UtilClient.is_unset(request.contact_zipcode):
            query['ContactZipcode'] = request.contact_zipcode
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.eaddress):
            query['EAddress'] = request.eaddress
        if not UtilClient.is_unset(request.ename):
            query['EName'] = request.ename
        if not UtilClient.is_unset(request.id_card_name):
            query['IdCardName'] = request.id_card_name
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.id_card_oss_key):
            query['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.legal_notice_oss_key):
            query['LegalNoticeOssKey'] = request.legal_notice_oss_key
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passport_oss_key):
            query['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.town):
            query['Town'] = request.town
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_material_with_options(request, runtime)

    def insert_renew_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.eng_address):
            query['EngAddress'] = request.eng_address
        if not UtilClient.is_unset(request.eng_name):
            query['EngName'] = request.eng_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.register_time):
            query['RegisterTime'] = request.register_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertRenewInfo',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertRenewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_renew_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_renew_info_with_options(request, runtime)

    def insert_tm_monitor_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.InsertTmMonitorRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classification):
            request.classification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classification, 'Classification', 'json')
        if not UtilClient.is_unset(tmp_req.notify_status):
            request.notify_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_status, 'NotifyStatus', 'json')
        query = {}
        if not UtilClient.is_unset(request.classification_shrink):
            query['Classification'] = request.classification_shrink
        if not UtilClient.is_unset(request.end_apply_date):
            query['EndApplyDate'] = request.end_apply_date
        if not UtilClient.is_unset(request.notify_status_shrink):
            query['NotifyStatus'] = request.notify_status_shrink
        if not UtilClient.is_unset(request.rule_keyword):
            query['RuleKeyword'] = request.rule_keyword
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_apply_date):
            query['StartApplyDate'] = request.start_apply_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTmMonitorRule',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTmMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_tm_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_tm_monitor_rule_with_options(request, runtime)

    def list_notary_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.notary_type):
            query['NotaryType'] = request.notary_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotaryInfos',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_notary_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notary_infos_with_options(request, runtime)

    def list_notary_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_order_id):
            query['AliyunOrderId'] = request.aliyun_order_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end_order_date):
            query['EndOrderDate'] = request.end_order_date
        if not UtilClient.is_unset(request.notary_status):
            query['NotaryStatus'] = request.notary_status
        if not UtilClient.is_unset(request.notary_type):
            query['NotaryType'] = request.notary_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by_type):
            query['SortByType'] = request.sort_by_type
        if not UtilClient.is_unset(request.sort_key_type):
            query['SortKeyType'] = request.sort_key_type
        if not UtilClient.is_unset(request.start_order_date):
            query['StartOrderDate'] = request.start_order_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotaryOrders',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_notary_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notary_orders_with_options(request, runtime)

    def list_trademark_sbj_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrademarkSbjKey',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListTrademarkSbjKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trademark_sbj_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trademark_sbj_key_with_options(request, runtime)

    def modify_submit_transfer_materail_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.ModifySubmitTransferMaterailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.other):
            request.other_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other, 'Other', 'json')
        query = {}
        if not UtilClient.is_unset(request.assignee_proxy):
            query['AssigneeProxy'] = request.assignee_proxy
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_business_license_translation):
            query['BuyerBusinessLicenseTranslation'] = request.buyer_business_license_translation
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.seller_business_license_translation):
            query['SellerBusinessLicenseTranslation'] = request.seller_business_license_translation
        if not UtilClient.is_unset(request.trade_material_full_update):
            query['TradeMaterialFullUpdate'] = request.trade_material_full_update
        body = {}
        if not UtilClient.is_unset(request.addr):
            body['Addr'] = request.addr
        if not UtilClient.is_unset(request.buyer_business_license):
            body['BuyerBusinessLicense'] = request.buyer_business_license
        if not UtilClient.is_unset(request.buyer_id_card):
            body['BuyerIdCard'] = request.buyer_id_card
        if not UtilClient.is_unset(request.card_no):
            body['CardNo'] = request.card_no
        if not UtilClient.is_unset(request.card_type):
            body['CardType'] = request.card_type
        if not UtilClient.is_unset(request.complete):
            body['Complete'] = request.complete
        if not UtilClient.is_unset(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_mobile):
            body['ContactMobile'] = request.contact_mobile
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notarization):
            body['Notarization'] = request.notarization
        if not UtilClient.is_unset(request.other_shrink):
            body['Other'] = request.other_shrink
        if not UtilClient.is_unset(request.registration_cert):
            body['RegistrationCert'] = request.registration_cert
        if not UtilClient.is_unset(request.seller_apply):
            body['SellerApply'] = request.seller_apply
        if not UtilClient.is_unset(request.seller_business_license):
            body['SellerBusinessLicense'] = request.seller_business_license
        if not UtilClient.is_unset(request.seller_id_card):
            body['SellerIdCard'] = request.seller_id_card
        if not UtilClient.is_unset(request.seller_proxy):
            body['SellerProxy'] = request.seller_proxy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySubmitTransferMaterail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.ModifySubmitTransferMaterailResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_submit_transfer_materail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_submit_transfer_materail_with_options(request, runtime)

    def operate_produce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_map):
            query['ExtMap'] = request.ext_map
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateProduce',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.OperateProduceResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_produce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_produce_with_options(request, runtime)

    def partner_update_trademark_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.event_scene_type):
            body['EventSceneType'] = request.event_scene_type
        if not UtilClient.is_unset(request.intention_biz_id):
            body['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.tm_comment):
            body['TmComment'] = request.tm_comment
        if not UtilClient.is_unset(request.tm_icon):
            body['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            body['TmName'] = request.tm_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PartnerUpdateTrademarkName',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.PartnerUpdateTrademarkNameResponse(),
            self.call_api(params, req, runtime)
        )

    def partner_update_trademark_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.partner_update_trademark_name_with_options(request, runtime)

    def query_communication_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommunicationLogs',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCommunicationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_communication_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_communication_logs_with_options(request, runtime)

    def query_credentials_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        body = {}
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCredentialsInfo',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCredentialsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_credentials_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_credentials_info_with_options(request, runtime)

    def query_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_key):
            query['AttributeKey'] = request.attribute_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExtensionAttribute',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_extension_attribute_with_options(request, runtime)

    def query_intention_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntentionDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_intention_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_detail_with_options(request, runtime)

    def query_intention_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntentionList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_intention_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_list_with_options(request, runtime)

    def query_intention_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntentionOwner',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def query_intention_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_owner_with_options(request, runtime)

    def query_intention_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntentionPrice',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_intention_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_price_with_options(request, runtime)

    def query_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.query_unconfirmed_info):
            query['QueryUnconfirmedInfo'] = request.query_unconfirmed_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def query_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_material_with_options(request, runtime)

    def query_material_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.material_version):
            query['MaterialVersion'] = request.material_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.system_version):
            query['SystemVersion'] = request.system_version
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMaterialList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_material_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_material_list_with_options(request, runtime)

    def query_monitor_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonitorKeywords',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMonitorKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_monitor_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_keywords_with_options(request, runtime)

    def query_official_file_custom_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOfficialFileCustomList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOfficialFileCustomListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_official_file_custom_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_official_file_custom_list_with_options(request, runtime)

    def query_order_logistics_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.produce_order_id):
            body['ProduceOrderId'] = request.produce_order_id
        if not UtilClient.is_unset(request.register_number):
            body['RegisterNumber'] = request.register_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderLogisticsList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOrderLogisticsListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_order_logistics_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_logistics_list_with_options(request, runtime)

    def query_oss_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOssResources',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOssResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_oss_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_oss_resources_with_options(request, runtime)

    def query_produce_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_no):
            query['ApplyNo'] = request.apply_no
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProduceDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryProduceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_produce_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_produce_detail_with_options(request, runtime)

    def query_produce_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.create_time_left):
            query['CreateTimeLeft'] = request.create_time_left
        if not UtilClient.is_unset(request.create_time_right):
            query['CreateTimeRight'] = request.create_time_right
        if not UtilClient.is_unset(request.material_name):
            query['MaterialName'] = request.material_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProduceList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryProduceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_produce_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_produce_list_with_options(request, runtime)

    def query_qr_code_upload_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field_key):
            query['FieldKey'] = request.field_key
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQrCodeUploadStatus',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryQrCodeUploadStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_qr_code_upload_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_qr_code_upload_status_with_options(request, runtime)

    def query_sbj_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySbjRule',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QuerySbjRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sbj_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sbj_rule_with_options(request, runtime)

    def query_supplement_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySupplementDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QuerySupplementDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_supplement_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_supplement_detail_with_options(request, runtime)

    def query_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryTaskList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    def query_tm_collection_page_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmCollectionPageList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTmCollectionPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tm_collection_page_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tm_collection_page_list_with_options(request, runtime)

    def query_tm_sbj_produce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.high_priority_biz_type_str):
            query['HighPriorityBizTypeStr'] = request.high_priority_biz_type_str
        if not UtilClient.is_unset(request.high_priority_material_name_str):
            query['HighPriorityMaterialNameStr'] = request.high_priority_material_name_str
        if not UtilClient.is_unset(request.high_priority_order_id_str):
            query['HighPriorityOrderIdStr'] = request.high_priority_order_id_str
        if not UtilClient.is_unset(request.high_priority_user_id_str):
            query['HighPriorityUserIdStr'] = request.high_priority_user_id_str
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.producer_type):
            query['ProducerType'] = request.producer_type
        if not UtilClient.is_unset(request.query_order_page_size):
            query['QueryOrderPageSize'] = request.query_order_page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmSbjProduce',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTmSbjProduceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tm_sbj_produce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tm_sbj_produce_with_options(request, runtime)

    def query_tm_sbj_produce_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmSbjProduceDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTmSbjProduceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tm_sbj_produce_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tm_sbj_produce_detail_with_options(request, runtime)

    def query_trade_intention_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin):
            query['Begin'] = request.begin
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeIntentionUserList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeIntentionUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_intention_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_intention_user_list_with_options(request, runtime)

    def query_trade_mark_application_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeMarkApplicationDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_mark_application_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_detail_with_options(request, runtime)

    def query_trade_mark_application_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeMarkApplicationLogs',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_mark_application_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_logs_with_options(request, runtime)

    def query_trade_mark_applications_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTradeMarkApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.classification_code):
            query['ClassificationCode'] = request.classification_code
        if not UtilClient.is_unset(request.hidden):
            query['Hidden'] = request.hidden
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.logistics_no):
            query['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.material_name):
            query['MaterialName'] = request.material_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.supplement_status):
            query['SupplementStatus'] = request.supplement_status
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeMarkApplications',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_mark_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_with_options(request, runtime)

    def query_trade_mark_applications_by_intention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.intention_biz_id):
            query['IntentionBizId'] = request.intention_biz_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tm_produce_status):
            query['TmProduceStatus'] = request.tm_produce_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeMarkApplicationsByIntention',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_mark_applications_by_intention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_by_intention_with_options(request, runtime)

    def query_trade_produce_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeProduceDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_produce_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_detail_with_options(request, runtime)

    def query_trade_produce_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_status):
            query['BuyerStatus'] = request.buyer_status
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pre_order_id):
            query['PreOrderId'] = request.pre_order_id
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTradeProduceList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trade_produce_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_list_with_options(request, runtime)

    def query_trademark_detail_by_apply_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_number):
            query['ApplyNumber'] = request.apply_number
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkDetailByApplyNumber',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkDetailByApplyNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_detail_by_apply_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_detail_by_apply_number_with_options(request, runtime)

    def query_trademark_detail_by_apply_number_esp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_number):
            query['ApplyNumber'] = request.apply_number
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkDetailByApplyNumberEsp',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkDetailByApplyNumberEspResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_detail_by_apply_number_esp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_detail_by_apply_number_esp_with_options(request, runtime)

    def query_trademark_model_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.review_supplement_material):
            query['ReviewSupplementMaterial'] = request.review_supplement_material
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkModelDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkModelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_model_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_model_detail_with_options(request, runtime)

    def query_trademark_model_esp_detail_with_options(self, request, runtime):
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
            action='QueryTrademarkModelEspDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkModelEspDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_model_esp_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_model_esp_detail_with_options(request, runtime)

    def query_trademark_model_esp_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTrademarkModelEspListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exist_status):
            request.exist_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exist_status, 'ExistStatus', 'json')
        query = {}
        if not UtilClient.is_unset(request.additional_submit_status):
            query['AdditionalSubmitStatus'] = request.additional_submit_status
        if not UtilClient.is_unset(request.additional_submit_time):
            query['AdditionalSubmitTime'] = request.additional_submit_time
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.exist_status_shrink):
            query['ExistStatus'] = request.exist_status_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_ids_str):
            query['OrderIdsStr'] = request.order_ids_str
        if not UtilClient.is_unset(request.order_instance_id):
            query['OrderInstanceId'] = request.order_instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.submit_status):
            query['SubmitStatus'] = request.submit_status
        if not UtilClient.is_unset(request.submit_time):
            query['SubmitTime'] = request.submit_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkModelEspList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkModelEspListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_model_esp_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_model_esp_list_with_options(request, runtime)

    def query_trademark_model_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.order_ids_str):
            query['OrderIdsStr'] = request.order_ids_str
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.produce_types_str):
            query['ProduceTypesStr'] = request.produce_types_str
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.submit_start):
            query['SubmitStart'] = request.submit_start
        if not UtilClient.is_unset(request.submit_status):
            query['SubmitStatus'] = request.submit_status
        if not UtilClient.is_unset(request.submit_time):
            query['SubmitTime'] = request.submit_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkModelList',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkModelListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_model_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_model_list_with_options(request, runtime)

    def query_trademark_monitor_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.apply_year):
            query['ApplyYear'] = request.apply_year
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.procedure_status):
            query['ProcedureStatus'] = request.procedure_status
        if not UtilClient.is_unset(request.registration_number):
            query['RegistrationNumber'] = request.registration_number
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkMonitorResults',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_monitor_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_results_with_options(request, runtime)

    def query_trademark_monitor_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.notify_update):
            query['NotifyUpdate'] = request.notify_update
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkMonitorRules',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_monitor_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_rules_with_options(request, runtime)

    def query_trademark_on_sale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.register_code):
            query['RegisterCode'] = request.register_code
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.tm_type):
            query['TmType'] = request.tm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkOnSale',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkOnSaleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_on_sale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_on_sale_with_options(request, runtime)

    def query_trademark_price_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTrademarkPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_data):
            request.order_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_data, 'OrderData', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_data_shrink):
            query['OrderData'] = request.order_data_shrink
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkPrice',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_price_with_options(request, runtime)

    def query_trademark_upload_audit_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.register_code):
            query['RegisterCode'] = request.register_code
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.tm_type):
            query['TmType'] = request.tm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrademarkUploadAuditResult',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkUploadAuditResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_trademark_upload_audit_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_upload_audit_result_with_options(request, runtime)

    def record_bank_balance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_date):
            query['ActionDate'] = request.action_date
        if not UtilClient.is_unset(request.balance):
            query['Balance'] = request.balance
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordBankBalance',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.RecordBankBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    def record_bank_balance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.record_bank_balance_with_options(request, runtime)

    def refund_produce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.refund_type):
            query['RefundType'] = request.refund_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundProduce',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefundProduceResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_produce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_produce_with_options(request, runtime)

    def refuse_additional_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseAdditionalMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseAdditionalMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def refuse_additional_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_additional_material_with_options(request, runtime)

    def refuse_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseApplicant',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def refuse_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_applicant_with_options(request, runtime)

    def reject_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectApplicant',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.RejectApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_applicant_with_options(request, runtime)

    def save_classification_conditions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveClassificationConditions',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveClassificationConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    def save_classification_conditions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_classification_conditions_with_options(request, runtime)

    def save_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_key):
            query['AttributeKey'] = request.attribute_key
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveExtensionAttribute',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def save_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_extension_attribute_with_options(request, runtime)

    def save_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.request):
            query['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTask',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_with_options(request, runtime)

    def save_task_for_official_file_custom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_accept_time):
            query['EndAcceptTime'] = request.end_accept_time
        if not UtilClient.is_unset(request.start_accept_time):
            query['StartAcceptTime'] = request.start_accept_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForOfficialFileCustom',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskForOfficialFileCustomResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_official_file_custom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_official_file_custom_with_options(request, runtime)

    def save_trade_mark_review_material_detail_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SaveTradeMarkReviewMaterialDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_oss_key_list):
            request.additional_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_oss_key_list, 'AdditionalOssKeyList', 'json')
        body = {}
        if not UtilClient.is_unset(request.additional_oss_key_list_shrink):
            body['AdditionalOssKeyList'] = request.additional_oss_key_list_shrink
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.application_oss_key):
            body['ApplicationOssKey'] = request.application_oss_key
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.business_licence_oss_key):
            body['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            body['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.change_name):
            body['ChangeName'] = request.change_name
        if not UtilClient.is_unset(request.contact_address):
            body['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_email):
            body['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            body['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.eng_address):
            body['EngAddress'] = request.eng_address
        if not UtilClient.is_unset(request.eng_name):
            body['EngName'] = request.eng_name
        if not UtilClient.is_unset(request.id_card_oss_key):
            body['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.legal_notice_oss_key):
            body['LegalNoticeOssKey'] = request.legal_notice_oss_key
        if not UtilClient.is_unset(request.loa_oss_key):
            body['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.passport_oss_key):
            body['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.review_material_additional_json):
            body['ReviewMaterialAdditionalJson'] = request.review_material_additional_json
        if not UtilClient.is_unset(request.separate):
            body['Separate'] = request.separate
        if not UtilClient.is_unset(request.submit_online):
            body['SubmitOnline'] = request.submit_online
        if not UtilClient.is_unset(request.submit_type):
            body['SubmitType'] = request.submit_type
        if not UtilClient.is_unset(request.supplement_flag):
            body['SupplementFlag'] = request.supplement_flag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTradeMarkReviewMaterialDetail',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def save_trade_mark_review_material_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_trade_mark_review_material_detail_with_options(request, runtime)

    def sbj_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.apply_no):
            query['ApplyNo'] = request.apply_no
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.file_date):
            query['FileDate'] = request.file_date
        if not UtilClient.is_unset(request.file_oss_key):
            query['FileOssKey'] = request.file_oss_key
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.order_no):
            query['OrderNo'] = request.order_no
        if not UtilClient.is_unset(request.receipt_oss_key):
            query['ReceiptOssKey'] = request.receipt_oss_key
        if not UtilClient.is_unset(request.submitted_success):
            query['SubmittedSuccess'] = request.submitted_success
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SbjOperate',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SbjOperateResponse(),
            self.call_api(params, req, runtime)
        )

    def sbj_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sbj_operate_with_options(request, runtime)

    def sbj_operate_new_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_submit_count):
            query['AddSubmitCount'] = request.add_submit_count
        if not UtilClient.is_unset(request.allow_resubmit):
            query['AllowResubmit'] = request.allow_resubmit
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.apply_no):
            query['ApplyNo'] = request.apply_no
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.change_status):
            query['ChangeStatus'] = request.change_status
        if not UtilClient.is_unset(request.error_msg_screenshot):
            query['ErrorMsgScreenshot'] = request.error_msg_screenshot
        if not UtilClient.is_unset(request.file_date):
            query['FileDate'] = request.file_date
        if not UtilClient.is_unset(request.file_oss_key):
            query['FileOssKey'] = request.file_oss_key
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.order_no):
            query['OrderNo'] = request.order_no
        if not UtilClient.is_unset(request.receipt_oss_key):
            query['ReceiptOssKey'] = request.receipt_oss_key
        if not UtilClient.is_unset(request.submitted_success):
            query['SubmittedSuccess'] = request.submitted_success
        if not UtilClient.is_unset(request.success_type):
            query['SuccessType'] = request.success_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SbjOperateNew',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SbjOperateNewResponse(),
            self.call_api(params, req, runtime)
        )

    def sbj_operate_new(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sbj_operate_new_with_options(request, runtime)

    def sbrain_service_execute_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SbrainServiceExecuteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_params):
            request.execute_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_params, 'ExecuteParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.execute_params_shrink):
            query['ExecuteParams'] = request.execute_params_shrink
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.reference_no):
            query['ReferenceNo'] = request.reference_no
        if not UtilClient.is_unset(request.reference_type):
            query['ReferenceType'] = request.reference_type
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        if not UtilClient.is_unset(request.service_place):
            query['ServicePlace'] = request.service_place
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SbrainServiceExecute',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SbrainServiceExecuteResponse(),
            self.call_api(params, req, runtime)
        )

    def sbrain_service_execute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sbrain_service_execute_with_options(request, runtime)

    def sbrain_service_has_running_task_batch_query_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SbrainServiceHasRunningTaskBatchQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_nos):
            request.reference_nos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_nos, 'ReferenceNos', 'json')
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.reference_nos_shrink):
            query['ReferenceNos'] = request.reference_nos_shrink
        if not UtilClient.is_unset(request.reference_type):
            query['ReferenceType'] = request.reference_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SbrainServiceHasRunningTaskBatchQuery',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SbrainServiceHasRunningTaskBatchQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def sbrain_service_has_running_task_batch_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sbrain_service_has_running_task_batch_query_with_options(request, runtime)

    def sbrain_service_scheme_match_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SbrainServiceSchemeMatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.match_params):
            request.match_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.match_params, 'MatchParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.match_params_shrink):
            query['MatchParams'] = request.match_params_shrink
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.reference_no):
            query['ReferenceNo'] = request.reference_no
        if not UtilClient.is_unset(request.reference_type):
            query['ReferenceType'] = request.reference_type
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SbrainServiceSchemeMatch',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SbrainServiceSchemeMatchResponse(),
            self.call_api(params, req, runtime)
        )

    def sbrain_service_scheme_match(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sbrain_service_scheme_match_with_options(request, runtime)

    def search_tm_onsales_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_price_left):
            query['OrderPriceLeft'] = request.order_price_left
        if not UtilClient.is_unset(request.order_price_right):
            query['OrderPriceRight'] = request.order_price_right
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.query_all):
            query['QueryAll'] = request.query_all
        if not UtilClient.is_unset(request.reg_left):
            query['RegLeft'] = request.reg_left
        if not UtilClient.is_unset(request.reg_right):
            query['RegRight'] = request.reg_right
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.sort_name):
            query['SortName'] = request.sort_name
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.top_search):
            query['TopSearch'] = request.top_search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTmOnsales',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SearchTmOnsalesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_tm_onsales(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_tm_onsales_with_options(request, runtime)

    def start_notary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notary_order_id):
            query['NotaryOrderId'] = request.notary_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNotary',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.StartNotaryResponse(),
            self.call_api(params, req, runtime)
        )

    def start_notary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_notary_with_options(request, runtime)

    def store_material_temporarily_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_county):
            query['ContactCounty'] = request.contact_county
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        if not UtilClient.is_unset(request.contact_zipcode):
            query['ContactZipcode'] = request.contact_zipcode
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.eaddress):
            query['EAddress'] = request.eaddress
        if not UtilClient.is_unset(request.ename):
            query['EName'] = request.ename
        if not UtilClient.is_unset(request.id_card_name):
            query['IdCardName'] = request.id_card_name
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.id_card_oss_key):
            query['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.legal_notice_oss_key):
            query['LegalNoticeOssKey'] = request.legal_notice_oss_key
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passport_oss_key):
            query['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.town):
            query['Town'] = request.town
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StoreMaterialTemporarily',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.StoreMaterialTemporarilyResponse(),
            self.call_api(params, req, runtime)
        )

    def store_material_temporarily(self, request):
        runtime = util_models.RuntimeOptions()
        return self.store_material_temporarily_with_options(request, runtime)

    def submit_supplement_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_oss_key_list):
            request.upload_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upload_oss_key_list, 'UploadOssKeyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.upload_oss_key_list_shrink):
            query['UploadOssKeyList'] = request.upload_oss_key_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSupplement',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_supplement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_supplement_with_options(request, runtime)

    def submit_trademark_application_complaint_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitTrademarkApplicationComplaintShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTrademarkApplicationComplaint',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_trademark_application_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_trademark_application_complaint_with_options(request, runtime)

    def sync_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.classification_code):
            query['ClassificationCode'] = request.classification_code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.original_price):
            query['OriginalPrice'] = request.original_price
        if not UtilClient.is_unset(request.owner_en_name):
            query['OwnerEnName'] = request.owner_en_name
        if not UtilClient.is_unset(request.owner_name):
            query['OwnerName'] = request.owner_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_ann_date):
            query['RegAnnDate'] = request.reg_ann_date
        if not UtilClient.is_unset(request.secondary_classification):
            query['SecondaryClassification'] = request.secondary_classification
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_classification):
            query['ThirdClassification'] = request.third_classification
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncTrademark',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.SyncTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_trademark_with_options(request, runtime)

    def update_applicant_contacter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        if not UtilClient.is_unset(request.contact_zip_code):
            query['ContactZipCode'] = request.contact_zip_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicantContacter',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateApplicantContacterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_applicant_contacter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_applicant_contacter_with_options(request, runtime)

    def update_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_address):
            query['ContactAddress'] = request.contact_address
        if not UtilClient.is_unset(request.contact_city):
            query['ContactCity'] = request.contact_city
        if not UtilClient.is_unset(request.contact_county):
            query['ContactCounty'] = request.contact_county
        if not UtilClient.is_unset(request.contact_district):
            query['ContactDistrict'] = request.contact_district
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_province):
            query['ContactProvince'] = request.contact_province
        if not UtilClient.is_unset(request.contact_zipcode):
            query['ContactZipcode'] = request.contact_zipcode
        if not UtilClient.is_unset(request.eaddress):
            query['EAddress'] = request.eaddress
        if not UtilClient.is_unset(request.ename):
            query['EName'] = request.ename
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.id_card_name):
            query['IdCardName'] = request.id_card_name
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.id_card_oss_key):
            query['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.legal_notice_oss_key):
            query['LegalNoticeOssKey'] = request.legal_notice_oss_key
        if not UtilClient.is_unset(request.loa_id):
            query['LoaId'] = request.loa_id
        if not UtilClient.is_unset(request.loa_oss_key):
            query['LoaOssKey'] = request.loa_oss_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passport_oss_key):
            query['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.town):
            query['Town'] = request.town
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMaterial',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def update_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_material_with_options(request, runtime)

    def update_produce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_map):
            query['ExtMap'] = request.ext_map
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProduce',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateProduceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_produce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_produce_with_options(request, runtime)

    def update_produce_loa_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.loa_oss_key):
            body['LoaOssKey'] = request.loa_oss_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduceLoaId',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateProduceLoaIdResponse(),
            self.call_api(params, req, runtime)
        )

    def update_produce_loa_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_produce_loa_id_with_options(request, runtime)

    def update_send_material_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSendMaterialNum',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateSendMaterialNumResponse(),
            self.call_api(params, req, runtime)
        )

    def update_send_material_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_send_material_num_with_options(request, runtime)

    def update_trademark_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.tm_comment):
            body['TmComment'] = request.tm_comment
        if not UtilClient.is_unset(request.tm_icon):
            body['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            body['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrademarkName',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_trademark_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_name_with_options(request, runtime)

    def update_trademark_onsale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.classification_code):
            query['ClassificationCode'] = request.classification_code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.original_price):
            query['OriginalPrice'] = request.original_price
        if not UtilClient.is_unset(request.owner_en_name):
            query['OwnerEnName'] = request.owner_en_name
        if not UtilClient.is_unset(request.owner_name):
            query['OwnerName'] = request.owner_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_ann_date):
            query['RegAnnDate'] = request.reg_ann_date
        if not UtilClient.is_unset(request.secondary_classification):
            query['SecondaryClassification'] = request.secondary_classification
        if not UtilClient.is_unset(request.third_classification):
            query['ThirdClassification'] = request.third_classification
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.tm_type):
            query['TmType'] = request.tm_type
        if not UtilClient.is_unset(request.trade_tm_detail_json):
            query['TradeTmDetailJson'] = request.trade_tm_detail_json
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrademarkOnsale',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkOnsaleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_trademark_onsale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_onsale_with_options(request, runtime)

    def upload_notary_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.notary_type):
            query['NotaryType'] = request.notary_type
        if not UtilClient.is_unset(request.upload_context):
            query['UploadContext'] = request.upload_context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadNotaryData',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadNotaryDataResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_notary_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_notary_data_with_options(request, runtime)

    def upload_trademark_on_sale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.classification_code):
            query['ClassificationCode'] = request.classification_code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.original_price):
            query['OriginalPrice'] = request.original_price
        if not UtilClient.is_unset(request.owner_en_name):
            query['OwnerEnName'] = request.owner_en_name
        if not UtilClient.is_unset(request.owner_name):
            query['OwnerName'] = request.owner_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_ann_date):
            query['RegAnnDate'] = request.reg_ann_date
        if not UtilClient.is_unset(request.secondary_classification):
            query['SecondaryClassification'] = request.secondary_classification
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_classification):
            query['ThirdClassification'] = request.third_classification
        if not UtilClient.is_unset(request.tm_icon):
            query['TmIcon'] = request.tm_icon
        if not UtilClient.is_unset(request.tm_name):
            query['TmName'] = request.tm_name
        if not UtilClient.is_unset(request.tm_number):
            query['TmNumber'] = request.tm_number
        if not UtilClient.is_unset(request.tm_type):
            query['TmType'] = request.tm_type
        if not UtilClient.is_unset(request.trade_tm_detail_json):
            query['TradeTmDetailJson'] = request.trade_tm_detail_json
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadTrademarkOnSale',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadTrademarkOnSaleResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_trademark_on_sale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_trademark_on_sale_with_options(request, runtime)

    def write_communication_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WriteCommunicationLog',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteCommunicationLogResponse(),
            self.call_api(params, req, runtime)
        )

    def write_communication_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.write_communication_log_with_options(request, runtime)

    def write_intention_communication_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.reject):
            query['Reject'] = request.reject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WriteIntentionCommunicationLog',
            version='2018-07-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteIntentionCommunicationLogResponse(),
            self.call_api(params, req, runtime)
        )

    def write_intention_communication_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.write_intention_communication_log_with_options(request, runtime)
