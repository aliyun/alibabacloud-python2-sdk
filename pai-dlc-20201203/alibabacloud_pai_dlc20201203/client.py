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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('pai-dlc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            self.do_roarequest('ListDataSources', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/datasources', 'json', req, runtime)
        )

    def get_jobs_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_jobs_statistics_with_options(request, headers, runtime)

    def get_jobs_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobsStatisticsResponse(),
            self.do_roarequest('GetJobsStatistics', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/statistics/jobs', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            self.do_roarequest('GetDataSource', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/datasources/%s' % TeaConverter.to_unicode(data_source_id), 'json', req, runtime)
        )

    def create_quota(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_with_options(request, headers, runtime)

    def create_quota_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_type):
            body['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.quota_detail):
            body['QuotaDetail'] = request.quota_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateQuotaResponse(),
            self.do_roarequest('CreateQuota', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/quotas', 'json', req, runtime)
        )

    def get_quota(self, quota_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(quota_id, headers, runtime)

    def get_quota_with_options(self, quota_id, headers, runtime):
        quota_id = OpenApiUtilClient.get_encode_param(quota_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetQuotaResponse(),
            self.do_roarequest('GetQuota', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/quotas/%s' % TeaConverter.to_unicode(quota_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            self.do_roarequest('GetCodeSource', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/codesources/%s' % TeaConverter.to_unicode(code_source_id), 'json', req, runtime)
        )

    def get_switch(self, switch_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_switch_with_options(switch_id, headers, runtime)

    def get_switch_with_options(self, switch_id, headers, runtime):
        switch_id = OpenApiUtilClient.get_encode_param(switch_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSwitchResponse(),
            self.do_roarequest('GetSwitch', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/switches/%s' % TeaConverter.to_unicode(switch_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            self.do_roarequest('GetPodEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s/pods/%s/events' % (TeaConverter.to_unicode(job_id), TeaConverter.to_unicode(pod_id)), 'json', req, runtime)
        )

    def list_switches(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_switches_with_options(request, headers, runtime)

    def list_switches_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSwitchesResponse(),
            self.do_roarequest('ListSwitches', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/switches', 'json', req, runtime)
        )

    def list_tensorboards(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tensorboards_with_options(request, headers, runtime)

    def list_tensorboards_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListTensorboardsResponse(),
            self.do_roarequest('ListTensorboards', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/tensorboards', 'json', req, runtime)
        )

    def list_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_security_groups_with_options(request, headers, runtime)

    def list_security_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSecurityGroupsResponse(),
            self.do_roarequest('ListSecurityGroups', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/securitygroups', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            self.do_roarequest('GetPodLogs', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s/pods/%s/logs' % (TeaConverter.to_unicode(job_id), TeaConverter.to_unicode(pod_id)), 'json', req, runtime)
        )

    def list_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpcs_with_options(request, headers, runtime)

    def list_vpcs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListVpcsResponse(),
            self.do_roarequest('ListVpcs', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/vpcs', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopTensorboardResponse(),
            self.do_roarequest('StopTensorboard', '2020-12-03', 'HTTPS', 'PUT', 'AK', '/api/v1/tensorboards/%s/stop' % TeaConverter.to_unicode(tensorboard_id), 'json', req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    def create_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        if not UtilClient.is_unset(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.settings):
            body['Settings'] = request.settings
        if not UtilClient.is_unset(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            self.do_roarequest('CreateJob', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/jobs', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            self.do_roarequest('ListCodeSources', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/codesources', 'json', req, runtime)
        )

    def job_dispatch_submit(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.job_dispatch_submit_with_options(request, headers, runtime)

    def job_dispatch_submit_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algo_name):
            body['AlgoName'] = request.algo_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.properties):
            body['Properties'] = request.properties
        if not UtilClient.is_unset(request.settings):
            body['Settings'] = request.settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.JobDispatchSubmitResponse(),
            self.do_roarequest('JobDispatchSubmit', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/jobdispatch', 'json', req, runtime)
        )

    def list_ecs_specs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    def list_ecs_specs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            self.do_roarequest('ListEcsSpecs', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/ecsspecs', 'json', req, runtime)
        )

    def delete_quota(self, quota_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_with_options(quota_id, headers, runtime)

    def delete_quota_with_options(self, quota_id, headers, runtime):
        quota_id = OpenApiUtilClient.get_encode_param(quota_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteQuotaResponse(),
            self.do_roarequest('DeleteQuota', '2020-12-03', 'HTTPS', 'DELETE', 'AK', '/api/v1/quotas/%s' % TeaConverter.to_unicode(quota_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.StartTensorboardResponse(),
            self.do_roarequest('StartTensorboard', '2020-12-03', 'HTTPS', 'PUT', 'AK', '/api/v1/tensorboards/%s/start' % TeaConverter.to_unicode(tensorboard_id), 'json', req, runtime)
        )

    def get_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def get_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardResponse(),
            self.do_roarequest('GetTensorboard', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id), 'json', req, runtime)
        )

    def get_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    def get_workspace_with_options(self, workspace_id, headers, runtime):
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetWorkspaceResponse(),
            self.do_roarequest('GetWorkspace', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/workspaces/%s' % TeaConverter.to_unicode(workspace_id), 'json', req, runtime)
        )

    def job_dispatch_query(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.job_dispatch_query_with_options(request, headers, runtime)

    def job_dispatch_query_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.JobDispatchQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        if not UtilClient.is_unset(tmp_req.settings):
            request.settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not UtilClient.is_unset(request.algo_name):
            query['AlgoName'] = request.algo_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.properties_shrink):
            query['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.settings_shrink):
            query['Settings'] = request.settings_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.JobDispatchQueryResponse(),
            self.do_roarequest('JobDispatchQuery', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobdispatch', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            self.do_roarequest('ListJobs', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs', 'json', req, runtime)
        )

    def get_vpc(self, vpc_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vpc_with_options(vpc_id, headers, runtime)

    def get_vpc_with_options(self, vpc_id, headers, runtime):
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetVpcResponse(),
            self.do_roarequest('GetVpc', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/vpcs/%s' % TeaConverter.to_unicode(vpc_id), 'json', req, runtime)
        )

    def create_code_source(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_code_source_with_options(request, headers, runtime)

    def create_code_source_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            self.do_roarequest('CreateCodeSource', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/codesources', 'json', req, runtime)
        )

    def get_job_metrics(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_metrics_with_options(job_id, request, headers, runtime)

    def get_job_metrics_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobMetricsResponse(),
            self.do_roarequest('GetJobMetrics', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s/metrics' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            self.do_roarequest('GetJob', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
        )

    def batch_get_jobs_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_jobs_statistics_with_options(request, headers, runtime)

    def batch_get_jobs_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.BatchGetJobsStatisticsResponse(),
            self.do_roarequest('BatchGetJobsStatistics', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/batch/statistics/jobs', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            self.do_roarequest('CreateDataSource', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/datasources', 'json', req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    def list_images_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            self.do_roarequest('ListImages', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/images', 'json', req, runtime)
        )

    def get_security_group(self, security_group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_security_group_with_options(security_group_id, headers, runtime)

    def get_security_group_with_options(self, security_group_id, headers, runtime):
        security_group_id = OpenApiUtilClient.get_encode_param(security_group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSecurityGroupResponse(),
            self.do_roarequest('GetSecurityGroup', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/securitygroups/%s' % TeaConverter.to_unicode(security_group_id), 'json', req, runtime)
        )

    def get_user_authorization(self, user_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_authorization_with_options(user_id, headers, runtime)

    def get_user_authorization_with_options(self, user_id, headers, runtime):
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetUserAuthorizationResponse(),
            self.do_roarequest('GetUserAuthorization', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/users/%s/authorization' % TeaConverter.to_unicode(user_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteTensorboardResponse(),
            self.do_roarequest('DeleteTensorboard', '2020-12-03', 'HTTPS', 'DELETE', 'AK', '/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            self.do_roarequest('StopJob', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/jobs/%s/stop' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
        )

    def get_job_events(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_events_with_options(job_id, request, headers, runtime)

    def get_job_events_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            self.do_roarequest('GetJobEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s/events' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobResponse(),
            self.do_roarequest('DeleteJob', '2020-12-03', 'HTTPS', 'DELETE', 'AK', '/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            self.do_roarequest('DeleteCodeSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', '/api/v1/codesources/%s' % TeaConverter.to_unicode(code_source_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            self.do_roarequest('DeleteDataSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', '/api/v1/datasources/%s' % TeaConverter.to_unicode(data_source_id), 'json', req, runtime)
        )

    def list_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    def list_workspaces_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_detail):
            query['NeedDetail'] = request.need_detail
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListWorkspacesResponse(),
            self.do_roarequest('ListWorkspaces', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/workspaces', 'json', req, runtime)
        )

    def get_token(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    def get_token_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTokenResponse(),
            self.do_roarequest('GetToken', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/tokens', 'json', req, runtime)
        )

    def get_authorization(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_authorization_with_options(headers, runtime)

    def get_authorization_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetAuthorizationResponse(),
            self.do_roarequest('GetAuthorization', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/authorization', 'json', req, runtime)
        )

    def list_quotas(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    def list_quotas_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListQuotasResponse(),
            self.do_roarequest('ListQuotas', '2020-12-03', 'HTTPS', 'GET', 'AK', '/api/v1/quotas', 'json', req, runtime)
        )

    def create_tensorboard(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tensorboard_with_options(request, headers, runtime)

    def create_tensorboard_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateTensorboardResponse(),
            self.do_roarequest('CreateTensorboard', '2020-12-03', 'HTTPS', 'POST', 'AK', '/api/v1/tensorboards', 'json', req, runtime)
        )

    def update_tensorboard(self, tensorboard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    def update_tensorboard_with_options(self, tensorboard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateTensorboardResponse(),
            self.do_roarequest('UpdateTensorboard', '2020-12-03', 'HTTPS', 'PUT', 'AK', '/api/v1/tensorboards/%s' % TeaConverter.to_unicode(tensorboard_id), 'json', req, runtime)
        )

    def update_quota(self, quota_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(quota_id, request, headers, runtime)

    def update_quota_with_options(self, quota_id, request, headers, runtime):
        UtilClient.validate_model(request)
        quota_id = OpenApiUtilClient.get_encode_param(quota_id)
        body = {}
        if not UtilClient.is_unset(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_type):
            body['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.quota_detail):
            body['QuotaDetail'] = request.quota_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateQuotaResponse(),
            self.do_roarequest('UpdateQuota', '2020-12-03', 'HTTPS', 'PUT', 'AK', '/api/v1/quotas/%s' % TeaConverter.to_unicode(quota_id), 'json', req, runtime)
        )
