# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbs20190306 import models as dbs_20190306_models
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

    def configure_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start_backup):
            query['AutoStartBackup'] = request.auto_start_backup
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ConfigureBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_backup_plan_with_options(request, runtime)

    def create_and_start_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndStartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateAndStartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_and_start_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_and_start_backup_plan_with_options(request, runtime)

    def create_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    def create_full_backup_set_download_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFullBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateFullBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def create_full_backup_set_download(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_full_backup_set_download_with_options(request, runtime)

    def create_get_dblist_from_agent_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGetDBListFromAgentTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateGetDBListFromAgentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_get_dblist_from_agent_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_get_dblist_from_agent_task_with_options(request, runtime)

    def create_increment_backup_set_download_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIncrementBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateIncrementBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def create_increment_backup_set_download(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_increment_backup_set_download_with_options(request, runtime)

    def create_restore_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.duplicate_conflict):
            query['DuplicateConflict'] = request.duplicate_conflict
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_dir):
            query['RestoreDir'] = request.restore_dir
        if not UtilClient.is_unset(request.restore_home):
            query['RestoreHome'] = request.restore_home
        if not UtilClient.is_unset(request.restore_objects):
            query['RestoreObjects'] = request.restore_objects
        if not UtilClient.is_unset(request.restore_task_name):
            query['RestoreTaskName'] = request.restore_task_name
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_restore_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_restore_task_with_options(request, runtime)

    def describe_backup_gateway_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupGatewayList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupGatewayListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_gateway_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_gateway_list_with_options(request, runtime)

    def describe_backup_plan_billing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanBilling',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanBillingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_plan_billing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_billing_with_options(request, runtime)

    def describe_backup_plan_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_plan_status):
            query['BackupPlanStatus'] = request.backup_plan_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_plan_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_list_with_options(request, runtime)

    def describe_backup_set_download_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_task_id):
            query['BackupSetDownloadTaskId'] = request.backup_set_download_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetDownloadTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_set_download_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_download_task_list_with_options(request, runtime)

    def describe_dlaservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDLAService',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeDLAServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dlaservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dlaservice_with_options(request, runtime)

    def describe_full_backup_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFullBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeFullBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_full_backup_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_full_backup_list_with_options(request, runtime)

    def describe_increment_backup_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIncrementBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeIncrementBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_increment_backup_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_increment_backup_list_with_options(request, runtime)

    def describe_job_error_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobErrorCode',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeJobErrorCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job_error_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_error_code_with_options(request, runtime)

    def describe_node_cidr_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeCidrList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeNodeCidrListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_cidr_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_cidr_list_with_options(request, runtime)

    def describe_pre_check_progress_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckProgressList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribePreCheckProgressListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pre_check_progress_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_progress_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_restore_range_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.begin_timestamp_for_restore):
            query['BeginTimestampForRestore'] = request.begin_timestamp_for_restore
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp_for_restore):
            query['EndTimestampForRestore'] = request.end_timestamp_for_restore
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recently_restore):
            query['RecentlyRestore'] = request.recently_restore
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreRangeInfo',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreRangeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_range_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_range_info_with_options(request, runtime)

    def describe_restore_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_task_list_with_options(request, runtime)

    def disable_backup_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DisableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_backup_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_backup_log_with_options(request, runtime)

    def enable_backup_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.EnableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_backup_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_log_with_options(request, runtime)

    def get_dblist_from_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBListFromAgent',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.GetDBListFromAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dblist_from_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dblist_from_agent_with_options(request, runtime)

    def initialize_dbs_service_linked_role_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeDbsServiceLinkedRole',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_dbs_service_linked_role(self):
        runtime = util_models.RuntimeOptions()
        return self.initialize_dbs_service_linked_role_with_options(runtime)

    def modify_backup_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupObjects',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_objects_with_options(request, runtime)

    def modify_backup_plan_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlanName',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupPlanNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_plan_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_name_with_options(request, runtime)

    def modify_backup_set_download_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_dir):
            query['BackupSetDownloadDir'] = request.backup_set_download_dir
        if not UtilClient.is_unset(request.backup_set_download_target_type):
            query['BackupSetDownloadTargetType'] = request.backup_set_download_target_type
        if not UtilClient.is_unset(request.backup_set_download_target_type_location):
            query['BackupSetDownloadTargetTypeLocation'] = request.backup_set_download_target_type_location
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.full_data_format):
            query['FullDataFormat'] = request.full_data_format
        if not UtilClient.is_unset(request.increment_data_format):
            query['IncrementDataFormat'] = request.increment_data_format
        if not UtilClient.is_unset(request.open_auto_download):
            query['OpenAutoDownload'] = request.open_auto_download
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupSetDownloadRules',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSetDownloadRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_set_download_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_set_download_rules_with_options(request, runtime)

    def modify_backup_source_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupSourceEndpoint',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSourceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_source_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_source_endpoint_with_options(request, runtime)

    def modify_backup_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_strategy_with_options(request, runtime)

    def modify_storage_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyStorageStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_storage_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_strategy_with_options(request, runtime)

    def release_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ReleaseBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def release_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_backup_plan_with_options(request, runtime)

    def renew_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.RenewBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_backup_plan_with_options(request, runtime)

    def start_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def start_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_backup_plan_with_options(request, runtime)

    def start_restore_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_restore_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_restore_task_with_options(request, runtime)

    def stop_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stop_method):
            query['StopMethod'] = request.stop_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StopBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_backup_plan_with_options(request, runtime)

    def upgrade_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.UpgradeBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_plan_with_options(request, runtime)
