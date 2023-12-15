# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nas20170626 import models as nas20170626_models
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
            'cn-chengdu': 'nas.aliyuncs.com',
            'me-east-1': 'nas.ap-northeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'nas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('nas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_client_to_black_list_with_options(self, request, runtime):
        """
        The API operation is available only for CPFS file systems.
        

        @param request: AddClientToBlackListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddClientToBlackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientToBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_client_to_black_list(self, request):
        """
        The API operation is available only for CPFS file systems.
        

        @param request: AddClientToBlackListRequest

        @return: AddClientToBlackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_client_to_black_list_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        """
        ## Limits
        *   Each tag includes a TagKey and a TagValue.
        *   Placeholders at the start and end of each TagKey and TagValue are automatically removed. These placeholders include the spacebar ( ), tab (\\t), line break (\\n), and carriage return (\\r).
        *   You must specify a TagKey. You can leave a TagValue empty.
        *   A TagKey and TagValue are not case-sensitive.
        *   A TagKey can be a maximum of 64 characters in length. A TagValue can be a maximum of 128 characters in length.
        *   You can add a maximum of 10 tags to a file system at a time. If you add two tags with the same TagKey, the new tag added will overwrite the existing tag.
        *   If you remove a tag from all linked file systems, the tag is automatically deleted.
        

        @param request: AddTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags(self, request):
        """
        ## Limits
        *   Each tag includes a TagKey and a TagValue.
        *   Placeholders at the start and end of each TagKey and TagValue are automatically removed. These placeholders include the spacebar ( ), tab (\\t), line break (\\n), and carriage return (\\r).
        *   You must specify a TagKey. You can leave a TagValue empty.
        *   A TagKey and TagValue are not case-sensitive.
        *   A TagKey can be a maximum of 64 characters in length. A TagValue can be a maximum of 128 characters in length.
        *   You can add a maximum of 10 tags to a file system at a time. If you add two tags with the same TagKey, the new tag added will overwrite the existing tag.
        *   If you remove a tag from all linked file systems, the tag is automatically deleted.
        

        @param request: AddTagsRequest

        @return: AddTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def apply_auto_snapshot_policy_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   You can apply only one automatic snapshot policy to each file system.
        *   Each automatic snapshot policy can be applied to multiple file systems.
        *   If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        

        @param request: ApplyAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_auto_snapshot_policy(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   You can apply only one automatic snapshot policy to each file system.
        *   Each automatic snapshot policy can be applied to multiple file systems.
        *   If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        

        @param request: ApplyAutoSnapshotPolicyRequest

        @return: ApplyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    def apply_data_flow_auto_refresh_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        *   You can add a maximum of five AutoRefresh configurations to a dataflow.
        *   It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](~~336901~~) operation to query the dataflow status.
        *   AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](~~182246~~).
        **\
        **Note** The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        *   The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        *   After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        *   AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        

        @param request: ApplyDataFlowAutoRefreshRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_data_flow_auto_refresh(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        *   You can add a maximum of five AutoRefresh configurations to a dataflow.
        *   It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](~~336901~~) operation to query the dataflow status.
        *   AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](~~182246~~).
        **\
        **Note** The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        *   The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        *   After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        *   AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        

        @param request: ApplyDataFlowAutoRefreshRequest

        @return: ApplyDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_data_flow_auto_refresh_with_options(request, runtime)

    def cancel_auto_snapshot_policy_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: CancelAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: CancelAutoSnapshotPolicyRequest

        @return: CancelAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    def cancel_data_flow_auto_refresh_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        *   It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](~~336901~~) operation to query the status of the AutoRefresh tasks.
        

        @param request: CancelDataFlowAutoRefreshRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.refresh_path):
            query['RefreshPath'] = request.refresh_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_data_flow_auto_refresh(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        *   It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](~~336901~~) operation to query the status of the AutoRefresh tasks.
        

        @param request: CancelDataFlowAutoRefreshRequest

        @return: CancelDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_data_flow_auto_refresh_with_options(request, runtime)

    def cancel_data_flow_task_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflow tasks. You can view the version information on the file system details page in the console.
        *   You can cancel only the dataflow tasks that are in the `Pending` and `Executing` states.
        *   It generally takes 5 to 10 minutes to cancel a dataflow task. You can query the task execution status by calling the [DescribeDataFlowTasks](~~2402275~~) operation.
        

        @param request: CancelDataFlowTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_data_flow_task(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflow tasks. You can view the version information on the file system details page in the console.
        *   You can cancel only the dataflow tasks that are in the `Pending` and `Executing` states.
        *   It generally takes 5 to 10 minutes to cancel a dataflow task. You can query the task execution status by calling the [DescribeDataFlowTasks](~~2402275~~) operation.
        

        @param request: CancelDataFlowTaskRequest

        @return: CancelDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_data_flow_task_with_options(request, runtime)

    def cancel_dir_quota_with_options(self, request, runtime):
        """
        Only General-purpose file systems support the directory quota feature.
        

        @param request: CancelDirQuotaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_dir_quota(self, request):
        """
        Only General-purpose file systems support the directory quota feature.
        

        @param request: CancelDirQuotaRequest

        @return: CancelDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_dir_quota_with_options(request, runtime)

    def cancel_lifecycle_retrieve_job_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: CancelLifecycleRetrieveJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_lifecycle_retrieve_job(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: CancelLifecycleRetrieveJobRequest

        @return: CancelLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_lifecycle_retrieve_job_with_options(request, runtime)

    def cancel_recycle_bin_job_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        *   If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        *   If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        

        @param request: CancelRecycleBinJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelRecycleBinJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRecycleBinJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelRecycleBinJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_recycle_bin_job(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        *   If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        *   If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        

        @param request: CancelRecycleBinJobRequest

        @return: CancelRecycleBinJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_recycle_bin_job_with_options(request, runtime)

    def create_access_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_group_type):
            query['AccessGroupType'] = request.access_group_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    def create_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    def create_auto_snapshot_policy_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        *   If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        *   A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        *   If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        *   If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        *   You can only apply automatic snapshot policies to a file system that is in the Running state.
        *   All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        *   After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        

        @param request: CreateAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_snapshot_policy(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        *   If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        *   A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        *   If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        *   If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        *   You can only apply automatic snapshot policies to a file system that is in the Running state.
        *   All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        *   After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        

        @param request: CreateAutoSnapshotPolicyRequest

        @return: CreateAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    def create_data_flow_with_options(self, request, runtime):
        """
        Billing
        *   If you create a dataflow, you are charged for using the dataflow throughput. For more information, see [Billing methods and billable items of CPFS](~~111858~~).
        *   When you configure the AutoRefresh feature for a dataflow, CPFS must use EventBridge to collect object modification events from the source Object Storage Service (OSS) bucket. Event fees are incurred. For more information, see [Billing of EventBridge](~~163752~~).
        *   Dataflow specifications
        *   The dataflow throughput supports the following specifications: 600 MB/s, 1,200 MB/s, and 1,500 MB/s. The dataflow throughput is the maximum transmission bandwidth that can be reached when data is imported or exported for a dataflow.
        *   When you create a dataflow, the vSwitch IP addresses used by a CPFS mount target are consumed. Make sure that the vSwitch can provide sufficient IP addresses.
        *   Inventory query: If you set the DryRun parameter to true, you can check whether the resources for the dataflow whose throughput is changed meet the requirements.
        *   Fileset
        *   The destination for a dataflow is a fileset in the CPFS file system. A fileset is a new directory tree structure (a small file directory) in a CPFS file system. Each fileset independently manages an inode space.
        *   When you create a dataflow, the related fileset must already exist and cannot be nested with other filesets. Only one dataflow can be created in a fileset, which corresponds to one source storage.
        *   A fileset supports a maximum of one million files. If the number of files imported from an OSS bucket into the fileset exceeds the upper limit, the `no space` error message is returned when you add new files.
        **\
        **Note** If data already exists in the fileset, after you create a dataflow, the existing data in the fileset is cleared and replaced with the data synchronized from the OSS bucket.
        *   Source storage
        *   The source storage is an OSS bucket. SourceStorage for a dataflow must be an OSS bucket. The prefix of an OSS bucket is not supported.
        *   CPFS dataflows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        *   If dataflows for multiple CPFS file systems or multiple dataflows for the same CPFS file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS file systems to one OSS bucket.
        *   Dataflows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        **\
        **Note** Before you create a dataflow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created dataflow can access the data in the OSS bucket. When a dataflow is being used, do not delete or modify the tag. Otherwise, the dataflow for CPFS cannot access the data in the OSS bucket.
        *   AutoRefresh
        *   After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        *   AutoRefresh depends on the object modification events collected by EventBridge from the source OSS bucket. You must first [activate EventBridge](~~182246~~).
        *   The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. You can configure a maximum of five AutoRefresh directories for a dataflow.
        *   AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes `Misconfigured`. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        *   When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        **\
        **Note** The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly
        *   Permissions
        When you create a dataflow, CPFS obtains two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](~~185138~~).
        *   Basic operations
        *   Only CPFS V2.2.0 and later support dataflows.
        *   You can create a dataflow only if the CPFS file system is in the Running state.
        *   A maximum of 10 dataflows can be created for a CPFS file system.
        *   It generally takes 2 to 5 minutes to create a dataflow. You can call the DescribeDataFlows operation to check whether the dataflow has been created.
        

        @param request: CreateDataFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.source_security_type):
            query['SourceSecurityType'] = request.source_security_type
        if not UtilClient.is_unset(request.source_storage):
            query['SourceStorage'] = request.source_storage
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_flow(self, request):
        """
        Billing
        *   If you create a dataflow, you are charged for using the dataflow throughput. For more information, see [Billing methods and billable items of CPFS](~~111858~~).
        *   When you configure the AutoRefresh feature for a dataflow, CPFS must use EventBridge to collect object modification events from the source Object Storage Service (OSS) bucket. Event fees are incurred. For more information, see [Billing of EventBridge](~~163752~~).
        *   Dataflow specifications
        *   The dataflow throughput supports the following specifications: 600 MB/s, 1,200 MB/s, and 1,500 MB/s. The dataflow throughput is the maximum transmission bandwidth that can be reached when data is imported or exported for a dataflow.
        *   When you create a dataflow, the vSwitch IP addresses used by a CPFS mount target are consumed. Make sure that the vSwitch can provide sufficient IP addresses.
        *   Inventory query: If you set the DryRun parameter to true, you can check whether the resources for the dataflow whose throughput is changed meet the requirements.
        *   Fileset
        *   The destination for a dataflow is a fileset in the CPFS file system. A fileset is a new directory tree structure (a small file directory) in a CPFS file system. Each fileset independently manages an inode space.
        *   When you create a dataflow, the related fileset must already exist and cannot be nested with other filesets. Only one dataflow can be created in a fileset, which corresponds to one source storage.
        *   A fileset supports a maximum of one million files. If the number of files imported from an OSS bucket into the fileset exceeds the upper limit, the `no space` error message is returned when you add new files.
        **\
        **Note** If data already exists in the fileset, after you create a dataflow, the existing data in the fileset is cleared and replaced with the data synchronized from the OSS bucket.
        *   Source storage
        *   The source storage is an OSS bucket. SourceStorage for a dataflow must be an OSS bucket. The prefix of an OSS bucket is not supported.
        *   CPFS dataflows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        *   If dataflows for multiple CPFS file systems or multiple dataflows for the same CPFS file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS file systems to one OSS bucket.
        *   Dataflows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        **\
        **Note** Before you create a dataflow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created dataflow can access the data in the OSS bucket. When a dataflow is being used, do not delete or modify the tag. Otherwise, the dataflow for CPFS cannot access the data in the OSS bucket.
        *   AutoRefresh
        *   After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        *   AutoRefresh depends on the object modification events collected by EventBridge from the source OSS bucket. You must first [activate EventBridge](~~182246~~).
        *   The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. You can configure a maximum of five AutoRefresh directories for a dataflow.
        *   AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes `Misconfigured`. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        *   When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        **\
        **Note** The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly
        *   Permissions
        When you create a dataflow, CPFS obtains two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](~~185138~~).
        *   Basic operations
        *   Only CPFS V2.2.0 and later support dataflows.
        *   You can create a dataflow only if the CPFS file system is in the Running state.
        *   A maximum of 10 dataflows can be created for a CPFS file system.
        *   It generally takes 2 to 5 minutes to create a dataflow. You can call the DescribeDataFlows operation to check whether the dataflow has been created.
        

        @param request: CreateDataFlowRequest

        @return: CreateDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_flow_with_options(request, runtime)

    def create_data_flow_task_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Dataflow tasks can be created only in CPFS V2.2.0 and later. You can view the version information on the file system details page in the console.
        *   You can create a dataflow task only for a dataflow that is in the Running state.
        *   Dataflow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](~~336914~~) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        *   When you manually run a dataflow task, the automatic data update task for the dataflow is interrupted and enters the pending state.
        

        @param request: CreateDataFlowTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directory):
            query['Directory'] = request.directory
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entry_list):
            query['EntryList'] = request.entry_list
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.src_task_id):
            query['SrcTaskId'] = request.src_task_id
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_flow_task(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Dataflow tasks can be created only in CPFS V2.2.0 and later. You can view the version information on the file system details page in the console.
        *   You can create a dataflow task only for a dataflow that is in the Running state.
        *   Dataflow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](~~336914~~) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        *   When you manually run a dataflow task, the automatic data update task for the dataflow is interrupted and enters the pending state.
        

        @param request: CreateDataFlowTaskRequest

        @return: CreateDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_flow_task_with_options(request, runtime)

    def create_file_with_options(self, request, runtime):
        """
        This operation is only available to some users.
        *   This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        

        @param request: CreateFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.owner_access_inheritable):
            query['OwnerAccessInheritable'] = request.owner_access_inheritable
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file(self, request):
        """
        This operation is only available to some users.
        *   This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        

        @param request: CreateFileRequest

        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    def create_file_system_with_options(self, request, runtime):
        """
        Before you call this operation, you must understand the billing and pricing of Apsara File Storage NAS. For more information, see [Billing](~~178365~~) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        *   Before you create a file system, you must complete real-name verification.
        *   When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](~~208530~~).
        

        @param request: CreateFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_system(self, request):
        """
        Before you call this operation, you must understand the billing and pricing of Apsara File Storage NAS. For more information, see [Billing](~~178365~~) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        *   Before you create a file system, you must complete real-name verification.
        *   When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](~~208530~~).
        

        @param request: CreateFileSystemRequest

        @return: CreateFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    def create_fileset_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset creation. You can view the version information on the file system details page in the console.
        *   A maximum of 10 filesets can be created for a CPFS file system.
        *   The maximum depth supported by a fileset is eight levels. The depth of the root directory / is 0 levels. For example, the /test/aaa/ccc/ fileset has three levels.
        *   Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset.
        *   A fileset supports a maximum of one million files. If the number of files exceeds the upper limit, the `no space` error message is returned when you add new files.
        

        @param request: CreateFilesetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_fileset(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset creation. You can view the version information on the file system details page in the console.
        *   A maximum of 10 filesets can be created for a CPFS file system.
        *   The maximum depth supported by a fileset is eight levels. The depth of the root directory / is 0 levels. For example, the /test/aaa/ccc/ fileset has three levels.
        *   Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset.
        *   A fileset supports a maximum of one million files. If the number of files exceeds the upper limit, the `no space` error message is returned when you add new files.
        

        @param request: CreateFilesetRequest

        @return: CreateFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_fileset_with_options(request, runtime)

    def create_ldapconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ldapconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ldapconfig_with_options(request, runtime)

    def create_lifecycle_policy_with_options(self, request, runtime):
        """
        You can create lifecycle policies only for General-purpose NAS file systems.
        *   You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        

        @param request: CreateLifecyclePolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_lifecycle_policy(self, request):
        """
        You can create lifecycle policies only for General-purpose NAS file systems.
        *   You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        

        @param request: CreateLifecyclePolicyRequest

        @return: CreateLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_policy_with_options(request, runtime)

    def create_lifecycle_retrieve_job_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        

        @param request: CreateLifecycleRetrieveJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_lifecycle_retrieve_job(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        

        @param request: CreateLifecycleRetrieveJobRequest

        @return: CreateLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_retrieve_job_with_options(request, runtime)

    def create_log_analysis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    def create_log_analysis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_log_analysis_with_options(request, runtime)

    def create_mount_target_with_options(self, request, runtime):
        """
        After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        *   When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](~~208530~~).
        

        @param request: CreateMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mount_target(self, request):
        """
        After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        *   When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](~~208530~~).
        

        @param request: CreateMountTargetRequest

        @return: CreateMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mount_target_with_options(request, runtime)

    def create_protocol_mount_target_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Prerequisites
        A protocol service is created.
        *   Others
        *   The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        *   The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        *   You can create a maximum of 10 export directories for a protocol service.
        *   When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        

        @param request: CreateProtocolMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_protocol_mount_target(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Prerequisites
        A protocol service is created.
        *   Others
        *   The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        *   The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        *   You can create a maximum of 10 export directories for a protocol service.
        *   When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        

        @param request: CreateProtocolMountTargetRequest

        @return: CreateProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_protocol_mount_target_with_options(request, runtime)

    def create_protocol_service_with_options(self, request, runtime):
        """
        This operation is available only to CPFS file systems on the China site (aliyun.com).
        *   Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        *   Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        *   General-purpose protocol services: provide NFS access and [directory-level mount targets](~~427175~~) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        *   Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](~~111858~~). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        *   Protocol type
        Only NFSv3 is supported.
        *   Others
        *   Only one protocol service can be created for a CPFS file system.
        *   A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        

        @param request: CreateProtocolServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_spec):
            query['ProtocolSpec'] = request.protocol_spec
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_protocol_service(self, request):
        """
        This operation is available only to CPFS file systems on the China site (aliyun.com).
        *   Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        *   Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        *   General-purpose protocol services: provide NFS access and [directory-level mount targets](~~427175~~) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        *   Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](~~111858~~). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        *   Protocol type
        Only NFSv3 is supported.
        *   Others
        *   Only one protocol service can be created for a CPFS file system.
        *   A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        

        @param request: CreateProtocolServiceRequest

        @return: CreateProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_protocol_service_with_options(request, runtime)

    def create_recycle_bin_delete_job_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   If you permanently delete a directory, the files in the directory are recursively cleared.
        *   You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        

        @param request: CreateRecycleBinDeleteJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRecycleBinDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinDeleteJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_recycle_bin_delete_job(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   If you permanently delete a directory, the files in the directory are recursively cleared.
        *   You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        

        @param request: CreateRecycleBinDeleteJobRequest

        @return: CreateRecycleBinDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_delete_job_with_options(request, runtime)

    def create_recycle_bin_restore_job_with_options(self, request, runtime):
        """
        ### Usage notes
        *   Only General-purpose NAS file systems support this operation.
        *   You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        *   You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        *   After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        

        @param request: CreateRecycleBinRestoreJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRecycleBinRestoreJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinRestoreJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_recycle_bin_restore_job(self, request):
        """
        ### Usage notes
        *   Only General-purpose NAS file systems support this operation.
        *   You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        *   You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        *   After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        

        @param request: CreateRecycleBinRestoreJobRequest

        @return: CreateRecycleBinRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_restore_job_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/zh/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support the snapshot feature.
        *   You can create a maximum of 128 snapshots for a file system.
        *   The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        *   You can create only one snapshot for a file system at a time.
        *   If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        *   When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        *   A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        *   Manually created snapshots will not be deleted until 15 days after the service is suspended due to an overdue payment. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        

        @param request: CreateSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/zh/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support the snapshot feature.
        *   You can create a maximum of 128 snapshots for a file system.
        *   The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        *   You can create only one snapshot for a file system at a time.
        *   If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        *   When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        *   A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        *   Manually created snapshots will not be deleted until 15 days after the service is suspended due to an overdue payment. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        

        @param request: CreateSnapshotRequest

        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def delete_access_group_with_options(self, request, runtime):
        """
        The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        

        @param request: DeleteAccessGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_group(self, request):
        """
        The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        

        @param request: DeleteAccessGroupRequest

        @return: DeleteAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    def delete_access_rule_with_options(self, request, runtime):
        """
        Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        

        @param request: DeleteAccessRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_rule(self, request):
        """
        Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        

        @param request: DeleteAccessRuleRequest

        @return: DeleteAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    def delete_auto_snapshot_policy_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        

        @param request: DeleteAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_snapshot_policy(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        

        @param request: DeleteAutoSnapshotPolicyRequest

        @return: DeleteAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    def delete_data_flow_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   You can create filesets only in CPFS V2.2.0 and later. You can view the version information on the file system details page in the console.
        *   You can delete the dataflows that are only in the `Running` or `Stopped` state.
        *   After a dataflow is deleted, the resources related to the dataflow are released and cannot be restored. You must create a dataflow again if required.
        

        @param request: DeleteDataFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_flow(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   You can create filesets only in CPFS V2.2.0 and later. You can view the version information on the file system details page in the console.
        *   You can delete the dataflows that are only in the `Running` or `Stopped` state.
        *   After a dataflow is deleted, the resources related to the dataflow are released and cannot be restored. You must create a dataflow again if required.
        

        @param request: DeleteDataFlowRequest

        @return: DeleteDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_flow_with_options(request, runtime)

    def delete_file_system_with_options(self, request, runtime):
        """
        Before you delete a file system, you must delete all mount targets of the file system.
        *   Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        *   After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        

        @param request: DeleteFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file_system(self, request):
        """
        Before you delete a file system, you must delete all mount targets of the file system.
        *   Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        *   After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        

        @param request: DeleteFileSystemRequest

        @return: DeleteFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    def delete_fileset_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset deletion. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        

        @param request: DeleteFilesetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_fileset(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset deletion. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        

        @param request: DeleteFilesetRequest

        @return: DeleteFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_fileset_with_options(request, runtime)

    def delete_ldapconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ldapconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ldapconfig_with_options(request, runtime)

    def delete_lifecycle_policy_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: DeleteLifecyclePolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_lifecycle_policy(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: DeleteLifecyclePolicyRequest

        @return: DeleteLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_policy_with_options(request, runtime)

    def delete_log_analysis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_log_analysis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_log_analysis_with_options(request, runtime)

    def delete_mount_target_with_options(self, request, runtime):
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        

        @param request: DeleteMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mount_target(self, request):
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        

        @param request: DeleteMountTargetRequest

        @return: DeleteMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mount_target_with_options(request, runtime)

    def delete_protocol_mount_target_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DeleteProtocolMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_protocol_mount_target(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DeleteProtocolMountTargetRequest

        @return: DeleteProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_protocol_mount_target_with_options(request, runtime)

    def delete_protocol_service_with_options(self, request, runtime):
        """
        This operation is available only to CPFS file systems on the China site (aliyun.com).
        *   When you delete a protocol service, the export directories in the protocol service are also deleted.
        

        @param request: DeleteProtocolServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_protocol_service(self, request):
        """
        This operation is available only to CPFS file systems on the China site (aliyun.com).
        *   When you delete a protocol service, the export directories in the protocol service are also deleted.
        

        @param request: DeleteProtocolServiceRequest

        @return: DeleteProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_protocol_service_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DeleteSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DeleteSnapshotRequest

        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def describe_access_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessGroups',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_groups_with_options(request, runtime)

    def describe_access_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessRules',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_rules_with_options(request, runtime)

    def describe_auto_snapshot_policies_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeAutoSnapshotPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAutoSnapshotPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_snapshot_policies(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeAutoSnapshotPoliciesRequest

        @return: DescribeAutoSnapshotPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policies_with_options(request, runtime)

    def describe_auto_snapshot_tasks_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeAutoSnapshotTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAutoSnapshotTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_ids):
            query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_snapshot_tasks(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeAutoSnapshotTasksRequest

        @return: DescribeAutoSnapshotTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_tasks_with_options(request, runtime)

    def describe_black_list_clients_with_options(self, request, runtime):
        """
        The API operation is available only for CPFS file systems.
        

        @param request: DescribeBlackListClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBlackListClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackListClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_black_list_clients(self, request):
        """
        The API operation is available only for CPFS file systems.
        

        @param request: DescribeBlackListClientsRequest

        @return: DescribeBlackListClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_black_list_clients_with_options(request, runtime)

    def describe_data_flow_tasks_with_options(self, request, runtime):
        """
        ###
        *\
        *\
        

        @param request: DescribeDataFlowTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataFlowTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlowTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_flow_tasks(self, request):
        """
        ###
        *\
        *\
        

        @param request: DescribeDataFlowTasksRequest

        @return: DescribeDataFlowTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_flow_tasks_with_options(request, runtime)

    def describe_data_flows_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath and Description support fuzzy match.
        *   Combined query is supported.
        

        @param request: DescribeDataFlowsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlows',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_flows(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath and Description support fuzzy match.
        *   Combined query is supported.
        

        @param request: DescribeDataFlowsRequest

        @return: DescribeDataFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_flows_with_options(request, runtime)

    def describe_dir_quotas_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support the directory quota feature.
        

        @param request: DescribeDirQuotasRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDirQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirQuotas',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dir_quotas(self, request):
        """
        Only General-purpose NAS file systems support the directory quota feature.
        

        @param request: DescribeDirQuotasRequest

        @return: DescribeDirQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dir_quotas_with_options(request, runtime)

    def describe_file_system_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystemStatistics',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_file_system_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_file_system_statistics_with_options(request, runtime)

    def describe_file_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_file_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_file_systems_with_options(request, runtime)

    def describe_filesets_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support filesets. You can view the version information on the file system details page in the console.
        *   In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        *   Combined query is supported.
        

        @param request: DescribeFilesetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFilesetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFilesets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFilesetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_filesets(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support filesets. You can view the version information on the file system details page in the console.
        *   In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        *   Combined query is supported.
        

        @param request: DescribeFilesetsRequest

        @return: DescribeFilesetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_filesets_with_options(request, runtime)

    def describe_lifecycle_policies_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: DescribeLifecyclePoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLifecyclePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecyclePolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lifecycle_policies(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: DescribeLifecyclePoliciesRequest

        @return: DescribeLifecyclePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_policies_with_options(request, runtime)

    def describe_log_analysis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_analysis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_analysis_with_options(request, runtime)

    def describe_mount_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mount_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mount_targets_with_options(request, runtime)

    def describe_mounted_clients_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        

        @param request: DescribeMountedClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMountedClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountedClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mounted_clients(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        

        @param request: DescribeMountedClientsRequest

        @return: DescribeMountedClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mounted_clients_with_options(request, runtime)

    def describe_nfs_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nfs_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nfs_acl_with_options(request, runtime)

    def describe_protocol_mount_target_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DescribeProtocolMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_protocol_mount_target(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DescribeProtocolMountTargetRequest

        @return: DescribeProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protocol_mount_target_with_options(request, runtime)

    def describe_protocol_service_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DescribeProtocolServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_protocol_service(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: DescribeProtocolServiceRequest

        @return: DescribeProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protocol_service_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_smb_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_smb_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_smb_acl_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeSnapshotsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshots(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: DescribeSnapshotsRequest

        @return: DescribeSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_storage_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStoragePackages',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_storage_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_packages_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def disable_and_clean_recycle_bin_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        *   If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        

        @param request: DisableAndCleanRecycleBinRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableAndCleanRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAndCleanRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableAndCleanRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_and_clean_recycle_bin(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        *   If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        

        @param request: DisableAndCleanRecycleBinRequest

        @return: DisableAndCleanRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_and_clean_recycle_bin_with_options(request, runtime)

    def disable_nfs_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_nfs_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_nfs_acl_with_options(request, runtime)

    def disable_smb_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_smb_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_smb_acl_with_options(request, runtime)

    def enable_nfs_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_nfs_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_nfs_acl_with_options(request, runtime)

    def enable_recycle_bin_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: EnableRecycleBinRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.reserved_days):
            query['ReservedDays'] = request.reserved_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_recycle_bin(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: EnableRecycleBinRequest

        @return: EnableRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_recycle_bin_with_options(request, runtime)

    def enable_smb_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_smb_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_smb_acl_with_options(request, runtime)

    def get_directory_or_file_properties_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: GetDirectoryOrFilePropertiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDirectoryOrFilePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryOrFileProperties',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_directory_or_file_properties(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: GetDirectoryOrFilePropertiesRequest

        @return: GetDirectoryOrFilePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_or_file_properties_with_options(request, runtime)

    def get_recycle_bin_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_recycle_bin_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_recycle_bin_attribute_with_options(request, runtime)

    def list_directories_and_files_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListDirectoriesAndFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_only):
            query['DirectoryOnly'] = request.directory_only
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_directories_and_files(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListDirectoriesAndFilesRequest

        @return: ListDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_directories_and_files_with_options(request, runtime)

    def list_lifecycle_retrieve_jobs_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListLifecycleRetrieveJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLifecycleRetrieveJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLifecycleRetrieveJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_lifecycle_retrieve_jobs(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListLifecycleRetrieveJobsRequest

        @return: ListLifecycleRetrieveJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lifecycle_retrieve_jobs_with_options(request, runtime)

    def list_recently_recycled_directories_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListRecentlyRecycledDirectoriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRecentlyRecycledDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentlyRecycledDirectories',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecentlyRecycledDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_recently_recycled_directories(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListRecentlyRecycledDirectoriesRequest

        @return: ListRecentlyRecycledDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recently_recycled_directories_with_options(request, runtime)

    def list_recycle_bin_jobs_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can query a maximum of 50 jobs that are recently executed.
        

        @param request: ListRecycleBinJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRecycleBinJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycleBinJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycleBinJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_recycle_bin_jobs(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        *   You can query a maximum of 50 jobs that are recently executed.
        

        @param request: ListRecycleBinJobsRequest

        @return: ListRecycleBinJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recycle_bin_jobs_with_options(request, runtime)

    def list_recycled_directories_and_files_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListRecycledDirectoriesAndFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRecycledDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycledDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycledDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_recycled_directories_and_files(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ListRecycledDirectoriesAndFilesRequest

        @return: ListRecycledDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recycled_directories_and_files_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_access_group_with_options(self, request, runtime):
        """
        The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        

        @param request: ModifyAccessGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_access_group(self, request):
        """
        The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        

        @param request: ModifyAccessGroupRequest

        @return: ModifyAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    def modify_access_rule_with_options(self, request, runtime):
        """
        The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        

        @param request: ModifyAccessRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_access_rule(self, request):
        """
        The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        

        @param request: ModifyAccessRuleRequest

        @return: ModifyAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    def modify_auto_snapshot_policy_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: ModifyAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_snapshot_policy(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        

        @param request: ModifyAutoSnapshotPolicyRequest

        @return: ModifyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    def modify_data_flow_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows.
        *   You can modify the attributes only of the dataflows that are in the `Running` state.
        *   It generally takes 2 to 5 minutes to modify the attributes of a dataflow. You can call the [DescribeDataFlows](~~336901~~) operation to query the status of the dataflow to be modified.
        *   Data flow specifications:
        *   The dataflow throughput supports the following specifications: 600 MB/s, 1,200 MB/s, and 1,500 MB/s. The dataflow throughput is the maximum transmission bandwidth that can be reached when data is imported or exported for a dataflow.
        *   Inventory query: If you set the DryRun parameter to true, you can check whether the resources for the dataflow whose throughput is changed meet the requirements.
        *   Billing
        Changing the dataflow throughput involves the billing of dataflow bandwidth. We recommend that you understand CPFS billing methods in advance. For more information, see [Billing methods and billable items of CPFS](~~111858~~).
        

        @param request: ModifyDataFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_data_flow(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows.
        *   You can modify the attributes only of the dataflows that are in the `Running` state.
        *   It generally takes 2 to 5 minutes to modify the attributes of a dataflow. You can call the [DescribeDataFlows](~~336901~~) operation to query the status of the dataflow to be modified.
        *   Data flow specifications:
        *   The dataflow throughput supports the following specifications: 600 MB/s, 1,200 MB/s, and 1,500 MB/s. The dataflow throughput is the maximum transmission bandwidth that can be reached when data is imported or exported for a dataflow.
        *   Inventory query: If you set the DryRun parameter to true, you can check whether the resources for the dataflow whose throughput is changed meet the requirements.
        *   Billing
        Changing the dataflow throughput involves the billing of dataflow bandwidth. We recommend that you understand CPFS billing methods in advance. For more information, see [Billing methods and billable items of CPFS](~~111858~~).
        

        @param request: ModifyDataFlowRequest

        @return: ModifyDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_data_flow_with_options(request, runtime)

    def modify_data_flow_auto_refresh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_data_flow_auto_refresh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_data_flow_auto_refresh_with_options(request, runtime)

    def modify_file_system_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_file_system(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    def modify_fileset_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset modification.
        

        @param request: ModifyFilesetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_fileset(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support fileset modification.
        

        @param request: ModifyFilesetRequest

        @return: ModifyFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_fileset_with_options(request, runtime)

    def modify_ldapconfig_with_options(self, request, runtime):
        """
        #
        

        @param request: ModifyLDAPConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyLDAPConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ldapconfig(self, request):
        """
        #
        

        @param request: ModifyLDAPConfigRequest

        @return: ModifyLDAPConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ldapconfig_with_options(request, runtime)

    def modify_lifecycle_policy_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ModifyLifecyclePolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_lifecycle_policy(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: ModifyLifecyclePolicyRequest

        @return: ModifyLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_policy_with_options(request, runtime)

    def modify_mount_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mount_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mount_target_with_options(request, runtime)

    def modify_protocol_mount_target_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: ModifyProtocolMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protocol_mount_target(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: ModifyProtocolMountTargetRequest

        @return: ModifyProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protocol_mount_target_with_options(request, runtime)

    def modify_protocol_service_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: ModifyProtocolServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protocol_service(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        

        @param request: ModifyProtocolServiceRequest

        @return: ModifyProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protocol_service_with_options(request, runtime)

    def modify_smb_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_anonymous_access):
            query['EnableAnonymousAccess'] = request.enable_anonymous_access
        if not UtilClient.is_unset(request.encrypt_data):
            query['EncryptData'] = request.encrypt_data
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.home_dir_path):
            query['HomeDirPath'] = request.home_dir_path
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        if not UtilClient.is_unset(request.reject_unencrypted_access):
            query['RejectUnencryptedAccess'] = request.reject_unencrypted_access
        if not UtilClient.is_unset(request.super_admin_sid):
            query['SuperAdminSid'] = request.super_admin_sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifySmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_smb_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_smb_acl_with_options(request, runtime)

    def open_nasservice_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenNASService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_nasservice(self):
        runtime = util_models.RuntimeOptions()
        return self.open_nasservice_with_options(runtime)

    def remove_client_from_black_list_with_options(self, request, runtime):
        """
        The IP address of a client to remove from the blacklist.
        

        @param request: RemoveClientFromBlackListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveClientFromBlackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientFromBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_client_from_black_list(self, request):
        """
        The IP address of a client to remove from the blacklist.
        

        @param request: RemoveClientFromBlackListRequest

        @return: RemoveClientFromBlackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_client_from_black_list_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        """
        A request ID is returned even if the tag that you want to remove or the associated file system does not exist. For example, if the associated file system does not exist, or the TagKey and TagValue cannot be found, a request ID is returned.
        

        @param request: RemoveTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags(self, request):
        """
        A request ID is returned even if the tag that you want to remove or the associated file system does not exist. For example, if the associated file system does not exist, or the TagKey and TagValue cannot be found, a request ID is returned.
        

        @param request: RemoveTagsRequest

        @return: RemoveTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def reset_file_system_with_options(self, request, runtime):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   The file system must be in the Running state.
        *   To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        

        @param request: ResetFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_file_system(self, request):
        """
        The snapshot feature is in public preview and is provided free of charge. [Apsara File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        *   Only advanced Extreme NAS file systems support this feature.
        *   The file system must be in the Running state.
        *   To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        

        @param request: ResetFileSystemRequest

        @return: ResetFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_file_system_with_options(request, runtime)

    def retry_lifecycle_retrieve_job_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: RetryLifecycleRetrieveJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RetryLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_lifecycle_retrieve_job(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: RetryLifecycleRetrieveJobRequest

        @return: RetryLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_lifecycle_retrieve_job_with_options(request, runtime)

    def set_dir_quota_with_options(self, request, runtime):
        """
        Only General-purpose NFS file systems support the directory quota feature.
        

        @param request: SetDirQuotaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.size_limit):
            query['SizeLimit'] = request.size_limit
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dir_quota(self, request):
        """
        Only General-purpose NFS file systems support the directory quota feature.
        

        @param request: SetDirQuotaRequest

        @return: SetDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dir_quota_with_options(request, runtime)

    def start_data_flow_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can enable the dataflows that are only in the `Stopped` state.
        *   If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified dataflow. If the resources are insufficient, the dataflow cannot be enabled.
        *   It generally takes 2 to 5 minutes to enable a dataflow. You can query the dataflow status by calling the [DescribeDataFlows](~~2402270~~) operation.
        

        @param request: StartDataFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StartDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def start_data_flow(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can enable the dataflows that are only in the `Stopped` state.
        *   If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified dataflow. If the resources are insufficient, the dataflow cannot be enabled.
        *   It generally takes 2 to 5 minutes to enable a dataflow. You can query the dataflow status by calling the [DescribeDataFlows](~~2402270~~) operation.
        

        @param request: StartDataFlowRequest

        @return: StartDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_data_flow_with_options(request, runtime)

    def stop_data_flow_with_options(self, request, runtime):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can disable only the dataflows that are in the `Running` state.
        *   After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        *   After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        *   It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](~~2402271~~) operation to query the dataflow status.
        

        @param request: StopDataFlowRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StopDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_data_flow(self, request):
        """
        This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        *   Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        *   You can disable only the dataflows that are in the `Running` state.
        *   After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        *   After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        *   It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](~~2402271~~) operation to query the dataflow status.
        

        @param request: StopDataFlowRequest

        @return: StopDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_data_flow_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_recycle_bin_attribute_with_options(self, request, runtime):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: UpdateRecycleBinAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRecycleBinAttributeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpdateRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_recycle_bin_attribute(self, request):
        """
        Only General-purpose NAS file systems support this operation.
        

        @param request: UpdateRecycleBinAttributeRequest

        @return: UpdateRecycleBinAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_recycle_bin_attribute_with_options(request, runtime)

    def upgrade_file_system_with_options(self, request, runtime):
        """
        Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        *   A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        

        @param request: UpgradeFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_file_system(self, request):
        """
        Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        *   A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        

        @param request: UpgradeFileSystemRequest

        @return: UpgradeFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_file_system_with_options(request, runtime)
