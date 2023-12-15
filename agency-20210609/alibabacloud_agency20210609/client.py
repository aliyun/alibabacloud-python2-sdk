# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_agency20210609 import models as agency_20210609_models
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
            'ap-northeast-1': 'agency.aliyuncs.com',
            'ap-northeast-2-pop': 'agency.aliyuncs.com',
            'ap-south-1': 'agency.aliyuncs.com',
            'ap-southeast-2': 'agency.aliyuncs.com',
            'ap-southeast-3': 'agency.aliyuncs.com',
            'ap-southeast-5': 'agency.aliyuncs.com',
            'cn-beijing': 'agency.aliyuncs.com',
            'cn-beijing-finance-1': 'agency.aliyuncs.com',
            'cn-beijing-finance-pop': 'agency.aliyuncs.com',
            'cn-beijing-gov-1': 'agency.aliyuncs.com',
            'cn-beijing-nu16-b01': 'agency.aliyuncs.com',
            'cn-chengdu': 'agency.aliyuncs.com',
            'cn-edge-1': 'agency.aliyuncs.com',
            'cn-fujian': 'agency.aliyuncs.com',
            'cn-haidian-cm12-c01': 'agency.aliyuncs.com',
            'cn-hangzhou': 'agency.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'agency.aliyuncs.com',
            'cn-hangzhou-finance': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'agency.aliyuncs.com',
            'cn-hangzhou-test-306': 'agency.aliyuncs.com',
            'cn-hongkong': 'agency.aliyuncs.com',
            'cn-hongkong-finance-pop': 'agency.aliyuncs.com',
            'cn-huhehaote': 'agency.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'agency.aliyuncs.com',
            'cn-north-2-gov-1': 'agency.aliyuncs.com',
            'cn-qingdao': 'agency.aliyuncs.com',
            'cn-qingdao-nebula': 'agency.aliyuncs.com',
            'cn-shanghai': 'agency.aliyuncs.com',
            'cn-shanghai-et15-b01': 'agency.aliyuncs.com',
            'cn-shanghai-et2-b01': 'agency.aliyuncs.com',
            'cn-shanghai-finance-1': 'agency.aliyuncs.com',
            'cn-shanghai-inner': 'agency.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'agency.aliyuncs.com',
            'cn-shenzhen': 'agency.aliyuncs.com',
            'cn-shenzhen-finance-1': 'agency.aliyuncs.com',
            'cn-shenzhen-inner': 'agency.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'agency.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'agency.aliyuncs.com',
            'cn-wuhan': 'agency.aliyuncs.com',
            'cn-wulanchabu': 'agency.aliyuncs.com',
            'cn-yushanfang': 'agency.aliyuncs.com',
            'cn-zhangbei': 'agency.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'agency.aliyuncs.com',
            'cn-zhangjiakou': 'agency.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'agency.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'agency.aliyuncs.com',
            'eu-central-1': 'agency.aliyuncs.com',
            'eu-west-1': 'agency.aliyuncs.com',
            'eu-west-1-oxs': 'agency.aliyuncs.com',
            'me-east-1': 'agency.aliyuncs.com',
            'rus-west-1-pop': 'agency.aliyuncs.com',
            'us-east-1': 'agency.aliyuncs.com',
            'us-west-1': 'agency.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('agency', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_owner_agreement_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnerAgreementInstance',
            version='2021-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20210609_models.GetOwnerAgreementInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_owner_agreement_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_owner_agreement_instance_with_options(request, runtime)

    def get_partner_by_uid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartnerByUid',
            version='2021-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20210609_models.GetPartnerByUidResponse(),
            self.call_api(params, req, runtime)
        )

    def get_partner_by_uid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_partner_by_uid_with_options(request, runtime)

    def query_fusion_order_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFusionOrderList',
            version='2021-06-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20210609_models.QueryFusionOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_fusion_order_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_fusion_order_list_with_options(request, runtime)
