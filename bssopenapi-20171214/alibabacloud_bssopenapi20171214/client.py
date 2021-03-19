# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bssopenapi20171214 import models as bss_open_api_20171214_models
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
            'ap-northeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'business.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'business.ap-southeast-1.aliyuncs.com',
            'cn-beijing': 'business.aliyuncs.com',
            'cn-beijing-finance-1': 'business.aliyuncs.com',
            'cn-beijing-finance-pop': 'business.aliyuncs.com',
            'cn-beijing-gov-1': 'business.aliyuncs.com',
            'cn-beijing-nu16-b01': 'business.aliyuncs.com',
            'cn-chengdu': 'business.aliyuncs.com',
            'cn-edge-1': 'business.aliyuncs.com',
            'cn-fujian': 'business.aliyuncs.com',
            'cn-haidian-cm12-c01': 'business.aliyuncs.com',
            'cn-hangzhou': 'business.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'business.aliyuncs.com',
            'cn-hangzhou-finance': 'business.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'business.aliyuncs.com',
            'cn-hangzhou-test-306': 'business.aliyuncs.com',
            'cn-hongkong': 'business.aliyuncs.com',
            'cn-hongkong-finance-pop': 'business.aliyuncs.com',
            'cn-huhehaote': 'business.aliyuncs.com',
            'cn-north-2-gov-1': 'business.aliyuncs.com',
            'cn-qingdao': 'business.aliyuncs.com',
            'cn-qingdao-nebula': 'business.aliyuncs.com',
            'cn-shanghai': 'business.aliyuncs.com',
            'cn-shanghai-et15-b01': 'business.aliyuncs.com',
            'cn-shanghai-et2-b01': 'business.aliyuncs.com',
            'cn-shanghai-finance-1': 'business.aliyuncs.com',
            'cn-shanghai-inner': 'business.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'business.aliyuncs.com',
            'cn-shenzhen': 'business.aliyuncs.com',
            'cn-shenzhen-finance-1': 'business.aliyuncs.com',
            'cn-shenzhen-inner': 'business.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'business.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'business.aliyuncs.com',
            'cn-wuhan': 'business.aliyuncs.com',
            'cn-yushanfang': 'business.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'business.aliyuncs.com',
            'cn-zhangjiakou': 'business.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'business.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'business.aliyuncs.com',
            'eu-central-1': 'business.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'business.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'business.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'business.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'business.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'business.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'business.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('bssopenapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.AllocateCostUnitResourceResponse().from_map(
            self.do_rpcrequest('AllocateCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_cost_unit_resource_with_options(request, runtime)

    def apply_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ApplyInvoiceResponse().from_map(
            self.do_rpcrequest('ApplyInvoice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_invoice_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CancelOrderResponse().from_map(
            self.do_rpcrequest('CancelOrder', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    def change_reseller_consume_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse().from_map(
            self.do_rpcrequest('ChangeResellerConsumeAmount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_reseller_consume_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_reseller_consume_amount_with_options(request, runtime)

    def convert_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ConvertChargeTypeResponse().from_map(
            self.do_rpcrequest('ConvertChargeType', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_charge_type_with_options(request, runtime)

    def create_ag_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateAgAccountResponse().from_map(
            self.do_rpcrequest('CreateAgAccount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ag_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    def create_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateCostUnitResponse().from_map(
            self.do_rpcrequest('CreateCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cost_unit_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResellerUserQuotaResponse().from_map(
            self.do_rpcrequest('CreateResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_reseller_user_quota_with_options(request, runtime)

    def create_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResourcePackageResponse().from_map(
            self.do_rpcrequest('CreateResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_package_with_options(request, runtime)

    def delete_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DeleteCostUnitResponse().from_map(
            self.do_rpcrequest('DeleteCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cost_unit_with_options(request, runtime)

    def describe_resource_package_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeResourcePackageProductResponse().from_map(
            self.do_rpcrequest('DescribeResourcePackageProduct', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_package_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_package_product_with_options(request, runtime)

    def describe_split_item_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeSplitItemBillResponse().from_map(
            self.do_rpcrequest('DescribeSplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_split_item_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_split_item_bill_with_options(request, runtime)

    def enable_bill_generation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.EnableBillGenerationResponse().from_map(
            self.do_rpcrequest('EnableBillGeneration', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_bill_generation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_bill_generation_with_options(request, runtime)

    def get_customer_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetCustomerAccountInfoResponse().from_map(
            self.do_rpcrequest('GetCustomerAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_customer_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customer_account_info_with_options(request, runtime)

    def get_customer_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.GetCustomerListResponse().from_map(
            self.do_rpcrequest('GetCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_customer_list(self):
        runtime = util_models.RuntimeOptions()
        return self.get_customer_list_with_options(runtime)

    def get_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetOrderDetailResponse().from_map(
            self.do_rpcrequest('GetOrderDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_order_detail_with_options(request, runtime)

    def get_pay_as_you_go_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetPayAsYouGoPriceResponse().from_map(
            self.do_rpcrequest('GetPayAsYouGoPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pay_as_you_go_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    def get_resource_package_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetResourcePackagePriceResponse().from_map(
            self.do_rpcrequest('GetResourcePackagePrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_package_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_package_price_with_options(request, runtime)

    def get_subscription_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetSubscriptionPriceResponse().from_map(
            self.do_rpcrequest('GetSubscriptionPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_subscription_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_price_with_options(request, runtime)

    def modify_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyCostUnitResponse().from_map(
            self.do_rpcrequest('ModifyCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cost_unit_with_options(request, runtime)

    def modify_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyInstanceResponse().from_map(
            self.do_rpcrequest('ModifyInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    def query_account_balance_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.QueryAccountBalanceResponse().from_map(
            self.do_rpcrequest('QueryAccountBalance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_account_balance(self):
        runtime = util_models.RuntimeOptions()
        return self.query_account_balance_with_options(runtime)

    def query_account_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountBillResponse().from_map(
            self.do_rpcrequest('QueryAccountBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_account_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_account_bill_with_options(request, runtime)

    def query_account_transaction_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse().from_map(
            self.do_rpcrequest('QueryAccountTransactionDetails', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_account_transaction_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_account_transaction_details_with_options(request, runtime)

    def query_account_transactions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionsResponse().from_map(
            self.do_rpcrequest('QueryAccountTransactions', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_account_transactions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_account_transactions_with_options(request, runtime)

    def query_available_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAvailableInstancesResponse().from_map(
            self.do_rpcrequest('QueryAvailableInstances', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_available_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_available_instances_with_options(request, runtime)

    def query_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillResponse().from_map(
            self.do_rpcrequest('QueryBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_with_options(request, runtime)

    def query_bill_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillOverviewResponse().from_map(
            self.do_rpcrequest('QueryBillOverview', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_bill_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_overview_with_options(request, runtime)

    def query_bill_to_osssubscription_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse().from_map(
            self.do_rpcrequest('QueryBillToOSSSubscription', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_bill_to_osssubscription(self):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_to_osssubscription_with_options(runtime)

    def query_cash_coupons_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCashCouponsResponse().from_map(
            self.do_rpcrequest('QueryCashCoupons', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cash_coupons(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cash_coupons_with_options(request, runtime)

    def query_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResponse().from_map(
            self.do_rpcrequest('QueryCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_with_options(request, runtime)

    def query_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResourceResponse().from_map(
            self.do_rpcrequest('QueryCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_resource_with_options(request, runtime)

    def query_customer_address_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCustomerAddressListResponse().from_map(
            self.do_rpcrequest('QueryCustomerAddressList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_customer_address_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_customer_address_list_with_options(request, runtime)

    def query_evaluate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryEvaluateListResponse().from_map(
            self.do_rpcrequest('QueryEvaluateList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_evaluate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_evaluate_list_with_options(request, runtime)

    def query_financial_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryFinancialAccountInfoResponse().from_map(
            self.do_rpcrequest('QueryFinancialAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_financial_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_financial_account_info_with_options(request, runtime)

    def query_instance_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceBillResponse().from_map(
            self.do_rpcrequest('QueryInstanceBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_instance_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_bill_with_options(request, runtime)

    def query_instance_by_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceByTagResponse().from_map(
            self.do_rpcrequest('QueryInstanceByTag', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_instance_by_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_by_tag_with_options(request, runtime)

    def query_instance_gaap_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceGaapCostResponse().from_map(
            self.do_rpcrequest('QueryInstanceGaapCost', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_instance_gaap_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_gaap_cost_with_options(request, runtime)

    def query_invoicing_customer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInvoicingCustomerListResponse().from_map(
            self.do_rpcrequest('QueryInvoicingCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_invoicing_customer_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_invoicing_customer_list_with_options(request, runtime)

    def query_monthly_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyBillResponse().from_map(
            self.do_rpcrequest('QueryMonthlyBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monthly_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_with_options(request, runtime)

    def query_monthly_instance_consumption_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse().from_map(
            self.do_rpcrequest('QueryMonthlyInstanceConsumption', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monthly_instance_consumption(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_instance_consumption_with_options(request, runtime)

    def query_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryOrdersResponse().from_map(
            self.do_rpcrequest('QueryOrders', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_orders_with_options(request, runtime)

    def query_permission_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPermissionListResponse().from_map(
            self.do_rpcrequest('QueryPermissionList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_permission_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_permission_list_with_options(request, runtime)

    def query_prepaid_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPrepaidCardsResponse().from_map(
            self.do_rpcrequest('QueryPrepaidCards', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_prepaid_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_prepaid_cards_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryProductListResponse().from_map(
            self.do_rpcrequest('QueryProductList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    def query_redeem_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return bss_open_api_20171214_models.QueryRedeemResponse().from_map(
            self.do_rpcrequest('QueryRedeem', '2017-12-14', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_redeem(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_redeem_with_options(request, runtime)

    def query_relation_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRelationListResponse().from_map(
            self.do_rpcrequest('QueryRelationList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_relation_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_relation_list_with_options(request, runtime)

    def query_reseller_available_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse().from_map(
            self.do_rpcrequest('QueryResellerAvailableQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_reseller_available_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_reseller_available_quota_with_options(request, runtime)

    def query_riutilization_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRIUtilizationDetailResponse().from_map(
            self.do_rpcrequest('QueryRIUtilizationDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_riutilization_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_riutilization_detail_with_options(request, runtime)

    def query_savings_plans_deduct_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse().from_map(
            self.do_rpcrequest('QuerySavingsPlansDeductLog', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_savings_plans_deduct_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_deduct_log_with_options(request, runtime)

    def query_savings_plans_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse().from_map(
            self.do_rpcrequest('QuerySavingsPlansInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_savings_plans_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_instance_with_options(request, runtime)

    def query_settle_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettleBillResponse().from_map(
            self.do_rpcrequest('QuerySettleBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_settle_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_settle_bill_with_options(request, runtime)

    def query_settlement_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettlementBillResponse().from_map(
            self.do_rpcrequest('QuerySettlementBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_settlement_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_settlement_bill_with_options(request, runtime)

    def query_split_item_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySplitItemBillResponse().from_map(
            self.do_rpcrequest('QuerySplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_split_item_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_split_item_bill_with_options(request, runtime)

    def query_user_oms_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryUserOmsDataResponse().from_map(
            self.do_rpcrequest('QueryUserOmsData', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_user_oms_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_oms_data_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def renew_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewResourcePackageResponse().from_map(
            self.do_rpcrequest('RenewResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_resource_package_with_options(request, runtime)

    def save_user_credit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SaveUserCreditResponse().from_map(
            self.do_rpcrequest('SaveUserCredit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_user_credit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_user_credit_with_options(request, runtime)

    def set_credit_label_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetCreditLabelActionResponse().from_map(
            self.do_rpcrequest('SetCreditLabelAction', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_credit_label_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_credit_label_action_with_options(request, runtime)

    def set_renewal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetRenewalResponse().from_map(
            self.do_rpcrequest('SetRenewal', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_renewal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_renewal_with_options(request, runtime)

    def set_reseller_user_alarm_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse().from_map(
            self.do_rpcrequest('SetResellerUserAlarmThreshold', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_reseller_user_alarm_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_alarm_threshold_with_options(request, runtime)

    def set_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserQuotaResponse().from_map(
            self.do_rpcrequest('SetResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_quota_with_options(request, runtime)

    def set_reseller_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserStatusResponse().from_map(
            self.do_rpcrequest('SetResellerUserStatus', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_reseller_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_status_with_options(request, runtime)

    def subscribe_bill_to_osswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SubscribeBillToOSSResponse().from_map(
            self.do_rpcrequest('SubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def subscribe_bill_to_oss(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_bill_to_osswith_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unsubscribe_bill_to_osswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UnsubscribeBillToOSSResponse().from_map(
            self.do_rpcrequest('UnsubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unsubscribe_bill_to_oss(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_bill_to_osswith_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UpgradeResourcePackageResponse().from_map(
            self.do_rpcrequest('UpgradeResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_resource_package_with_options(request, runtime)
