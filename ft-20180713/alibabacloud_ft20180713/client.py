# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ft20180713 import models as ft_20180713_models
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
            'ap-northeast-2-pop': 'ft.aliyuncs.com',
            'ap-south-1': 'ft.aliyuncs.com',
            'ap-southeast-1': 'ft.aliyuncs.com',
            'ap-southeast-2': 'ft.aliyuncs.com',
            'ap-southeast-3': 'ft.aliyuncs.com',
            'ap-southeast-5': 'ft.aliyuncs.com',
            'cn-beijing': 'ft.aliyuncs.com',
            'cn-beijing-finance-1': 'ft.aliyuncs.com',
            'cn-beijing-finance-pop': 'ft.aliyuncs.com',
            'cn-beijing-gov-1': 'ft.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ft.aliyuncs.com',
            'cn-chengdu': 'ft.aliyuncs.com',
            'cn-edge-1': 'ft.aliyuncs.com',
            'cn-fujian': 'ft.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ft.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ft.aliyuncs.com',
            'cn-hangzhou-finance': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ft.aliyuncs.com',
            'cn-hangzhou-test-306': 'ft.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ft.aliyuncs.com',
            'cn-huhehaote': 'ft.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ft.aliyuncs.com',
            'cn-qingdao': 'ft.aliyuncs.com',
            'cn-qingdao-nebula': 'ft.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ft.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ft.aliyuncs.com',
            'cn-shanghai-finance-1': 'ft.aliyuncs.com',
            'cn-shanghai-inner': 'ft.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ft.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ft.aliyuncs.com',
            'cn-shenzhen-inner': 'ft.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ft.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ft.aliyuncs.com',
            'cn-wuhan': 'ft.aliyuncs.com',
            'cn-wulanchabu': 'ft.aliyuncs.com',
            'cn-yushanfang': 'ft.aliyuncs.com',
            'cn-zhangbei': 'ft.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ft.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ft.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ft.aliyuncs.com',
            'eu-central-1': 'ft.aliyuncs.com',
            'eu-west-1': 'ft.aliyuncs.com',
            'eu-west-1-oxs': 'ft.aliyuncs.com',
            'me-east-1': 'ft.aliyuncs.com',
            'rus-west-1-pop': 'ft.aliyuncs.com',
            'us-west-1': 'ft.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ft', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_audit_test_01with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_audit_test_01):
            query['BatchAuditTest01'] = request.batch_audit_test_01
        if not UtilClient.is_unset(request.demo_01):
            query['Demo01'] = request.demo_01
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        body = {}
        if not UtilClient.is_unset(request.test_010101):
            body['Test010101'] = request.test_010101
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAuditTest01',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.BatchAuditTest01Response(),
            self.call_api(params, req, runtime)
        )

    def batch_audit_test_01(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_audit_test_01with_options(request, runtime)

    def f_tapi_alias_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FTApiAliasApi',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FTApiAliasApiResponse(),
            self.call_api(params, req, runtime)
        )

    def f_tapi_alias_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.f_tapi_alias_api_with_options(request, runtime)

    def ft_dynamic_address_dubbo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.int_value):
            query['IntValue'] = request.int_value
        if not UtilClient.is_unset(request.string_value):
            query['StringValue'] = request.string_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtDynamicAddressDubbo',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtDynamicAddressDubboResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_dynamic_address_dubbo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_dubbo_with_options(request, runtime)

    def ft_dynamic_address_hsf_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='FtDynamicAddressHsf',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtDynamicAddressHsfResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_dynamic_address_hsf(self):
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_hsf_with_options(runtime)

    def ft_dynamic_address_http_vpc_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.FtDynamicAddressHttpVpcShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.default_value):
            request.default_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.default_value, 'DefaultValue', 'json')
        if not UtilClient.is_unset(tmp_req.other_param):
            request.other_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_param, 'OtherParam', 'json')
        if not UtilClient.is_unset(tmp_req.string_value):
            request.string_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.string_value, 'StringValue', 'json')
        query = {}
        if not UtilClient.is_unset(request.boolean_param):
            query['BooleanParam'] = request.boolean_param
        if not UtilClient.is_unset(request.default_value_shrink):
            query['DefaultValue'] = request.default_value_shrink
        if not UtilClient.is_unset(request.other_param_shrink):
            query['OtherParam'] = request.other_param_shrink
        if not UtilClient.is_unset(request.p_1):
            query['P1'] = request.p_1
        if not UtilClient.is_unset(request.string_value_shrink):
            query['StringValue'] = request.string_value_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtDynamicAddressHttpVpc',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtDynamicAddressHttpVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_dynamic_address_http_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_http_vpc_with_options(request, runtime)

    def ft_eagle_eye_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtEagleEye',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtEagleEyeResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_eagle_eye(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_eagle_eye_with_options(request, runtime)

    def ft_flow_special_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtFlowSpecial',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtFlowSpecialResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_flow_special(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_flow_special_with_options(request, runtime)

    def ft_gated_launch_policy_4with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_gated_launch):
            query['IsGatedLaunch'] = request.is_gated_launch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtGatedLaunchPolicy4',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtGatedLaunchPolicy4Response(),
            self.call_api(params, req, runtime)
        )

    def ft_gated_launch_policy_4(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_gated_launch_policy_4with_options(request, runtime)

    def ft_ip_flow_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtIpFlowControl',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtIpFlowControlResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_ip_flow_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_ip_flow_control_with_options(request, runtime)

    def ft_param_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk):
            query['Disk'] = request.disk
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FtParamList',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.FtParamListResponse(),
            self.call_api(params, req, runtime)
        )

    def ft_param_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ft_param_list_with_options(request, runtime)

    def test_flow_strategy_01with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestFlowStrategy01ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        body = {}
        if not UtilClient.is_unset(request.names_shrink):
            body['Names'] = request.names_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestFlowStrategy01',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.TestFlowStrategy01Response(),
            self.call_api(params, req, runtime)
        )

    def test_flow_strategy_01(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_flow_strategy_01with_options(request, runtime)

    def test_http_api_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestHttpApiShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.default_value):
            request.default_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.default_value, 'DefaultValue', 'json')
        if not UtilClient.is_unset(tmp_req.other_param):
            request.other_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_param, 'OtherParam', 'json')
        if not UtilClient.is_unset(tmp_req.string_value):
            request.string_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.string_value, 'StringValue', 'json')
        query = {}
        if not UtilClient.is_unset(request.boolean_param):
            query['BooleanParam'] = request.boolean_param
        if not UtilClient.is_unset(request.default_value_shrink):
            query['DefaultValue'] = request.default_value_shrink
        if not UtilClient.is_unset(request.other_param_shrink):
            query['OtherParam'] = request.other_param_shrink
        if not UtilClient.is_unset(request.string_value_shrink):
            query['StringValue'] = request.string_value_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestHttpApi',
            version='2018-07-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20180713_models.TestHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    def test_http_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_http_api_with_options(request, runtime)
