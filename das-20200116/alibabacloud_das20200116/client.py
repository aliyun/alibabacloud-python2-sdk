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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.flush_account):
            query['FlushAccount'] = request.flush_account
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.src_engine):
            query['SrcEngine'] = request.src_engine
        if not UtilClient.is_unset(request.src_engine_version):
            query['SrcEngineVersion'] = request.src_engine_version
        if not UtilClient.is_unset(request.src_max_qps):
            query['SrcMaxQps'] = request.src_max_qps
        if not UtilClient.is_unset(request.src_mean_qps):
            query['SrcMeanQps'] = request.src_mean_qps
        if not UtilClient.is_unset(request.src_sql_oss_addr):
            query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_connection_string):
            query['DstConnectionString'] = request.dst_connection_string
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.dst_type):
            query['DstType'] = request.dst_type
        if not UtilClient.is_unset(request.dts_job_class):
            query['DtsJobClass'] = request.dts_job_class
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_state):
            query['EndState'] = request.end_state
        if not UtilClient.is_unset(request.gateway_vpc_id):
            query['GatewayVpcId'] = request.gateway_vpc_id
        if not UtilClient.is_unset(request.gateway_vpc_ip):
            query['GatewayVpcIp'] = request.gateway_vpc_ip
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_end_time):
            query['RequestEndTime'] = request.request_end_time
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.smart_pressure_time):
            query['SmartPressureTime'] = request.smart_pressure_time
        if not UtilClient.is_unset(request.src_instance_id):
            query['SrcInstanceId'] = request.src_instance_id
        if not UtilClient.is_unset(request.src_public_ip):
            query['SrcPublicIp'] = request.src_public_ip
        if not UtilClient.is_unset(request.src_super_account):
            query['SrcSuperAccount'] = request.src_super_account
        if not UtilClient.is_unset(request.src_super_password):
            query['SrcSuperPassword'] = request.src_super_password
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.work_dir):
            query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    def create_request_diagnosis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_request_diagnosis_with_options(request, runtime)

    def delete_cloud_bench_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DeleteCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cloud_bench_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_bench_task_with_options(request, runtime)

    def describe_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.concurrency_control_time):
            query['ConcurrencyControlTime'] = request.concurrency_control_time
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.sql_keywords):
            query['SqlKeywords'] = request.sql_keywords
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_sql_concurrency_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    def get_async_error_request_list_by_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestListByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_error_request_list_by_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_list_by_code_with_options(request, runtime)

    def get_async_error_request_stat_by_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_error_request_stat_by_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_by_code_with_options(request, runtime)

    def get_async_error_request_stat_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_id_list):
            query['SqlIdList'] = request.sql_id_list
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_error_request_stat_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_result_with_options(request, runtime)

    def get_auto_resource_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.span_id):
            query['SpanId'] = request.span_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_context):
            query['EventContext'] = request.event_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.min_level):
            query['MinLevel'] = request.min_level
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_offset):
            query['PageOffset'] = request.page_offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_endpoint_switch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    def get_error_request_sample_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorRequestSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetErrorRequestSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_error_request_sample(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_error_request_sample_with_options(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_map):
            query['SearchMap'] = request.search_map
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_inspections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    def get_query_optimize_data_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_data_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_stats_with_options(request, runtime)

    def get_query_optimize_data_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTop',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTopResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_data_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_top_with_options(request, runtime)

    def get_query_optimize_data_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTrend',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_data_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_trend_with_options(request, runtime)

    def get_query_optimize_exec_error_sample_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_exec_error_sample(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_sample_with_options(request, runtime)

    def get_query_optimize_exec_error_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_exec_error_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_stats_with_options(request, runtime)

    def get_query_optimize_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeRuleList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_rule_list_with_options(request, runtime)

    def get_query_optimize_solution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeSolution',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_optimize_solution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_solution_with_options(request, runtime)

    def get_request_diagnosis_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceOptimizeHistoryList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_text):
            query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_dt):
            query['EndDt'] = request.end_dt
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.start_dt):
            query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.stop_or_rollback):
            query['StopOrRollback'] = request.stop_or_rollback
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopOrRollbackOptimizeTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.wait_for_modify_security_ips):
            query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TurnOffAutoResourceOptimize',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.auto_defragment):
            query['AutoDefragment'] = request.auto_defragment
        if not UtilClient.is_unset(request.auto_duplicate_index_delete):
            query['AutoDuplicateIndexDelete'] = request.auto_duplicate_index_delete
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.table_fragmentation_ratio):
            query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        if not UtilClient.is_unset(request.table_space_size):
            query['TableSpaceSize'] = request.table_space_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auto_resource_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_config_with_options(request, runtime)
