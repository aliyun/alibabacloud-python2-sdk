# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

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
            'cn-hangzhou': 'business.aliyuncs.com',
            'cn-shanghai': 'business.aliyuncs.com',
            'ap-southeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'business.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'business.ap-southeast-1.aliyuncs.com',
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
            'cn-huhehaote-nebula-1': 'business.aliyuncs.com',
            'cn-north-2-gov-1': 'business.aliyuncs.com',
            'cn-qingdao': 'business.aliyuncs.com',
            'cn-qingdao-nebula': 'business.aliyuncs.com',
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
            'cn-wulanchabu': 'business.aliyuncs.com',
            'cn-yushanfang': 'business.aliyuncs.com',
            'cn-zhangbei': 'business.aliyuncs.com',
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

    def add_account_relation_with_options(self, request, runtime):
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        

        @param request: AddAccountRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddAccountRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AddAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_account_relation(self, request):
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        

        @param request: AddAccountRelationRequest

        @return: AddAccountRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_account_relation_with_options(request, runtime)

    def allocate_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_unit_id):
            query['FromUnitId'] = request.from_unit_id
        if not UtilClient.is_unset(request.from_unit_user_id):
            query['FromUnitUserId'] = request.from_unit_user_id
        if not UtilClient.is_unset(request.resource_instance_list):
            query['ResourceInstanceList'] = request.resource_instance_list
        if not UtilClient.is_unset(request.to_unit_id):
            query['ToUnitId'] = request.to_unit_id
        if not UtilClient.is_unset(request.to_unit_user_id):
            query['ToUnitUserId'] = request.to_unit_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AllocateCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_cost_unit_resource_with_options(request, runtime)

    def apply_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.apply_user_nick):
            query['ApplyUserNick'] = request.apply_user_nick
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.invoice_amount):
            query['InvoiceAmount'] = request.invoice_amount
        if not UtilClient.is_unset(request.invoice_by_amount):
            query['InvoiceByAmount'] = request.invoice_by_amount
        if not UtilClient.is_unset(request.invoicing_type):
            query['InvoicingType'] = request.invoicing_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_way):
            query['ProcessWay'] = request.process_way
        if not UtilClient.is_unset(request.selected_ids):
            query['SelectedIds'] = request.selected_ids
        if not UtilClient.is_unset(request.user_remark):
            query['UserRemark'] = request.user_remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyInvoice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ApplyInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_invoice_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    def change_reseller_consume_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjust_type):
            query['AdjustType'] = request.adjust_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.extend_map):
            query['ExtendMap'] = request.extend_map
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResellerConsumeAmount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse(),
            self.call_api(params, req, runtime)
        )

    def change_reseller_consume_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_reseller_consume_amount_with_options(request, runtime)

    def confirm_relation_with_options(self, request, runtime):
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        

        @param request: ConfirmRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfirmRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.confirm_code):
            query['ConfirmCode'] = request.confirm_code
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConfirmRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_relation(self, request):
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        

        @param request: ConfirmRelationRequest

        @return: ConfirmRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_relation_with_options(request, runtime)

    def convert_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertChargeType',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConvertChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def convert_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_charge_type_with_options(request, runtime)

    def create_ag_account_with_options(self, request, runtime):
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        

        @param request: CreateAgAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAgAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_attr):
            query['AccountAttr'] = request.account_attr
        if not UtilClient.is_unset(request.city_name):
            query['CityName'] = request.city_name
        if not UtilClient.is_unset(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.nation_code):
            query['NationCode'] = request.nation_code
        if not UtilClient.is_unset(request.postcode):
            query['Postcode'] = request.postcode
        if not UtilClient.is_unset(request.province_name):
            query['ProvinceName'] = request.province_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgAccount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ag_account(self, request):
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        

        @param request: CreateAgAccountRequest

        @return: CreateAgAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    def create_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cost_unit_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logistics):
            query['Logistics'] = request.logistics
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def create_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_reseller_user_quota_with_options(request, runtime)

    def create_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_package_with_options(request, runtime)

    def create_savings_plans_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.CreateSavingsPlansInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_map):
            request.extend_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.extend_map_shrink):
            query['ExtendMap'] = request.extend_map_shrink
        if not UtilClient.is_unset(request.pay_mode):
            query['PayMode'] = request.pay_mode
        if not UtilClient.is_unset(request.pool_value):
            query['PoolValue'] = request.pool_value
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_savings_plans_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_savings_plans_instance_with_options(request, runtime)

    def delete_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DeleteCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cost_unit_with_options(request, runtime)

    def describe_cost_budgets_summary_with_options(self, request, runtime):
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        

        @param request: DescribeCostBudgetsSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCostBudgetsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.budget_name):
            query['BudgetName'] = request.budget_name
        if not UtilClient.is_unset(request.budget_status):
            query['BudgetStatus'] = request.budget_status
        if not UtilClient.is_unset(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostBudgetsSummary',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cost_budgets_summary(self, request):
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        

        @param request: DescribeCostBudgetsSummaryRequest

        @return: DescribeCostBudgetsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_budgets_summary_with_options(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_with_options(self, request, runtime):
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        

        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period(self, request):
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        

        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest

        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_with_options(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_date_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_date_end):
            body['AmortizationDateEnd'] = request.amortization_date_end
        if not UtilClient.is_unset(request.amortization_date_start):
            body['AmortizationDateStart'] = request.amortization_date_start
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriodDate',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period_date(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_date_with_options(request, runtime)

    def describe_instance_amortized_cost_by_consume_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_consume_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_consume_period_with_options(request, runtime)

    def describe_instance_bill_with_options(self, request, runtime):
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        

        @param request: DescribeInstanceBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_bill(self, request):
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        

        @param request: DescribeInstanceBillRequest

        @return: DescribeInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_bill_with_options(request, runtime)

    def describe_instance_deduct_amortized_cost_by_amortization_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDeductAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_deduct_amortized_cost_by_amortization_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_deduct_amortized_cost_by_amortization_period_with_options(request, runtime)

    def describe_pricing_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePricingModule',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribePricingModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pricing_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pricing_module_with_options(request, runtime)

    def describe_product_amortized_cost_by_amortization_period_with_options(self, request, runtime):
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        

        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_product_amortized_cost_by_amortization_period(self, request):
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        

        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest

        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_amortized_cost_by_amortization_period_with_options(request, runtime)

    def describe_product_amortized_cost_by_consume_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_product_amortized_cost_by_consume_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_product_amortized_cost_by_consume_period_with_options(request, runtime)

    def describe_resource_coverage_detail_with_options(self, request, runtime):
        """
        1\\. The queried coverage details are the same as those displayed in the table on the Coverage tab of the Manage Reserved Instances page in the Billing Management console.
        2\\. You can call this operation to query the coverage details of RIs or SCUs.
        3\\. You can call this operation to query coverage details at an hourly, daily, or monthly granularity.
        

        @param request: DescribeResourceCoverageDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeResourceCoverageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_coverage_detail(self, request):
        """
        1\\. The queried coverage details are the same as those displayed in the table on the Coverage tab of the Manage Reserved Instances page in the Billing Management console.
        2\\. You can call this operation to query the coverage details of RIs or SCUs.
        3\\. You can call this operation to query coverage details at an hourly, daily, or monthly granularity.
        

        @param request: DescribeResourceCoverageDetailRequest

        @return: DescribeResourceCoverageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_coverage_detail_with_options(request, runtime)

    def describe_resource_coverage_total_with_options(self, request, runtime):
        """
        The queried total coverage data is the same as the aggregated data displayed on the Coverage tab of the Manage Reserved Instances page in the Billing Management console.
        You can call this operation to query the total coverage data of RIs or SCUs.
        

        @param request: DescribeResourceCoverageTotalRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeResourceCoverageTotalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_coverage_total(self, request):
        """
        The queried total coverage data is the same as the aggregated data displayed on the Coverage tab of the Manage Reserved Instances page in the Billing Management console.
        You can call this operation to query the total coverage data of RIs or SCUs.
        

        @param request: DescribeResourceCoverageTotalRequest

        @return: DescribeResourceCoverageTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_coverage_total_with_options(request, runtime)

    def describe_resource_package_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePackageProduct',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourcePackageProductResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_package_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_package_product_with_options(request, runtime)

    def describe_resource_usage_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_usage_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_detail_with_options(request, runtime)

    def describe_resource_usage_total_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_usage_total(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_total_with_options(request, runtime)

    def describe_savings_plans_coverage_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_savings_plans_coverage_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_coverage_detail_with_options(request, runtime)

    def describe_savings_plans_coverage_total_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_savings_plans_coverage_total(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_coverage_total_with_options(request, runtime)

    def describe_savings_plans_usage_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_savings_plans_usage_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_usage_detail_with_options(request, runtime)

    def describe_savings_plans_usage_total_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_savings_plans_usage_total(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_usage_total_with_options(request, runtime)

    def describe_split_item_bill_with_options(self, request, runtime):
        """
        The data that you query by calling this operation is the same as the data that is queried by billing cycles in the Split Bill module of Cost Allocation.
        *   You can query split bills that were generated within the last 12 months by calling this operation.
        *   You can query split bills only after you enable the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in the User Center console.
        

        @param request: DescribeSplitItemBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.split_item_id):
            query['SplitItemID'] = request.split_item_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_split_item_bill(self, request):
        """
        The data that you query by calling this operation is the same as the data that is queried by billing cycles in the Split Bill module of Cost Allocation.
        *   You can query split bills that were generated within the last 12 months by calling this operation.
        *   You can query split bills only after you enable the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in the User Center console.
        

        @param request: DescribeSplitItemBillRequest

        @return: DescribeSplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_split_item_bill_with_options(request, runtime)

    def enable_bill_generation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBillGeneration',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.EnableBillGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_bill_generation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_bill_generation_with_options(request, runtime)

    def get_account_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_relation_with_options(request, runtime)

    def get_customer_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_customer_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customer_account_info_with_options(request, runtime)

    def get_customer_list_with_options(self, runtime):
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        

        @param request: GetCustomerListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCustomerListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_customer_list(self):
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        

        @return: GetCustomerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_customer_list_with_options(runtime)

    def get_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_order_detail_with_options(request, runtime)

    def get_pay_as_you_go_price_with_options(self, request, runtime):
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        

        @param request: GetPayAsYouGoPriceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPayAsYouGoPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayAsYouGoPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetPayAsYouGoPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pay_as_you_go_price(self, request):
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        

        @param request: GetPayAsYouGoPriceRequest

        @return: GetPayAsYouGoPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    def get_resource_package_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePackagePrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetResourcePackagePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_package_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_package_price_with_options(request, runtime)

    def get_subscription_price_with_options(self, request, runtime):
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        

        @param request: GetSubscriptionPriceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSubscriptionPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.service_period_quantity):
            query['ServicePeriodQuantity'] = request.service_period_quantity
        if not UtilClient.is_unset(request.service_period_unit):
            query['ServicePeriodUnit'] = request.service_period_unit
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetSubscriptionPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subscription_price(self, request):
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        

        @param request: GetSubscriptionPriceRequest

        @return: GetSubscriptionPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_price_with_options(request, runtime)

    def inquiry_price_refund_instance_with_options(self, request, runtime):
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        

        @param request: InquiryPriceRefundInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InquiryPriceRefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InquiryPriceRefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def inquiry_price_refund_instance(self, request):
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        

        @param request: InquiryPriceRefundInstanceRequest

        @return: InquiryPriceRefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inquiry_price_refund_instance_with_options(request, runtime)

    def modify_account_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_operation):
            query['RelationOperation'] = request.relation_operation
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_relation_with_options(request, runtime)

    def modify_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cost_unit_with_options(request, runtime)

    def modify_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    def query_account_balance_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAccountBalance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_account_balance(self):
        runtime = util_models.RuntimeOptions()
        return self.query_account_balance_with_options(runtime)

    def query_account_bill_with_options(self, request, runtime):
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        

        @param request: QueryAccountBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryAccountBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_group_by_product):
            query['IsGroupByProduct'] = request.is_group_by_product
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBillResponse(),
            self.call_api(params, req, runtime)
        )

    def query_account_bill(self, request):
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        

        @param request: QueryAccountBillRequest

        @return: QueryAccountBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_account_bill_with_options(request, runtime)

    def query_account_transaction_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactionDetails',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_account_transaction_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_account_transaction_details_with_options(request, runtime)

    def query_account_transactions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_flow):
            query['TransactionFlow'] = request.transaction_flow
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactions',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_account_transactions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_account_transactions_with_options(request, runtime)

    def query_available_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.end_time_start):
            query['EndTimeStart'] = request.end_time_start
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvailableInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAvailableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_available_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_available_instances_with_options(request, runtime)

    def query_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillResponse(),
            self.call_api(params, req, runtime)
        )

    def query_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_with_options(request, runtime)

    def query_bill_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBillOverview',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def query_bill_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_overview_with_options(request, runtime)

    def query_bill_to_osssubscription_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryBillToOSSSubscription',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_bill_to_osssubscription(self):
        runtime = util_models.RuntimeOptions()
        return self.query_bill_to_osssubscription_with_options(runtime)

    def query_cash_coupons_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCashCoupons',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCashCouponsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cash_coupons(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cash_coupons_with_options(request, runtime)

    def query_commodity_list_with_options(self, request, runtime):
        """
        You can call this operation to query the information about a service based on the service code.
        

        @param request: QueryCommodityListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryCommodityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommodityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCommodityListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_commodity_list(self, request):
        """
        You can call this operation to query the information about a service based on the service code.
        

        @param request: QueryCommodityListRequest

        @return: QueryCommodityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_commodity_list_with_options(request, runtime)

    def query_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_unit_id):
            query['ParentUnitId'] = request.parent_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cost_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_with_options(request, runtime)

    def query_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_resource_with_options(request, runtime)

    def query_customer_address_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomerAddressList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCustomerAddressListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_customer_address_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_customer_address_list_with_options(request, runtime)

    def query_dputilization_detail_with_options(self, request, runtime):
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        

        @param request: QueryDPUtilizationDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryDPUtilizationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_share):
            query['IncludeShare'] = request.include_share
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.last_token):
            query['LastToken'] = request.last_token
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDPUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryDPUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dputilization_detail(self, request):
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        

        @param request: QueryDPUtilizationDetailRequest

        @return: QueryDPUtilizationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dputilization_detail_with_options(request, runtime)

    def query_evaluate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.biz_type_list):
            query['BizTypeList'] = request.biz_type_list
        if not UtilClient.is_unset(request.end_amount):
            query['EndAmount'] = request.end_amount
        if not UtilClient.is_unset(request.end_biz_time):
            query['EndBizTime'] = request.end_biz_time
        if not UtilClient.is_unset(request.end_search_time):
            query['EndSearchTime'] = request.end_search_time
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.start_amount):
            query['StartAmount'] = request.start_amount
        if not UtilClient.is_unset(request.start_biz_time):
            query['StartBizTime'] = request.start_biz_time
        if not UtilClient.is_unset(request.start_search_time):
            query['StartSearchTime'] = request.start_search_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEvaluateList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryEvaluateListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_evaluate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_evaluate_list_with_options(request, runtime)

    def query_financial_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFinancialAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryFinancialAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_financial_account_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_financial_account_info_with_options(request, runtime)

    def query_instance_bill_with_options(self, request, runtime):
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        

        @param request: QueryInstanceBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instance_bill(self, request):
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        

        @param request: QueryInstanceBillRequest

        @return: QueryInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_instance_bill_with_options(request, runtime)

    def query_instance_by_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceByTag',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceByTagResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instance_by_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_by_tag_with_options(request, runtime)

    def query_instance_gaap_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceGaapCost',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceGaapCostResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instance_gaap_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instance_gaap_cost_with_options(request, runtime)

    def query_invoicing_customer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvoicingCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInvoicingCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_invoicing_customer_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_invoicing_customer_list_with_options(request, runtime)

    def query_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_status):
            query['PaymentStatus'] = request.payment_status
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_orders_with_options(request, runtime)

    def query_permission_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPermissionList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPermissionListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_permission_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_permission_list_with_options(request, runtime)

    def query_prepaid_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrepaidCards',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPrepaidCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_prepaid_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_prepaid_cards_with_options(request, runtime)

    def query_price_entity_list_with_options(self, request, runtime):
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        

        @param request: QueryPriceEntityListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryPriceEntityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPriceEntityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPriceEntityListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_price_entity_list(self, request):
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        

        @param request: QueryPriceEntityListRequest

        @return: QueryPriceEntityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_price_entity_list_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_total_count):
            query['QueryTotalCount'] = request.query_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryProductListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    def query_riutilization_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ricommodity_code):
            query['RICommodityCode'] = request.ricommodity_code
        if not UtilClient.is_unset(request.riinstance_id):
            query['RIInstanceId'] = request.riinstance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRIUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRIUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_riutilization_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_riutilization_detail_with_options(request, runtime)

    def query_redeem_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRedeem',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    def query_redeem(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_redeem_with_options(request, runtime)

    def query_relation_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRelationList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRelationListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_relation_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_relation_list_with_options(request, runtime)

    def query_reseller_available_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_codes):
            query['ItemCodes'] = request.item_codes
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerAvailableQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def query_reseller_available_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_reseller_available_quota_with_options(request, runtime)

    def query_reseller_user_alarm_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_reseller_user_alarm_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_reseller_user_alarm_threshold_with_options(request, runtime)

    def query_resource_package_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        if not UtilClient.is_unset(request.include_partner):
            query['IncludePartner'] = request.include_partner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourcePackageInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResourcePackageInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_resource_package_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_resource_package_instances_with_options(request, runtime)

    def query_savings_plans_deduct_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDeductLog',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse(),
            self.call_api(params, req, runtime)
        )

    def query_savings_plans_deduct_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_deduct_log_with_options(request, runtime)

    def query_savings_plans_discount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDiscount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse(),
            self.call_api(params, req, runtime)
        )

    def query_savings_plans_discount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_discount_with_options(request, runtime)

    def query_savings_plans_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_savings_plans_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_instance_with_options(request, runtime)

    def query_settle_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySettleBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySettleBillResponse(),
            self.call_api(params, req, runtime)
        )

    def query_settle_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_settle_bill_with_options(request, runtime)

    def query_sku_price_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.QuerySkuPriceListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.price_factor_condition_map):
            request.price_factor_condition_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.price_factor_condition_map, 'PriceFactorConditionMap', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySkuPriceList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySkuPriceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sku_price_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sku_price_list_with_options(request, runtime)

    def query_split_item_bill_with_options(self, request, runtime):
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        

        @param request: QuerySplitItemBillRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuerySplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    def query_split_item_bill(self, request):
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        

        @param request: QuerySplitItemBillRequest

        @return: QuerySplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_split_item_bill_with_options(request, runtime)

    def query_user_oms_data_with_options(self, request, runtime):
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        

        @param request: QueryUserOmsDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryUserOmsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table):
            query['Table'] = request.table
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserOmsData',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryUserOmsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_oms_data(self, request):
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        

        @param request: QueryUserOmsDataRequest

        @return: QueryUserOmsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_oms_data_with_options(request, runtime)

    def refund_instance_with_options(self, request, runtime):
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        

        @param request: RefundInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.immediately_release):
            query['ImmediatelyRelease'] = request.immediately_release
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_instance(self, request):
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        

        @param request: RefundInstanceRequest

        @return: RefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        

        @param request: ReleaseInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance(self, request):
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        

        @param request: ReleaseInstanceRequest

        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def relieve_account_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RelieveAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RelieveAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def relieve_account_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.relieve_account_relation_with_options(request, runtime)

    def renew_change_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewChangeInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewChangeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_change_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_change_instance_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def renew_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_resource_package_with_options(request, runtime)

    def save_user_credit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avoid_expiration):
            query['AvoidExpiration'] = request.avoid_expiration
        if not UtilClient.is_unset(request.avoid_notification):
            query['AvoidNotification'] = request.avoid_notification
        if not UtilClient.is_unset(request.avoid_prepaid_expiration):
            query['AvoidPrepaidExpiration'] = request.avoid_prepaid_expiration
        if not UtilClient.is_unset(request.avoid_prepaid_notification):
            query['AvoidPrepaidNotification'] = request.avoid_prepaid_notification
        if not UtilClient.is_unset(request.credit_type):
            query['CreditType'] = request.credit_type
        if not UtilClient.is_unset(request.credit_value):
            query['CreditValue'] = request.credit_value
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveUserCredit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SaveUserCreditResponse(),
            self.call_api(params, req, runtime)
        )

    def save_user_credit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_user_credit_with_options(request, runtime)

    def set_all_expiration_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.unify_expire_day):
            query['UnifyExpireDay'] = request.unify_expire_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAllExpirationDay',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetAllExpirationDayResponse(),
            self.call_api(params, req, runtime)
        )

    def set_all_expiration_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_all_expiration_day_with_options(request, runtime)

    def set_credit_label_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.clear_cycle):
            query['ClearCycle'] = request.clear_cycle
        if not UtilClient.is_unset(request.credit_amount):
            query['CreditAmount'] = request.credit_amount
        if not UtilClient.is_unset(request.currency_code):
            query['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.daily_cycle):
            query['DailyCycle'] = request.daily_cycle
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.is_need_add_settle_label):
            query['IsNeedAddSettleLabel'] = request.is_need_add_settle_label
        if not UtilClient.is_unset(request.is_need_adjust_credit_account):
            query['IsNeedAdjustCreditAccount'] = request.is_need_adjust_credit_account
        if not UtilClient.is_unset(request.is_need_save_notify_rule):
            query['IsNeedSaveNotifyRule'] = request.is_need_save_notify_rule
        if not UtilClient.is_unset(request.is_need_set_credit_amount):
            query['IsNeedSetCreditAmount'] = request.is_need_set_credit_amount
        if not UtilClient.is_unset(request.need_notice):
            query['NeedNotice'] = request.need_notice
        if not UtilClient.is_unset(request.new_create_mode):
            query['NewCreateMode'] = request.new_create_mode
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.site_code):
            query['SiteCode'] = request.site_code
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLabelAction',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetCreditLabelActionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_credit_label_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_credit_label_action_with_options(request, runtime)

    def set_renewal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renewal_period):
            query['RenewalPeriod'] = request.renewal_period
        if not UtilClient.is_unset(request.renewal_period_unit):
            query['RenewalPeriodUnit'] = request.renewal_period_unit
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRenewal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetRenewalResponse(),
            self.call_api(params, req, runtime)
        )

    def set_renewal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_renewal_with_options(request, runtime)

    def set_reseller_user_alarm_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_thresholds):
            query['AlarmThresholds'] = request.alarm_thresholds
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def set_reseller_user_alarm_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_alarm_threshold_with_options(request, runtime)

    def set_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def set_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_quota_with_options(request, runtime)

    def set_reseller_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.stop_mode):
            query['StopMode'] = request.stop_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserStatus',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_reseller_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_status_with_options(request, runtime)

    def subscribe_bill_to_osswith_options(self, request, runtime):
        """
        Before you call this operation, take note of the following items:
        *   You can subscribe to only one type of bill at a time.
        *   The bills generated on the previous day are pushed on a daily basis the next day after you subscribe to the bills. The full-data bills for the previous month are pushed on the fourth day of each month. The monthly bills in the PDF format for the previous month are pushed on the fourth day of each month.
        *   The daily bills may be delayed. The delayed bills are pushed the next day after they are generated. The delayed bills may include the bills that should have been pushed on the previous day. We recommend that you query the full-data bills for the previous month at the beginning of each month.
        *   The bill subscriber must have the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The SubscribeBillToOSS operation has the same functionality as the Save Expense Details to OSS Bucket feature in User Center.
        *   To subscribe to the bills stored in an OSS bucket, make sure that the directory name specified for the OSS bucket conforms to the following naming rules:
        1.  1.  The directory name can contain only UTF-8 characters and cannot contain emoticons.
        2.  2.  Forward slashes (/) are used to separate paths and can be used to create subdirectories with ease. The directory name cannot start with a forward slash (/), a backslash (\\\\), or consecutive forward slashes (/).
        3.  3.  The name of a subdirectory cannot be set to two consecutive periods (..).
        4.  4.  The directory name must be 1 to 254 characters in length.
        *   File names:
        *   **BillingItemDetailForBillingPeriod** (Detailed bills of billable items)
        *   File name format for a daily push: `UID_BillingItemDetail_YYYYMMDD`. Example: `169**_BillingItemDetail_20190310`.
        *   File name format for a full-data push at the beginning of the next month: `UID_BillingItemDetail_YYYYMM`. Example: `169**_BillingItemDetail_201903`.
        *   **InstanceDetailForBillingPeriod** (Detailed bills of instances)
        *   File name format for a daily push: `UID_InstanceDetail_YYYYMMDD`. Example: `169**_InstanceDetail_20190310`.
        *   File name format for a full-data push at the beginning of the next month: `UID_InstanceDetail_YYYYMM`. Example: `169**_InstanceDetail_201903`.
        *   **InstanceDetailMonthly** (Instance-based bills summarized by billing cycle)
        *   File name format for a daily push: `UID_InstanceDetailMonthly_YYYYMM`. Example: `169**_InstanceDetailMonthly_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **BillingItemDetailMonthly** (Billable item-based bills summarized by billing cycle)
        *   File name format for a daily push: `UID_BillingItemDetailMonthly_YYYYMM`. Example: `169**_BillingItemDetailMonthly_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **SplitItemDetailDaily** (Split bills summarized by day)
        *   File name format for a daily push: `UID_SplitItemDetailDaily_YYYYMM`. Example: `169**_SplitItemDetailDaily_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **MonthBill** (Monthly bill in the PDF format)
        *   File name format for a monthly push: `UID_MonthBill_YYYYMM`. Example: `169**_MonthBill_201903`. The bill for the previous month is pushed on the fourth day of each month.
        *   The bills of the MonthBill type are PDF files, whereas the bills of other types are CSV files. If the number of data rows in a bill exceeds a threshold, the bill is automatically split into multiple CSV files. Then, the multiple CSV files are automatically merged and compressed into a ZIP file that has the same name format as the original file.
        

        @param request: SubscribeBillToOSSRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubscribeBillToOSSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.bucket_path):
            query['BucketPath'] = request.bucket_path
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.row_limit_per_file):
            query['RowLimitPerFile'] = request.row_limit_per_file
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    def subscribe_bill_to_oss(self, request):
        """
        Before you call this operation, take note of the following items:
        *   You can subscribe to only one type of bill at a time.
        *   The bills generated on the previous day are pushed on a daily basis the next day after you subscribe to the bills. The full-data bills for the previous month are pushed on the fourth day of each month. The monthly bills in the PDF format for the previous month are pushed on the fourth day of each month.
        *   The daily bills may be delayed. The delayed bills are pushed the next day after they are generated. The delayed bills may include the bills that should have been pushed on the previous day. We recommend that you query the full-data bills for the previous month at the beginning of each month.
        *   The bill subscriber must have the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The SubscribeBillToOSS operation has the same functionality as the Save Expense Details to OSS Bucket feature in User Center.
        *   To subscribe to the bills stored in an OSS bucket, make sure that the directory name specified for the OSS bucket conforms to the following naming rules:
        1.  1.  The directory name can contain only UTF-8 characters and cannot contain emoticons.
        2.  2.  Forward slashes (/) are used to separate paths and can be used to create subdirectories with ease. The directory name cannot start with a forward slash (/), a backslash (\\\\), or consecutive forward slashes (/).
        3.  3.  The name of a subdirectory cannot be set to two consecutive periods (..).
        4.  4.  The directory name must be 1 to 254 characters in length.
        *   File names:
        *   **BillingItemDetailForBillingPeriod** (Detailed bills of billable items)
        *   File name format for a daily push: `UID_BillingItemDetail_YYYYMMDD`. Example: `169**_BillingItemDetail_20190310`.
        *   File name format for a full-data push at the beginning of the next month: `UID_BillingItemDetail_YYYYMM`. Example: `169**_BillingItemDetail_201903`.
        *   **InstanceDetailForBillingPeriod** (Detailed bills of instances)
        *   File name format for a daily push: `UID_InstanceDetail_YYYYMMDD`. Example: `169**_InstanceDetail_20190310`.
        *   File name format for a full-data push at the beginning of the next month: `UID_InstanceDetail_YYYYMM`. Example: `169**_InstanceDetail_201903`.
        *   **InstanceDetailMonthly** (Instance-based bills summarized by billing cycle)
        *   File name format for a daily push: `UID_InstanceDetailMonthly_YYYYMM`. Example: `169**_InstanceDetailMonthly_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **BillingItemDetailMonthly** (Billable item-based bills summarized by billing cycle)
        *   File name format for a daily push: `UID_BillingItemDetailMonthly_YYYYMM`. Example: `169**_BillingItemDetailMonthly_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **SplitItemDetailDaily** (Split bills summarized by day)
        *   File name format for a daily push: `UID_SplitItemDetailDaily_YYYYMM`. Example: `169**_SplitItemDetailDaily_201903`. A bill of this type contains the full data generated from the beginning of the month to the current day, and is updated every day until the fourth day of the next month.
        *   **MonthBill** (Monthly bill in the PDF format)
        *   File name format for a monthly push: `UID_MonthBill_YYYYMM`. Example: `169**_MonthBill_201903`. The bill for the previous month is pushed on the fourth day of each month.
        *   The bills of the MonthBill type are PDF files, whereas the bills of other types are CSV files. If the number of data rows in a bill exceeds a threshold, the bill is automatically split into multiple CSV files. Then, the multiple CSV files are automatically merged and compressed into a ZIP file that has the same name format as the original file.
        

        @param request: SubscribeBillToOSSRequest

        @return: SubscribeBillToOSSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.subscribe_bill_to_osswith_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unsubscribe_bill_to_osswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnsubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UnsubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    def unsubscribe_bill_to_oss(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_bill_to_osswith_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UpgradeResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_resource_package_with_options(request, runtime)
