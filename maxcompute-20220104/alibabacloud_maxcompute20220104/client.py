# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_maxcompute20220104 import models as max_compute_20220104_models
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
            'ap-northeast-1': 'maxcompute.aliyuncs.com',
            'ap-northeast-2-pop': 'maxcompute.aliyuncs.com',
            'ap-south-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-2': 'maxcompute.aliyuncs.com',
            'ap-southeast-3': 'maxcompute.aliyuncs.com',
            'ap-southeast-5': 'maxcompute.aliyuncs.com',
            'cn-beijing': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-beijing-gov-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-nu16-b01': 'maxcompute.aliyuncs.com',
            'cn-chengdu': 'maxcompute.aliyuncs.com',
            'cn-edge-1': 'maxcompute.aliyuncs.com',
            'cn-fujian': 'maxcompute.aliyuncs.com',
            'cn-haidian-cm12-c01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-finance': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-test-306': 'maxcompute.aliyuncs.com',
            'cn-hongkong': 'maxcompute.aliyuncs.com',
            'cn-hongkong-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-huhehaote': 'maxcompute.aliyuncs.com',
            'cn-north-2-gov-1': 'maxcompute.aliyuncs.com',
            'cn-qingdao': 'maxcompute.aliyuncs.com',
            'cn-qingdao-nebula': 'maxcompute.aliyuncs.com',
            'cn-shanghai': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et15-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et2-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shanghai-inner': 'maxcompute.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-inner': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'maxcompute.aliyuncs.com',
            'cn-wuhan': 'maxcompute.aliyuncs.com',
            'cn-yushanfang': 'maxcompute.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'maxcompute.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'maxcompute.aliyuncs.com',
            'eu-central-1': 'maxcompute.aliyuncs.com',
            'eu-west-1': 'maxcompute.aliyuncs.com',
            'eu-west-1-oxs': 'maxcompute.aliyuncs.com',
            'me-east-1': 'maxcompute.aliyuncs.com',
            'rus-west-1-pop': 'maxcompute.aliyuncs.com',
            'us-east-1': 'maxcompute.aliyuncs.com',
            'us-west-1': 'maxcompute.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('maxcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_quota(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_with_options(request, headers, runtime)

    def create_quota_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not UtilClient.is_unset(request.nickname):
            body['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quota(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_with_options(nickname, request, headers, runtime)

    def delete_quota_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        nickname = OpenApiUtilClient.get_encode_param(nickname)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s' % TeaConverter.to_unicode(nickname),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(nickname, request, headers, runtime)

    def get_quota_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        nickname = OpenApiUtilClient.get_encode_param(nickname)
        query = {}
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s' % TeaConverter.to_unicode(nickname),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quotas(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    def list_quotas_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quota(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(nickname, request, headers, runtime)

    def update_quota_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        nickname = OpenApiUtilClient.get_encode_param(nickname)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s' % TeaConverter.to_unicode(nickname),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sub_quotas(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sub_quotas_with_options(nickname, request, headers, runtime)

    def update_sub_quotas_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        nickname = OpenApiUtilClient.get_encode_param(nickname)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateSubQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/subquotas' % TeaConverter.to_unicode(nickname),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateSubQuotasResponse(),
            self.call_api(params, req, runtime)
        )
