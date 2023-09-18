# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_avatar20220130 import models as avatar_20220130_models
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
        self._endpoint = self.get_endpoint('avatar', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_video_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.CancelVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CancelVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_video_task_with_options(request, runtime)

    def client_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_info):
            query['DeviceInfo'] = request.device_info
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def client_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.client_auth_with_options(request, runtime)

    def client_start_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientStart',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientStartResponse(),
            self.call_api(params, req, runtime)
        )

    def client_start(self, request):
        runtime = util_models.RuntimeOptions()
        return self.client_start_with_options(request, runtime)

    def close_timed_reset_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CloseTimedResetOperateResponse(),
            self.call_api(params, req, runtime)
        )

    def close_timed_reset_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_timed_reset_operate_with_options(request, runtime)

    def create_2d_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Create2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Create2dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def create_2d_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_2d_avatar_with_options(request, runtime)

    def delete_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DeleteAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_avatar_with_options(request, runtime)

    def duplex_decision_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.DuplexDecisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_keywords):
            request.custom_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_keywords, 'CustomKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.dialog_context):
            request.dialog_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dialog_context, 'DialogContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_request_id):
            query['BizRequestId'] = request.biz_request_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.custom_keywords_shrink):
            query['CustomKeywords'] = request.custom_keywords_shrink
        if not UtilClient.is_unset(request.dialog_context_shrink):
            query['DialogContext'] = request.dialog_context_shrink
        if not UtilClient.is_unset(request.dialog_status):
            query['DialogStatus'] = request.dialog_status
        if not UtilClient.is_unset(request.interrupt_type):
            query['InterruptType'] = request.interrupt_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DuplexDecision',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DuplexDecisionResponse(),
            self.call_api(params, req, runtime)
        )

    def duplex_decision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.duplex_decision_with_options(request, runtime)

    def get_video_task_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.GetVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.GetVideoTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_task_info_with_options(request, runtime)

    def license_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LicenseAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.LicenseAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def license_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.license_auth_with_options(request, runtime)

    def query_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def query_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_avatar_with_options(request, runtime)

    def query_avatar_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarList',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_avatar_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_avatar_list_with_options(request, runtime)

    def query_running_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryRunningInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRunningInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryRunningInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_running_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_running_instance_with_options(request, runtime)

    def query_timed_reset_operate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimedResetOperateStatus',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryTimedResetOperateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_timed_reset_operate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_timed_reset_operate_status_with_options(request, runtime)

    def query_video_task_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.order_by_id):
            query['OrderById'] = request.order_by_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryVideoTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_video_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_video_task_info_with_options(request, runtime)

    def render_3d_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Render3dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Render3dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def render_3d_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.render_3d_avatar_with_options(request, runtime)

    def send_command_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCommand',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def send_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_command_with_options(request, runtime)

    def send_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        if not UtilClient.is_unset(tmp_req.text_request):
            request.text_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_request, 'TextRequest', 'json')
        if not UtilClient.is_unset(tmp_req.vamlrequest):
            request.vamlrequest_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vamlrequest, 'VAMLRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text_request_shrink):
            query['TextRequest'] = request.text_request_shrink
        if not UtilClient.is_unset(request.vamlrequest_shrink):
            query['VAMLRequest'] = request.vamlrequest_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    def send_text_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendText',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendTextResponse(),
            self.call_api(params, req, runtime)
        )

    def send_text(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_text_with_options(request, runtime)

    def send_vaml_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vaml):
            query['Vaml'] = request.vaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVaml',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendVamlResponse(),
            self.call_api(params, req, runtime)
        )

    def send_vaml(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_vaml_with_options(request, runtime)

    def start_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.StartInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.channel):
            request.channel_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel, 'Channel', 'json')
        if not UtilClient.is_unset(tmp_req.command_request):
            request.command_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.command_request, 'CommandRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.channel_shrink):
            query['Channel'] = request.channel_shrink
        if not UtilClient.is_unset(request.command_request_shrink):
            query['CommandRequest'] = request.command_request_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def start_timed_reset_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartTimedResetOperateResponse(),
            self.call_api(params, req, runtime)
        )

    def start_timed_reset_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_timed_reset_operate_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def submit_audio_to_2davatar_video_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_audio_to_2davatar_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_to_2davatar_video_task_with_options(request, runtime)

    def submit_audio_to_3davatar_video_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_audio_to_3davatar_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_to_3davatar_video_task_with_options(request, runtime)

    def submit_text_to_2davatar_video_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_text_to_2davatar_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_text_to_2davatar_video_task_with_options(request, runtime)

    def submit_text_to_3davatar_video_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_text_to_3davatar_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_text_to_3davatar_video_task_with_options(request, runtime)

    def update_2d_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Update2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Update2dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def update_2d_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_2d_avatar_with_options(request, runtime)
