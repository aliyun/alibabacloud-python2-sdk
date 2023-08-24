# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20221125 import models as cloudauth_20221125_models
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
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def ent_element_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntElementVerify',
            version='2022-11-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20221125_models.EntElementVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def ent_element_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ent_element_verify_with_options(request, runtime)

    def ent_risk_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.param_value):
            query['ParamValue'] = request.param_value
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntRiskQuery',
            version='2022-11-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20221125_models.EntRiskQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def ent_risk_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ent_risk_query_with_options(request, runtime)

    def ent_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_no):
            query['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.ent_name):
            query['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.info_verify_type):
            query['InfoVerifyType'] = request.info_verify_type
        if not UtilClient.is_unset(request.legal_person_cert_no):
            query['LegalPersonCertNo'] = request.legal_person_cert_no
        if not UtilClient.is_unset(request.legal_person_mobile):
            query['LegalPersonMobile'] = request.legal_person_mobile
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.risk_model_version):
            query['RiskModelVersion'] = request.risk_model_version
        if not UtilClient.is_unset(request.risk_verify_type):
            query['RiskVerifyType'] = request.risk_verify_type
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.user_authorization):
            query['UserAuthorization'] = request.user_authorization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EntVerify',
            version='2022-11-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20221125_models.EntVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def ent_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ent_verify_with_options(request, runtime)
