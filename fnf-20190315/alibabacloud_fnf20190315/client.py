# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fnf20190315 import models as fnf_20190315_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'cn-beijing.fnf.aliyuncs.com',
            'cn-hangzhou': 'cn-hangzhou.fnf.aliyuncs.com',
            'cn-shanghai': 'cn-shanghai.fnf.aliyuncs.com',
            'cn-shenzhen': 'cn-shenzhen.fnf.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('fnf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_flow_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        *   The number of flows that each user can create is restricted by resources. For more information, see [Limits](~~122093~~). If you want to create more flows, submit a ticket.
        *   At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        

        @param request: CreateFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.external_storage_location):
            body['ExternalStorageLocation'] = request.external_storage_location
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def create_flow(self, request):
        """
        ## [](#)Usage notes
        *   The number of flows that each user can create is restricted by resources. For more information, see [Limits](~~122093~~). If you want to create more flows, submit a ticket.
        *   At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        

        @param request: CreateFlowRequest

        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    def create_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_with_options(request, runtime)

    def delete_flow_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        

        @param request: DeleteFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_flow(self, request):
        """
        ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        

        @param request: DeleteFlowRequest

        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    def delete_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_with_options(request, runtime)

    def describe_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_execution_with_options(request, runtime)

    def describe_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    def describe_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_with_options(request, runtime)

    def get_execution_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecutionHistory',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.GetExecutionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_execution_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_execution_history_with_options(request, runtime)

    def list_executions_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        

        @param request: ListExecutionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_executions(self, request):
        """
        ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        

        @param request: ListExecutionsRequest

        @return: ListExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    def list_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_flows(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    def list_schedules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_schedules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_schedules_with_options(request, runtime)

    def report_task_failed_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        You can use this operation to call back the task step of `pattern: waitForCallback`, which indicates that the current task fails to be executed.
        

        @param request: ReportTaskFailedRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReportTaskFailedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskFailed',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskFailedResponse(),
            self.call_api(params, req, runtime)
        )

    def report_task_failed(self, request):
        """
        ## [](#)Usage notes
        You can use this operation to call back the task step of `pattern: waitForCallback`, which indicates that the current task fails to be executed.
        

        @param request: ReportTaskFailedRequest

        @return: ReportTaskFailedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_task_failed_with_options(request, runtime)

    def report_task_succeeded_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        You can use this operation to call back the task step of `pattern: waitForCallback`, which indicates that the current task is successfully executed.
        

        @param request: ReportTaskSucceededRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReportTaskSucceededResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskSucceeded',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskSucceededResponse(),
            self.call_api(params, req, runtime)
        )

    def report_task_succeeded(self, request):
        """
        ## [](#)Usage notes
        You can use this operation to call back the task step of `pattern: waitForCallback`, which indicates that the current task is successfully executed.
        

        @param request: ReportTaskSucceededRequest

        @return: ReportTaskSucceededResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_task_succeeded_with_options(request, runtime)

    def start_execution_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        *   The flow is created.
        *   If you do not specify an execution, the system automatically generates an execution and starts the execution.
        *   If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        *   If the ongoing execution with the same name has ended (succeeded or failed), the `ExecutionAlreadyExists` error is returned.
        *   If no execution with the same name exists, the system starts a new execution.
        

        @param request: StartExecutionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.callback_fn_ftask_token):
            body['CallbackFnFTaskToken'] = request.callback_fn_ftask_token
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def start_execution(self, request):
        """
        ## [](#)Usage notes
        *   The flow is created.
        *   If you do not specify an execution, the system automatically generates an execution and starts the execution.
        *   If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        *   If the ongoing execution with the same name has ended (succeeded or failed), the `ExecutionAlreadyExists` error is returned.
        *   If no execution with the same name exists, the system starts a new execution.
        

        @param request: StartExecutionRequest

        @return: StartExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    def start_sync_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSyncExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartSyncExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def start_sync_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_sync_execution_with_options(request, runtime)

    def stop_execution_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        The flow must be in progress.
        

        @param request: StopExecutionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StopExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_execution(self, request):
        """
        ## [](#)Usage notes
        The flow must be in progress.
        

        @param request: StopExecutionRequest

        @return: StopExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_execution_with_options(request, runtime)

    def update_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def update_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    def update_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_with_options(request, runtime)
