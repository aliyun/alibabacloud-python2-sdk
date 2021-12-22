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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def adapt_game_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FrameRate'] = request.frame_rate
        query['Resolution'] = request.resolution
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AdaptGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AdaptGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def adapt_game_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.adapt_game_version_with_options(request, runtime)

    def add_game_to_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGameToProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.AddGameToProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def add_game_to_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_game_to_project_with_options(request, runtime)

    def batch_dispatch_game_slot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.queue_user_list):
            body['QueueUserList'] = request.queue_user_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchDispatchGameSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_dispatch_game_slot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_dispatch_game_slot_with_options(request, runtime)

    def batch_stop_game_sessions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        query['Reason'] = request.reason
        query['Tags'] = request.tags
        query['Token'] = request.token
        query['TrackInfo'] = request.track_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopGameSessions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.BatchStopGameSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_game_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_game_sessions_with_options(request, runtime)

    def close_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CloseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def close_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_order_with_options(request, runtime)

    def create_game_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['GameName'] = request.game_name
        query['PlatformType'] = request.platform_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameResponse(),
            self.call_api(params, req, runtime)
        )

    def create_game(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_game_with_options(request, runtime)

    def create_game_deploy_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['FrameRate'] = request.frame_rate
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['Instance'] = request.instance
        query['ProjectId'] = request.project_id
        query['Resolution'] = request.resolution
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGameDeployWorkflow',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateGameDeployWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def create_game_deploy_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_game_deploy_workflow_with_options(request, runtime)

    def create_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['Amount'] = request.amount
        query['BuyerAccountId'] = request.buyer_account_id
        query['IdempotentCode'] = request.idempotent_code
        query['ItemId'] = request.item_id
        query['OriginPrice'] = request.origin_price
        query['SettlementPrice'] = request.settlement_price
        query['SkuId'] = request.sku_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def create_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['CurrentToken'] = request.current_token
        query['Session'] = request.session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    def delete_game_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_game(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_game_with_options(request, runtime)

    def delete_game_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_game_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_game_version_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def delivery_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeliveryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DeliveryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def delivery_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delivery_order_with_options(request, runtime)

    def dispatch_game_slot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.cancel):
            body['Cancel'] = request.cancel
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.game_command):
            body['GameCommand'] = request.game_command
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.game_start_param):
            body['GameStartParam'] = request.game_start_param
        if not UtilClient.is_unset(request.reconnect):
            body['Reconnect'] = request.reconnect
        if not UtilClient.is_unset(request.region_name):
            body['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.system_info):
            body['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_level):
            body['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DispatchGameSlot',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.DispatchGameSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def dispatch_game_slot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dispatch_game_slot_with_options(request, runtime)

    def get_game_ccu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['RegionName'] = request.region_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameCcu',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameCcuResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_ccu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_ccu_with_options(request, runtime)

    def get_game_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_status_with_options(request, runtime)

    def get_game_stock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        query['UserLevel'] = request.user_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameStock',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameStockResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_stock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_stock_with_options(request, runtime)

    def get_game_trial_surplus_duration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameTrialSurplusDuration',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameTrialSurplusDurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_trial_surplus_duration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_trial_surplus_duration_with_options(request, runtime)

    def get_game_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersion',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_version_with_options(request, runtime)

    def get_game_version_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGameVersionProgress',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetGameVersionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def get_game_version_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_game_version_progress_with_options(request, runtime)

    def get_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItem',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetItemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_item_with_options(request, runtime)

    def get_out_account_bind_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['OutAccountType'] = request.out_account_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOutAccountBindDetail',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetOutAccountBindDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_out_account_bind_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_out_account_bind_detail_with_options(request, runtime)

    def get_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_with_options(request, runtime)

    def get_stop_game_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStopGameToken',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.GetStopGameTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stop_game_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stop_game_token_with_options(request, runtime)

    def kick_player_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameSession'] = request.game_session
        query['KickedAccountId'] = request.kicked_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickPlayer',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.KickPlayerResponse(),
            self.call_api(params, req, runtime)
        )

    def kick_player(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kick_player_with_options(request, runtime)

    def list_bought_games_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBoughtGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListBoughtGamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bought_games(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bought_games_with_options(request, runtime)

    def list_container_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionIdList'] = request.game_session_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_container_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_status_with_options(request, runtime)

    def list_deployable_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployableInstances',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListDeployableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deployable_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_deployable_instances_with_options(request, runtime)

    def list_game_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGameVersions',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGameVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_game_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_game_versions_with_options(request, runtime)

    def list_games_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGames',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListGamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_games(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_games_with_options(request, runtime)

    def list_history_container_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['LastGameSessionId'] = request.last_game_session_id
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHistoryContainerStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListHistoryContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_history_container_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_history_container_status_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def query_game_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGame',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryGameResponse(),
            self.call_api(params, req, runtime)
        )

    def query_game(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_game_with_options(request, runtime)

    def query_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItems',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_items_with_options(request, runtime)

    def query_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['BuyerAccountId'] = request.buyer_account_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_order_with_options(request, runtime)

    def query_out_account_bind_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDomain'] = request.account_domain
        query['AccountId'] = request.account_id
        query['GameId'] = request.game_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOutAccountBindStatus',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryOutAccountBindStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_out_account_bind_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_out_account_bind_status_with_options(request, runtime)

    def query_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def query_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_project_with_options(request, runtime)

    def query_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTenant',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.QueryTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tenant_with_options(request, runtime)

    def remove_game_from_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameId'] = request.game_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveGameFromProject',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.RemoveGameFromProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_game_from_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_game_from_project_with_options(request, runtime)

    def skip_trial_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GameSessionId'] = request.game_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipTrialPolicy',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SkipTrialPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_trial_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.skip_trial_policy_with_options(request, runtime)

    def stop_game_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.biz_param):
            body['BizParam'] = request.biz_param
        if not UtilClient.is_unset(request.game_id):
            body['GameId'] = request.game_id
        if not UtilClient.is_unset(request.game_session):
            body['GameSession'] = request.game_session
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopGameSession',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.StopGameSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_game_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_game_session_with_options(request, runtime)

    def submit_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CloudGameInstanceIds'] = request.cloud_game_instance_ids
        query['GameId'] = request.game_id
        query['OperationType'] = request.operation_type
        query['ProjectId'] = request.project_id
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDeployment',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_deployment_with_options(request, runtime)

    def submit_internal_purchase_charge_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ActiveUserRetentionRateOneDay'] = request.active_user_retention_rate_one_day
        query['ActiveUserRetentionRateSevenDay'] = request.active_user_retention_rate_seven_day
        query['ActiveUserRetentionRateThirtyDay'] = request.active_user_retention_rate_thirty_day
        query['Arpu'] = request.arpu
        query['ChargeDate'] = request.charge_date
        query['Dau'] = request.dau
        query['GameId'] = request.game_id
        query['Mau'] = request.mau
        query['NewUserRetentionRateOneDay'] = request.new_user_retention_rate_one_day
        query['NewUserRetentionRateSevenDay'] = request.new_user_retention_rate_seven_day
        query['NewUserRetentionRateThirtyDay'] = request.new_user_retention_rate_thirty_day
        query['PaymentConversionRate'] = request.payment_conversion_rate
        query['PlayTimeAverageOneDay'] = request.play_time_average_one_day
        query['PlayTimeAverageThirtyDay'] = request.play_time_average_thirty_day
        query['PlayTimeNinetyPointsOneDay'] = request.play_time_ninety_points_one_day
        query['PlayTimeNinetyPointsThirtyDay'] = request.play_time_ninety_points_thirty_day
        query['PlayTimeRangeOneDay'] = request.play_time_range_one_day
        query['PlayTimeRangeThirtyDay'] = request.play_time_range_thirty_day
        query['UserActivationRate'] = request.user_activation_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseChargeData',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseChargeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_internal_purchase_charge_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_charge_data_with_options(request, runtime)

    def submit_internal_purchase_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OrderList'] = request.order_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseOrders',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_internal_purchase_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_orders_with_options(request, runtime)

    def submit_internal_purchase_ready_flag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BatchInfoList'] = request.batch_info_list
        query['ChargeDate'] = request.charge_date
        query['GameId'] = request.game_id
        query['OrderTotalCount'] = request.order_total_count
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInternalPurchaseReadyFlag',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.SubmitInternalPurchaseReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_internal_purchase_ready_flag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_internal_purchase_ready_flag_with_options(request, runtime)

    def upload_game_version_by_download_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DownloadType'] = request.download_type
        query['FileType'] = request.file_type
        query['GameId'] = request.game_id
        query['GameVersion'] = request.game_version
        query['Hash'] = request.hash
        query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadGameVersionByDownload',
            version='2020-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_game_api20200728_models.UploadGameVersionByDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_game_version_by_download(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_game_version_by_download_with_options(request, runtime)
