# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eais20190624 import models as eais_20190624_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'eais.aliyuncs.com',
            'ap-northeast-2-pop': 'eais.aliyuncs.com',
            'ap-south-1': 'eais.aliyuncs.com',
            'ap-southeast-1': 'eais.aliyuncs.com',
            'ap-southeast-2': 'eais.aliyuncs.com',
            'ap-southeast-3': 'eais.aliyuncs.com',
            'ap-southeast-5': 'eais.aliyuncs.com',
            'cn-beijing-finance-1': 'eais.aliyuncs.com',
            'cn-beijing-finance-pop': 'eais.aliyuncs.com',
            'cn-beijing-gov-1': 'eais.aliyuncs.com',
            'cn-beijing-nu16-b01': 'eais.aliyuncs.com',
            'cn-edge-1': 'eais.aliyuncs.com',
            'cn-fujian': 'eais.aliyuncs.com',
            'cn-haidian-cm12-c01': 'eais.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'eais.aliyuncs.com',
            'cn-hangzhou-finance': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'eais.aliyuncs.com',
            'cn-hangzhou-test-306': 'eais.aliyuncs.com',
            'cn-hongkong': 'eais.aliyuncs.com',
            'cn-hongkong-finance-pop': 'eais.aliyuncs.com',
            'cn-huhehaote': 'eais.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'eais.aliyuncs.com',
            'cn-north-2-gov-1': 'eais.aliyuncs.com',
            'cn-qingdao': 'eais.aliyuncs.com',
            'cn-qingdao-nebula': 'eais.aliyuncs.com',
            'cn-shanghai-et15-b01': 'eais.aliyuncs.com',
            'cn-shanghai-et2-b01': 'eais.aliyuncs.com',
            'cn-shanghai-finance-1': 'eais.aliyuncs.com',
            'cn-shanghai-inner': 'eais.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'eais.aliyuncs.com',
            'cn-shenzhen-finance-1': 'eais.aliyuncs.com',
            'cn-shenzhen-inner': 'eais.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'eais.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'eais.aliyuncs.com',
            'cn-wuhan': 'eais.aliyuncs.com',
            'cn-wulanchabu': 'eais.aliyuncs.com',
            'cn-yushanfang': 'eais.aliyuncs.com',
            'cn-zhangbei': 'eais.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'eais.aliyuncs.com',
            'cn-zhangjiakou': 'eais.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'eais.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'eais.aliyuncs.com',
            'eu-central-1': 'eais.aliyuncs.com',
            'eu-west-1': 'eais.aliyuncs.com',
            'eu-west-1-oxs': 'eais.aliyuncs.com',
            'me-east-1': 'eais.aliyuncs.com',
            'rus-west-1-pop': 'eais.aliyuncs.com',
            'us-east-1': 'eais.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eais', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_eai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.AttachEaiResponse().from_map(
            self.do_rpcrequest('AttachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_eai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_eai_with_options(request, runtime)

    def create_eai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiResponse().from_map(
            self.do_rpcrequest('CreateEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_eai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_eai_with_options(request, runtime)

    def create_eai_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiAllResponse().from_map(
            self.do_rpcrequest('CreateEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_eai_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_eai_all_with_options(request, runtime)

    def delete_eai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiResponse().from_map(
            self.do_rpcrequest('DeleteEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_eai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_with_options(request, runtime)

    def delete_eai_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiAllResponse().from_map(
            self.do_rpcrequest('DeleteEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_eai_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_all_with_options(request, runtime)

    def describe_eais_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DescribeEaisResponse().from_map(
            self.do_rpcrequest('DescribeEais', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eais(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eais_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return eais_20190624_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def detach_eai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DetachEaiResponse().from_map(
            self.do_rpcrequest('DetachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_eai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_eai_with_options(request, runtime)

    def get_private_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.GetPrivateIpResponse().from_map(
            self.do_rpcrequest('GetPrivateIp', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_private_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_private_ip_with_options(request, runtime)
