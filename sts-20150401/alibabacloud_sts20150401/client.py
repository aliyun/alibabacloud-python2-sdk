# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sts20150401 import models as sts_20150401_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'sts.aliyuncs.com',
            'cn-beijing-finance-1': 'sts.aliyuncs.com',
            'cn-beijing-finance-pop': 'sts.aliyuncs.com',
            'cn-beijing-gov-1': 'sts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'sts.aliyuncs.com',
            'cn-edge-1': 'sts.aliyuncs.com',
            'cn-fujian': 'sts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'sts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'sts.aliyuncs.com',
            'cn-hangzhou-finance': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'sts.aliyuncs.com',
            'cn-hangzhou-test-306': 'sts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'sts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'sts.aliyuncs.com',
            'cn-north-2-gov-1': 'sts-vpc.cn-north-2-gov-1.aliyuncs.com',
            'cn-qingdao-nebula': 'sts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'sts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'sts.aliyuncs.com',
            'cn-shanghai-inner': 'sts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'sts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'sts-vpc.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen-inner': 'sts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'sts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'sts.aliyuncs.com',
            'cn-wuhan': 'sts.aliyuncs.com',
            'cn-yushanfang': 'sts.aliyuncs.com',
            'cn-zhangbei': 'sts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'sts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'sts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'sts.aliyuncs.com',
            'eu-west-1-oxs': 'sts.aliyuncs.com',
            'rus-west-1-pop': 'sts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def assume_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRole',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def assume_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_options(request, runtime)

    def assume_role_with_oidcwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.oidcprovider_arn):
            query['OIDCProviderArn'] = request.oidcprovider_arn
        if not UtilClient.is_unset(request.oidctoken):
            query['OIDCToken'] = request.oidctoken
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_session_name):
            query['RoleSessionName'] = request.role_session_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithOIDC',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithOIDCResponse(),
            self.call_api(params, req, runtime)
        )

    def assume_role_with_oidc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_oidcwith_options(request, runtime)

    def assume_role_with_samlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.samlassertion):
            query['SAMLAssertion'] = request.samlassertion
        if not UtilClient.is_unset(request.samlprovider_arn):
            query['SAMLProviderArn'] = request.samlprovider_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssumeRoleWithSAML',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.AssumeRoleWithSAMLResponse(),
            self.call_api(params, req, runtime)
        )

    def assume_role_with_saml(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_samlwith_options(request, runtime)

    def get_caller_identity_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCallerIdentity',
            version='2015-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sts_20150401_models.GetCallerIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_caller_identity(self):
        runtime = util_models.RuntimeOptions()
        return self.get_caller_identity_with_options(runtime)
