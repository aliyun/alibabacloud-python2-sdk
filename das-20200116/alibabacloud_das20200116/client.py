# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_das20200116 import models as das20200116_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-shanghai': 'das.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('das', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def access_hdminstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AccessHDMInstanceResponse(),
            self.do_rpcrequest('AccessHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def access_hdminstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.access_hdminstance_with_options(request, runtime)

    def add_hdminstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            self.do_rpcrequest('AddHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hdminstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    def create_adam_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            self.do_rpcrequest('CreateAdamBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adam_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adam_bench_task_with_options(request, runtime)

    def create_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            self.do_rpcrequest('CreateCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    def create_cloud_bench_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            self.do_rpcrequest('CreateCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cloud_bench_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_bench_tasks_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            self.do_rpcrequest('CreateDiagnosticReport', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def describe_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    def describe_cache_analysis_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJobs', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    def describe_cloud_bench_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            self.do_rpcrequest('DescribeCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_bench_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_bench_tasks_with_options(request, runtime)

    def describe_cloudbench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            self.do_rpcrequest('DescribeCloudbenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloudbench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_with_options(request, runtime)

    def describe_cloudbench_task_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            self.do_rpcrequest('DescribeCloudbenchTaskConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloudbench_task_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_config_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            self.do_rpcrequest('DescribeDiagnosticReportList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def describe_hot_big_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            self.do_rpcrequest('DescribeHotBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_big_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_big_keys_with_options(request, runtime)

    def describe_hot_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            self.do_rpcrequest('DescribeHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    def describe_top_big_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            self.do_rpcrequest('DescribeTopBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_top_big_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_big_keys_with_options(request, runtime)

    def describe_top_hot_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            self.do_rpcrequest('DescribeTopHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_top_hot_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_hot_keys_with_options(request, runtime)

    def disable_all_sql_concurrency_control_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            self.do_rpcrequest('DisableAllSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_all_sql_concurrency_control_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_all_sql_concurrency_control_rules_with_options(request, runtime)

    def disable_sql_concurrency_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            self.do_rpcrequest('DisableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_sql_concurrency_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_concurrency_control_with_options(request, runtime)

    def enable_sql_concurrency_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            self.do_rpcrequest('EnableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_concurrency_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    def get_auto_resource_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('GetAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auto_resource_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_config_with_options(request, runtime)

    def get_autonomous_notify_event_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventContent', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    def get_autonomous_notify_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventDetailResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventDetail', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_detail_with_options(request, runtime)

    def get_autonomous_notify_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEvents', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_with_options(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventsInRange', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events_in_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    def get_endpoint_switch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.do_rpcrequest('GetEndpointSwitchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_endpoint_switch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    def get_event_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEventOverviewResponse(),
            self.do_rpcrequest('GetEventOverview', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_event_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_overview_with_options(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmaliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMLastAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmlast_aliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    def get_instance_inspections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.do_rpcrequest('GetInstanceInspections', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_inspections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    def get_request_diagnosis_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisIdResponse(),
            self.do_rpcrequest('GetRequestDiagnosisId', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_request_diagnosis_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_id_with_options(request, runtime)

    def get_request_diagnosis_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            self.do_rpcrequest('GetRequestDiagnosisPage', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_request_diagnosis_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_page_with_options(request, runtime)

    def get_request_diagnosis_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            self.do_rpcrequest('GetRequestDiagnosisResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_request_diagnosis_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_result_with_options(request, runtime)

    def get_resource_optimize_history_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            self.do_rpcrequest('GetResourceOptimizeHistoryList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_optimize_history_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_optimize_history_list_with_options(request, runtime)

    def get_running_sql_concurrency_control_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            self.do_rpcrequest('GetRunningSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_running_sql_concurrency_control_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_running_sql_concurrency_control_rules_with_options(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            self.do_rpcrequest('GetSqlConcurrencyControlRulesHistory', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_concurrency_control_rules_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_rules_history_with_options(request, runtime)

    def get_sql_optimize_advice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            self.do_rpcrequest('GetSqlOptimizeAdvice', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_optimize_advice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_optimize_advice_with_options(request, runtime)

    def run_cloud_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            self.do_rpcrequest('RunCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cloud_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_bench_task_with_options(request, runtime)

    def stop_cloud_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            self.do_rpcrequest('StopCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_cloud_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_bench_task_with_options(request, runtime)

    def stop_or_rollback_optimize_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            self.do_rpcrequest('StopOrRollbackOptimizeTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_or_rollback_optimize_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_or_rollback_optimize_task_with_options(request, runtime)

    def sync_hdmaliyun_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            self.do_rpcrequest('SyncHDMAliyunResource', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_hdmaliyun_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_hdmaliyun_resource_with_options(request, runtime)

    def turn_off_auto_resource_optimize_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            self.do_rpcrequest('TurnOffAutoResourceOptimize', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def turn_off_auto_resource_optimize(self, request):
        runtime = util_models.RuntimeOptions()
        return self.turn_off_auto_resource_optimize_with_options(request, runtime)

    def update_auto_resource_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('UpdateAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_auto_resource_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_config_with_options(request, runtime)
