# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypls20170830 import models as dypls_20170830_models
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
        self._endpoint = self.get_endpoint('dypls', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_ar_invoice_with_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.address):
            body_flat['Address'] = request.address
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.applier):
            body['Applier'] = request.applier
        if not UtilClient.is_unset(request.apply_date):
            body['ApplyDate'] = request.apply_date
        if not UtilClient.is_unset(request.currency_code):
            body['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.excluding_tax_amount):
            body['ExcludingTaxAmount'] = request.excluding_tax_amount
        if not UtilClient.is_unset(request.input_type):
            body['InputType'] = request.input_type
        if not UtilClient.is_unset(request.invoice_type):
            body['InvoiceType'] = request.invoice_type
        if not UtilClient.is_unset(request.is_merged):
            body['IsMerged'] = request.is_merged
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.purchaser_bank_info):
            body['PurchaserBankInfo'] = request.purchaser_bank_info
        if not UtilClient.is_unset(request.purchaser_contact_info):
            body['PurchaserContactInfo'] = request.purchaser_contact_info
        if not UtilClient.is_unset(request.purchaser_name):
            body['PurchaserName'] = request.purchaser_name
        if not UtilClient.is_unset(request.purchaser_tax_no):
            body['PurchaserTaxNo'] = request.purchaser_tax_no
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.source_list):
            body['SourceList'] = request.source_list
        if not UtilClient.is_unset(request.tax_amount):
            body['TaxAmount'] = request.tax_amount
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyArInvoiceWithSource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyArInvoiceWithSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_ar_invoice_with_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_ar_invoice_with_source_with_options(request, runtime)

    def apply_black_info_export_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyBlackInfoExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyBlackInfoExportResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_black_info_export(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_black_info_export_with_options(request, runtime)

    def apply_call_record_export_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCallRecordExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyCallRecordExportResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_call_record_export(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_call_record_export_with_options(request, runtime)

    def apply_group_number_export_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyGroupNumberExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyGroupNumberExportResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_group_number_export(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_group_number_export_with_options(request, runtime)

    def apply_ring_tone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_ring_tone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_ring_tone_with_options(request, runtime)

    def batch_occupy_secret_res_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dypls_20170830_models.BatchOccupySecretResShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.batch_occupy_list):
            request.batch_occupy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.batch_occupy_list, 'BatchOccupyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_occupy_list_shrink):
            query['BatchOccupyList'] = request.batch_occupy_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchOccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BatchOccupySecretResResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_occupy_secret_res(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_occupy_secret_res_with_options(request, runtime)

    def bind_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_status):
            query['AsrStatus'] = request.asr_status
        if not UtilClient.is_unset(request.axn_extension_b):
            query['AxnExtensionB'] = request.axn_extension_b
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.exp_time):
            query['ExpTime'] = request.exp_time
        if not UtilClient.is_unset(request.is_record):
            query['IsRecord'] = request.is_record
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BindResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_resource_with_options(request, runtime)

    def black_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_map):
            query['BlackMap'] = request.black_map
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlackOperate',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BlackOperateResponse(),
            self.call_api(params, req, runtime)
        )

    def black_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.black_operate_with_options(request, runtime)

    def create_certify_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateCertifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_certify_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certify_info_with_options(request, runtime)

    def create_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_contacts_with_options(request, runtime)

    def create_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_detail_with_options(request, runtime)

    def create_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_info_with_options(request, runtime)

    def create_logical_delete_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateLogicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_logical_delete(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_logical_delete_with_options(request, runtime)

    def create_message_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def create_message_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_message_callback_with_options(request, runtime)

    def create_message_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_ids):
            query['BillIds'] = request.bill_ids
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_title):
            query['QueueTitle'] = request.queue_title
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageQueue',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def create_message_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_message_queue_with_options(request, runtime)

    def create_physical_delete_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhysicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePhysicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_physical_delete(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_physical_delete_with_options(request, runtime)

    def create_pool_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pool_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pool_info_with_options(request, runtime)

    def create_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    def create_ring_tone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_name):
            query['RingName'] = request.ring_name
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ring_tone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ring_tone_with_options(request, runtime)

    def create_subs_trial_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_a):
            query['PhoneA'] = request.phone_a
        if not UtilClient.is_unset(request.phone_b):
            query['PhoneB'] = request.phone_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubsTrial',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateSubsTrialResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subs_trial(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subs_trial_with_options(request, runtime)

    def create_transfer_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.origin_bill_id):
            query['OriginBillId'] = request.origin_bill_id
        if not UtilClient.is_unset(request.origin_name):
            query['OriginName'] = request.origin_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_bill_id):
            query['TargetBillId'] = request.target_bill_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transfer_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transfer_record_with_options(request, runtime)

    def delete_certify_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteCertifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_certify_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_certify_info_with_options(request, runtime)

    def delete_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_contacts_with_options(request, runtime)

    def delete_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id_list):
            query['IdList'] = request.id_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_detail_with_options(request, runtime)

    def delete_message_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_message_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    def delete_ring_tone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ring_tone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ring_tone_with_options(request, runtime)

    def download_complete_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadComplete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DownloadCompleteResponse(),
            self.call_api(params, req, runtime)
        )

    def download_complete(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_complete_with_options(request, runtime)

    def export_res_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ExportResResponse(),
            self.call_api(params, req, runtime)
        )

    def export_res(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_res_with_options(request, runtime)

    def get_einvoice_pdf_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.invoice_code):
            body['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_no):
            body['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEinvoicePdfData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetEinvoicePdfDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_einvoice_pdf_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_einvoice_pdf_data_with_options(request, runtime)

    def get_secret_asr_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretAsrInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetSecretAsrInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_secret_asr_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_secret_asr_info_with_options(request, runtime)

    def get_user_resource_tag_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserResourceTagStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetUserResourceTagStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_resource_tag_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_resource_tag_status_with_options(request, runtime)

    def list_asr_language_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsrLanguageModels',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ListAsrLanguageModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_asr_language_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asr_language_models_with_options(request, runtime)

    def lock_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.LockResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_resource_with_options(request, runtime)

    def occupy_secret_res_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.order_detail_id):
            query['OrderDetailId'] = request.order_detail_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no_type):
            query['SecretNoType'] = request.secret_no_type
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.secret_no):
            query['secretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OccupySecretResResponse(),
            self.call_api(params, req, runtime)
        )

    def occupy_secret_res(self, request):
        runtime = util_models.RuntimeOptions()
        return self.occupy_secret_res_with_options(request, runtime)

    def order_succeeded_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderSucceededCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OrderSucceededCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def order_succeeded_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.order_succeeded_callback_with_options(request, runtime)

    def pool_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.frozen_day):
            query['FrozenDay'] = request.frozen_day
        if not UtilClient.is_unset(request.need_all_call_records):
            query['NeedAllCallRecords'] = request.need_all_call_records
        if not UtilClient.is_unset(request.open_sms_white):
            query['OpenSmsWhite'] = request.open_sms_white
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_warning_limit):
            query['PoolWarningLimit'] = request.pool_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.select_xmode):
            query['SelectXMode'] = request.select_xmode
        if not UtilClient.is_unset(request.smart_sms_whitelist):
            query['SmartSmsWhitelist'] = request.smart_sms_whitelist
        if not UtilClient.is_unset(request.sms_channel):
            query['SmsChannel'] = request.sms_channel
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PoolConfig',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PoolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def pool_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pool_config_with_options(request, runtime)

    def purchase_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.buy_number):
            query['BuyNumber'] = request.buy_number
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        if not UtilClient.is_unset(request.usage_scenarios):
            query['UsageScenarios'] = request.usage_scenarios
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseResources',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PurchaseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def purchase_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purchase_resources_with_options(request, runtime)

    def query_binding_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBindingDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBindingDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_binding_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_binding_details_with_options(request, runtime)

    def query_black_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_prefix):
            query['BlackPrefix'] = request.black_prefix
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBlackList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_black_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_black_list_with_options(request, runtime)

    def query_buy_page_init_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageInitData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageInitDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_buy_page_init_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_init_data_with_options(request, runtime)

    def query_buy_page_res_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResCount',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResCountResponse(),
            self.call_api(params, req, runtime)
        )

    def query_buy_page_res_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_res_count_with_options(request, runtime)

    def query_buy_page_res_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_buy_page_res_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_res_info_with_options(request, runtime)

    def query_buy_res_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyResInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_buy_res_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_buy_res_info_with_options(request, runtime)

    def query_call_recording_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallRecordingList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCallRecordingListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_call_recording_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_recording_list_with_options(request, runtime)

    def query_certify_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_status):
            query['CertifyStatus'] = request.certify_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCertifyInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_certify_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_certify_info_list_with_options(request, runtime)

    def query_certify_overview_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCertifyOverviewInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyOverviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_certify_overview_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_certify_overview_info_with_options(request, runtime)

    def query_contacts_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactsList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryContactsListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_contacts_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_contacts_list_with_options(request, runtime)

    def query_cust_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCustInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cust_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cust_info_with_options(request, runtime)

    def query_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDownloadUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_download_url_with_options(request, runtime)

    def query_effective_invoice_list_by_bill_nos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.bill_no):
            body['BillNo'] = request.bill_no
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.major_bill_no):
            body['MajorBillNo'] = request.major_bill_no
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEffectiveInvoiceListByBillNos',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse(),
            self.call_api(params, req, runtime)
        )

    def query_effective_invoice_list_by_bill_nos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_effective_invoice_list_by_bill_nos_with_options(request, runtime)

    def query_export_res_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExportResUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryExportResUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_export_res_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_export_res_url_with_options(request, runtime)

    def query_group_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupDetailList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_group_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_group_detail_list_with_options(request, runtime)

    def query_group_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.query_key):
            query['QueryKey'] = request.query_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_group_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_group_info_list_with_options(request, runtime)

    def query_invoice_info_by_request_no_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInvoiceInfoByRequestNo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_invoice_info_by_request_no(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_invoice_info_by_request_no_with_options(request, runtime)

    def query_message_callback_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageCallbackInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageCallbackInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_message_callback_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_message_callback_info_with_options(request, runtime)

    def query_message_queue_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageQueueList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageQueueListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_message_queue_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_message_queue_list_with_options(request, runtime)

    def query_monthly_bill_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject_item_id):
            query['SubjectItemId'] = request.subject_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyBillInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_monthly_bill_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_info_with_options(request, runtime)

    def query_monthly_statistics_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_monthly_statistics_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_statistics_info_with_options(request, runtime)

    def query_no_buy_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNoBuyTasks',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoBuyTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def query_no_buy_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_no_buy_tasks_with_options(request, runtime)

    def query_no_distribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNoDistribute',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoDistributeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_no_distribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_no_distribute_with_options(request, runtime)

    def query_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpenStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_open_status_with_options(request, runtime)

    def query_package_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPackageDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_package_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_package_detail_with_options(request, runtime)

    def query_package_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPackageList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_package_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_package_list_with_options(request, runtime)

    def query_package_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPackageStatistics',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_package_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_package_statistics_with_options(request, runtime)

    def query_pool_city_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolCityList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolCityListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pool_city_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pool_city_list_with_options(request, runtime)

    def query_pool_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_fuzzy_query):
            query['IsFuzzyQuery'] = request.is_fuzzy_query
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_param):
            query['SearchParam'] = request.search_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pool_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pool_info_list_with_options(request, runtime)

    def query_pool_monthly_bill_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolMonthlyBillInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pool_monthly_bill_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pool_monthly_bill_info_with_options(request, runtime)

    def query_pool_statistics_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pool_statistics_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pool_statistics_info_with_options(request, runtime)

    def query_pool_summary_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pool_summary_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pool_summary_info_with_options(request, runtime)

    def query_purchased_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_purchased_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_purchased_info_with_options(request, runtime)

    def query_purchased_res_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedResList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedResListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_purchased_res_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_purchased_res_list_with_options(request, runtime)

    def query_qrcode_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_number):
            query['SecretNumber'] = request.secret_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQRCodeInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryQRCodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_qrcode_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_qrcode_info_with_options(request, runtime)

    def query_recording_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordingUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRecordingUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_recording_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_recording_url_with_options(request, runtime)

    def query_res_summary_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryResSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_res_summary_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_res_summary_info_with_options(request, runtime)

    def query_ring_tone_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRingToneUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingToneUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_ring_tone_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_ring_tone_url_with_options(request, runtime)

    def query_ring_tones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRingTones',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingTonesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_ring_tones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_ring_tones_with_options(request, runtime)

    def query_simple_pool_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimplePoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QuerySimplePoolInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_simple_pool_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_simple_pool_info_list_with_options(request, runtime)

    def query_statistics_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_statistics_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_statistics_info_with_options(request, runtime)

    def query_tag_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_key):
            query['AttributeKey'] = request.attribute_key
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_attribute_key):
            query['SubAttributeKey'] = request.sub_attribute_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagOpenStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTagOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tag_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tag_open_status_with_options(request, runtime)

    def query_transfer_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_details_with_options(request, runtime)

    def query_transfer_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_record_with_options(request, runtime)

    def query_transfer_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecords',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_records_with_options(request, runtime)

    def query_user_delete_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDeleteStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserDeleteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_delete_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_delete_status_with_options(request, runtime)

    def query_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_with_options(request, runtime)

    def query_user_res_pool_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserResPoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserResPoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_res_pool_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_res_pool_info_with_options(request, runtime)

    def query_virtual_operation_show_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVirtualOperationShow',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryVirtualOperationShowResponse(),
            self.call_api(params, req, runtime)
        )

    def query_virtual_operation_show(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_operation_show_with_options(request, runtime)

    def query_warning_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWarningList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWarningListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_warning_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_warning_list_with_options(request, runtime)

    def query_waybill_order_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaybillOrderInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_waybill_order_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_waybill_order_info_with_options(request, runtime)

    def query_waybill_order_statistics_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaybillOrderStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_waybill_order_statistics_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_waybill_order_statistics_info_with_options(request, runtime)

    def release_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ReleaseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def release_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_resource_with_options(request, runtime)

    def test_tts_ring_tone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        if not UtilClient.is_unset(request.voice_speed):
            query['VoiceSpeed'] = request.voice_speed
        if not UtilClient.is_unset(request.voice_style):
            query['VoiceStyle'] = request.voice_style
        if not UtilClient.is_unset(request.voice_type):
            query['VoiceType'] = request.voice_type
        if not UtilClient.is_unset(request.voice_volume):
            query['VoiceVolume'] = request.voice_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestTtsRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.TestTtsRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    def test_tts_ring_tone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_tts_ring_tone_with_options(request, runtime)

    def unbind_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bind_ids):
            query['BindIds'] = request.bind_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnbindResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_resource_with_options(request, runtime)

    def unlock_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnlockResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_resource_with_options(request, runtime)

    def update_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_contacts_with_options(request, runtime)

    def update_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_detail_with_options(request, runtime)

    def update_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_info_with_options(request, runtime)

    def update_pool_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePoolName',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdatePoolNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pool_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pool_name_with_options(request, runtime)

    def update_res_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResRemark',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateResRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_res_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_res_remark_with_options(request, runtime)

    def validate_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateOrder',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ValidateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_order_with_options(request, runtime)
