# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbs20210101 import models as dbs_20210101_models
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
            'cn-qingdao': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'dbs-api.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'dbs-api.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'dbs-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dbs-api.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dbs-api.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dbs-api.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'dbs-api.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'us-east-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'eu-central-1': 'dbs-api.eu-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-south-1': 'dbs-api.ap-south-1.aliyuncs.com',
            'eu-west-1': 'dbs-api.eu-west-1.aliyuncs.com',
            'me-east-1': 'dbs-api.me-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def create_download_with_options(self, request, runtime):
        """
        For ApsaraDB RDS for MySQL instances that use standard SSDs or enhanced SSDs (ESSDs) and meet your business requirements, you can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: CreateDownloadRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bak_set_id):
            query['BakSetId'] = request.bak_set_id
        if not UtilClient.is_unset(request.bak_set_size):
            query['BakSetSize'] = request.bak_set_size
        if not UtilClient.is_unset(request.bak_set_type):
            query['BakSetType'] = request.bak_set_type
        if not UtilClient.is_unset(request.download_point_in_time):
            query['DownloadPointInTime'] = request.download_point_in_time
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not UtilClient.is_unset(request.target_oss_region):
            query['TargetOssRegion'] = request.target_oss_region
        if not UtilClient.is_unset(request.target_path):
            query['TargetPath'] = request.target_path
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownload',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.CreateDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def create_download(self, request):
        """
        For ApsaraDB RDS for MySQL instances that use standard SSDs or enhanced SSDs (ESSDs) and meet your business requirements, you can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: CreateDownloadRequest

        @return: CreateDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_download_with_options(request, runtime)

    def create_sandbox_instance_with_options(self, request, runtime):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: CreateSandboxInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSandboxInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.sandbox_instance_name):
            query['SandboxInstanceName'] = request.sandbox_instance_name
        if not UtilClient.is_unset(request.sandbox_password):
            query['SandboxPassword'] = request.sandbox_password
        if not UtilClient.is_unset(request.sandbox_specification):
            query['SandboxSpecification'] = request.sandbox_specification
        if not UtilClient.is_unset(request.sandbox_type):
            query['SandboxType'] = request.sandbox_type
        if not UtilClient.is_unset(request.sandbox_user):
            query['SandboxUser'] = request.sandbox_user
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_switch_id):
            query['VpcSwitchId'] = request.vpc_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.CreateSandboxInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sandbox_instance(self, request):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: CreateSandboxInstanceRequest

        @return: CreateSandboxInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sandbox_instance_with_options(request, runtime)

    def delete_sandbox_instance_with_options(self, request, runtime):
        """
        This operation is available only for the Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DeleteSandboxInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSandboxInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSandboxInstance',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DeleteSandboxInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sandbox_instance(self, request):
        """
        This operation is available only for the Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DeleteSandboxInstanceRequest

        @return: DeleteSandboxInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sandbox_instance_with_options(request, runtime)

    def describe_dbtables_recovery_backup_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBTablesRecoveryBackupSet',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDBTablesRecoveryBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbtables_recovery_backup_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbtables_recovery_backup_set_with_options(request, runtime)

    def describe_dbtables_recovery_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBTablesRecoveryState',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDBTablesRecoveryStateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbtables_recovery_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbtables_recovery_state_with_options(request, runtime)

    def describe_dbtables_recovery_time_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBTablesRecoveryTimeRange',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDBTablesRecoveryTimeRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbtables_recovery_time_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbtables_recovery_time_range_with_options(request, runtime)

    def describe_download_backup_set_storage_info_with_options(self, request, runtime):
        """
        You can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadBackupSetStorageInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadBackupSetStorageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadBackupSetStorageInfo',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDownloadBackupSetStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_backup_set_storage_info(self, request):
        """
        You can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadBackupSetStorageInfoRequest

        @return: DescribeDownloadBackupSetStorageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_backup_set_storage_info_with_options(request, runtime)

    def describe_download_support_with_options(self, request, runtime):
        """
        You can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadSupportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadSupportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadSupport',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDownloadSupportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_support(self, request):
        """
        You can create an advanced download task by point in time or backup set. You can set the download destination to an URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadSupportRequest

        @return: DescribeDownloadSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_support_with_options(request, runtime)

    def describe_download_task_with_options(self, request, runtime):
        """
        You can create an advanced download task by point in time or backup set. You can set the Download Destination parameter to URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.datasource_id):
            query['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direct):
            query['OrderDirect'] = request.order_direct
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadTask',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_task(self, request):
        """
        You can create an advanced download task by point in time or backup set. You can set the Download Destination parameter to URL or directly upload the downloaded data to your Object Storage Service (OSS) bucket to facilitate data analysis and offline archiving. For more information, see [Download the backup files of an ApsaraDB RDS for MySQL instance](~~98819~~).
        

        @param request: DescribeDownloadTaskRequest

        @return: DescribeDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_task_with_options(request, runtime)

    def describe_sandbox_backup_sets_with_options(self, request, runtime):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only for the Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxBackupSetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSandboxBackupSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxBackupSets',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxBackupSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sandbox_backup_sets(self, request):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only for the Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxBackupSetsRequest

        @return: DescribeSandboxBackupSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_backup_sets_with_options(request, runtime)

    def describe_sandbox_instances_with_options(self, request, runtime):
        """
        This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSandboxInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxInstances',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sandbox_instances(self, request):
        """
        This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxInstancesRequest

        @return: DescribeSandboxInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_instances_with_options(request, runtime)

    def describe_sandbox_recovery_time_with_options(self, request, runtime):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxRecoveryTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSandboxRecoveryTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSandboxRecoveryTime',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.DescribeSandboxRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sandbox_recovery_time(self, request):
        """
        Before you call this operation, you must enable the sandbox feature for the database instance. For more information, see [Use the emergency recovery feature of an ApsaraDB RDS for MySQL instance](~~203154~~) or [Create a sandbox instance for emergency disaster recovery of a self-managed MySQL database](~~185577~~). This operation is available only in Database Backup (DBS) API of the 2021-01-01 version.
        

        @param request: DescribeSandboxRecoveryTimeRequest

        @return: DescribeSandboxRecoveryTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sandbox_recovery_time_with_options(request, runtime)

    def modify_dbtables_recovery_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBTablesRecoveryState',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.ModifyDBTablesRecoveryStateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbtables_recovery_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbtables_recovery_state_with_options(request, runtime)

    def support_dbtable_recovery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SupportDBTableRecovery',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20210101_models.SupportDBTableRecoveryResponse(),
            self.call_api(params, req, runtime)
        )

    def support_dbtable_recovery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.support_dbtable_recovery_with_options(request, runtime)
