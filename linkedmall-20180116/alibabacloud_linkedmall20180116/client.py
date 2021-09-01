# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkedmall20180116 import models as linkedmall_20180116_models
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

    def add_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddAddressResponse(),
            self.do_rpcrequest('AddAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_address_with_options(request, runtime)

    def add_item_limit_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemLimitRuleResponse(),
            self.do_rpcrequest('AddItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_item_limit_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_item_limit_rule_with_options(request, runtime)

    def add_item_to_sub_bizs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.AddItemToSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemToSubBizsResponse(),
            self.do_rpcrequest('AddItemToSubBizs', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_item_to_sub_bizs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_item_to_sub_bizs_with_options(request, runtime)

    def add_supplier_new_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddSupplierNewItemsResponse(),
            self.do_rpcrequest('AddSupplierNewItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_supplier_new_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_supplier_new_items_with_options(request, runtime)

    def apply_refund_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundResponse(),
            self.do_rpcrequest('ApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_refund(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_refund_with_options(request, runtime)

    def batch_regist_anonymous_tb_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse(),
            self.do_rpcrequest('BatchRegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_regist_anonymous_tb_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_regist_anonymous_tb_account_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderResponse(),
            self.do_rpcrequest('CancelOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    def cancel_refund_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundResponse(),
            self.do_rpcrequest('CancelRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_refund(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_refund_with_options(request, runtime)

    def confirm_disburse_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseResponse(),
            self.do_rpcrequest('ConfirmDisburse', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_disburse(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_disburse_with_options(request, runtime)

    def create_movie_ticket_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateMovieTicketOrderResponse(),
            self.do_rpcrequest('CreateMovieTicketOrder', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_movie_ticket_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_movie_ticket_order_with_options(request, runtime)

    def create_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderResponse(),
            self.do_rpcrequest('CreateOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    def create_order_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderV2Response(),
            self.do_rpcrequest('CreateOrderV2', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_v2with_options(request, runtime)

    def create_pay_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreatePayUrlResponse(),
            self.do_rpcrequest('CreatePayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pay_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pay_url_with_options(request, runtime)

    def create_virtual_product_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateVirtualProductOrderResponse(),
            self.do_rpcrequest('CreateVirtualProductOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_product_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_product_order_with_options(request, runtime)

    def create_withhold_trade_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateWithholdTradeResponse(),
            self.do_rpcrequest('CreateWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_withhold_trade(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_withhold_trade_with_options(request, runtime)

    def delete_biz_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteBizItemsResponse(),
            self.do_rpcrequest('DeleteBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_biz_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_items_with_options(request, runtime)

    def delete_item_limit_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteItemLimitRuleResponse(),
            self.do_rpcrequest('DeleteItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_item_limit_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_item_limit_rule_with_options(request, runtime)

    def enable_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderResponse(),
            self.do_rpcrequest('EnableOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_order_with_options(request, runtime)

    def execute_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ExecuteNodeResponse(),
            self.do_rpcrequest('ExecuteNode', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_node_with_options(request, runtime)

    def get_category_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryChainResponse(),
            self.do_rpcrequest('GetCategoryChain', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_category_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_category_chain_with_options(request, runtime)

    def get_category_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryListResponse(),
            self.do_rpcrequest('GetCategoryList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_category_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_category_list_with_options(request, runtime)

    def get_custom_service_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCustomServiceUrlResponse(),
            self.do_rpcrequest('GetCustomServiceUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_custom_service_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_custom_service_url_with_options(request, runtime)

    def get_guide_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetGuidePageResponse(),
            self.do_rpcrequest('GetGuidePage', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_guide_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_guide_page_with_options(request, runtime)

    def get_item_promotion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetItemPromotionResponse(),
            self.do_rpcrequest('GetItemPromotion', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_item_promotion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_item_promotion_with_options(request, runtime)

    def get_login_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetLoginPageResponse(),
            self.do_rpcrequest('GetLoginPage', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_page_with_options(request, runtime)

    def get_switch_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetSwitchUrlResponse(),
            self.do_rpcrequest('GetSwitchUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_switch_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_switch_url_with_options(request, runtime)

    def get_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserInfoResponse(),
            self.do_rpcrequest('GetUserInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    def get_withhold_sign_page_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetWithholdSignPageUrlResponse(),
            self.do_rpcrequest('GetWithholdSignPageUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_withhold_sign_page_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_withhold_sign_page_url_with_options(request, runtime)

    def init_apply_refund_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundResponse(),
            self.do_rpcrequest('InitApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_apply_refund(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_apply_refund_with_options(request, runtime)

    def list_item_activities_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ListItemActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListItemActivitiesResponse(),
            self.do_rpcrequest('ListItemActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_item_activities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_item_activities_with_options(request, runtime)

    def modify_basic_and_biz_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicAndBizItemsResponse(),
            self.do_rpcrequest('ModifyBasicAndBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_basic_and_biz_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_basic_and_biz_items_with_options(request, runtime)

    def modify_biz_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBizItemsResponse(),
            self.do_rpcrequest('ModifyBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_biz_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_biz_items_with_options(request, runtime)

    def modify_item_limit_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyItemLimitRuleResponse(),
            self.do_rpcrequest('ModifyItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_item_limit_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_item_limit_rule_with_options(request, runtime)

    def notify_pay_order_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyPayOrderStatusResponse(),
            self.do_rpcrequest('NotifyPayOrderStatus', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def notify_pay_order_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.notify_pay_order_status_with_options(request, runtime)

    def notify_withhold_fund_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyWithholdFundResponse(),
            self.do_rpcrequest('NotifyWithholdFund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def notify_withhold_fund(self, request):
        runtime = util_models.RuntimeOptions()
        return self.notify_withhold_fund_with_options(request, runtime)

    def query_activity_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryActivityItemsResponse(),
            self.do_rpcrequest('QueryActivityItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_activity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_activity_items_with_options(request, runtime)

    def query_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressResponse(),
            self.do_rpcrequest('QueryAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_address_with_options(request, runtime)

    def query_address_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressDetailResponse(),
            self.do_rpcrequest('QueryAddressDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_address_detail_with_options(request, runtime)

    def query_address_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressListResponse(),
            self.do_rpcrequest('QueryAddressList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_address_list_with_options(request, runtime)

    def query_advertisement_settle_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse(),
            self.do_rpcrequest('QueryAdvertisementSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_advertisement_settle_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_advertisement_settle_info_with_options(request, runtime)

    def query_agreement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAgreementResponse(),
            self.do_rpcrequest('QueryAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_agreement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_agreement_with_options(request, runtime)

    def query_all_cinemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCinemasResponse(),
            self.do_rpcrequest('QueryAllCinemas', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_all_cinemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_all_cinemas_with_options(request, runtime)

    def query_all_cities_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryAllCitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCitiesResponse(),
            self.do_rpcrequest('QueryAllCities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_all_cities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_all_cities_with_options(request, runtime)

    def query_batch_regist_anonymous_tb_account_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse(),
            self.do_rpcrequest('QueryBatchRegistAnonymousTbAccountResult', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_batch_regist_anonymous_tb_account_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_batch_regist_anonymous_tb_account_result_with_options(request, runtime)

    def query_best_session_4items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBestSession4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBestSession4ItemsResponse(),
            self.do_rpcrequest('QueryBestSession4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_best_session_4items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_best_session_4items_with_options(request, runtime)

    def query_biz_item_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListResponse(),
            self.do_rpcrequest('QueryBizItemList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_biz_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_biz_item_list_with_options(request, runtime)

    def query_biz_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsResponse(),
            self.do_rpcrequest('QueryBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_biz_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_options(request, runtime)

    def query_biz_items_with_activity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemsWithActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsWithActivityResponse(),
            self.do_rpcrequest('QueryBizItemsWithActivity', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_biz_items_with_activity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_activity_with_options(request, runtime)

    def query_guide_item_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupResponse(),
            self.do_rpcrequest('QueryGuideItemGroup', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_guide_item_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_options(request, runtime)

    def query_guide_item_group_with_out_inventory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse(),
            self.do_rpcrequest('QueryGuideItemGroupWithOutInventory', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_guide_item_group_with_out_inventory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_out_inventory_with_options(request, runtime)

    def query_hot_movies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryHotMoviesResponse(),
            self.do_rpcrequest('QueryHotMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_hot_movies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_hot_movies_with_options(request, runtime)

    def query_inventory_of_items_in_biz_item_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse(),
            self.do_rpcrequest('QueryInventoryOfItemsInBizItemGroup', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_inventory_of_items_in_biz_item_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_inventory_of_items_in_biz_item_group_with_options(request, runtime)

    def query_item_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailResponse(),
            self.do_rpcrequest('QueryItemDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_with_options(request, runtime)

    def query_item_detail_inner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailInnerResponse(),
            self.do_rpcrequest('QueryItemDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_detail_inner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_inner_with_options(request, runtime)

    def query_item_in_sub_bizs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemInSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInSubBizsResponse(),
            self.do_rpcrequest('QueryItemInSubBizs', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_item_in_sub_bizs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_in_sub_bizs_with_options(request, runtime)

    def query_item_inventory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryResponse(),
            self.do_rpcrequest('QueryItemInventory', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_inventory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_inventory_with_options(request, runtime)

    def query_logistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryLogisticsResponse(),
            self.do_rpcrequest('QueryLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_logistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_logistics_with_options(request, runtime)

    def query_media_settle_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMediaSettleInfoResponse(),
            self.do_rpcrequest('QueryMediaSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_settle_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_media_settle_info_with_options(request, runtime)

    def query_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMessagesResponse(),
            self.do_rpcrequest('QueryMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_messages_with_options(request, runtime)

    def query_movie_comments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieCommentsResponse(),
            self.do_rpcrequest('QueryMovieComments', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_comments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_movie_comments_with_options(request, runtime)

    def query_movie_schedules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSchedulesResponse(),
            self.do_rpcrequest('QueryMovieSchedules', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_schedules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_movie_schedules_with_options(request, runtime)

    def query_movie_seats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSeatsResponse(),
            self.do_rpcrequest('QueryMovieSeats', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_seats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_movie_seats_with_options(request, runtime)

    def query_movie_tickets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieTicketsResponse(),
            self.do_rpcrequest('QueryMovieTickets', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_movie_tickets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_movie_tickets_with_options(request, runtime)

    def query_order_and_payment_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListResponse(),
            self.do_rpcrequest('QueryOrderAndPaymentList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_and_payment_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_and_payment_list_with_options(request, runtime)

    def query_order_commission_rate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderCommissionRateResponse(),
            self.do_rpcrequest('QueryOrderCommissionRate', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_commission_rate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_commission_rate_with_options(request, runtime)

    def query_order_detail_inner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderDetailInnerResponse(),
            self.do_rpcrequest('QueryOrderDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_detail_inner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_detail_inner_with_options(request, runtime)

    def query_order_id_by_pay_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderIdByPayIdResponse(),
            self.do_rpcrequest('QueryOrderIdByPayId', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_id_by_pay_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_id_by_pay_id_with_options(request, runtime)

    def query_order_info_after_sale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse(),
            self.do_rpcrequest('QueryOrderInfoAfterSale', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_order_info_after_sale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_info_after_sale_with_options(request, runtime)

    def query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(),
            self.do_rpcrequest('QueryOrderItemInfoByPaymentIdForAiZhanYou', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_item_info_by_payment_id_for_ai_zhan_you(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(request, runtime)

    def query_order_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListResponse(),
            self.do_rpcrequest('QueryOrderList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_with_options(request, runtime)

    def query_order_logistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsResponse(),
            self.do_rpcrequest('QueryOrderLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_logistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_logistics_with_options(request, runtime)

    def query_refund_application_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplicationDetailResponse(),
            self.do_rpcrequest('QueryRefundApplicationDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_refund_application_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_refund_application_detail_with_options(request, runtime)

    def query_statements_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryStatementsResponse(),
            self.do_rpcrequest('QueryStatements', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_statements(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_statements_with_options(request, runtime)

    def query_unfinished_activities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedActivitiesResponse(),
            self.do_rpcrequest('QueryUnfinishedActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_activities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_activities_with_options(request, runtime)

    def query_unfinished_sessions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessionsResponse(),
            self.do_rpcrequest('QueryUnfinishedSessions', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_with_options(request, runtime)

    def query_unfinished_sessions_4items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUnfinishedSessions4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse(),
            self.do_rpcrequest('QueryUnfinishedSessions4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_sessions_4items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_4items_with_options(request, runtime)

    def query_upcoming_movies_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUpcomingMoviesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUpcomingMoviesResponse(),
            self.do_rpcrequest('QueryUpcomingMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_upcoming_movies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_upcoming_movies_with_options(request, runtime)

    def query_withhold_trade_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryWithholdTradeResponse(),
            self.do_rpcrequest('QueryWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_withhold_trade(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_withhold_trade_with_options(request, runtime)

    def refund_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundOrderResponse(),
            self.do_rpcrequest('RefundOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_order_with_options(request, runtime)

    def refund_point_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundPointResponse(),
            self.do_rpcrequest('RefundPoint', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_point(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_point_with_options(request, runtime)

    def refuse_merchant_sync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefuseMerchantSyncTaskResponse(),
            self.do_rpcrequest('RefuseMerchantSyncTask', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_merchant_sync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_merchant_sync_task_with_options(request, runtime)

    def regist_anonymous_tb_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegistAnonymousTbAccountResponse(),
            self.do_rpcrequest('RegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def regist_anonymous_tb_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.regist_anonymous_tb_account_with_options(request, runtime)

    def release_movie_seat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReleaseMovieSeatResponse(),
            self.do_rpcrequest('ReleaseMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_movie_seat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_movie_seat_with_options(request, runtime)

    def remove_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveAddressResponse(),
            self.do_rpcrequest('RemoveAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_address_with_options(request, runtime)

    def remove_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveMessagesResponse(),
            self.do_rpcrequest('RemoveMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_messages_with_options(request, runtime)

    def render_h5order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderH5OrderResponse(),
            self.do_rpcrequest('RenderH5Order', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def render_h5order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.render_h5order_with_options(request, runtime)

    def render_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderResponse(),
            self.do_rpcrequest('RenderOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def render_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.render_order_with_options(request, runtime)

    def repay_for_pay_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayForPayUrlResponse(),
            self.do_rpcrequest('RepayForPayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def repay_for_pay_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.repay_for_pay_url_with_options(request, runtime)

    def repay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayOrderResponse(),
            self.do_rpcrequest('RepayOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def repay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.repay_order_with_options(request, runtime)

    def reserve_movie_seat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReserveMovieSeatResponse(),
            self.do_rpcrequest('ReserveMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reserve_movie_seat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reserve_movie_seat_with_options(request, runtime)

    def settle_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SettleOrderResponse(),
            self.do_rpcrequest('SettleOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def settle_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.settle_order_with_options(request, runtime)

    def submit_return_good_logistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse(),
            self.do_rpcrequest('SubmitReturnGoodLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_return_good_logistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_return_good_logistics_with_options(request, runtime)

    def sync_merchant_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SyncMerchantInfoResponse(),
            self.do_rpcrequest('SyncMerchantInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_merchant_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_merchant_info_with_options(request, runtime)

    def unsign_withhold_agreement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnsignWithholdAgreementResponse(),
            self.do_rpcrequest('UnsignWithholdAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unsign_withhold_agreement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsign_withhold_agreement_with_options(request, runtime)

    def update_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UpdateAddressResponse(),
            self.do_rpcrequest('UpdateAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_address_with_options(request, runtime)

    def validate_taobao_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ValidateTaobaoAccountResponse(),
            self.do_rpcrequest('ValidateTaobaoAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_taobao_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_taobao_account_with_options(request, runtime)
