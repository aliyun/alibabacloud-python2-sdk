# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudgameapi20200728 import models as cloud_game_api20200728_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudgameapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_dispatch_game_slot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            self.do_rpcrequest('BatchDispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_dispatch_game_slot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_dispatch_game_slot_with_options(request, runtime)

    def batch_stop_game_sessions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            self.do_rpcrequest('BatchStopGameSessions', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_game_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_game_sessions_with_options(request, runtime)

    def close_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            self.do_rpcrequest('CloseOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_order_with_options(request, runtime)

    def create_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            self.do_rpcrequest('CreateOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    def create_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            self.do_rpcrequest('CreateToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    def delivery_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            self.do_rpcrequest('DeliveryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delivery_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delivery_order_with_options(request, runtime)

    def dispatch_game_slot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            self.do_rpcrequest('DispatchGameSlot', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dispatch_game_slot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dispatch_game_slot_with_options(request, runtime)

    def get_game_ccu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            self.do_rpcrequest('GetGameCcu', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_game_ccu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_ccu_with_options(request, runtime)

    def get_game_stock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            self.do_rpcrequest('GetGameStock', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_game_stock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_stock_with_options(request, runtime)

    def get_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            self.do_rpcrequest('GetItem', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_item_with_options(request, runtime)

    def get_out_account_bind_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            self.do_rpcrequest('GetOutAccountBindDetail', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_out_account_bind_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_out_account_bind_detail_with_options(request, runtime)

    def get_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            self.do_rpcrequest('GetSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_with_options(request, runtime)

    def get_stop_game_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            self.do_rpcrequest('GetStopGameToken', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stop_game_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stop_game_token_with_options(request, runtime)

    def list_bought_games_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            self.do_rpcrequest('ListBoughtGames', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bought_games(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bought_games_with_options(request, runtime)

    def query_game_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            self.do_rpcrequest('QueryGame', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_game(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_game_with_options(request, runtime)

    def query_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            self.do_rpcrequest('QueryItems', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_items_with_options(request, runtime)

    def query_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            self.do_rpcrequest('QueryOrder', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_with_options(request, runtime)

    def query_out_account_bind_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            self.do_rpcrequest('QueryOutAccountBindStatus', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_out_account_bind_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_out_account_bind_status_with_options(request, runtime)

    def query_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            self.do_rpcrequest('QueryProject', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_project_with_options(request, runtime)

    def query_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            self.do_rpcrequest('QueryTenant', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tenant_with_options(request, runtime)

    def skip_trial_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            self.do_rpcrequest('SkipTrialPolicy', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def skip_trial_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.skip_trial_policy_with_options(request, runtime)

    def stop_game_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            self.do_rpcrequest('StopGameSession', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_game_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_game_session_with_options(request, runtime)

    def submit_internal_purchase_charge_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseChargeData', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_charge_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_charge_data_with_options(request, runtime)

    def submit_internal_purchase_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseOrders', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_orders_with_options(request, runtime)

    def submit_internal_purchase_ready_flag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            self.do_rpcrequest('SubmitInternalPurchaseReadyFlag', '2020-07-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_internal_purchase_ready_flag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_ready_flag_with_options(request, runtime)
