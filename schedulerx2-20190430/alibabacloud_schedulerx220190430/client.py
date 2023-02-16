# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_schedulerx220190430 import models as schedulerx_220190430_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'schedulerx.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'schedulerx.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'schedulerx.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'schedulerx.cn-shenzhen.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('schedulerx2', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_delete_jobs_with_options(self, request, runtime):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchDeleteJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchDeleteJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_jobs(self, request):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchDeleteJobsRequest

        @return: BatchDeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_jobs_with_options(request, runtime)

    def batch_disable_jobs_with_options(self, request, runtime):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchDisableJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchDisableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDisableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_disable_jobs(self, request):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchDisableJobsRequest

        @return: BatchDisableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_disable_jobs_with_options(request, runtime)

    def batch_enable_jobs_with_options(self, request, runtime):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchEnableJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchEnableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchEnableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_enable_jobs(self, request):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        

        @param request: BatchEnableJobsRequest

        @return: BatchEnableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_enable_jobs_with_options(request, runtime)

    def create_app_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    def create_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not UtilClient.is_unset(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    def create_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    def create_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_workflow_with_options(request, runtime)

    def delete_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    def delete_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def designate_workers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesignateWorkers',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DesignateWorkersResponse(),
            self.call_api(params, req, runtime)
        )

    def designate_workers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.designate_workers_with_options(request, runtime)

    def disable_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableJobResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_job_with_options(request, runtime)

    def disable_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_workflow_with_options(request, runtime)

    def enable_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableJobResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_job_with_options(request, runtime)

    def enable_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_workflow_with_options(request, runtime)

    def execute_job_with_options(self, request, runtime):
        """
        > : The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        

        @param request: ExecuteJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExecuteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_job(self, request):
        """
        > : The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        

        @param request: ExecuteJobRequest

        @return: ExecuteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_job_with_options(request, runtime)

    def execute_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_workflow_with_options(request, runtime)

    def get_job_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_info_with_options(request, runtime)

    def get_job_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_with_options(request, runtime)

    def get_job_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstanceList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_list_with_options(request, runtime)

    def get_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLog',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_with_options(request, runtime)

    def get_work_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkFlow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_work_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_work_flow_with_options(request, runtime)

    def get_worker_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkerList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkerListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_worker_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_worker_list_with_options(request, runtime)

    def get_workflow_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workflow_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_instance_with_options(request, runtime)

    def grant_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantPermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GrantPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_permission_with_options(request, runtime)

    def list_groups_with_options(self, request, runtime):
        """
        >  Before you call this operation, you must add the following dependency to the pom.xml file:
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        

        @param request: ListGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        """
        >  Before you call this operation, you must add the following dependency to the pom.xml file:
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        

        @param request: ListGroupsRequest

        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_jobs_with_options(self, request, runtime):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        

        @param request: ListJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, request):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        

        @param request: ListJobsRequest

        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    def list_namespaces_with_options(self, request, runtime):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        

        @param request: ListNamespacesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_namespaces(self, request):
        """
        Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        

        @param request: ListNamespacesRequest

        @return: ListNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    def list_workflow_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workflow_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_instance_with_options(request, runtime)

    def rerun_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_time):
            body['DataTime'] = request.data_time
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RerunJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    def rerun_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    def retry_job_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RetryJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_job_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_job_instance_with_options(request, runtime)

    def revoke_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokePermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RevokePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_permission_with_options(request, runtime)

    def set_job_instance_success_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetJobInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetJobInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    def set_job_instance_success(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_job_instance_success_with_options(request, runtime)

    def set_wf_instance_success_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wf_instance_id):
            query['WfInstanceId'] = request.wf_instance_id
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWfInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetWfInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    def set_wf_instance_success(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_wf_instance_success_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def update_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    def update_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_with_options(request, runtime)

    def update_workflow_dag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.dag_json):
            body['DagJson'] = request.dag_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDag',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowDagResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workflow_dag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_dag_with_options(request, runtime)
