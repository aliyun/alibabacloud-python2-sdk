# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkedmall20220531 import models as linkedmall_20220531_models
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
            'cn-hangzhou': 'linkedmall.aliyuncs.com',
            'cn-shanghai': 'linkedmall.aliyuncs.com',
            'ap-northeast-1': 'linkedmall.aliyuncs.com',
            'ap-northeast-2-pop': 'linkedmall.aliyuncs.com',
            'ap-south-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-2': 'linkedmall.aliyuncs.com',
            'ap-southeast-3': 'linkedmall.aliyuncs.com',
            'ap-southeast-5': 'linkedmall.aliyuncs.com',
            'cn-beijing': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-beijing-gov-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkedmall.aliyuncs.com',
            'cn-chengdu': 'linkedmall.aliyuncs.com',
            'cn-edge-1': 'linkedmall.aliyuncs.com',
            'cn-fujian': 'linkedmall.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-finance': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkedmall.aliyuncs.com',
            'cn-hongkong': 'linkedmall.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-huhehaote': 'linkedmall.aliyuncs.com',
            'cn-north-2-gov-1': 'linkedmall.aliyuncs.com',
            'cn-qingdao': 'linkedmall.aliyuncs.com',
            'cn-qingdao-nebula': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shanghai-inner': 'linkedmall.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-inner': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkedmall.aliyuncs.com',
            'cn-wuhan': 'linkedmall.aliyuncs.com',
            'cn-yushanfang': 'linkedmall.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkedmall.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkedmall.aliyuncs.com',
            'eu-central-1': 'linkedmall.aliyuncs.com',
            'eu-west-1': 'linkedmall.aliyuncs.com',
            'eu-west-1-oxs': 'linkedmall.aliyuncs.com',
            'me-east-1': 'linkedmall.aliyuncs.com',
            'rus-west-1-pop': 'linkedmall.aliyuncs.com',
            'us-east-1': 'linkedmall.aliyuncs.com',
            'us-west-1': 'linkedmall.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkedmall', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_create_distribution_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20220531_models.ApplyCreateDistributionOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_info_lists):
            request.item_info_lists_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_info_lists, 'ItemInfoLists', 'json')
        body = {}
        if not UtilClient.is_unset(request.buyer_id):
            body['BuyerId'] = request.buyer_id
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.distribution_out_trade_id):
            body['DistributionOutTradeId'] = request.distribution_out_trade_id
        if not UtilClient.is_unset(request.distribution_supplier_id):
            body['DistributionSupplierId'] = request.distribution_supplier_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.item_info_lists_shrink):
            body['ItemInfoLists'] = request.item_info_lists_shrink
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCreateDistributionOrder',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ApplyCreateDistributionOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_create_distribution_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_create_distribution_order_with_options(request, runtime)

    def apply_refund_4distribution_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20220531_models.ApplyRefund4DistributionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.leave_picture_lists):
            request.leave_picture_lists_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.leave_picture_lists, 'LeavePictureLists', 'json')
        body = {}
        if not UtilClient.is_unset(request.apply_reason_text_id):
            body['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            body['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            body['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            body['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_lists_shrink):
            body['LeavePictureLists'] = request.leave_picture_lists_shrink
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyRefund4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ApplyRefund4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_refund_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_refund_4distribution_with_options(request, runtime)

    def cancel_distribution_trade_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_trade_id):
            body['DistributionTradeId'] = request.distribution_trade_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelDistributionTrade',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.CancelDistributionTradeResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_distribution_trade(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_distribution_trade_with_options(request, runtime)

    def cancel_refund_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelRefund4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.CancelRefund4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_refund_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_refund_4distribution_with_options(request, runtime)

    def confirm_disburse_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_trade_id):
            body['DistributionTradeId'] = request.distribution_trade_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.main_distribution_order_id):
            body['MainDistributionOrderId'] = request.main_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ConfirmDisburse4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_disburse_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_disburse_4distribution_with_options(request, runtime)

    def init_apply_refund_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_claim_type):
            body['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitApplyRefund4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.InitApplyRefund4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def init_apply_refund_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_apply_refund_4distribution_with_options(request, runtime)

    def init_modify_refund_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_claim_type):
            body['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitModifyRefund4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.InitModifyRefund4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def init_modify_refund_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_modify_refund_4distribution_with_options(request, runtime)

    def list_distribution_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.item_status):
            body['ItemStatus'] = request.item_status
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDistributionItem',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ListDistributionItemResponse(),
            self.call_api(params, req, runtime)
        )

    def list_distribution_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distribution_item_with_options(request, runtime)

    def list_distribution_item_without_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.item_status):
            body['ItemStatus'] = request.item_status
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDistributionItemWithoutCache',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ListDistributionItemWithoutCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def list_distribution_item_without_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distribution_item_without_cache_with_options(request, runtime)

    def list_distribution_mall_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_supplier_id):
            body['ChannelSupplierId'] = request.channel_supplier_id
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distribution_mall_name):
            body['DistributionMallName'] = request.distribution_mall_name
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDistributionMall',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ListDistributionMallResponse(),
            self.call_api(params, req, runtime)
        )

    def list_distribution_mall(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distribution_mall_with_options(request, runtime)

    def modify_refund_4distribution_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20220531_models.ModifyRefund4DistributionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.leave_picture_lists):
            request.leave_picture_lists_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.leave_picture_lists, 'LeavePictureLists', 'json')
        body = {}
        if not UtilClient.is_unset(request.apply_reason_text_id):
            body['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            body['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            body['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            body['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_lists_shrink):
            body['LeavePictureLists'] = request.leave_picture_lists_shrink
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyRefund4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.ModifyRefund4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_refund_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_refund_4distribution_with_options(request, runtime)

    def query_child_division_code_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.division_code):
            body['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryChildDivisionCodeById',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryChildDivisionCodeByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_child_division_code_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_child_division_code_by_id_with_options(request, runtime)

    def query_distribution_bill_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bill_period):
            body['BillPeriod'] = request.bill_period
        if not UtilClient.is_unset(request.bill_status):
            body['BillStatus'] = request.bill_status
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distribution_mall_name):
            body['DistributionMallName'] = request.distribution_mall_name
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDistributionBillDetail',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryDistributionBillDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_distribution_bill_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_distribution_bill_detail_with_options(request, runtime)

    def query_distribution_mall_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDistributionMall',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryDistributionMallResponse(),
            self.call_api(params, req, runtime)
        )

    def query_distribution_mall(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_distribution_mall_with_options(request, runtime)

    def query_distribution_trade_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_supplier_id):
            body['DistributionSupplierId'] = request.distribution_supplier_id
        if not UtilClient.is_unset(request.distribution_trade_id):
            body['DistributionTradeId'] = request.distribution_trade_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDistributionTradeStatus',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryDistributionTradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_distribution_trade_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_distribution_trade_status_with_options(request, runtime)

    def query_item_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryItemDetail',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_item_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_with_options(request, runtime)

    def query_item_detail_with_division_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.division_code):
            body['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryItemDetailWithDivision',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryItemDetailWithDivisionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_item_detail_with_division(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_with_division_with_options(request, runtime)

    def query_item_guide_retail_price_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20220531_models.QueryItemGuideRetailPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            body['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryItemGuideRetailPrice',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryItemGuideRetailPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_item_guide_retail_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_guide_retail_price_with_options(request, runtime)

    def query_logistics_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.main_distribution_order_id):
            body['MainDistributionOrderId'] = request.main_distribution_order_id
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLogistics4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryLogistics4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_logistics_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_logistics_4distribution_with_options(request, runtime)

    def query_mall_category_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.distribution_mall_id):
            body['DistributionMallId'] = request.distribution_mall_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMallCategoryList',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryMallCategoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mall_category_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mall_category_list_with_options(request, runtime)

    def query_order_detail_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.main_distribution_order_id):
            body['MainDistributionOrderId'] = request.main_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderDetail4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryOrderDetail4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_order_detail_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_detail_4distribution_with_options(request, runtime)

    def query_order_list_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.filter_option):
            body['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderList4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryOrderList4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_order_list_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_4distribution_with_options(request, runtime)

    def query_refund_application_detail_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRefundApplicationDetail4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.QueryRefundApplicationDetail4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_refund_application_detail_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_refund_application_detail_4distribution_with_options(request, runtime)

    def render_distribution_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20220531_models.RenderDistributionOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_info_lists):
            request.item_info_lists_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_info_lists, 'ItemInfoLists', 'json')
        body = {}
        if not UtilClient.is_unset(request.buyer_id):
            body['BuyerId'] = request.buyer_id
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.distribution_supplier_id):
            body['DistributionSupplierId'] = request.distribution_supplier_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.item_info_lists_shrink):
            body['ItemInfoLists'] = request.item_info_lists_shrink
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenderDistributionOrder',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.RenderDistributionOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def render_distribution_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.render_distribution_order_with_options(request, runtime)

    def submit_return_good_logistics_4distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cp_code):
            body['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.distributor_id):
            body['DistributorId'] = request.distributor_id
        if not UtilClient.is_unset(request.logistics_no):
            body['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.sub_distribution_order_id):
            body['SubDistributionOrderId'] = request.sub_distribution_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitReturnGoodLogistics4Distribution',
            version='2022-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20220531_models.SubmitReturnGoodLogistics4DistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_return_good_logistics_4distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_return_good_logistics_4distribution_with_options(request, runtime)
