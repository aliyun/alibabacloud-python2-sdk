# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trademark20190902 import models as trademark_20190902_models
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

    def bind_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.BindApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_applicant_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    def check_authorization_letter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.color):
            query['Color'] = request.color
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAuthorizationLetter',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    def check_authorization_letter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_authorization_letter_with_options(request, runtime)

    def check_biz_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBizAvailable',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckBizAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_biz_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_biz_available_with_options(request, runtime)

    def check_duplicate_applicant_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.event_scene_type):
            query['EventSceneType'] = request.event_scene_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDuplicateApplicantRisk',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckDuplicateApplicantRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def check_duplicate_applicant_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_duplicate_applicant_risk_with_options(request, runtime)

    def check_duplicate_classification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.event_scene_type):
            query['EventSceneType'] = request.event_scene_type
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDuplicateClassification',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckDuplicateClassificationResponse(),
            self.call_api(params, req, runtime)
        )

    def check_duplicate_classification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_duplicate_classification_with_options(request, runtime)

    def check_duplicate_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.event_scene_type):
            query['EventSceneType'] = request.event_scene_type
        if not UtilClient.is_unset(request.material_name):
            query['MaterialName'] = request.material_name
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDuplicateTrademark',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckDuplicateTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    def check_duplicate_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_duplicate_trademark_with_options(request, runtime)

    def check_material_validity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_license_oss_key):
            query['BusinessLicenseOssKey'] = request.business_license_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.id_card_name):
            query['IdCardName'] = request.id_card_name
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.id_card_oss_key):
            query['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.material_region):
            query['MaterialRegion'] = request.material_region
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMaterialValidity',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckMaterialValidityResponse(),
            self.call_api(params, req, runtime)
        )

    def check_material_validity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_material_validity_with_options(request, runtime)

    def check_trademark_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_scene_type):
            query['EventSceneType'] = request.event_scene_type
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTrademarkName',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CheckTrademarkNameResponse(),
            self.call_api(params, req, runtime)
        )

    def check_trademark_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_name_with_options(request, runtime)

    def close_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CloseTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def close_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_trademark_application_with_options(request, runtime)

    def combine_authorization_letter_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.tm_produce_type):
            query['TmProduceType'] = request.tm_produce_type
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CombineAuthorizationLetter',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CombineAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    def combine_authorization_letter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.combine_authorization_letter_with_options(request, runtime)

    def complement_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_id):
            query['AgreementId'] = request.agreement_id
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.is_black_icon):
            query['IsBlackIcon'] = request.is_black_icon
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.order_data):
            query['OrderData'] = request.order_data
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.trademark_comment):
            query['TrademarkComment'] = request.trademark_comment
        if not UtilClient.is_unset(request.trademark_icon_oss_key):
            query['TrademarkIconOssKey'] = request.trademark_icon_oss_key
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.trademark_name_type):
            query['TrademarkNameType'] = request.trademark_name_type
        if not UtilClient.is_unset(request.trademark_type):
            query['TrademarkType'] = request.trademark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComplementTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ComplementTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def complement_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complement_trademark_application_with_options(request, runtime)

    def confirm_expert_solution_with_options(self, request, runtime):
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
            action='ConfirmExpertSolution',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ConfirmExpertSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_expert_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_expert_solution_with_options(request, runtime)

    def create_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.applicant_region):
            query['ApplicantRegion'] = request.applicant_region
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
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
        if not UtilClient.is_unset(request.passport_oss_key):
            query['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CreateApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def create_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_applicant_with_options(request, runtime)

    def create_commodity_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20190902_models.CreateCommodityOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.order_params):
            request.order_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_params, 'OrderParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.components_shrink):
            query['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_params_shrink):
            query['OrderParams'] = request.order_params_shrink
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.spec_code):
            query['SpecCode'] = request.spec_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommodityOrder',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CreateCommodityOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_commodity_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_commodity_order_with_options(request, runtime)

    def create_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_id):
            query['AgreementId'] = request.agreement_id
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.black_and_white_icon):
            query['BlackAndWhiteIcon'] = request.black_and_white_icon
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.classifications):
            query['Classifications'] = request.classifications
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.legal_notice_key):
            query['LegalNoticeKey'] = request.legal_notice_key
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.payment_callback):
            query['PaymentCallback'] = request.payment_callback
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.trademark_comment):
            query['TrademarkComment'] = request.trademark_comment
        if not UtilClient.is_unset(request.trademark_icon):
            query['TrademarkIcon'] = request.trademark_icon
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.trademark_name_type):
            query['TrademarkNameType'] = request.trademark_name_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    def create_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_id):
            query['AgreementId'] = request.agreement_id
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.black_and_white_icon):
            query['BlackAndWhiteIcon'] = request.black_and_white_icon
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.classifications):
            query['Classifications'] = request.classifications
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.legal_notice_key):
            query['LegalNoticeKey'] = request.legal_notice_key
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.trademark_comment):
            query['TrademarkComment'] = request.trademark_comment
        if not UtilClient.is_unset(request.trademark_icon):
            query['TrademarkIcon'] = request.trademark_icon
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.trademark_name_type):
            query['TrademarkNameType'] = request.trademark_name_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.CreateTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_trademark_application_with_options(request, runtime)

    def delete_search_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.condition_id):
            query['ConditionId'] = request.condition_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.umid):
            query['Umid'] = request.umid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSearchCondition',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DeleteSearchConditionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_search_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_search_condition_with_options(request, runtime)

    def describe_admin_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdminTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeAdminTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_admin_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_admin_trademark_application_with_options(request, runtime)

    def describe_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_applicant_with_options(request, runtime)

    def describe_partner_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePartnerTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribePartnerTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_partner_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_partner_trademark_application_with_options(request, runtime)

    def describe_qualification_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tb_uid):
            query['TbUid'] = request.tb_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualificationStatus',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeQualificationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_qualification_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_qualification_status_with_options(request, runtime)

    def describe_supplement_with_options(self, request, runtime):
        """
        ***\
        

        @param request: DescribeSupplementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSupplementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupplement',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_supplement(self, request):
        """
        ***\
        

        @param request: DescribeSupplementRequest

        @return: DescribeSupplementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_supplement_with_options(request, runtime)

    def describe_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrademarkApplication',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeTrademarkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trademark_application_with_options(request, runtime)

    def describe_trademark_detail_for_inner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.umid):
            query['Umid'] = request.umid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrademarkDetailForInner',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.DescribeTrademarkDetailForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trademark_detail_for_inner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trademark_detail_for_inner_with_options(request, runtime)

    def generate_upload_file_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadFilePolicy',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.GenerateUploadFilePolicyResponse(),
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
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.GetAlipayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alipay_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alipay_url_with_options(request, runtime)

    def get_order_confirm_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        if not UtilClient.is_unset(request.out_trace_code):
            query['OutTraceCode'] = request.out_trace_code
        if not UtilClient.is_unset(request.out_trace_type):
            query['OutTraceType'] = request.out_trace_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderConfirmUrl',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.GetOrderConfirmUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_order_confirm_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_order_confirm_url_with_options(request, runtime)

    def get_sts_by_taobao_uid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.tb_uid):
            query['TbUid'] = request.tb_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStsByTaobaoUid',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.GetStsByTaobaoUidResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sts_by_taobao_uid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sts_by_taobao_uid_with_options(request, runtime)

    def list_admin_trademark_application_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdminTrademarkApplicationLogs',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListAdminTrademarkApplicationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_admin_trademark_application_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_admin_trademark_application_logs_with_options(request, runtime)

    def list_admin_trademark_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.application_status):
            query['ApplicationStatus'] = request.application_status
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.supplement_status):
            query['SupplementStatus'] = request.supplement_status
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.trademark_number):
            query['TrademarkNumber'] = request.trademark_number
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdminTrademarkApplications',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListAdminTrademarkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_admin_trademark_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_admin_trademark_applications_with_options(request, runtime)

    def list_applicants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.applicant_region):
            query['ApplicantRegion'] = request.applicant_region
        if not UtilClient.is_unset(request.applicant_type):
            query['ApplicantType'] = request.applicant_type
        if not UtilClient.is_unset(request.applicant_version):
            query['ApplicantVersion'] = request.applicant_version
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.system_version):
            query['SystemVersion'] = request.system_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicants',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListApplicantsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applicants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applicants_with_options(request, runtime)

    def list_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.parent_code):
            query['ParentCode'] = request.parent_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAreas',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_areas_with_options(request, runtime)

    def list_classification_conditions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClassificationConditions',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListClassificationConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_classification_conditions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_classification_conditions_with_options(request, runtime)

    def list_classifications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_code):
            query['ParentCode'] = request.parent_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClassifications',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListClassificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_classifications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_classifications_with_options(request, runtime)

    def list_trademark_application_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrademarkApplicationLogs',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListTrademarkApplicationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trademark_application_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trademark_application_logs_with_options(request, runtime)

    def list_trademark_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.application_status):
            query['ApplicationStatus'] = request.application_status
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.create_time_left):
            query['CreateTimeLeft'] = request.create_time_left
        if not UtilClient.is_unset(request.create_time_right):
            query['CreateTimeRight'] = request.create_time_right
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.query_voucher_order_done_flag):
            query['QueryVoucherOrderDoneFlag'] = request.query_voucher_order_done_flag
        if not UtilClient.is_unset(request.query_voucher_order_flag):
            query['QueryVoucherOrderFlag'] = request.query_voucher_order_flag
        if not UtilClient.is_unset(request.sort_filed):
            query['SortFiled'] = request.sort_filed
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.supplement_status):
            query['SupplementStatus'] = request.supplement_status
        if not UtilClient.is_unset(request.trademark_name):
            query['TrademarkName'] = request.trademark_name
        if not UtilClient.is_unset(request.trademark_number):
            query['TrademarkNumber'] = request.trademark_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrademarkApplications',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListTrademarkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trademark_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trademark_applications_with_options(request, runtime)

    def list_trademark_search_for_inner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_begin_time):
            query['ApplyBeginTime'] = request.apply_begin_time
        if not UtilClient.is_unset(request.apply_end_time):
            query['ApplyEndTime'] = request.apply_end_time
        if not UtilClient.is_unset(request.classification):
            query['Classification'] = request.classification
        if not UtilClient.is_unset(request.if_precision):
            query['IfPrecision'] = request.if_precision
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_preference):
            query['SearchPreference'] = request.search_preference
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.umid):
            query['Umid'] = request.umid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrademarkSearchForInner',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.ListTrademarkSearchForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trademark_search_for_inner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trademark_search_for_inner_with_options(request, runtime)

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
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.PutMeasureDataResponse(),
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
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.PutMeasureReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    def put_measure_ready_flag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_measure_ready_flag_with_options(request, runtime)

    def query_activity_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.floor_index):
            query['FloorIndex'] = request.floor_index
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.um_id):
            query['UmId'] = request.um_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryActivityItems',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.QueryActivityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_activity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_activity_items_with_options(request, runtime)

    def query_aliyun_uid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tb_uid):
            query['TbUid'] = request.tb_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAliyunUid',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.QueryAliyunUidResponse(),
            self.call_api(params, req, runtime)
        )

    def query_aliyun_uid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_aliyun_uid_with_options(request, runtime)

    def query_detail_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail_convert_type):
            query['DetailConvertType'] = request.detail_convert_type
        if not UtilClient.is_unset(request.detail_id):
            query['DetailId'] = request.detail_id
        if not UtilClient.is_unset(request.detail_type):
            query['DetailType'] = request.detail_type
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDetailItem',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.QueryDetailItemResponse(),
            self.call_api(params, req, runtime)
        )

    def query_detail_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_detail_item_with_options(request, runtime)

    def query_remain_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRemainResources',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.QueryRemainResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_remain_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_remain_resources_with_options(request, runtime)

    def refuse_supplement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseSupplement',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.RefuseSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    def refuse_supplement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_supplement_with_options(request, runtime)

    def reject_expert_solution_with_options(self, request, runtime):
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
            action='RejectExpertSolution',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.RejectExpertSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_expert_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_expert_solution_with_options(request, runtime)

    def remove_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.RemoveApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_applicant_with_options(request, runtime)

    def save_search_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.condition_content):
            body['ConditionContent'] = request.condition_content
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.umid):
            body['Umid'] = request.umid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveSearchCondition',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SaveSearchConditionResponse(),
            self.call_api(params, req, runtime)
        )

    def save_search_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_search_condition_with_options(request, runtime)

    def save_temporary_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.complete_applicant):
            query['CompleteApplicant'] = request.complete_applicant
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
        if not UtilClient.is_unset(request.contact_zip_code):
            query['ContactZipCode'] = request.contact_zip_code
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.eaddress):
            query['EAddress'] = request.eaddress
        if not UtilClient.is_unset(request.ename):
            query['EName'] = request.ename
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
            action='SaveTemporaryApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SaveTemporaryApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def save_temporary_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_temporary_applicant_with_options(request, runtime)

    def search_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.excluded_tags):
            query['ExcludedTags'] = request.excluded_tags
        if not UtilClient.is_unset(request.excluded_uids):
            query['ExcludedUids'] = request.excluded_uids
        if not UtilClient.is_unset(request.feeds_type):
            query['FeedsType'] = request.feeds_type
        if not UtilClient.is_unset(request.int_cls):
            query['IntCls'] = request.int_cls
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.price_left):
            query['PriceLeft'] = request.price_left
        if not UtilClient.is_unset(request.price_right):
            query['PriceRight'] = request.price_right
        if not UtilClient.is_unset(request.products):
            query['Products'] = request.products
        if not UtilClient.is_unset(request.register_number):
            query['RegisterNumber'] = request.register_number
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.trademark_name_length):
            query['TrademarkNameLength'] = request.trademark_name_length
        if not UtilClient.is_unset(request.trademark_name_type):
            query['TrademarkNameType'] = request.trademark_name_type
        if not UtilClient.is_unset(request.um_id):
            query['UmId'] = request.um_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchItems',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SearchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def search_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_items_with_options(request, runtime)

    def search_similarity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20190902_models.SearchSimilarityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classifications):
            request.classifications_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classifications, 'Classifications', 'json')
        if not UtilClient.is_unset(tmp_req.similar_groups):
            request.similar_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.similar_groups, 'SimilarGroups', 'json')
        query = {}
        if not UtilClient.is_unset(request.classifications_shrink):
            query['Classifications'] = request.classifications_shrink
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_uri_list):
            query['NameUriList'] = request.name_uri_list
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        if not UtilClient.is_unset(request.similar_groups_shrink):
            query['SimilarGroups'] = request.similar_groups_shrink
        if not UtilClient.is_unset(request.sorter):
            query['Sorter'] = request.sorter
        if not UtilClient.is_unset(request.umid):
            query['Umid'] = request.umid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchSimilarity',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SearchSimilarityResponse(),
            self.call_api(params, req, runtime)
        )

    def search_similarity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_similarity_with_options(request, runtime)

    def search_similarity_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20190902_models.SearchSimilarityListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classifications):
            request.classifications_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classifications, 'Classifications', 'json')
        if not UtilClient.is_unset(tmp_req.similar_groups):
            request.similar_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.similar_groups, 'SimilarGroups', 'json')
        query = {}
        if not UtilClient.is_unset(request.classifications_shrink):
            query['Classifications'] = request.classifications_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.similar_groups_shrink):
            query['SimilarGroups'] = request.similar_groups_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.success_search_type):
            query['SuccessSearchType'] = request.success_search_type
        if not UtilClient.is_unset(request.umid):
            query['Umid'] = request.umid
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchSimilarityList',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SearchSimilarityListResponse(),
            self.call_api(params, req, runtime)
        )

    def search_similarity_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_similarity_list_with_options(request, runtime)

    def send_message_to_user_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20190902_models.SendMessageToUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_data):
            request.template_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_data, 'TemplateData', 'json')
        query = {}
        if not UtilClient.is_unset(request.receiver_nick_name):
            query['ReceiverNickName'] = request.receiver_nick_name
        if not UtilClient.is_unset(request.sender_nick_name):
            query['SenderNickName'] = request.sender_nick_name
        if not UtilClient.is_unset(request.template_data_shrink):
            query['TemplateData'] = request.template_data_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessageToUser',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SendMessageToUserResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message_to_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_to_user_with_options(request, runtime)

    def submit_supplement_with_options(self, tmp_req, runtime):
        """
        **\
        

        @param tmp_req: SubmitSupplementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitSupplementResponse
        """
        UtilClient.validate_model(tmp_req)
        request = trademark_20190902_models.SubmitSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_files):
            request.user_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_files, 'UserFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        if not UtilClient.is_unset(request.user_files_shrink):
            query['UserFiles'] = request.user_files_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSupplement',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.SubmitSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_supplement(self, request):
        """
        **\
        

        @param request: SubmitSupplementRequest

        @return: SubmitSupplementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_supplement_with_options(request, runtime)

    def update_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.applicant_id):
            query['ApplicantId'] = request.applicant_id
        if not UtilClient.is_unset(request.applicant_name):
            query['ApplicantName'] = request.applicant_name
        if not UtilClient.is_unset(request.authorization_oss_key):
            query['AuthorizationOssKey'] = request.authorization_oss_key
        if not UtilClient.is_unset(request.business_licence_oss_key):
            query['BusinessLicenceOssKey'] = request.business_licence_oss_key
        if not UtilClient.is_unset(request.card_number):
            query['CardNumber'] = request.card_number
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
        if not UtilClient.is_unset(request.id_card_name):
            query['IdCardName'] = request.id_card_name
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.id_card_oss_key):
            query['IdCardOssKey'] = request.id_card_oss_key
        if not UtilClient.is_unset(request.legal_notice_oss_key):
            query['LegalNoticeOssKey'] = request.legal_notice_oss_key
        if not UtilClient.is_unset(request.passport_oss_key):
            query['PassportOssKey'] = request.passport_oss_key
        if not UtilClient.is_unset(request.personal_type):
            query['PersonalType'] = request.personal_type
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicant',
            version='2019-09-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trademark_20190902_models.UpdateApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    def update_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_applicant_with_options(request, runtime)
