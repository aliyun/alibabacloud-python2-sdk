# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieiap_1_0 import models as ali_genieiap__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def app_use_time_report_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.AppUseTimeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppUseTimeReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/vip/use/time/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.AppUseTimeReportResponse(),
            self.call_api(params, req, runtime)
        )

    def app_use_time_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.AppUseTimeReportHeaders()
        return self.app_use_time_report_with_options(request, headers, runtime)

    def call_back_third_right_send_plan_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CallBackThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.card_type):
            query['CardType'] = request.card_type
        if not UtilClient.is_unset(request.error_msg):
            query['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.genie_open_id):
            query['GenieOpenId'] = request.genie_open_id
        if not UtilClient.is_unset(request.receive_status):
            query['ReceiveStatus'] = request.receive_status
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CallBackThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/1.0/iap/business/CallBackThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CallBackThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def call_back_third_right_send_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CallBackThirdRightSendPlanHeaders()
        return self.call_back_third_right_send_plan_with_options(request, headers, runtime)

    def check_third_right_send_plan_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CheckThirdRightSendPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_info):
            request.extend_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_info, 'ExtendInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_group):
            query['BizGroup'] = request.biz_group
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.extend_info_shrink):
            query['ExtendInfo'] = request.extend_info_shrink
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.supplier_id):
            query['SupplierId'] = request.supplier_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckThirdRightSendPlan',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/business/CheckThirdRightSendPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CheckThirdRightSendPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def check_third_right_send_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CheckThirdRightSendPlanHeaders()
        return self.check_third_right_send_plan_with_options(request, headers, runtime)

    def create_reminder_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.CreateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/reminder/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.CreateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_reminder(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.CreateReminderHeaders()
        return self.create_reminder_with_options(request, headers, runtime)

    def delete_reminder_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.DeleteReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/reminder/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.DeleteReminderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_reminder(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.DeleteReminderHeaders()
        return self.delete_reminder_with_options(request, headers, runtime)

    def get_account_for_app_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetAccountForAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountForApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/vip/account/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetAccountForAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_for_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetAccountForAppHeaders()
        return self.get_account_for_app_with_options(request, headers, runtime)

    def get_bus_app_config_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetBusAppConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusAppConfig',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/app/config/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetBusAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bus_app_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetBusAppConfigHeaders()
        return self.get_bus_app_config_with_options(request, headers, runtime)

    def get_phone_number_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetPhoneNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhoneNumber',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/profile/phoneNumber',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetPhoneNumberHeaders()
        return self.get_phone_number_with_options(request, headers, runtime)

    def get_reminder_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.GetReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/reminder/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.GetReminderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_reminder(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.GetReminderHeaders()
        return self.get_reminder_with_options(request, headers, runtime)

    def list_reminders_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.ListRemindersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReminders',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/reminder/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.ListRemindersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_reminders(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.ListRemindersHeaders()
        return self.list_reminders_with_options(request, headers, runtime)

    def pull_cashier_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PullCashierShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullCashier',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/pull/cashier/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PullCashierResponse(),
            self.call_api(params, req, runtime)
        )

    def pull_cashier(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PullCashierHeaders()
        return self.pull_cashier_with_options(request, headers, runtime)

    def push_notifications_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.PushNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.PushNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def push_notifications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.PushNotificationsHeaders()
        return self.push_notifications_with_options(request, headers, runtime)

    def send_notifications_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.SendNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.notification_unicast_request):
            request.notification_unicast_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_unicast_request, 'NotificationUnicastRequest', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.notification_unicast_request_shrink):
            body['NotificationUnicastRequest'] = request.notification_unicast_request_shrink
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendNotifications',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/general/notifications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.SendNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def send_notifications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.SendNotificationsHeaders()
        return self.send_notifications_with_options(request, headers, runtime)

    def update_reminder_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.UpdateReminderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReminder',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/reminder/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.UpdateReminderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_reminder(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.UpdateReminderHeaders()
        return self.update_reminder_with_options(request, headers, runtime)

    def video_app_report_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = ali_genieiap__1__0_models.VideoAppReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            body['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.payload_shrink):
            body['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoAppReport',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/vip/use/video/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.VideoAppReportResponse(),
            self.call_api(params, req, runtime)
        )

    def video_app_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.VideoAppReportHeaders()
        return self.video_app_report_with_options(request, headers, runtime)

    def wake_up_app_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_debug):
            body['IsDebug'] = request.is_debug
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.target_info):
            body['TargetInfo'] = request.target_info
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WakeUpApp',
            version='iap_1.0',
            protocol='HTTPS',
            pathname='/v1.0/iap/wakeup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            ali_genieiap__1__0_models.WakeUpAppResponse(),
            self.call_api(params, req, runtime)
        )

    def wake_up_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ali_genieiap__1__0_models.WakeUpAppHeaders()
        return self.wake_up_app_with_options(request, headers, runtime)
