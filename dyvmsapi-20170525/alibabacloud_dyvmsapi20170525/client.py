# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyvmsapi20170525 import models as dyvmsapi_20170525_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dyvmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_rtc_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddRtcAccountResponse(),
            self.do_rpcrequest('AddRtcAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_rtc_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rtc_account_with_options(request, runtime)

    def add_virtual_number_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            self.do_rpcrequest('AddVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_virtual_number_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_virtual_number_relation_with_options(request, runtime)

    def batch_robot_smart_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            self.do_rpcrequest('BatchRobotSmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_robot_smart_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_robot_smart_call_with_options(request, runtime)

    def bind_number_and_voip_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BindNumberAndVoipIdResponse(),
            self.do_rpcrequest('BindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_number_and_voip_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_number_and_voip_id_with_options(request, runtime)

    def cancel_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelCallResponse(),
            self.do_rpcrequest('CancelCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_call_with_options(request, runtime)

    def cancel_order_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            self.do_rpcrequest('CancelOrderRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_robot_task_with_options(request, runtime)

    def cancel_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            self.do_rpcrequest('CancelRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_robot_task_with_options(request, runtime)

    def click_to_dial_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ClickToDialResponse(),
            self.do_rpcrequest('ClickToDial', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def click_to_dial(self, request):
        runtime = util_models.RuntimeOptions()
        return self.click_to_dial_with_options(request, runtime)

    def close_sip_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CloseSipAccountResponse(),
            self.do_rpcrequest('CloseSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_sip_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_sip_account_with_options(request, runtime)

    def create_call_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            self.do_rpcrequest('CreateCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_call_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_call_task_with_options(request, runtime)

    def create_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            self.do_rpcrequest('CreateRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_robot_task_with_options(request, runtime)

    def create_sip_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateSipAccountResponse(),
            self.do_rpcrequest('CreateSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sip_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sip_account_with_options(request, runtime)

    def delete_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            self.do_rpcrequest('DeleteRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_robot_task_with_options(request, runtime)

    def describe_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DescribeRecordDataResponse(),
            self.do_rpcrequest('DescribeRecordData', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    def do_rtc_number_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoRtcNumberAuthResponse(),
            self.do_rpcrequest('DoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_rtc_number_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_rtc_number_auth_with_options(request, runtime)

    def double_call_seat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoubleCallSeatResponse(),
            self.do_rpcrequest('DoubleCallSeat', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def double_call_seat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.double_call_seat_with_options(request, runtime)

    def execute_call_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            self.do_rpcrequest('ExecuteCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_call_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_call_task_with_options(request, runtime)

    def get_hotline_qualification_by_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse(),
            self.do_rpcrequest('GetHotlineQualificationByOrder', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_qualification_by_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_qualification_by_order_with_options(request, runtime)

    def get_rtc_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetRtcTokenResponse(),
            self.do_rpcrequest('GetRtcToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rtc_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    def get_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            self.do_rpcrequest('GetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    def ivr_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            self.do_rpcrequest('IvrCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ivr_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ivr_call_with_options(request, runtime)

    def list_call_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            self.do_rpcrequest('ListCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_with_options(request, runtime)

    def list_call_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            self.do_rpcrequest('ListCallTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_detail_with_options(request, runtime)

    def list_hotline_transfer_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferNumberResponse(),
            self.do_rpcrequest('ListHotlineTransferNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hotline_transfer_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_number_with_options(request, runtime)

    def list_hotline_transfer_register_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse(),
            self.do_rpcrequest('ListHotlineTransferRegisterFile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hotline_transfer_register_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_register_file_with_options(request, runtime)

    def list_ordered_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOrderedNumbersResponse(),
            self.do_rpcrequest('ListOrderedNumbers', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ordered_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ordered_numbers_with_options(request, runtime)

    def list_outbound_strategies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOutboundStrategiesResponse(),
            self.do_rpcrequest('ListOutboundStrategies', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_strategies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_strategies_with_options(request, runtime)

    def list_robot_task_calls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListRobotTaskCallsResponse(),
            self.do_rpcrequest('ListRobotTaskCalls', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_robot_task_calls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_robot_task_calls_with_options(request, runtime)

    def query_call_detail_by_call_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            self.do_rpcrequest('QueryCallDetailByCallId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_detail_by_call_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_call_id_with_options(request, runtime)

    def query_call_detail_by_task_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            self.do_rpcrequest('QueryCallDetailByTaskId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_detail_by_task_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_task_id_with_options(request, runtime)

    def query_call_in_pool_transfer_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse(),
            self.do_rpcrequest('QueryCallInPoolTransferConfig', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_in_pool_transfer_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_pool_transfer_config_with_options(request, runtime)

    def query_call_in_transfer_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInTransferRecordResponse(),
            self.do_rpcrequest('QueryCallInTransferRecord', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_in_transfer_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_transfer_record_with_options(request, runtime)

    def query_robot_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            self.do_rpcrequest('QueryRobotInfoList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_info_list_with_options(request, runtime)

    def query_robot_task_call_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            self.do_rpcrequest('QueryRobotTaskCallDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_call_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_detail_with_options(request, runtime)

    def query_robot_task_call_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            self.do_rpcrequest('QueryRobotTaskCallList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_call_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_list_with_options(request, runtime)

    def query_robot_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            self.do_rpcrequest('QueryRobotTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_detail_with_options(request, runtime)

    def query_robot_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            self.do_rpcrequest('QueryRobotTaskList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_list_with_options(request, runtime)

    def query_robotv_2all_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            self.do_rpcrequest('QueryRobotv2AllList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robotv_2all_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robotv_2all_list_with_options(request, runtime)

    def query_rtc_number_auth_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse(),
            self.do_rpcrequest('QueryRtcNumberAuthStatus', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_rtc_number_auth_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_rtc_number_auth_status_with_options(request, runtime)

    def query_virtual_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            self.do_rpcrequest('QueryVirtualNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_virtual_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_with_options(request, runtime)

    def query_virtual_number_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            self.do_rpcrequest('QueryVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_virtual_number_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_relation_with_options(request, runtime)

    def query_voip_number_bind_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse(),
            self.do_rpcrequest('QueryVoipNumberBindInfos', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_voip_number_bind_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_voip_number_bind_infos_with_options(request, runtime)

    def report_voip_problems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ReportVoipProblemsResponse(),
            self.do_rpcrequest('ReportVoipProblems', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_voip_problems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_voip_problems_with_options(request, runtime)

    def send_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SendVerificationResponse(),
            self.do_rpcrequest('SendVerification', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verification_with_options(request, runtime)

    def set_transfer_callee_pool_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse(),
            self.do_rpcrequest('SetTransferCalleePoolConfig', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_transfer_callee_pool_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_transfer_callee_pool_config_with_options(request, runtime)

    def single_call_by_tts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            self.do_rpcrequest('SingleCallByTts', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_call_by_tts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_tts_with_options(request, runtime)

    def single_call_by_voice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            self.do_rpcrequest('SingleCallByVoice', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_call_by_voice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_voice_with_options(request, runtime)

    def smart_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            self.do_rpcrequest('SmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def smart_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.smart_call_with_options(request, runtime)

    def smart_call_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            self.do_rpcrequest('SmartCallOperate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def smart_call_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.smart_call_operate_with_options(request, runtime)

    def start_micro_outbound_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartMicroOutboundResponse(),
            self.do_rpcrequest('StartMicroOutbound', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_micro_outbound(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    def start_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            self.do_rpcrequest('StartRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_robot_task_with_options(request, runtime)

    def stop_robot_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            self.do_rpcrequest('StopRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_robot_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_robot_task_with_options(request, runtime)

    def submit_hotline_transfer_register_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse(),
            self.do_rpcrequest('SubmitHotlineTransferRegister', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_hotline_transfer_register(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_hotline_transfer_register_with_options(request, runtime)

    def unbind_number_and_voip_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse(),
            self.do_rpcrequest('UnbindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_number_and_voip_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_number_and_voip_id_with_options(request, runtime)

    def undo_rtc_number_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UndoRtcNumberAuthResponse(),
            self.do_rpcrequest('UndoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def undo_rtc_number_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.undo_rtc_number_auth_with_options(request, runtime)

    def upload_robot_task_called_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            self.do_rpcrequest('UploadRobotTaskCalledFile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_robot_task_called_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_robot_task_called_file_with_options(request, runtime)

    def voip_add_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipAddAccountResponse(),
            self.do_rpcrequest('VoipAddAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def voip_add_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.voip_add_account_with_options(request, runtime)

    def voip_get_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipGetTokenResponse(),
            self.do_rpcrequest('VoipGetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def voip_get_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.voip_get_token_with_options(request, runtime)
