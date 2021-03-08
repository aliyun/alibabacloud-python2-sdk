# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hitsdb20170601 import models as hitsdb_20170601_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'hitsdb.aliyuncs.com',
            'cn-beijing': 'hitsdb.aliyuncs.com',
            'cn-hangzhou': 'hitsdb.aliyuncs.com',
            'cn-shanghai': 'hitsdb.aliyuncs.com',
            'cn-shenzhen': 'hitsdb.aliyuncs.com',
            'cn-hongkong': 'hitsdb.aliyuncs.com',
            'ap-southeast-1': 'hitsdb.aliyuncs.com',
            'us-west-1': 'hitsdb.aliyuncs.com',
            'us-east-1': 'hitsdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'hitsdb.aliyuncs.com',
            'ap-northeast-2-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-gov-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hitsdb.aliyuncs.com',
            'cn-chengdu': 'hitsdb.aliyuncs.com',
            'cn-edge-1': 'hitsdb.aliyuncs.com',
            'cn-fujian': 'hitsdb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-finance': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-test-306': 'hitsdb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hitsdb.aliyuncs.com',
            'cn-qingdao-nebula': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-inner': 'hitsdb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-inner': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hitsdb.aliyuncs.com',
            'cn-wuhan': 'hitsdb.aliyuncs.com',
            'cn-wulanchabu': 'hitsdb.aliyuncs.com',
            'cn-yushanfang': 'hitsdb.aliyuncs.com',
            'cn-zhangbei': 'hitsdb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hitsdb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hitsdb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hitsdb.aliyuncs.com',
            'eu-west-1-oxs': 'hitsdb.aliyuncs.com',
            'me-east-1': 'hitsdb.aliyuncs.com',
            'rus-west-1-pop': 'hitsdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hitsdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_hi_tsdbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.CreateHiTSDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateHiTSDBInstance', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_hi_tsdbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hi_tsdbinstance_with_options(request, runtime)

    def delete_hi_tsdbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DeleteHiTSDBInstanceResponse().from_map(
            self.do_rpcrequest('DeleteHiTSDBInstance', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_hi_tsdbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_hi_tsdbinstance_with_options(request, runtime)

    def describe_hi_tsdbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DescribeHiTSDBInstanceResponse().from_map(
            self.do_rpcrequest('DescribeHiTSDBInstance', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hi_tsdbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_with_options(request, runtime)

    def describe_hi_tsdbinstance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse().from_map(
            self.do_rpcrequest('DescribeHiTSDBInstanceList', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hi_tsdbinstance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_list_with_options(request, runtime)

    def describe_hi_tsdbinstance_security_ip_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse().from_map(
            self.do_rpcrequest('DescribeHiTSDBInstanceSecurityIpList', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hi_tsdbinstance_security_ip_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_security_ip_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def modify_hi_tsdbinstance_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse().from_map(
            self.do_rpcrequest('ModifyHiTSDBInstanceClass', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hi_tsdbinstance_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hi_tsdbinstance_class_with_options(request, runtime)

    def modify_hi_tsdbinstance_security_ip_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse().from_map(
            self.do_rpcrequest('ModifyHiTSDBInstanceSecurityIpList', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hi_tsdbinstance_security_ip_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hi_tsdbinstance_security_ip_list_with_options(request, runtime)

    def rename_hi_tsdbinstance_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse().from_map(
            self.do_rpcrequest('RenameHiTSDBInstanceAlias', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_hi_tsdbinstance_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rename_hi_tsdbinstance_alias_with_options(request, runtime)

    def renew_tsdbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.RenewTSDBInstanceResponse().from_map(
            self.do_rpcrequest('RenewTSDBInstance', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_tsdbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_tsdbinstance_with_options(request, runtime)

    def restart_hi_tsdbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.RestartHiTSDBInstanceResponse().from_map(
            self.do_rpcrequest('RestartHiTSDBInstance', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_hi_tsdbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_hi_tsdbinstance_with_options(request, runtime)

    def switch_hi_tsdbinstance_public_net_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse().from_map(
            self.do_rpcrequest('SwitchHiTSDBInstancePublicNet', '2017-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_hi_tsdbinstance_public_net(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_hi_tsdbinstance_public_net_with_options(request, runtime)
