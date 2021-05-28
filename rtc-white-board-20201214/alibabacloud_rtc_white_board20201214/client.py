# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rtc_white_board20201214 import models as rtc_white_board_20201214_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('rtc-white-board', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeAppsResponse(),
            self.do_rpcrequest('DescribeApps', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    def pause_white_board_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse(),
            self.do_rpcrequest('PauseWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pause_white_board_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_white_board_recording_with_options(request, runtime)

    def set_app_callback_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackUrlResponse(),
            self.do_rpcrequest('SetAppCallbackUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_callback_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_app_callback_url_with_options(request, runtime)

    def start_white_board_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse(),
            self.do_rpcrequest('StartWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_white_board_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_white_board_recording_with_options(request, runtime)

    def set_app_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppNameResponse(),
            self.do_rpcrequest('SetAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_app_name_with_options(request, runtime)

    def describe_white_boards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeWhiteBoardsResponse(),
            self.do_rpcrequest('DescribeWhiteBoards', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_white_boards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_white_boards_with_options(request, runtime)

    def resume_white_board_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse(),
            self.do_rpcrequest('ResumeWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_white_board_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_white_board_recording_with_options(request, runtime)

    def set_app_domain_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppDomainNamesResponse(),
            self.do_rpcrequest('SetAppDomainNames', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_domain_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_app_domain_names_with_options(request, runtime)

    def open_white_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.OpenWhiteBoardResponse(),
            self.do_rpcrequest('OpenWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_white_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_white_board_with_options(request, runtime)

    def refresh_users_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.RefreshUsersPermissionsResponse(),
            self.do_rpcrequest('RefreshUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_users_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_users_permissions_with_options(request, runtime)

    def set_app_callback_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackTypeResponse(),
            self.do_rpcrequest('SetAppCallbackType', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_callback_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_app_callback_type_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def set_users_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetUsersPermissionsResponse(),
            self.do_rpcrequest('SetUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_users_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_users_permissions_with_options(request, runtime)

    def create_white_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateWhiteBoardResponse(),
            self.do_rpcrequest('CreateWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_white_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_white_board_with_options(request, runtime)

    def set_app_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppStatusResponse(),
            self.do_rpcrequest('SetAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_app_status_with_options(request, runtime)

    def stop_white_board_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse(),
            self.do_rpcrequest('StopWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_white_board_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_white_board_recording_with_options(request, runtime)
