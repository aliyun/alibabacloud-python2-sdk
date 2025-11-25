# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr_serverless_spark20230808 import models as emr_serverless_spark_20230808_models
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
        self._endpoint = self.get_endpoint('emr-serverless-spark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_members_with_options(self, request, headers, runtime):
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        

        @param request: AddMembersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/auth/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.AddMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_members(self, request):
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        

        @param request: AddMembersRequest

        @return: AddMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_members_with_options(request, headers, runtime)

    def cancel_job_run_with_options(self, workspace_id, job_run_id, request, headers, runtime):
        """
        @summary Terminates a Spark job.
        

        @param request: CancelJobRunRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_run_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_job_run(self, workspace_id, job_run_id, request):
        """
        @summary Terminates a Spark job.
        

        @param request: CancelJobRunRequest

        @return: CancelJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    def cancel_kyuubi_spark_application_with_options(self, workspace_id, kyuubi_service_id, application_id, request, headers, runtime):
        """
        @summary CancelKyuubiSparkApplication
        

        @param request: CancelKyuubiSparkApplicationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelKyuubiSparkApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelKyuubiSparkApplication',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s/application/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelKyuubiSparkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_kyuubi_spark_application(self, workspace_id, kyuubi_service_id, application_id, request):
        """
        @summary CancelKyuubiSparkApplication
        

        @param request: CancelKyuubiSparkApplicationRequest

        @return: CancelKyuubiSparkApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_kyuubi_spark_application_with_options(workspace_id, kyuubi_service_id, application_id, request, headers, runtime)

    def create_kyuubi_service_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary CreateKyuubiService
        

        @param request: CreateKyuubiServiceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateKyuubiServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not UtilClient.is_unset(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not UtilClient.is_unset(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.queue):
            body['queue'] = request.queue
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        if not UtilClient.is_unset(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_kyuubi_service(self, workspace_id, request):
        """
        @summary CreateKyuubiService
        

        @param request: CreateKyuubiServiceRequest

        @return: CreateKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_kyuubi_service_with_options(workspace_id, request, headers, runtime)

    def create_kyuubi_token_with_options(self, workspace_id, kyuubi_service_id, request, headers, runtime):
        """
        @summary 创建kyuubi的token
        

        @param request: CreateKyuubiTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/kyuubiService/%s/token' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_kyuubi_token(self, workspace_id, kyuubi_service_id, request):
        """
        @summary 创建kyuubi的token
        

        @param request: CreateKyuubiTokenRequest

        @return: CreateKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_kyuubi_token_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    def create_livy_compute_with_options(self, workspace_biz_id, request, headers, runtime):
        """
        @summary 创建Livy compute
        

        @param request: CreateLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_livy_compute(self, workspace_biz_id, request):
        """
        @summary 创建Livy compute
        

        @param request: CreateLivyComputeRequest

        @return: CreateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    def create_livy_compute_token_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 创建Livy Compute的token
        

        @param request: CreateLivyComputeTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/token' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_livy_compute_token(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 创建Livy Compute的token
        

        @param request: CreateLivyComputeTokenRequest

        @return: CreateLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def create_process_definition_with_schedule_with_options(self, biz_id, tmp_req, headers, runtime):
        """
        @summary Creates a workflow.
        

        @param tmp_req: CreateProcessDefinitionWithScheduleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/dolphinscheduler/projects/%s/process-definition' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(biz_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_process_definition_with_schedule(self, biz_id, request):
        """
        @summary Creates a workflow.
        

        @param request: CreateProcessDefinitionWithScheduleRequest

        @return: CreateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_process_definition_with_schedule_with_options(biz_id, request, headers, runtime)

    def create_session_cluster_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Creates a session.
        

        @param request: CreateSessionClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.application_configs):
            body['applicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.kind):
            body['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/sessionClusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_session_cluster(self, workspace_id, request):
        """
        @summary Creates a session.
        

        @param request: CreateSessionClusterRequest

        @return: CreateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_session_cluster_with_options(workspace_id, request, headers, runtime)

    def create_sql_statement_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Creates an SQL query task.
        

        @param request: CreateSqlStatementRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.code_content):
            body['codeContent'] = request.code_content
        if not UtilClient.is_unset(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not UtilClient.is_unset(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        if not UtilClient.is_unset(request.task_biz_id):
            body['taskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/statement' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sql_statement(self, workspace_id, request):
        """
        @summary Creates an SQL query task.
        

        @param request: CreateSqlStatementRequest

        @return: CreateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sql_statement_with_options(workspace_id, request, headers, runtime)

    def create_workspace_with_options(self, request, headers, runtime):
        """
        @summary Creates a workspace.
        

        @param request: CreateWorkspaceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_renew_period_unit):
            body['autoRenewPeriodUnit'] = request.auto_renew_period_unit
        if not UtilClient.is_unset(request.auto_start_session_cluster):
            body['autoStartSessionCluster'] = request.auto_start_session_cluster
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dlf_catalog_id):
            body['dlfCatalogId'] = request.dlf_catalog_id
        if not UtilClient.is_unset(request.dlf_type):
            body['dlfType'] = request.dlf_type
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.oss_bucket):
            body['ossBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.ram_role_name):
            body['ramRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.release_type):
            body['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        if not UtilClient.is_unset(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace(self, request):
        """
        @summary Creates a workspace.
        

        @param request: CreateWorkspaceRequest

        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    def delete_kyuubi_service_with_options(self, workspace_id, kyuubi_service_id, headers, runtime):
        """
        @summary DeleteKyuubiService
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteKyuubiServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_kyuubi_service(self, workspace_id, kyuubi_service_id):
        """
        @summary DeleteKyuubiService
        

        @return: DeleteKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    def delete_kyuubi_token_with_options(self, workspace_id, kyuubi_service_id, token_id, request, headers, runtime):
        """
        @summary 删除compute的token
        

        @param request: DeleteKyuubiTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/kyuubiService/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_kyuubi_token(self, workspace_id, kyuubi_service_id, token_id, request):
        """
        @summary 删除compute的token
        

        @param request: DeleteKyuubiTokenRequest

        @return: DeleteKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def delete_livy_compute_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 删除livy compute
        

        @param request: DeleteLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_livy_compute(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 删除livy compute
        

        @param request: DeleteLivyComputeRequest

        @return: DeleteLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def delete_livy_compute_token_with_options(self, workspace_biz_id, livy_compute_id, token_id, request, headers, runtime):
        """
        @summary 删除Livy Compute的token
        

        @param request: DeleteLivyComputeTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_livy_compute_token(self, workspace_biz_id, livy_compute_id, token_id, request):
        """
        @summary 删除Livy Compute的token
        

        @param request: DeleteLivyComputeTokenRequest

        @return: DeleteLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def edit_workspace_queue_with_options(self, request, headers, runtime):
        """
        @summary Modifies the queue of a workspace.
        

        @param request: EditWorkspaceQueueRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: EditWorkspaceQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.environments):
            body['environments'] = request.environments
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_queue_name):
            body['workspaceQueueName'] = request.workspace_queue_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditWorkspaceQueue',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/queues/action/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_workspace_queue(self, request):
        """
        @summary Modifies the queue of a workspace.
        

        @param request: EditWorkspaceQueueRequest

        @return: EditWorkspaceQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edit_workspace_queue_with_options(request, headers, runtime)

    def generate_task_codes_with_options(self, biz_id, request, headers, runtime):
        """
        @summary 上线工作流及其调度
        

        @param request: GenerateTaskCodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateTaskCodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gen_num):
            query['genNum'] = request.gen_num
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTaskCodes',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/dolphinscheduler/projects/%s/task-definition/gen-task-codes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(biz_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GenerateTaskCodesResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_task_codes(self, biz_id, request):
        """
        @summary 上线工作流及其调度
        

        @param request: GenerateTaskCodesRequest

        @return: GenerateTaskCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_task_codes_with_options(biz_id, request, headers, runtime)

    def get_cu_hours_with_options(self, workspace_id, queue, request, headers, runtime):
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        

        @param request: GetCuHoursRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCuHoursResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCuHours',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/metric/cuHours/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(queue))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetCuHoursResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cu_hours(self, workspace_id, queue, request):
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        

        @param request: GetCuHoursRequest

        @return: GetCuHoursResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cu_hours_with_options(workspace_id, queue, request, headers, runtime)

    def get_doctor_application_with_options(self, workspace_id, run_id, request, headers, runtime):
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        

        @param request: GetDoctorApplicationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['locale'] = request.locale
        if not UtilClient.is_unset(request.query_time):
            query['queryTime'] = request.query_time
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/runs/%s/action/getDoctorApplication' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(run_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_application(self, workspace_id, run_id, request):
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        

        @param request: GetDoctorApplicationRequest

        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_doctor_application_with_options(workspace_id, run_id, request, headers, runtime)

    def get_job_run_with_options(self, workspace_id, job_run_id, request, headers, runtime):
        """
        @summary Obtain the job details.
        

        @param request: GetJobRunRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_run_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_run(self, workspace_id, job_run_id, request):
        """
        @summary Obtain the job details.
        

        @param request: GetJobRunRequest

        @return: GetJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    def get_kyuubi_service_with_options(self, workspace_id, kyuubi_service_id, headers, runtime):
        """
        @summary GetKyuubiService
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetKyuubiServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_kyuubi_service(self, workspace_id, kyuubi_service_id):
        """
        @summary GetKyuubiService
        

        @return: GetKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    def get_kyuubi_token_with_options(self, workspace_id, kyuubi_service_id, token_id, request, headers, runtime):
        """
        @summary 获取compute的token
        

        @param request: GetKyuubiTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/kyuubiService/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_kyuubi_token(self, workspace_id, kyuubi_service_id, token_id, request):
        """
        @summary 获取compute的token
        

        @param request: GetKyuubiTokenRequest

        @return: GetKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def get_livy_compute_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 获取livy compute
        

        @param request: GetLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_livy_compute(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 获取livy compute
        

        @param request: GetLivyComputeRequest

        @return: GetLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def get_livy_compute_token_with_options(self, workspace_biz_id, livy_compute_id, token_id, request, headers, runtime):
        """
        @summary 获取livy compute token
        

        @param request: GetLivyComputeTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_livy_compute_token(self, workspace_biz_id, livy_compute_id, token_id, request):
        """
        @summary 获取livy compute token
        

        @param request: GetLivyComputeTokenRequest

        @return: GetLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def get_session_cluster_with_options(self, workspace_id, session_cluster_id, request, headers, runtime):
        """
        @summary Queries the information about a session.
        

        @param request: GetSessionClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/sessionClusters/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(session_cluster_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_session_cluster(self, workspace_id, session_cluster_id, request):
        """
        @summary Queries the information about a session.
        

        @param request: GetSessionClusterRequest

        @return: GetSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_session_cluster_with_options(workspace_id, session_cluster_id, request, headers, runtime)

    def get_sql_statement_with_options(self, workspace_id, statement_id, request, headers, runtime):
        """
        @summary Queries the status of an SQL query task.
        

        @param request: GetSqlStatementRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/statement/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(statement_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sql_statement(self, workspace_id, statement_id, request):
        """
        @summary Queries the status of an SQL query task.
        

        @param request: GetSqlStatementRequest

        @return: GetSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    def get_template_with_options(self, workspace_biz_id, request, headers, runtime):
        """
        @summary Queries task templates.
        

        @param request: GetTemplateRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.template_biz_id):
            query['templateBizId'] = request.template_biz_id
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/template' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, workspace_biz_id, request):
        """
        @summary Queries task templates.
        

        @param request: GetTemplateRequest

        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(workspace_biz_id, request, headers, runtime)

    def grant_role_to_users_with_options(self, request, headers, runtime):
        """
        @summary Assigns a specified role to users.
        

        @param request: GrantRoleToUsersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_role_to_users(self, request):
        """
        @summary Assigns a specified role to users.
        

        @param request: GrantRoleToUsersRequest

        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    def list_catalogs_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary 查看数据目录列表
        

        @param request: ListCatalogsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/catalogs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_catalogs(self, workspace_id, request):
        """
        @summary 查看数据目录列表
        

        @param request: ListCatalogsRequest

        @return: ListCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(workspace_id, request, headers, runtime)

    def list_job_executors_with_options(self, workspace_id, job_run_id, request, headers, runtime):
        """
        @summary 列出作业的executors
        

        @param request: ListJobExecutorsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListJobExecutorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.executor_type):
            query['executorType'] = request.executor_type
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobExecutors',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns/%s/executors' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_run_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job_executors(self, workspace_id, job_run_id, request):
        """
        @summary 列出作业的executors
        

        @param request: ListJobExecutorsRequest

        @return: ListJobExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_executors_with_options(workspace_id, job_run_id, request, headers, runtime)

    def list_job_runs_with_options(self, workspace_id, tmp_req, headers, runtime):
        """
        @summary Queries a list of Spark jobs.
        

        @param tmp_req: ListJobRunsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListJobRunsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['applicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.is_workflow):
            query['isWorkflow'] = request.is_workflow
        if not UtilClient.is_unset(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.runtime_configs):
            query['runtimeConfigs'] = request.runtime_configs
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job_runs(self, workspace_id, request):
        """
        @summary Queries a list of Spark jobs.
        

        @param request: ListJobRunsRequest

        @return: ListJobRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_runs_with_options(workspace_id, request, headers, runtime)

    def list_kyuubi_services_with_options(self, workspace_id, headers, runtime):
        """
        @summary ListKyuubiServices
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListKyuubiServicesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListKyuubiServices',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_kyuubi_services(self, workspace_id):
        """
        @summary ListKyuubiServices
        

        @return: ListKyuubiServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_services_with_options(workspace_id, headers, runtime)

    def list_kyuubi_spark_applications_with_options(self, workspace_id, kyuubi_service_id, tmp_req, headers, runtime):
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        

        @param tmp_req: ListKyuubiSparkApplicationsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListKyuubiSparkApplicationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'orderBy', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['applicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_name):
            query['applicationName'] = request.application_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_shrink):
            query['orderBy'] = request.order_by_shrink
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiSparkApplications',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s/applications' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_kyuubi_spark_applications(self, workspace_id, kyuubi_service_id, request):
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        

        @param request: ListKyuubiSparkApplicationsRequest

        @return: ListKyuubiSparkApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_spark_applications_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_kyuubi_token_with_options(self, workspace_id, kyuubi_service_id, request, headers, runtime):
        """
        @summary 列出compute的token
        

        @param request: ListKyuubiTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/kyuubiService/%s/token' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def list_kyuubi_token(self, workspace_id, kyuubi_service_id, request):
        """
        @summary 列出compute的token
        

        @param request: ListKyuubiTokenRequest

        @return: ListKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_token_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_livy_compute_with_options(self, workspace_biz_id, request, headers, runtime):
        """
        @summary 列出livy compute
        

        @param request: ListLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_livy_compute(self, workspace_biz_id, request):
        """
        @summary 列出livy compute
        

        @param request: ListLivyComputeRequest

        @return: ListLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    def list_livy_compute_token_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 列出livy compute token
        

        @param request: ListLivyComputeTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/token' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def list_livy_compute_token(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 列出livy compute token
        

        @param request: ListLivyComputeTokenRequest

        @return: ListLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def list_log_contents_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Get Log Content
        

        @param request: ListLogContentsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.length):
            query['length'] = request.length
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogContents',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/action/listLogContents' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLogContentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_log_contents(self, workspace_id, request):
        """
        @summary Get Log Content
        

        @param request: ListLogContentsRequest

        @return: ListLogContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_contents_with_options(workspace_id, request, headers, runtime)

    def list_members_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary 查询用户列表
        

        @param request: ListMembersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/auth/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_members(self, workspace_id, request):
        """
        @summary 查询用户列表
        

        @param request: ListMembersRequest

        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_members_with_options(workspace_id, request, headers, runtime)

    def list_release_versions_with_options(self, request, headers, runtime):
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        

        @param request: ListReleaseVersionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_type):
            query['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.release_version):
            query['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        if not UtilClient.is_unset(request.service_filter):
            query['serviceFilter'] = request.service_filter
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/releaseVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_release_versions(self, request):
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        

        @param request: ListReleaseVersionsRequest

        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_release_versions_with_options(request, headers, runtime)

    def list_session_clusters_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Queries the list of sessions.
        

        @param request: ListSessionClustersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSessionClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.queue_name):
            query['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/sessionClusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_session_clusters(self, workspace_id, request):
        """
        @summary Queries the list of sessions.
        

        @param request: ListSessionClustersRequest

        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_session_clusters_with_options(workspace_id, request, headers, runtime)

    def list_sql_statement_contents_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary 获取sql statement内容
        

        @param request: ListSqlStatementContentsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSqlStatementContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSqlStatementContents',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/action/listSqlStatementContents' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSqlStatementContentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sql_statement_contents(self, workspace_id, request):
        """
        @summary 获取sql statement内容
        

        @param request: ListSqlStatementContentsRequest

        @return: ListSqlStatementContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sql_statement_contents_with_options(workspace_id, request, headers, runtime)

    def list_template_with_options(self, workspace_biz_id, request, headers, runtime):
        """
        @summary 获取任务模板列表
        

        @param request: ListTemplateRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplate',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/template/listing' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_template(self, workspace_biz_id, request):
        """
        @summary 获取任务模板列表
        

        @param request: ListTemplateRequest

        @return: ListTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_template_with_options(workspace_biz_id, request, headers, runtime)

    def list_workspace_queues_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Queries the list of queues in a Spark workspace.
        

        @param request: ListWorkspaceQueuesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListWorkspaceQueuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceQueues',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/queues' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workspace_queues(self, workspace_id, request):
        """
        @summary Queries the list of queues in a Spark workspace.
        

        @param request: ListWorkspaceQueuesRequest

        @return: ListWorkspaceQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspace_queues_with_options(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(self, tmp_req, headers, runtime):
        """
        @summary Queries a list of workspaces.
        

        @param tmp_req: ListWorkspacesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workspaces(self, request):
        """
        @summary Queries a list of workspaces.
        

        @param request: ListWorkspacesRequest

        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    def refresh_livy_compute_token_with_options(self, workspace_biz_id, livy_compute_id, token_id, request, headers, runtime):
        """
        @summary 更新Livy Compute的token
        

        @param request: RefreshLivyComputeTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefreshLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_livy_compute_token(self, workspace_biz_id, livy_compute_id, token_id, request):
        """
        @summary 更新Livy Compute的token
        

        @param request: RefreshLivyComputeTokenRequest

        @return: RefreshLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def start_job_run_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Starts a Spark job.
        

        @param request: StartJobRunRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def start_job_run(self, workspace_id, request):
        """
        @summary Starts a Spark job.
        

        @param request: StartJobRunRequest

        @return: StartJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_job_run_with_options(workspace_id, request, headers, runtime)

    def start_kyuubi_service_with_options(self, workspace_id, kyuubi_service_id, headers, runtime):
        """
        @summary StartKyuubiService
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartKyuubiServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s/start' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_kyuubi_service(self, workspace_id, kyuubi_service_id):
        """
        @summary StartKyuubiService
        

        @return: StartKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    def start_livy_compute_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 启动livy compute
        

        @param request: StartLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/start' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def start_livy_compute(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 启动livy compute
        

        @param request: StartLivyComputeRequest

        @return: StartLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def start_process_instance_with_options(self, biz_id, request, headers, runtime):
        """
        @summary Manually runs a workflow.
        

        @param request: StartProcessInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartProcessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.comments):
            query['comments'] = request.comments
        if not UtilClient.is_unset(request.email):
            query['email'] = request.email
        if not UtilClient.is_unset(request.interval):
            query['interval'] = request.interval
        if not UtilClient.is_unset(request.is_prod):
            query['isProd'] = request.is_prod
        if not UtilClient.is_unset(request.process_definition_code):
            query['processDefinitionCode'] = request.process_definition_code
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.runtime_queue):
            query['runtimeQueue'] = request.runtime_queue
        if not UtilClient.is_unset(request.version_hash_code):
            query['versionHashCode'] = request.version_hash_code
        if not UtilClient.is_unset(request.version_number):
            query['versionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartProcessInstance',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/dolphinscheduler/projects/%s/executors/start-process-instance' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(biz_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartProcessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_process_instance(self, biz_id, request):
        """
        @summary Manually runs a workflow.
        

        @param request: StartProcessInstanceRequest

        @return: StartProcessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_process_instance_with_options(biz_id, request, headers, runtime)

    def start_session_cluster_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Starts a session.
        

        @param request: StartSessionClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/sessionClusters/action/startSessionCluster' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def start_session_cluster(self, workspace_id, request):
        """
        @summary Starts a session.
        

        @param request: StartSessionClusterRequest

        @return: StartSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_session_cluster_with_options(workspace_id, request, headers, runtime)

    def stop_kyuubi_service_with_options(self, workspace_id, kyuubi_service_id, headers, runtime):
        """
        @summary StopKyuubiService
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopKyuubiServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_kyuubi_service(self, workspace_id, kyuubi_service_id):
        """
        @summary StopKyuubiService
        

        @return: StopKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    def stop_livy_compute_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 停止livy compute
        

        @param request: StopLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_livy_compute(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 停止livy compute
        

        @param request: StopLivyComputeRequest

        @return: StopLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def stop_session_cluster_with_options(self, workspace_id, request, headers, runtime):
        """
        @summary Stops a session.
        

        @param request: StopSessionClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/sessionClusters/action/stopSessionCluster' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_session_cluster(self, workspace_id, request):
        """
        @summary Stops a session.
        

        @param request: StopSessionClusterRequest

        @return: StopSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_session_cluster_with_options(workspace_id, request, headers, runtime)

    def terminate_sql_statement_with_options(self, workspace_id, statement_id, request, headers, runtime):
        """
        @summary Terminates an SQL query task.
        

        @param request: TerminateSqlStatementRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TerminateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/statement/%s/terminate' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(statement_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.TerminateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_sql_statement(self, workspace_id, statement_id, request):
        """
        @summary Terminates an SQL query task.
        

        @param request: TerminateSqlStatementRequest

        @return: TerminateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    def update_kyuubi_service_with_options(self, workspace_id, kyuubi_service_id, request, headers, runtime):
        """
        @summary UpdateKyuubiService
        

        @param request: UpdateKyuubiServiceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKyuubiServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not UtilClient.is_unset(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not UtilClient.is_unset(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.queue):
            body['queue'] = request.queue
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        if not UtilClient.is_unset(request.restart):
            body['restart'] = request.restart
        if not UtilClient.is_unset(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKyuubiService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/kyuubi/%s/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_kyuubi_service(self, workspace_id, kyuubi_service_id, request):
        """
        @summary UpdateKyuubiService
        

        @param request: UpdateKyuubiServiceRequest

        @return: UpdateKyuubiServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kyuubi_service_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    def update_kyuubi_token_with_options(self, workspace_id, kyuubi_service_id, token_id, request, headers, runtime):
        """
        @summary 更新kyuubi的token
        

        @param request: UpdateKyuubiTokenRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/kyuubiService/%s/token/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(kyuubi_service_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def update_kyuubi_token(self, workspace_id, kyuubi_service_id, token_id, request):
        """
        @summary 更新kyuubi的token
        

        @param request: UpdateKyuubiTokenRequest

        @return: UpdateKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def update_livy_compute_with_options(self, workspace_biz_id, livy_compute_id, request, headers, runtime):
        """
        @summary 更新livy compute
        

        @param request: UpdateLivyComputeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/interactive/v1/workspace/%s/livycompute/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(livy_compute_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_livy_compute(self, workspace_biz_id, livy_compute_id, request):
        """
        @summary 更新livy compute
        

        @param request: UpdateLivyComputeRequest

        @return: UpdateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def update_process_definition_with_schedule_with_options(self, biz_id, code, tmp_req, headers, runtime):
        """
        @summary Updates the workflow and time-based scheduling configurations.
        

        @param tmp_req: UpdateProcessDefinitionWithScheduleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_state):
            query['releaseState'] = request.release_state
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/dolphinscheduler/projects/%s/process-definition/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(biz_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(code))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_process_definition_with_schedule(self, biz_id, code, request):
        """
        @summary Updates the workflow and time-based scheduling configurations.
        

        @param request: UpdateProcessDefinitionWithScheduleRequest

        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_process_definition_with_schedule_with_options(biz_id, code, request, headers, runtime)
