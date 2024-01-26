# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pts20150801 import models as pts20150801_models
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
        self._endpoint = self.get_endpoint('pts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_transaction_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateTransactionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransactionResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.transaction_name):
            query['TransactionName'] = request.transaction_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransaction',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.CreateTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transaction(self, request):
        """
        @deprecated
        

        @param request: CreateTransactionRequest

        @return: CreateTransactionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transaction_with_options(request, runtime)

    def get_key_secret_with_options(self, runtime):
        """
        @deprecated
        

        @param request: GetKeySecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetKeySecretResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetKeySecret',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.GetKeySecretResponse(),
            self.call_api(params, req, runtime)
        )

    def get_key_secret(self):
        """
        @deprecated
        

        @return: GetKeySecretResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_key_secret_with_options(runtime)

    def get_script_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetScriptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetScriptResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.tfsname):
            query['Tfsname'] = request.tfsname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScript',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.GetScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def get_script(self, request):
        """
        @deprecated
        

        @param request: GetScriptRequest

        @return: GetScriptResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_script_with_options(request, runtime)

    def get_tasks_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTasksResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTasks',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.GetTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tasks(self, request):
        """
        @deprecated
        

        @param request: GetTasksRequest

        @return: GetTasksResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tasks_with_options(request, runtime)

    def report_log_sample_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ReportLogSampleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReportLogSampleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_sample):
            query['LogSample'] = request.log_sample
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.wskey):
            query['Wskey'] = request.wskey
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportLogSample',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.ReportLogSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def report_log_sample(self, request):
        """
        @deprecated
        

        @param request: ReportLogSampleRequest

        @return: ReportLogSampleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.report_log_sample_with_options(request, runtime)

    def report_test_sample_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ReportTestSampleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReportTestSampleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.test_sample):
            query['TestSample'] = request.test_sample
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportTestSample',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.ReportTestSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def report_test_sample(self, request):
        """
        @deprecated
        

        @param request: ReportTestSampleRequest

        @return: ReportTestSampleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.report_test_sample_with_options(request, runtime)

    def report_vuser_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ReportVuserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReportVuserResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gmt_created):
            query['GmtCreated'] = request.gmt_created
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.vuser):
            query['Vuser'] = request.vuser
        if not UtilClient.is_unset(request.wskey):
            query['Wskey'] = request.wskey
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportVuser',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.ReportVuserResponse(),
            self.call_api(params, req, runtime)
        )

    def report_vuser(self, request):
        """
        @deprecated
        

        @param request: ReportVuserRequest

        @return: ReportVuserResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.report_vuser_with_options(request, runtime)

    def send_wang_wang_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: SendWangWangRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendWangWangResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = pts20150801_models.SendWangWangShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.to):
            request.to_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to, 'To', 'json')
        query = {}
        if not UtilClient.is_unset(request.msg):
            query['Msg'] = request.msg
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.to_shrink):
            query['To'] = request.to_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendWangWang',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.SendWangWangResponse(),
            self.call_api(params, req, runtime)
        )

    def send_wang_wang(self, request):
        """
        @deprecated
        

        @param request: SendWangWangRequest

        @return: SendWangWangResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.send_wang_wang_with_options(request, runtime)

    def set_scenario_status_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: SetScenarioStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetScenarioStatusResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_ip):
            query['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.wskey):
            query['Wskey'] = request.wskey
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScenarioStatus',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.SetScenarioStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scenario_status(self, request):
        """
        @deprecated
        

        @param request: SetScenarioStatusRequest

        @return: SetScenarioStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_scenario_status_with_options(request, runtime)

    def set_task_status_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: SetTaskStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetTaskStatusResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.wskey):
            query['Wskey'] = request.wskey
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTaskStatus',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.SetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_task_status(self, request):
        """
        @deprecated
        

        @param request: SetTaskStatusRequest

        @return: SetTaskStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_task_status_with_options(request, runtime)

    def stop_task_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: StopTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopTaskResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.msg):
            query['Msg'] = request.msg
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2015-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20150801_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_task(self, request):
        """
        @deprecated
        

        @param request: StopTaskRequest

        @return: StopTaskResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_task_with_options(request, runtime)
