# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xgippop20220520 import models as xgip_pop_20220520_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('xgippop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_application_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ChangeApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def change_application_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_application_info_with_options(request, runtime)

    def create_application_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.CreateApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_info_with_options(request, runtime)

    def get_aliyun_xgip_token_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAliyunXgipToken',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetAliyunXgipTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aliyun_xgip_token(self):
        runtime = util_models.RuntimeOptions()
        return self.get_aliyun_xgip_token_with_options(runtime)

    def get_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    def get_free_flow_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowInstance',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_free_flow_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_instance_with_options(request, runtime)

    def get_free_flow_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowProductList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowProductListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_free_flow_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_product_list_with_options(request, runtime)

    def get_free_flow_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsage',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_free_flow_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_usage_with_options(request, runtime)

    def get_free_flow_usage_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsageStatistic',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_free_flow_usage_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_usage_statistic_with_options(request, runtime)

    def get_order_free_flow_product_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderFreeFlowProductStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_order_free_flow_product_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_order_free_flow_product_status_with_options(request, runtime)

    def get_qos_flow_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosFlowUsage',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetQosFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_qos_flow_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_qos_flow_usage_with_options(request, runtime)

    def get_qos_usage_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosUsageStatistic',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetQosUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_qos_usage_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_qos_usage_statistic_with_options(request, runtime)

    def get_uat_data_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatDataList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetUatDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_uat_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_uat_data_list_with_options(request, runtime)

    def get_uat_spec_ct_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatSpecCtData',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetUatSpecCtDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_uat_spec_ct_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_uat_spec_ct_data_with_options(request, runtime)

    def mock_get_order_free_flow_product_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MockGetOrderFreeFlowProductStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def mock_get_order_free_flow_product_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mock_get_order_free_flow_product_status_with_options(request, runtime)

    def mock_order_free_flow_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.customer_flow_request_id):
            query['CustomerFlowRequestId'] = request.customer_flow_request_id
        if not UtilClient.is_unset(request.flow_product_id):
            query['FlowProductId'] = request.flow_product_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lasting):
            query['Lasting'] = request.lasting
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.purchase_order_id):
            query['PurchaseOrderId'] = request.purchase_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MockOrderFreeFlowProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.MockOrderFreeFlowProductResponse(),
            self.call_api(params, req, runtime)
        )

    def mock_order_free_flow_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mock_order_free_flow_product_with_options(request, runtime)

    def modify_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ModifyApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_application_with_options(request, runtime)

    def order_free_flow_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.customer_flow_request_id):
            query['CustomerFlowRequestId'] = request.customer_flow_request_id
        if not UtilClient.is_unset(request.flow_product_id):
            query['FlowProductId'] = request.flow_product_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lasting):
            query['Lasting'] = request.lasting
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.purchase_order_id):
            query['PurchaseOrderId'] = request.purchase_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderFreeFlowProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.OrderFreeFlowProductResponse(),
            self.call_api(params, req, runtime)
        )

    def order_free_flow_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.order_free_flow_product_with_options(request, runtime)

    def order_qos_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provice):
            query['Provice'] = request.provice
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.ipv_6):
            body['IPv6'] = request.ipv_6
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            body['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.mobile_number):
            body['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.private_ipv_4):
            body['PrivateIpv4'] = request.private_ipv_4
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.public_ipv_4):
            body['PublicIpv4'] = request.public_ipv_4
        if not UtilClient.is_unset(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.target_ip_list):
            body['TargetIpList'] = request.target_ip_list
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OrderQosProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.OrderQosProductResponse(),
            self.call_api(params, req, runtime)
        )

    def order_qos_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.order_qos_product_with_options(request, runtime)

    def save_application_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SaveApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def save_application_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_application_info_with_options(request, runtime)

    def sdk_validate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SdkValidateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_validate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_validate_status_with_options(request, runtime)

    def valid_controller_author_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidControllerAuthor',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ValidControllerAuthorResponse(),
            self.call_api(params, req, runtime)
        )

    def valid_controller_author(self, request):
        runtime = util_models.RuntimeOptions()
        return self.valid_controller_author_with_options(request, runtime)

    def validate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ValidateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_status_with_options(request, runtime)
