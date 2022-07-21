# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pai_dlc20201203 import models as pai_dlc_20201203_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('pai-dlc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_code_source(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_code_source_with_options(request, headers, runtime)

    def create_code_source_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/codesources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_source_with_options(request, headers, runtime)

    def create_data_source_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    def create_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.debugger_config_content):
            body['DebuggerConfigContent'] = request.debugger_config_content
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        if not UtilClient.is_unset(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.settings):
            body['Settings'] = request.settings
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tensorboard(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tensorboard_with_options(request, headers, runtime)

    def create_tensorboard_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_running_time_minutes):
            body['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_code_source(self, code_source_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_code_source_with_options(code_source_id, headers, runtime)

    def delete_code_source_with_options(self, code_source_id, headers, runtime):
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/codesources/%s' % TeaConverter.to_unicode(code_source_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source(self, data_source_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_source_with_options(data_source_id, headers, runtime)

    def delete_data_source_with_options(self, data_source_id, headers, runtime):
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/datasources/%s' % TeaConverter.to_unicode(data_source_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_job(self, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(job_id, headers, runtime)

    def delete_job_with_options(self, job_id, headers, runtime):
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_jobs_with_options(request, headers, runtime)

    def delete_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/batch/jobs/delete',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def delete_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    def get_code_source(self, code_source_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_source_with_options(code_source_id, headers, runtime)

    def get_code_source_with_options(self, code_source_id, headers, runtime):
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/codesources/%s' % TeaConverter.to_unicode(code_source_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source(self, data_source_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_with_options(data_source_id, headers, runtime)

    def get_data_source_with_options(self, data_source_id, headers, runtime):
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/datasources/%s' % TeaConverter.to_unicode(data_source_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job(self, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, headers, runtime)

    def get_job_with_options(self, job_id, headers, runtime):
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_events(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_events_with_options(job_id, request, headers, runtime)

    def get_job_events_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s/events' % TeaConverter.to_unicode(job_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_metrics(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_metrics_with_options(job_id, request, headers, runtime)

    def get_job_metrics_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobMetrics',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s/metrics' % TeaConverter.to_unicode(job_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pod_events(self, job_id, pod_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_events_with_options(job_id, pod_id, request, headers, runtime)

    def get_pod_events_with_options(self, job_id, pod_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s/pods/%s/events' % (TeaConverter.to_unicode(job_id), TeaConverter.to_unicode(pod_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pod_logs(self, job_id, pod_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_logs_with_options(job_id, pod_id, request, headers, runtime)

    def get_pod_logs_with_options(self, job_id, pod_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodLogs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s/pods/%s/logs' % (TeaConverter.to_unicode(job_id), TeaConverter.to_unicode(pod_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def get_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    def list_code_sources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_code_sources_with_options(request, headers, runtime)

    def list_code_sources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/codesources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(request, headers, runtime)

    def list_data_sources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ecs_specs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    def list_ecs_specs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    def list_images_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    def list_jobs_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_all_workspaces):
            query['FromAllWorkspaces'] = request.from_all_workspaces
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tensorboards(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tensorboards_with_options(request, headers, runtime)

    def list_tensorboards_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTensorboards',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListTensorboardsResponse(),
            self.call_api(params, req, runtime)
        )

    def start_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def start_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards/%s/start' % TeaConverter.to_unicode(tensorboard_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StartTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_job(self, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    def stop_job_with_options(self, job_id, headers, runtime):
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s/stop' % TeaConverter.to_unicode(job_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_jobs_with_options(request, headers, runtime)

    def stop_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/batch/jobs/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def stop_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards/%s/stop' % TeaConverter.to_unicode(tensorboard_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    def update_job(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(job_id, request, headers, runtime)

    def update_job_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        body = {}
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def update_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname='/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )
