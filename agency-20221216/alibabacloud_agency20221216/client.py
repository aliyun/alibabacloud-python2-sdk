# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_agency20221216 import models as agency_20221216_models
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

    def cancel_subscription_bill_with_options(self, request, runtime):
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        

        @param request: CancelSubscriptionBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelSubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CancelSubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_subscription_bill(self, request):
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        

        @param request: CancelSubscriptionBillRequest

        @return: CancelSubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_subscription_bill_with_options(request, runtime)

    def create_customer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.customer_source):
            query['CustomerSource'] = request.customer_source
        if not UtilClient.is_unset(request.customer_sub_trade):
            query['CustomerSubTrade'] = request.customer_sub_trade
        if not UtilClient.is_unset(request.customer_trade):
            query['CustomerTrade'] = request.customer_trade
        if not UtilClient.is_unset(request.nation):
            query['Nation'] = request.nation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CreateCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_customer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_customer_with_options(request, runtime)

    def customer_quota_record_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomerQuotaRecordList',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CustomerQuotaRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    def customer_quota_record_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.customer_quota_record_list_with_options(request, runtime)

    def deduct_outstanding_balance_with_options(self, request, runtime):
        """
        Note that sometimes you may find that the customer\\"s Used Credit is negative. This indicates that there is no need to restore the Used Credit, and its ready for customer\\"s usage. This phenomenon occurs because a refund is generated while the customer\\"s credit is full, thereby triggered additional increasing on the customer\\"s credit.
        For example, if the customer\\"s maximum Available Credit is 1000 with no usage, and a refund of 300 occurs, the Used Credit will become -300.
        

        @param request: DeductOutstandingBalanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeductOutstandingBalanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deduct_amount):
            query['DeductAmount'] = request.deduct_amount
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeductOutstandingBalance',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.DeductOutstandingBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    def deduct_outstanding_balance(self, request):
        """
        Note that sometimes you may find that the customer\\"s Used Credit is negative. This indicates that there is no need to restore the Used Credit, and its ready for customer\\"s usage. This phenomenon occurs because a refund is generated while the customer\\"s credit is full, thereby triggered additional increasing on the customer\\"s credit.
        For example, if the customer\\"s maximum Available Credit is 1000 with no usage, and a refund of 300 occurs, the Used Credit will become -300.
        

        @param request: DeductOutstandingBalanceRequest

        @return: DeductOutstandingBalanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deduct_outstanding_balance_with_options(request, runtime)

    def edit_end_user_status_with_options(self, request, runtime):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditEndUserStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EditEndUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditEndUserStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditEndUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_end_user_status(self, request):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditEndUserStatusRequest

        @return: EditEndUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_end_user_status_with_options(request, runtime)

    def edit_new_buy_status_with_options(self, request, runtime):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditNewBuyStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EditNewBuyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_buy_status):
            query['NewBuyStatus'] = request.new_buy_status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditNewBuyStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditNewBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_new_buy_status(self, request):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditNewBuyStatusRequest

        @return: EditNewBuyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_new_buy_status_with_options(request, runtime)

    def edit_zero_credit_shutdown_with_options(self, request, runtime):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditZeroCreditShutdownRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EditZeroCreditShutdownResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.shutdown_policy):
            query['ShutdownPolicy'] = request.shutdown_policy
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditZeroCreditShutdown',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditZeroCreditShutdownResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_zero_credit_shutdown(self, request):
        """
        The caller should be the Partner as identified in the Alibaba Cloud distribution model. </br>
        **This content is only published on the international site. **\
        

        @param request: EditZeroCreditShutdownRequest

        @return: EditZeroCreditShutdownResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_zero_credit_shutdown_with_options(request, runtime)

    def export_customer_quota_record_with_options(self, request, runtime):
        """
        Caller must be a Partner from International Site, either Distribution or Reseller will do.
        

        @param request: ExportCustomerQuotaRecordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportCustomerQuotaRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_user_pk):
            query['EndUserPk'] = request.end_user_pk
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCustomerQuotaRecord',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ExportCustomerQuotaRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def export_customer_quota_record(self, request):
        """
        Caller must be a Partner from International Site, either Distribution or Reseller will do.
        

        @param request: ExportCustomerQuotaRecordRequest

        @return: ExportCustomerQuotaRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_customer_quota_record_with_options(request, runtime)

    def get_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_info_with_options(request, runtime)

    def get_credit_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreditInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetCreditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_credit_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_credit_info_with_options(request, runtime)

    def get_daily_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDailyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetDailyBillResponse(),
            self.call_api(params, req, runtime)
        )

    def get_daily_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_daily_bill_with_options(request, runtime)

    def get_invite_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_status_list):
            query['InviteStatusList'] = request.invite_status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInviteStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetInviteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_invite_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_invite_status_with_options(request, runtime)

    def get_monthly_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonthlyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetMonthlyBillResponse(),
            self.call_api(params, req, runtime)
        )

    def get_monthly_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monthly_bill_with_options(request, runtime)

    def get_unassociated_customer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUnassociatedCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetUnassociatedCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_unassociated_customer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_unassociated_customer_with_options(request, runtime)

    def invite_sub_account_with_options(self, request, runtime):
        """
        The current API request rate for the Cloud Product has not been disclosed.
        

        @param request: InviteSubAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InviteSubAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_info_list):
            query['AccountInfoList'] = request.account_info_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteSubAccount',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.InviteSubAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def invite_sub_account(self, request):
        """
        The current API request rate for the Cloud Product has not been disclosed.
        

        @param request: InviteSubAccountRequest

        @return: InviteSubAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.invite_sub_account_with_options(request, runtime)

    def list_countries_with_options(self, runtime):
        """
        The current API request rate for cloud products has not been disclosed.
        

        @param request: ListCountriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCountriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCountries',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ListCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_countries(self):
        """
        The current API request rate for cloud products has not been disclosed.
        

        @return: ListCountriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_countries_with_options(runtime)

    def list_coupon_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.coupon_template_id):
            query['CouponTemplateId'] = request.coupon_template_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCouponUsage',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ListCouponUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_coupon_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_coupon_usage_with_options(request, runtime)

    def quota_list_export_paged_with_options(self, request, runtime):
        """
        Caller must be a Partner from International Site, either Distribution or Reseller will do.
        

        @param request: QuotaListExportPagedRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuotaListExportPagedResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuotaListExportPaged',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.QuotaListExportPagedResponse(),
            self.call_api(params, req, runtime)
        )

    def quota_list_export_paged(self, request):
        """
        Caller must be a Partner from International Site, either Distribution or Reseller will do.
        

        @param request: QuotaListExportPagedRequest

        @return: QuotaListExportPagedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.quota_list_export_paged_with_options(request, runtime)

    def resend_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_id):
            query['InviteId'] = request.invite_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmail',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ResendEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def resend_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_email_with_options(request, runtime)

    def set_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_nickname):
            query['AccountNickname'] = request.account_nickname
        if not UtilClient.is_unset(request.customer_bd):
            query['CustomerBd'] = request.customer_bd
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_account_info_with_options(request, runtime)

    def set_credit_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credit_line):
            query['CreditLine'] = request.credit_line
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLine',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetCreditLineResponse(),
            self.call_api(params, req, runtime)
        )

    def set_credit_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_credit_line_with_options(request, runtime)

    def set_warning_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.warning_value):
            query['WarningValue'] = request.warning_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWarningThreshold',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetWarningThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def set_warning_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_warning_threshold_with_options(request, runtime)

    def subscription_bill_with_options(self, request, runtime):
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        

        @param request: SubscriptionBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bill_format):
            query['BillFormat'] = request.bill_format
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_segment_size):
            query['SubscribeSegmentSize'] = request.subscribe_segment_size
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    def subscription_bill(self, request):
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        

        @param request: SubscriptionBillRequest

        @return: SubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.subscription_bill_with_options(request, runtime)
