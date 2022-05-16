# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_linkcard20210520 import models as linkcard_20210520_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkcard', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def card_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CardStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.CardStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def card_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.card_statistics_with_options(runtime)

    def force_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_type):
            query['DateType'] = request.date_type
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForceActivation',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ForceActivationResponse(),
            self.call_api(params, req, runtime)
        )

    def force_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.force_activation_with_options(request, runtime)

    def get_card_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destroy_card):
            query['DestroyCard'] = request.destroy_card
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.show_psim):
            query['ShowPsim'] = request.show_psim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_card_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_card_detail_with_options(request, runtime)

    def get_card_flow_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_list):
            query['DateList'] = request.date_list
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardFlowInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_card_flow_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_card_flow_info_with_options(request, runtime)

    def get_credential_pool_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialPoolStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCredentialPoolStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_credential_pool_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_credential_pool_statistics_with_options(request, runtime)

    def list_card_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_time_end):
            query['ActiveTimeEnd'] = request.active_time_end
        if not UtilClient.is_unset(request.active_time_start):
            query['ActiveTimeStart'] = request.active_time_start
        if not UtilClient.is_unset(request.ali_fee):
            query['AliFee'] = request.ali_fee
        if not UtilClient.is_unset(request.aliyun_order_id):
            query['AliyunOrderId'] = request.aliyun_order_id
        if not UtilClient.is_unset(request.apn_name):
            query['ApnName'] = request.apn_name
        if not UtilClient.is_unset(request.certify_type):
            query['CertifyType'] = request.certify_type
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not UtilClient.is_unset(request.data_level):
            query['DataLevel'] = request.data_level
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directional_group_id):
            query['DirectionalGroupId'] = request.directional_group_id
        if not UtilClient.is_unset(request.expire_time_end):
            query['ExpireTimeEnd'] = request.expire_time_end
        if not UtilClient.is_unset(request.expire_time_start):
            query['ExpireTimeStart'] = request.expire_time_start
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.imsi):
            query['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.is_auto_recharge):
            query['IsAutoRecharge'] = request.is_auto_recharge
        if not UtilClient.is_unset(request.msisdn):
            query['Msisdn'] = request.msisdn
        if not UtilClient.is_unset(request.notify_id):
            query['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.os_status):
            query['OsStatus'] = request.os_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pool_id):
            query['PoolId'] = request.pool_id
        if not UtilClient.is_unset(request.sim_type):
            query['SimType'] = request.sim_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListCardInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_card_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_card_info_with_options(request, runtime)

    def list_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrder',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ListOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def list_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_order_with_options(request, runtime)

    def rebind_resume_single_card_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.RebindResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RebindResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def rebind_resume_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebind_resume_single_card_with_options(request, runtime)

    def renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_num):
            query['BuyNum'] = request.buy_num
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.offer_code):
            query['OfferCode'] = request.offer_code
        if not UtilClient.is_unset(request.recharge_type):
            query['RechargeType'] = request.recharge_type
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        body = {}
        if not UtilClient.is_unset(request.api_product):
            body['ApiProduct'] = request.api_product
        if not UtilClient.is_unset(request.api_revision):
            body['ApiRevision'] = request.api_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Renew',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RenewResponse(),
            self.call_api(params, req, runtime)
        )

    def renew(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_with_options(request, runtime)

    def resume_single_card_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.ResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_single_card_with_options(request, runtime)

    def set_card_stop_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_restore):
            query['AutoRestore'] = request.auto_restore
        if not UtilClient.is_unset(request.flow_limit):
            query['FlowLimit'] = request.flow_limit
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCardStopRule',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.SetCardStopRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def set_card_stop_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_card_stop_rule_with_options(request, runtime)

    def stop_single_card_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.StopSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.StopSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_single_card_with_options(request, runtime)

    def update_auto_recharge_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoRechargeSwitch',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.UpdateAutoRechargeSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auto_recharge_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_recharge_switch_with_options(request, runtime)
