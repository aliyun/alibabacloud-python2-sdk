# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_linkedmall20230930 import models as linkedmall_20230930_models
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

    def cancel_refund_order_with_options(self, dispute_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/%s/commands/cancel' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(dispute_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CancelRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_refund_order(self, dispute_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_refund_order_with_options(dispute_id, headers, runtime)

    def confirm_disburse_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/confirmDisburse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ConfirmDisburseResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_disburse(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_disburse_with_options(request, headers, runtime)

    def create_goods_shipping_notice_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateGoodsShippingNotice',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/command/createGoodsShippingNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateGoodsShippingNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_goods_shipping_notice(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_goods_shipping_notice_with_options(request, headers, runtime)

    def create_purchase_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreatePurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_purchase_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_purchase_order_with_options(request, headers, runtime)

    def create_refund_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_refund_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_refund_order_with_options(request, headers, runtime)

    def get_order_with_options(self, order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(order_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_order(self, order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_order_with_options(order_id, headers, runtime)

    def get_purchase_order_status_with_options(self, purchase_order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaseOrderStatus',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/%s/status' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(purchase_order_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaseOrderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_purchase_order_status(self, purchase_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_purchase_order_status_with_options(purchase_order_id, headers, runtime)

    def get_purchaser_shop_with_options(self, purchaser_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaserShop',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(purchaser_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaserShopResponse(),
            self.call_api(params, req, runtime)
        )

    def get_purchaser_shop(self, purchaser_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_purchaser_shop_with_options(purchaser_id, headers, runtime)

    def get_refund_order_with_options(self, dispute_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(dispute_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_refund_order(self, dispute_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_refund_order_with_options(dispute_id, headers, runtime)

    def get_selection_product_with_options(self, product_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProduct',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductResponse(),
            self.call_api(params, req, runtime)
        )

    def get_selection_product(self, product_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_selection_product_with_options(product_id, request, headers, runtime)

    def get_selection_product_sale_info_with_options(self, product_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProductSaleInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/%s/saleInfo' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductSaleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_selection_product_sale_info(self, product_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_selection_product_sale_info_with_options(product_id, request, headers, runtime)

    def list_logistics_orders_with_options(self, order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListLogisticsOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/%s/logisticsOrders' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(order_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListLogisticsOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_logistics_orders(self, order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logistics_orders_with_options(order_id, headers, runtime)

    def list_purchaser_shops_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPurchaserShops',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListPurchaserShopsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_purchaser_shops(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_purchaser_shops_with_options(request, headers, runtime)

    def list_selection_product_sale_infos_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionProductSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_selection_product_sale_infos(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_product_sale_infos_with_options(request, headers, runtime)

    def list_selection_products_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSelectionProducts',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_selection_products(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_products_with_options(request, headers, runtime)

    def list_selection_sku_sale_infos_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionSkuSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/skus/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_selection_sku_sale_infos(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_sku_sale_infos_with_options(request, headers, runtime)

    def query_child_division_code_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryChildDivisionCode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/division/commands/queryChildDivisionCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryChildDivisionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_child_division_code(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_child_division_code_with_options(request, headers, runtime)

    def query_orders_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_orders(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_orders_with_options(request, headers, runtime)

    def render_purchase_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderPurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderPurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def render_purchase_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.render_purchase_order_with_options(request, headers, runtime)

    def render_refund_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def render_refund_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.render_refund_order_with_options(request, headers, runtime)
