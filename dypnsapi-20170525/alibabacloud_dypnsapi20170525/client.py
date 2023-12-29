# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypnsapi20170525 import models as dypnsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dypnsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_sms_verify_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.case_auth_policy):
            query['CaseAuthPolicy'] = request.case_auth_policy
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSmsVerifyCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.CheckSmsVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def check_sms_verify_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_sms_verify_code_with_options(request, runtime)

    def create_scheme_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_package_name):
            query['AndroidPackageName'] = request.android_package_name
        if not UtilClient.is_unset(request.android_package_sign):
            query['AndroidPackageSign'] = request.android_package_sign
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.h_5origin):
            query['H5Origin'] = request.h_5origin
        if not UtilClient.is_unset(request.h_5url):
            query['H5Url'] = request.h_5url
        if not UtilClient.is_unset(request.ios_bundle_id):
            query['IosBundleId'] = request.ios_bundle_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemeConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.CreateSchemeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scheme_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scheme_config_with_options(request, runtime)

    def create_verify_scheme_with_options(self, request, runtime):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateVerifySchemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVerifySchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not UtilClient.is_unset(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not UtilClient.is_unset(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pack_name):
            query['PackName'] = request.pack_name
        if not UtilClient.is_unset(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifyScheme',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.CreateVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_verify_scheme(self, request):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateVerifySchemeRequest

        @return: CreateVerifySchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_verify_scheme_with_options(request, runtime)

    def delete_verify_scheme_with_options(self, request, runtime):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteVerifySchemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVerifySchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVerifyScheme',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.DeleteVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_verify_scheme(self, request):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteVerifySchemeRequest

        @return: DeleteVerifySchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_verify_scheme_with_options(request, runtime)

    def describe_verify_scheme_with_options(self, request, runtime):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeVerifySchemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVerifySchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyScheme',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.DescribeVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_verify_scheme(self, request):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeVerifySchemeRequest

        @return: DescribeVerifySchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_scheme_with_options(request, runtime)

    def get_auth_token_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the phone number verification feature for HTML5 pages](~~169786~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetAuthTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAuthTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auth_token(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the phone number verification feature for HTML5 pages](~~169786~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetAuthTokenRequest

        @return: GetAuthTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    def get_authorization_url_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account and obtain an Alibaba Cloud AccessKey pair. For more information, see [Process of communication authorization](~~196922~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetAuthorizationUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAuthorizationUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetAuthorizationUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization_url(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account and obtain an Alibaba Cloud AccessKey pair. For more information, see [Process of communication authorization](~~196922~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetAuthorizationUrlRequest

        @return: GetAuthorizationUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_url_with_options(request, runtime)

    def get_fusion_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.package_sign):
            query['PackageSign'] = request.package_sign
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_code):
            query['SchemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFusionAuthToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetFusionAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_fusion_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_fusion_auth_token_with_options(request, runtime)

    def get_mobile_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable only to one-click logon or registration. You can call this operation only after you confirm the authorization on the authorization page provided by the SDK for one-click logon. You are prohibited from simulating or bypassing the authorization process. Alibaba Cloud reserves the right to terminate our services and take legal actions against such violations.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetMobileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMobileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMobile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetMobileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mobile(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable only to one-click logon or registration. You can call this operation only after you confirm the authorization on the authorization page provided by the SDK for one-click logon. You are prohibited from simulating or bypassing the authorization process. Alibaba Cloud reserves the right to terminate our services and take legal actions against such violations.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetMobileRequest

        @return: GetMobileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mobile_with_options(request, runtime)

    def get_phone_with_token_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable only to one-click logon or registration in HTML5 pages. You can call this operation only after you confirm the authorization on the authorization page provided by the JavaScript SDK. You are prohibited from simulating or bypassing the authorization process. Alibaba Cloud reserves the right to terminate our services and take legal actions against such violations.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetPhoneWithTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPhoneWithTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneWithToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetPhoneWithTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_phone_with_token(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable only to one-click logon or registration in HTML5 pages. You can call this operation only after you confirm the authorization on the authorization page provided by the JavaScript SDK. You are prohibited from simulating or bypassing the authorization process. Alibaba Cloud reserves the right to terminate our services and take legal actions against such violations.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetPhoneWithTokenRequest

        @return: GetPhoneWithTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_phone_with_token_with_options(request, runtime)

    def get_sms_auth_tokens_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the SMS verification feature](~~313209~~).
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetSmsAuthTokensRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSmsAuthTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_code_expire):
            query['SmsCodeExpire'] = request.sms_code_expire
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsAuthTokens',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetSmsAuthTokensResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sms_auth_tokens(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the SMS verification feature](~~313209~~).
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetSmsAuthTokensRequest

        @return: GetSmsAuthTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sms_auth_tokens_with_options(request, runtime)

    def jy_create_verify_scheme_with_options(self, request, runtime):
        """
        @deprecated : JyCreateVerifyScheme is deprecated, please use Dypnsapi::2017-05-25::CreateVerifyScheme instead.
        

        @param request: JyCreateVerifySchemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: JyCreateVerifySchemeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not UtilClient.is_unset(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not UtilClient.is_unset(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pack_name):
            query['PackName'] = request.pack_name
        if not UtilClient.is_unset(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JyCreateVerifyScheme',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.JyCreateVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    def jy_create_verify_scheme(self, request):
        """
        @deprecated : JyCreateVerifyScheme is deprecated, please use Dypnsapi::2017-05-25::CreateVerifyScheme instead.
        

        @param request: JyCreateVerifySchemeRequest

        @return: JyCreateVerifySchemeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.jy_create_verify_scheme_with_options(request, runtime)

    def jy_query_app_info_by_scene_code_with_options(self, request, runtime):
        """
        @deprecated : JyQueryAppInfoBySceneCode is deprecated, please use Dypnsapi::2017-05-25::QueryAppInfoBySceneCode instead.
        

        @param request: JyQueryAppInfoBySceneCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: JyQueryAppInfoBySceneCodeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JyQueryAppInfoBySceneCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.JyQueryAppInfoBySceneCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def jy_query_app_info_by_scene_code(self, request):
        """
        @deprecated : JyQueryAppInfoBySceneCode is deprecated, please use Dypnsapi::2017-05-25::QueryAppInfoBySceneCode instead.
        

        @param request: JyQueryAppInfoBySceneCodeRequest

        @return: JyQueryAppInfoBySceneCodeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.jy_query_app_info_by_scene_code_with_options(request, runtime)

    def query_gate_verify_billing_public_with_options(self, request, runtime):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGateVerifyBillingPublicRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryGateVerifyBillingPublicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyBillingPublic',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.QueryGateVerifyBillingPublicResponse(),
            self.call_api(params, req, runtime)
        )

    def query_gate_verify_billing_public(self, request):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGateVerifyBillingPublicRequest

        @return: QueryGateVerifyBillingPublicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_gate_verify_billing_public_with_options(request, runtime)

    def query_gate_verify_statistic_public_with_options(self, request, runtime):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGateVerifyStatisticPublicRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryGateVerifyStatisticPublicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGateVerifyStatisticPublic',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.QueryGateVerifyStatisticPublicResponse(),
            self.call_api(params, req, runtime)
        )

    def query_gate_verify_statistic_public(self, request):
        """
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGateVerifyStatisticPublicRequest

        @return: QueryGateVerifyStatisticPublicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_gate_verify_statistic_public_with_options(request, runtime)

    def query_send_details_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: QuerySendDetailsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuerySendDetailsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.QuerySendDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_send_details(self, request):
        """
        @deprecated
        

        @param request: QuerySendDetailsRequest

        @return: QuerySendDetailsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    def send_sms_verify_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_length):
            query['CodeLength'] = request.code_length
        if not UtilClient.is_unset(request.code_type):
            query['CodeType'] = request.code_type
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.duplicate_policy):
            query['DuplicatePolicy'] = request.duplicate_policy
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.return_verify_code):
            query['ReturnVerifyCode'] = request.return_verify_code
        if not UtilClient.is_unset(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        if not UtilClient.is_unset(request.valid_time):
            query['ValidTime'] = request.valid_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSmsVerifyCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.SendSmsVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def send_sms_verify_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_sms_verify_code_with_options(request, runtime)

    def verify_mobile_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable to only the verification of thephone number that you use. To obtain a phone number for one-click logon, call [GetMobile](~~189865~~).
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifyMobileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: VerifyMobileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_code):
            query['AccessCode'] = request.access_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMobile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifyMobileResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_mobile(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Getting Started](~~84541~~).
        >  This operation is applicable to only the verification of thephone number that you use. To obtain a phone number for one-click logon, call [GetMobile](~~189865~~).
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifyMobileRequest

        @return: VerifyMobileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_mobile_with_options(request, runtime)

    def verify_phone_with_token_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the phone number verification feature for HTML5 pages](~~169786~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifyPhoneWithTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: VerifyPhoneWithTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sp_token):
            query['SpToken'] = request.sp_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhoneWithToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifyPhoneWithTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_phone_with_token(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the phone number verification feature for HTML5 pages](~~169786~~).
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifyPhoneWithTokenRequest

        @return: VerifyPhoneWithTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_token_with_options(request, runtime)

    def verify_sms_code_with_options(self, request, runtime):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the SMS verification feature](~~313209~~).
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifySmsCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: VerifySmsCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.sms_code):
            query['SmsCode'] = request.sms_code
        if not UtilClient.is_unset(request.sms_token):
            query['SmsToken'] = request.sms_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySmsCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifySmsCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_sms_code(self, request):
        """
        ### [](#)Preparations
        You must register an Alibaba Cloud account, obtain an Alibaba Cloud AccessKey pair, and create a verification service. For more information, see [Use the SMS verification feature](~~313209~~).
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: VerifySmsCodeRequest

        @return: VerifySmsCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_sms_code_with_options(request, runtime)

    def verify_with_fusion_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verify_token):
            query['VerifyToken'] = request.verify_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyWithFusionAuthToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifyWithFusionAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_with_fusion_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_with_fusion_auth_token_with_options(request, runtime)
