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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def add_hdminstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Engine'] = request.engine
        query['FlushAccount'] = request.flush_account
        query['InstanceAlias'] = request.instance_alias
        query['InstanceArea'] = request.instance_area
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NetworkType'] = request.network_type
        query['Password'] = request.password
        query['Port'] = request.port
        query['Region'] = request.region
        query['Username'] = request.username
        query['VpcId'] = request.vpc_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_hdminstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    def create_adam_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DstInstanceId'] = request.dst_instance_id
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestStartTime'] = request.request_start_time
        query['SrcEngine'] = request.src_engine
        query['SrcEngineVersion'] = request.src_engine_version
        query['SrcMaxQps'] = request.src_max_qps
        query['SrcMeanQps'] = request.src_mean_qps
        query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_adam_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adam_bench_task_with_options(request, runtime)

    def create_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupSetId'] = request.backup_set_id
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    def create_cloud_bench_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Amount'] = request.amount
        query['BackupId'] = request.backup_id
        query['BackupTime'] = request.backup_time
        query['ClientType'] = request.client_type
        query['Description'] = request.description
        query['DstConnectionString'] = request.dst_connection_string
        query['DstInstanceId'] = request.dst_instance_id
        query['DstPort'] = request.dst_port
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['DstType'] = request.dst_type
        query['DtsJobClass'] = request.dts_job_class
        query['DtsJobId'] = request.dts_job_id
        query['EndState'] = request.end_state
        query['GatewayVpcId'] = request.gateway_vpc_id
        query['GatewayVpcIp'] = request.gateway_vpc_ip
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestEndTime'] = request.request_end_time
        query['RequestStartTime'] = request.request_start_time
        query['SmartPressureTime'] = request.smart_pressure_time
        query['SrcInstanceId'] = request.src_instance_id
        query['SrcPublicIp'] = request.src_public_ip
        query['SrcSuperAccount'] = request.src_super_account
        query['SrcSuperPassword'] = request.src_super_password
        query['TaskType'] = request.task_type
        query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cloud_bench_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_bench_tasks_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def create_request_diagnosis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Database'] = request.database
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    def create_request_diagnosis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_request_diagnosis_with_options(request, runtime)

    def describe_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    def describe_cache_analysis_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cache_analysis_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    def describe_cloud_bench_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_bench_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_bench_tasks_with_options(request, runtime)

    def describe_cloudbench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloudbench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_with_options(request, runtime)

    def describe_cloudbench_task_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloudbench_task_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_config_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def describe_hot_big_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hot_big_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_big_keys_with_options(request, runtime)

    def describe_hot_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hot_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    def describe_top_big_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_top_big_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_big_keys_with_options(request, runtime)

    def describe_top_hot_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_top_hot_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_hot_keys_with_options(request, runtime)

    def disable_all_sql_concurrency_control_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_all_sql_concurrency_control_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_all_sql_concurrency_control_rules_with_options(request, runtime)

    def disable_sql_concurrency_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_sql_concurrency_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_concurrency_control_with_options(request, runtime)

    def enable_sql_concurrency_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConcurrencyControlTime'] = request.concurrency_control_time
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['MaxConcurrency'] = request.max_concurrency
        query['SqlKeywords'] = request.sql_keywords
        query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_sql_concurrency_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    def get_auto_resource_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auto_resource_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_config_with_options(request, runtime)

    def get_autonomous_notify_event_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SpanId'] = request.span_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_autonomous_notify_event_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['EventContext'] = request.event_context
        query['InstanceId'] = request.instance_id
        query['Level'] = request.level
        query['MinLevel'] = request.min_level
        query['NodeId'] = request.node_id
        query['PageOffset'] = request.page_offset
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_autonomous_notify_events_in_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    def get_endpoint_switch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_endpoint_switch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hdmaliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hdmlast_aliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    def get_instance_inspections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['Engine'] = request.engine
        query['InstanceArea'] = request.instance_area
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['SearchMap'] = request.search_map
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_inspections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    def get_request_diagnosis_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_request_diagnosis_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_page_with_options(request, runtime)

    def get_request_diagnosis_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['MessageId'] = request.message_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_request_diagnosis_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_result_with_options(request, runtime)

    def get_resource_optimize_history_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Page'] = request.page
        query['PageSize'] = request.page_size
        query['Signature'] = request.signature
        query['StartTime'] = request.start_time
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResourceOptimizeHistoryList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_optimize_history_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_optimize_history_list_with_options(request, runtime)

    def get_running_sql_concurrency_control_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_running_sql_concurrency_control_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_running_sql_concurrency_control_rules_with_options(request, runtime)

    def get_sql_concurrency_control_keywords_from_sql_text_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sql_concurrency_control_keywords_from_sql_text(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_keywords_from_sql_text_with_options(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sql_concurrency_control_rules_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_rules_history_with_options(request, runtime)

    def get_sql_optimize_advice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndDt'] = request.end_dt
        query['Engine'] = request.engine
        query['InstanceIds'] = request.instance_ids
        query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sql_optimize_advice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_optimize_advice_with_options(request, runtime)

    def run_cloud_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def run_cloud_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_bench_task_with_options(request, runtime)

    def stop_cloud_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cloud_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_bench_task_with_options(request, runtime)

    def stop_or_rollback_optimize_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['StopOrRollback'] = request.stop_or_rollback
        query['TaskType'] = request.task_type
        query['TaskUuid'] = request.task_uuid
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopOrRollbackOptimizeTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_or_rollback_optimize_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_or_rollback_optimize_task_with_options(request, runtime)

    def sync_hdmaliyun_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Async'] = request.async
        query['ResourceTypes'] = request.resource_types
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_hdmaliyun_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_hdmaliyun_resource_with_options(request, runtime)

    def turn_off_auto_resource_optimize_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TurnOffAutoResourceOptimize',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            self.call_api(params, req, runtime)
        )

    def turn_off_auto_resource_optimize(self, request):
        runtime = util_models.RuntimeOptions()
        return self.turn_off_auto_resource_optimize_with_options(request, runtime)

    def update_auto_resource_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['AutoDefragment'] = request.auto_defragment
        query['AutoDuplicateIndexDelete'] = request.auto_duplicate_index_delete
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        query['TableSpaceSize'] = request.table_space_size
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auto_resource_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_config_with_options(request, runtime)
