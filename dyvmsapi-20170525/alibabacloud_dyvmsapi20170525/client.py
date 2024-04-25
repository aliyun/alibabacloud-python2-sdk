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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def add_virtual_number_relation_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 200 times per second per account.
        

        @param request: AddVirtualNumberRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddVirtualNumberRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_name_list):
            query['CorpNameList'] = request.corp_name_list
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_virtual_number_relation(self, request):
        """
        ### QPS limits
        You can call this operation up to 200 times per second per account.
        

        @param request: AddVirtualNumberRelationRequest

        @return: AddVirtualNumberRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_virtual_number_relation_with_options(request, runtime)

    def batch_robot_smart_call_with_options(self, request, runtime):
        """
        In an intelligent speech interaction task, you can use the robot communication scripts preset in the Voice Messaging Service console, or invoke the callback function to return the response mode configured by the business party in each call.
        *   The BatchRobotSmartCall operation is used to initiate an outbound robocall task by using the robot communication scripts preset in the Voice Messaging Service console.
        ## Prerequisites
        *   You have passed the real-name verification for an enterprise user and passed the enterprise qualification review.
        *   You have purchased numbers in the [Voice Messaging Service console](https://dyvms.console.aliyun.com/dyvms.htm#/number/normal).
        *   You have added communication scripts on the [Communication script management](https://dyvms.console.aliyun.com/dyvms.htm#/smart-call/saas/robot/list) page, and the communication scripts have been approved.
        > Before you call this operation, make sure that you are familiar with the [billing](https://www.aliyun.com/price/product#/vms/detail) of Voice Messaging Service (VMS).
        

        @param request: BatchRobotSmartCallRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchRobotSmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_call):
            query['ScheduleCall'] = request.schedule_call
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRobotSmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_robot_smart_call(self, request):
        """
        In an intelligent speech interaction task, you can use the robot communication scripts preset in the Voice Messaging Service console, or invoke the callback function to return the response mode configured by the business party in each call.
        *   The BatchRobotSmartCall operation is used to initiate an outbound robocall task by using the robot communication scripts preset in the Voice Messaging Service console.
        ## Prerequisites
        *   You have passed the real-name verification for an enterprise user and passed the enterprise qualification review.
        *   You have purchased numbers in the [Voice Messaging Service console](https://dyvms.console.aliyun.com/dyvms.htm#/number/normal).
        *   You have added communication scripts on the [Communication script management](https://dyvms.console.aliyun.com/dyvms.htm#/smart-call/saas/robot/list) page, and the communication scripts have been approved.
        > Before you call this operation, make sure that you are familiar with the [billing](https://www.aliyun.com/price/product#/vms/detail) of Voice Messaging Service (VMS).
        

        @param request: BatchRobotSmartCallRequest

        @return: BatchRobotSmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_robot_smart_call_with_options(request, runtime)

    def cancel_order_robot_task_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CancelOrderRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelOrderRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CancelOrderRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_order_robot_task(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CancelOrderRobotTaskRequest

        @return: CancelOrderRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_robot_task_with_options(request, runtime)

    def cancel_robot_task_with_options(self, request, runtime):
        """
        Only a task in progress can be terminated by calling the CancelRobotTask operation, and the task cannot be resumed after it is terminated.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CancelRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CancelRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_robot_task(self, request):
        """
        Only a task in progress can be terminated by calling the CancelRobotTask operation, and the task cannot be resumed after it is terminated.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CancelRobotTaskRequest

        @return: CancelRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_robot_task_with_options(request, runtime)

    def change_media_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_num):
            query['CalledNum'] = request.called_num
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
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
            action='ChangeMediaType',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ChangeMediaTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def change_media_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_media_type_with_options(request, runtime)

    def create_call_task_with_options(self, request, runtime):
        """
        You can create up to 1,000 voice notifications for each task.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CreateCallTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.fire_time):
            query['FireTime'] = request.fire_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.stop_time):
            query['StopTime'] = request.stop_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_call_task(self, request):
        """
        You can create up to 1,000 voice notifications for each task.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CreateCallTaskRequest

        @return: CreateCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_call_task_with_options(request, runtime)

    def create_robot_task_with_options(self, request, runtime):
        """
        You can call this operation to initiate an outbound robocall task by using the robot communication scripts preset in the Voice Messaging Service console. In an intelligent speech interaction task, you can use the robot communication scripts preset in the Voice Messaging Service console, or invoke the callback function to return the response mode configured by the business party in each call.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CreateRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not UtilClient.is_unset(request.number_status_ident):
            query['NumberStatusIdent'] = request.number_status_ident
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recall_interval):
            query['RecallInterval'] = request.recall_interval
        if not UtilClient.is_unset(request.recall_state_codes):
            query['RecallStateCodes'] = request.recall_state_codes
        if not UtilClient.is_unset(request.recall_times):
            query['RecallTimes'] = request.recall_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retry_type):
            query['RetryType'] = request.retry_type
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_robot_task(self, request):
        """
        You can call this operation to initiate an outbound robocall task by using the robot communication scripts preset in the Voice Messaging Service console. In an intelligent speech interaction task, you can use the robot communication scripts preset in the Voice Messaging Service console, or invoke the callback function to return the response mode configured by the business party in each call.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: CreateRobotTaskRequest

        @return: CreateRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_robot_task_with_options(request, runtime)

    def degrade_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
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
            action='DegradeVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DegradeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def degrade_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.degrade_video_file_with_options(request, runtime)

    def delete_robot_task_with_options(self, request, runtime):
        """
        You can call this operation to delete only tasks that are not started, that are completed, and that are terminated.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: DeleteRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DeleteRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_robot_task(self, request):
        """
        You can call this operation to delete only tasks that are not started, that are completed, and that are terminated.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: DeleteRobotTaskRequest

        @return: DeleteRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_robot_task_with_options(request, runtime)

    def execute_call_task_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ExecuteCallTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExecuteCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fire_time):
            query['FireTime'] = request.fire_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_call_task(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ExecuteCallTaskRequest

        @return: ExecuteCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_call_task_with_options(request, runtime)

    def get_call_media_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
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
            action='GetCallMediaType',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetCallMediaTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_call_media_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_call_media_type_with_options(request, runtime)

    def get_call_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_num):
            query['CalledNum'] = request.called_num
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
            action='GetCallProgress',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetCallProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def get_call_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_call_progress_with_options(request, runtime)

    def get_hotline_qualification_by_order_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: GetHotlineQualificationByOrderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetHotlineQualificationByOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='GetHotlineQualificationByOrder',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetHotlineQualificationByOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotline_qualification_by_order(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: GetHotlineQualificationByOrderRequest

        @return: GetHotlineQualificationByOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_qualification_by_order_with_options(request, runtime)

    def get_temporary_file_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemporaryFileUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTemporaryFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_temporary_file_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_temporary_file_url_with_options(request, runtime)

    def get_token_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to five times per second per account.
        

        @param request: GetTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_token(self, request):
        """
        ### QPS limits
        You can call this operation up to five times per second per account.
        

        @param request: GetTokenRequest

        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    def get_video_field_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.video_file):
            query['VideoFile'] = request.video_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoFieldUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetVideoFieldUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_field_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_field_url_with_options(request, runtime)

    def ivr_call_with_options(self, request, runtime):
        """
        Your enterprise qualification is approved. For more information, see [Submit enterprise qualifications](~~149795~~).
        *   Voice numbers are purchased. For more information, see [Purchase numbers](~~149794~~).
        *   When the subscriber answers the call, the subscriber hears a voice that instructs the subscriber to press a key as needed. If the [message receipt](~~112503~~) feature is enabled, the Voice Messaging Service (VMS) platform returns the information about the key pressed by the subscriber to the business system. The key information includes the order confirmation, questionnaire survey, and satisfaction survey completed by the subscriber.
        ## QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: IvrCallRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: IvrCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bye_code):
            query['ByeCode'] = request.bye_code
        if not UtilClient.is_unset(request.bye_tts_params):
            query['ByeTtsParams'] = request.bye_tts_params
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.menu_key_map):
            query['MenuKeyMap'] = request.menu_key_map
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_code):
            query['StartCode'] = request.start_code
        if not UtilClient.is_unset(request.start_tts_params):
            query['StartTtsParams'] = request.start_tts_params
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IvrCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            self.call_api(params, req, runtime)
        )

    def ivr_call(self, request):
        """
        Your enterprise qualification is approved. For more information, see [Submit enterprise qualifications](~~149795~~).
        *   Voice numbers are purchased. For more information, see [Purchase numbers](~~149794~~).
        *   When the subscriber answers the call, the subscriber hears a voice that instructs the subscriber to press a key as needed. If the [message receipt](~~112503~~) feature is enabled, the Voice Messaging Service (VMS) platform returns the information about the key pressed by the subscriber to the business system. The key information includes the order confirmation, questionnaire survey, and satisfaction survey completed by the subscriber.
        ## QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: IvrCallRequest

        @return: IvrCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ivr_call_with_options(request, runtime)

    def list_call_task_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListCallTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCallTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_call_task(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListCallTaskRequest

        @return: ListCallTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_with_options(request, runtime)

    def list_call_task_detail_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListCallTaskDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCallTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_num):
            query['CalledNum'] = request.called_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def list_call_task_detail(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListCallTaskDetailRequest

        @return: ListCallTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_detail_with_options(request, runtime)

    def list_hotline_transfer_number_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListHotlineTransferNumberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListHotlineTransferNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotline_transfer_number(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListHotlineTransferNumberRequest

        @return: ListHotlineTransferNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_number_with_options(request, runtime)

    def list_hotline_transfer_register_file_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListHotlineTransferRegisterFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListHotlineTransferRegisterFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotlineTransferRegisterFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListHotlineTransferRegisterFileResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotline_transfer_register_file(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: ListHotlineTransferRegisterFileRequest

        @return: ListHotlineTransferRegisterFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_transfer_register_file_with_options(request, runtime)

    def pause_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
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
            action='PauseVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.PauseVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_video_file_with_options(request, runtime)

    def play_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlayVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.PlayVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def play_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.play_video_file_with_options(request, runtime)

    def query_call_detail_by_call_id_with_options(self, request, runtime):
        """
        QueryCallDetailByCallId is a common query operation. You can call this operation to query the details of a voice notification, voice verification code, interactive voice response (IVR), intelligent inbound voice call, intelligent outbound voice call, or intelligent robocall.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallDetailByCallIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryCallDetailByCallIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.query_date):
            query['QueryDate'] = request.query_date
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallDetailByCallId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_call_detail_by_call_id(self, request):
        """
        QueryCallDetailByCallId is a common query operation. You can call this operation to query the details of a voice notification, voice verification code, interactive voice response (IVR), intelligent inbound voice call, intelligent outbound voice call, or intelligent robocall.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallDetailByCallIdRequest

        @return: QueryCallDetailByCallIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_call_id_with_options(request, runtime)

    def query_call_detail_by_task_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_date):
            query['QueryDate'] = request.query_date
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
            action='QueryCallDetailByTaskId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_call_detail_by_task_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_task_id_with_options(request, runtime)

    def query_call_in_pool_transfer_config_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallInPoolTransferConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryCallInPoolTransferConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallInPoolTransferConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInPoolTransferConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def query_call_in_pool_transfer_config(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallInPoolTransferConfigRequest

        @return: QueryCallInPoolTransferConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_pool_transfer_config_with_options(request, runtime)

    def query_call_in_transfer_record_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallInTransferRecordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryCallInTransferRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_in_caller):
            query['CallInCaller'] = request.call_in_caller
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.query_date):
            query['QueryDate'] = request.query_date
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallInTransferRecord',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallInTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_call_in_transfer_record(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryCallInTransferRecordRequest

        @return: QueryCallInTransferRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_call_in_transfer_record_with_options(request, runtime)

    def query_robot_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
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
            action='QueryRobotInfoList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robot_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_robot_info_list_with_options(request, runtime)

    def query_robot_task_call_detail_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskCallDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRobotTaskCallDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callee):
            query['Callee'] = request.callee
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_date):
            query['QueryDate'] = request.query_date
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
            action='QueryRobotTaskCallDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robot_task_call_detail(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskCallDetailRequest

        @return: QueryRobotTaskCallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_detail_with_options(request, runtime)

    def query_robot_task_call_list_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskCallListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRobotTaskCallListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_result):
            query['CallResult'] = request.call_result
        if not UtilClient.is_unset(request.called):
            query['Called'] = request.called
        if not UtilClient.is_unset(request.dialog_count_from):
            query['DialogCountFrom'] = request.dialog_count_from
        if not UtilClient.is_unset(request.dialog_count_to):
            query['DialogCountTo'] = request.dialog_count_to
        if not UtilClient.is_unset(request.duration_from):
            query['DurationFrom'] = request.duration_from
        if not UtilClient.is_unset(request.duration_to):
            query['DurationTo'] = request.duration_to
        if not UtilClient.is_unset(request.hangup_direction):
            query['HangupDirection'] = request.hangup_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='QueryRobotTaskCallList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robot_task_call_list(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskCallListRequest

        @return: QueryRobotTaskCallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_list_with_options(request, runtime)

    def query_robot_task_detail_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRobotTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='QueryRobotTaskDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robot_task_detail(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskDetailRequest

        @return: QueryRobotTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_detail_with_options(request, runtime)

    def query_robot_task_list_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRobotTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRobotTaskList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robot_task_list(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotTaskListRequest

        @return: QueryRobotTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_list_with_options(request, runtime)

    def query_robotv_2all_list_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotv2AllListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRobotv2AllListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryRobotv2AllList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_robotv_2all_list(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryRobotv2AllListRequest

        @return: QueryRobotv2AllListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_robotv_2all_list_with_options(request, runtime)

    def query_video_play_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
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
            action='QueryVideoPlayProgress',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVideoPlayProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def query_video_play_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_video_play_progress_with_options(request, runtime)

    def query_virtual_number_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryVirtualNumberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryVirtualNumberResponse
        """
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
        if not UtilClient.is_unset(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumber',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def query_virtual_number(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: QueryVirtualNumberRequest

        @return: QueryVirtualNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_with_options(request, runtime)

    def query_virtual_number_relation_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 200 times per second per account.
        

        @param request: QueryVirtualNumberRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryVirtualNumberRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.region_name_city):
            query['RegionNameCity'] = request.region_name_city
        if not UtilClient.is_unset(request.related_num):
            query['RelatedNum'] = request.related_num
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_type):
            query['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVirtualNumberRelation',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_virtual_number_relation(self, request):
        """
        ### QPS limits
        You can call this operation up to 200 times per second per account.
        

        @param request: QueryVirtualNumberRelationRequest

        @return: QueryVirtualNumberRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_relation_with_options(request, runtime)

    def query_voice_file_audit_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.voice_codes):
            query['VoiceCodes'] = request.voice_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVoiceFileAuditInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVoiceFileAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_voice_file_audit_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_voice_file_audit_info_with_options(request, runtime)

    def recover_call_in_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
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
            action='RecoverCallInConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.RecoverCallInConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def recover_call_in_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recover_call_in_config_with_options(request, runtime)

    def resume_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
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
            action='ResumeVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ResumeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_video_file_with_options(request, runtime)

    def seek_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.seek_times):
            query['SeekTimes'] = request.seek_times
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SeekVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SeekVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def seek_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.seek_video_file_with_options(request, runtime)

    def send_verification_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SendVerificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SendVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verification(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SendVerificationRequest

        @return: SendVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_with_options(request, runtime)

    def set_transfer_callee_pool_config_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SetTransferCalleePoolConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetTransferCalleePoolConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_route_mode):
            query['CalledRouteMode'] = request.called_route_mode
        if not UtilClient.is_unset(request.details):
            query['Details'] = request.details
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTransferCalleePoolConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SetTransferCalleePoolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_transfer_callee_pool_config(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SetTransferCalleePoolConfigRequest

        @return: SetTransferCalleePoolConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_transfer_callee_pool_config_with_options(request, runtime)

    def single_call_by_tts_with_options(self, request, runtime):
        """
        Due to business adjustments, the updates of the voice notification and voice verification code services have been stopped in regions outside the Chinese mainland and the services have been discontinued since March 2022. Only qualified customers can continue using the voice notification and voice verification code services.
        *   For more information about voice plans or voice service billing, see [Pricing of VMS on China site (aliyun.com)](~~150083~~).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account.
        

        @param request: SingleCallByTtsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SingleCallByTtsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleCallByTts',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            self.call_api(params, req, runtime)
        )

    def single_call_by_tts(self, request):
        """
        Due to business adjustments, the updates of the voice notification and voice verification code services have been stopped in regions outside the Chinese mainland and the services have been discontinued since March 2022. Only qualified customers can continue using the voice notification and voice verification code services.
        *   For more information about voice plans or voice service billing, see [Pricing of VMS on China site (aliyun.com)](~~150083~~).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account.
        

        @param request: SingleCallByTtsRequest

        @return: SingleCallByTtsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_tts_with_options(request, runtime)

    def single_call_by_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.video_code):
            query['VideoCode'] = request.video_code
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleCallByVideo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def single_call_by_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_video_with_options(request, runtime)

    def single_call_by_voice_with_options(self, request, runtime):
        """
        > Due to business adjustments, the updates of the voice notification and voice verification code services have been stopped in regions outside the Chinese mainland and the services have been discontinued since March 2022. Only qualified customers can continue using the voice notification and voice verification code services.
        You can call the [SingleCallByTts](~~393519~~) operation to send voice notifications with variables.
        ### QPS limits
        You can call this operation up to 1,200 times per second per account.
        

        @param request: SingleCallByVoiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SingleCallByVoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_times):
            query['PlayTimes'] = request.play_times
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleCallByVoice',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def single_call_by_voice(self, request):
        """
        > Due to business adjustments, the updates of the voice notification and voice verification code services have been stopped in regions outside the Chinese mainland and the services have been discontinued since March 2022. Only qualified customers can continue using the voice notification and voice verification code services.
        You can call the [SingleCallByTts](~~393519~~) operation to send voice notifications with variables.
        ### QPS limits
        You can call this operation up to 1,200 times per second per account.
        

        @param request: SingleCallByVoiceRequest

        @return: SingleCallByVoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_voice_with_options(request, runtime)

    def skip_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.skip_times):
            query['SkipTimes'] = request.skip_times
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SkipVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.skip_video_file_with_options(request, runtime)

    def smart_call_with_options(self, request, runtime):
        """
        The SmartCall operation must be used together with the [intelligent outbound HTTP operation](~~112703~~). After the call initiated by the Voice Messaging Service (VMS) platform is connected, the VMS platform sends the text converted from speech back to the business side, and the business side then returns the follow-up action to the VMS platform.
        *   The SmartCall operation does not support the following characters: `@ = : "" $ { } ^ * ￥`.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account.
        

        @param request: SmartCallRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SmartCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not UtilClient.is_unset(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not UtilClient.is_unset(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not UtilClient.is_unset(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not UtilClient.is_unset(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not UtilClient.is_unset(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not UtilClient.is_unset(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not UtilClient.is_unset(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not UtilClient.is_unset(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not UtilClient.is_unset(request.noise_threshold):
            query['NoiseThreshold'] = request.noise_threshold
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not UtilClient.is_unset(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.stream_asr):
            query['StreamAsr'] = request.stream_asr
        if not UtilClient.is_unset(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not UtilClient.is_unset(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not UtilClient.is_unset(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not UtilClient.is_unset(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not UtilClient.is_unset(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not UtilClient.is_unset(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmartCall',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    def smart_call(self, request):
        """
        The SmartCall operation must be used together with the [intelligent outbound HTTP operation](~~112703~~). After the call initiated by the Voice Messaging Service (VMS) platform is connected, the VMS platform sends the text converted from speech back to the business side, and the business side then returns the follow-up action to the VMS platform.
        *   The SmartCall operation does not support the following characters: `@ = : "" $ { } ^ * ￥`.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account.
        

        @param request: SmartCallRequest

        @return: SmartCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.smart_call_with_options(request, runtime)

    def smart_call_operate_with_options(self, request, runtime):
        """
        You can call this operation to initiate a specified action on the called number of an outbound robocall when the call is transferred to an agent of the call center.
        > You can only initiate the action of bridging a called number and an agent of the call center.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SmartCallOperateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SmartCallOperateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmartCallOperate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    def smart_call_operate(self, request):
        """
        You can call this operation to initiate a specified action on the called number of an outbound robocall when the call is transferred to an agent of the call center.
        > You can only initiate the action of bridging a called number and an agent of the call center.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SmartCallOperateRequest

        @return: SmartCallOperateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.smart_call_operate_with_options(request, runtime)

    def start_robot_task_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: StartRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_robot_task(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: StartRobotTaskRequest

        @return: StartRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_robot_task_with_options(request, runtime)

    def stop_call_in_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
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
            action='StopCallInConfig',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopCallInConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_call_in_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_call_in_config_with_options(request, runtime)

    def stop_robot_task_with_options(self, request, runtime):
        """
        After you stop a robocall task, you can call the [StartRobotTask](~~StartRobotTask~~) operation to start it again.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: StopRobotTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopRobotTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='StopRobotTask',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_robot_task(self, request):
        """
        After you stop a robocall task, you can call the [StartRobotTask](~~StartRobotTask~~) operation to start it again.
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: StopRobotTaskRequest

        @return: StopRobotTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_robot_task_with_options(request, runtime)

    def submit_hotline_transfer_register_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SubmitHotlineTransferRegisterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitHotlineTransferRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement):
            query['Agreement'] = request.agreement
        if not UtilClient.is_unset(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not UtilClient.is_unset(request.operator_identity_card):
            query['OperatorIdentityCard'] = request.operator_identity_card
        if not UtilClient.is_unset(request.operator_mail):
            query['OperatorMail'] = request.operator_mail
        if not UtilClient.is_unset(request.operator_mail_verify_code):
            query['OperatorMailVerifyCode'] = request.operator_mail_verify_code
        if not UtilClient.is_unset(request.operator_mobile):
            query['OperatorMobile'] = request.operator_mobile
        if not UtilClient.is_unset(request.operator_mobile_verify_code):
            query['OperatorMobileVerifyCode'] = request.operator_mobile_verify_code
        if not UtilClient.is_unset(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transfer_phone_number_infos):
            query['TransferPhoneNumberInfos'] = request.transfer_phone_number_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotlineTransferRegister',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SubmitHotlineTransferRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_hotline_transfer_register(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: SubmitHotlineTransferRegisterRequest

        @return: SubmitHotlineTransferRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_hotline_transfer_register_with_options(request, runtime)

    def upgrade_video_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
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
            action='UpgradeVideoFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UpgradeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_video_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_video_file_with_options(request, runtime)

    def upload_robot_task_called_file_with_options(self, request, runtime):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: UploadRobotTaskCalledFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadRobotTaskCalledFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not UtilClient.is_unset(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadRobotTaskCalledFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_robot_task_called_file(self, request):
        """
        ### QPS limits
        You can call this operation up to 100 times per second per account.
        

        @param request: UploadRobotTaskCalledFileRequest

        @return: UploadRobotTaskCalledFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_robot_task_called_file_with_options(request, runtime)
