# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mindlive20210301 import models as mind_live_20210301_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('mindlive', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def login_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LoginDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def login_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.login_device_with_options(request, runtime)

    def logout_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LogoutDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LogoutDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def logout_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.logout_device_with_options(request, runtime)

    def query_item_backgrounds_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.QueryItemBackgroundsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemBackgrounds',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.QueryItemBackgroundsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_item_backgrounds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_item_backgrounds_with_options(request, runtime)

    def report_current_background_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.ReportCurrentBackgroundShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bg_config):
            request.bg_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bg_config, 'BgConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.bg_config_shrink):
            query['BgConfig'] = request.bg_config_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.resource_uuid):
            query['ResourceUuid'] = request.resource_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportCurrentBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportCurrentBackgroundResponse(),
            self.call_api(params, req, runtime)
        )

    def report_current_background(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_current_background_with_options(request, runtime)

    def report_dev_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportDevConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportDevConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def report_dev_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_dev_config_with_options(request, runtime)

    def report_live_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.live_mode):
            query['LiveMode'] = request.live_mode
        if not UtilClient.is_unset(request.live_state):
            query['LiveState'] = request.live_state
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportLiveState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportLiveStateResponse(),
            self.call_api(params, req, runtime)
        )

    def report_live_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_live_state_with_options(request, runtime)

    def report_screen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportScreen',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportScreenResponse(),
            self.call_api(params, req, runtime)
        )

    def report_screen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_screen_with_options(request, runtime)

    def report_user_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def report_user_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_user_config_with_options(request, runtime)

    def request_authorization_data_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestAuthorizationData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestAuthorizationDataResponse(),
            self.call_api(params, req, runtime)
        )

    def request_authorization_data(self):
        runtime = util_models.RuntimeOptions()
        return self.request_authorization_data_with_options(runtime)

    def request_background_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBackgroundResponse(),
            self.call_api(params, req, runtime)
        )

    def request_background(self):
        runtime = util_models.RuntimeOptions()
        return self.request_background_with_options(runtime)

    def request_bind_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestBindData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindDataResponse(),
            self.call_api(params, req, runtime)
        )

    def request_bind_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_bind_data_with_options(request, runtime)

    def request_binding_state_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBindingState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindingStateResponse(),
            self.call_api(params, req, runtime)
        )

    def request_binding_state(self):
        runtime = util_models.RuntimeOptions()
        return self.request_binding_state_with_options(runtime)

    def request_device_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestDeviceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def request_device_info(self):
        runtime = util_models.RuntimeOptions()
        return self.request_device_info_with_options(runtime)

    def request_iot_triad_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestIotTriad',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestIotTriadResponse(),
            self.call_api(params, req, runtime)
        )

    def request_iot_triad(self):
        runtime = util_models.RuntimeOptions()
        return self.request_iot_triad_with_options(runtime)

    def request_live_sell_point_state_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveSellPointStateResponse(),
            self.call_api(params, req, runtime)
        )

    def request_live_sell_point_state(self):
        runtime = util_models.RuntimeOptions()
        return self.request_live_sell_point_state_with_options(runtime)

    def request_live_teleprompter_state_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveTeleprompterStateResponse(),
            self.call_api(params, req, runtime)
        )

    def request_live_teleprompter_state(self):
        runtime = util_models.RuntimeOptions()
        return self.request_live_teleprompter_state_with_options(runtime)

    def request_oss_sts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestOssSts',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestOssStsResponse(),
            self.call_api(params, req, runtime)
        )

    def request_oss_sts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_oss_sts_with_options(request, runtime)

    def request_paster_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestPaster',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestPasterResponse(),
            self.call_api(params, req, runtime)
        )

    def request_paster(self):
        runtime = util_models.RuntimeOptions()
        return self.request_paster_with_options(runtime)

    def request_reset_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestResetData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestResetDataResponse(),
            self.call_api(params, req, runtime)
        )

    def request_reset_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_reset_data_with_options(request, runtime)

    def request_service_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestServiceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestServiceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def request_service_info(self):
        runtime = util_models.RuntimeOptions()
        return self.request_service_info_with_options(runtime)

    def request_user_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def request_user_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_user_config_with_options(request, runtime)

    def request_user_sell_point_template_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestUserSellPointTemplate',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserSellPointTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def request_user_sell_point_template(self):
        runtime = util_models.RuntimeOptions()
        return self.request_user_sell_point_template_with_options(runtime)

    def reset_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ResetDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_device_with_options(request, runtime)

    def update_current_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCurrentItem',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateCurrentItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_current_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_current_item_with_options(request, runtime)

    def update_live_sell_point_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveSellPointStateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_sell_point_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_sell_point_state_with_options(request, runtime)

    def update_live_teleprompter_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveTeleprompterStateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_teleprompter_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_teleprompter_state_with_options(request, runtime)
