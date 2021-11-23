# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dds20151201 import models as dds_20151201_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'mongodb.aliyuncs.com',
            'cn-beijing': 'mongodb.aliyuncs.com',
            'cn-chengdu': 'mongodb.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'mongodb.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'mongodb.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'mongodb.aliyuncs.com',
            'cn-shanghai': 'mongodb.aliyuncs.com',
            'cn-shenzhen': 'mongodb.aliyuncs.com',
            'cn-heyuan': 'mongodb.aliyuncs.com',
            'cn-hongkong': 'mongodb.aliyuncs.com',
            'ap-southeast-1': 'mongodb.aliyuncs.com',
            'ap-southeast-2': 'mongodb.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'mongodb.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'mongodb.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'mongodb.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'mongodb.eu-west-1.aliyuncs.com',
            'us-west-1': 'mongodb.aliyuncs.com',
            'us-east-1': 'mongodb.aliyuncs.com',
            'eu-central-1': 'mongodb.eu-central-1.aliyuncs.com',
            'me-east-1': 'mongodb.me-east-1.aliyuncs.com',
            'ap-south-1': 'mongodb.ap-south-1.aliyuncs.com',
            'cn-hangzhou-finance': 'mongodb.aliyuncs.com',
            'cn-shanghai-finance-1': 'mongodb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mongodb.aliyuncs.com',
            'cn-north-2-gov-1': 'mongodb.aliyuncs.com',
            'ap-northeast-2-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-1': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-gov-1': 'mongodb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mongodb.aliyuncs.com',
            'cn-edge-1': 'mongodb.aliyuncs.com',
            'cn-fujian': 'mongodb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mongodb.aliyuncs.com',
            'cn-hangzhou-test-306': 'mongodb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mongodb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mongodb.aliyuncs.com',
            'cn-qingdao-nebula': 'mongodb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-inner': 'mongodb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-shenzhen-inner': 'mongodb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mongodb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mongodb.aliyuncs.com',
            'cn-wuhan': 'mongodb.aliyuncs.com',
            'cn-wulanchabu': 'mongodb.aliyuncs.com',
            'cn-yushanfang': 'mongodb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mongodb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mongodb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mongodb.aliyuncs.com',
            'eu-west-1-oxs': 'mongodb.aliyuncs.com',
            'rus-west-1-pop': 'mongodb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_node_private_network_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocateNodePrivateNetworkAddressResponse(),
            self.do_rpcrequest('AllocateNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_node_private_network_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_node_private_network_address_with_options(request, runtime)

    def allocate_public_network_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocatePublicNetworkAddressResponse(),
            self.do_rpcrequest('AllocatePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_public_network_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckCloudResourceAuthorizedResponse(),
            self.do_rpcrequest('CheckCloudResourceAuthorized', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def check_recovery_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckRecoveryConditionResponse(),
            self.do_rpcrequest('CheckRecoveryCondition', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_recovery_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_recovery_condition_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateBackupResponse(),
            self.do_rpcrequest('CreateBackup', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeResponse(),
            self.do_rpcrequest('CreateNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    def create_node_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeBatchResponse(),
            self.do_rpcrequest('CreateNodeBatch', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_node_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_node_batch_with_options(request, runtime)

    def create_recommendation_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateRecommendationTaskResponse(),
            self.do_rpcrequest('CreateRecommendationTask', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_recommendation_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_recommendation_task_with_options(request, runtime)

    def create_serverless_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateServerlessDBInstanceResponse(),
            self.do_rpcrequest('CreateServerlessDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_serverless_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_serverless_dbinstance_with_options(request, runtime)

    def create_sharding_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateShardingDBInstanceResponse(),
            self.do_rpcrequest('CreateShardingDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sharding_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sharding_dbinstance_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteNodeResponse(),
            self.do_rpcrequest('DeleteNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_active_operation_task_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskCountResponse(),
            self.do_rpcrequest('DescribeActiveOperationTaskCount', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    def describe_active_operation_task_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskTypeResponse(),
            self.do_rpcrequest('DescribeActiveOperationTaskType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_type_with_options(request, runtime)

    def describe_audit_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditFilesResponse(),
            self.do_rpcrequest('DescribeAuditFiles', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_files_with_options(request, runtime)

    def describe_audit_log_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditLogFilterResponse(),
            self.do_rpcrequest('DescribeAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_log_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_filter_with_options(request, runtime)

    def describe_audit_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditPolicyResponse(),
            self.do_rpcrequest('DescribeAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_policy_with_options(request, runtime)

    def describe_audit_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditRecordsResponse(),
            self.do_rpcrequest('DescribeAuditRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    def describe_available_engine_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableEngineVersionResponse(),
            self.do_rpcrequest('DescribeAvailableEngineVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_engine_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_engine_version_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_available_time_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableTimeRangeResponse(),
            self.do_rpcrequest('DescribeAvailableTimeRange', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_time_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_time_range_with_options(request, runtime)

    def describe_backup_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupDBsResponse(),
            self.do_rpcrequest('DescribeBackupDBs', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_encryption_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.do_rpcrequest('DescribeDBInstanceEncryptionKey', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_encryption_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    def describe_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceMonitorResponse(),
            self.do_rpcrequest('DescribeDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancePerformanceResponse(),
            self.do_rpcrequest('DescribeDBInstancePerformance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceSSLResponse(),
            self.do_rpcrequest('DescribeDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_dbinstance_tdeinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceTDEInfoResponse(),
            self.do_rpcrequest('DescribeDBInstanceTDEInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tdeinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdeinfo_with_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDedicatedClusterInstanceListResponse(),
            self.do_rpcrequest('DescribeDedicatedClusterInstanceList', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_cluster_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    def describe_error_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeErrorLogRecordsResponse(),
            self.do_rpcrequest('DescribeErrorLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_error_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_error_log_records_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_kernel_release_notes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeKernelReleaseNotesResponse(),
            self.do_rpcrequest('DescribeKernelReleaseNotes', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_kernel_release_notes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_kernel_release_notes_with_options(request, runtime)

    def describe_mongo_dblog_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeMongoDBLogConfigResponse(),
            self.do_rpcrequest('DescribeMongoDBLogConfig', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mongo_dblog_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mongo_dblog_config_with_options(request, runtime)

    def describe_parameter_modification_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterModificationHistoryResponse(),
            self.do_rpcrequest('DescribeParameterModificationHistory', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_modification_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterTemplatesResponse(),
            self.do_rpcrequest('DescribeParameterTemplates', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRenewalPriceResponse(),
            self.do_rpcrequest('DescribeRenewalPrice', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_replica_set_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeReplicaSetRoleResponse(),
            self.do_rpcrequest('DescribeReplicaSetRole', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_replica_set_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_replica_set_role_with_options(request, runtime)

    def describe_role_zone_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRoleZoneInfoResponse(),
            self.do_rpcrequest('DescribeRoleZoneInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_role_zone_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    def describe_running_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRunningLogRecordsResponse(),
            self.do_rpcrequest('DescribeRunningLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_running_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityGroupConfigurationResponse(),
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def describe_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityIpsResponse(),
            self.do_rpcrequest('DescribeSecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    def describe_sharding_network_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeShardingNetworkAddressResponse(),
            self.do_rpcrequest('DescribeShardingNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sharding_network_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sharding_network_address_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_user_encryption_key_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeUserEncryptionKeyListResponse(),
            self.do_rpcrequest('DescribeUserEncryptionKeyList', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_encryption_key_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    def destroy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.DestroyInstanceResponse(),
            self.do_rpcrequest('DestroyInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_instance_with_options(request, runtime)

    def evaluate_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.EvaluateResourceResponse(),
            self.do_rpcrequest('EvaluateResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def evaluate_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.evaluate_resource_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def migrate_available_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateAvailableZoneResponse(),
            self.do_rpcrequest('MigrateAvailableZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_available_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_available_zone_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateToOtherZoneResponse(),
            self.do_rpcrequest('MigrateToOtherZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_audit_log_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditLogFilterResponse(),
            self.do_rpcrequest('ModifyAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_log_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_filter_with_options(request, runtime)

    def modify_audit_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditPolicyResponse(),
            self.do_rpcrequest('ModifyAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_policy_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceConnectionStringResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    def modify_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMonitorResponse(),
            self.do_rpcrequest('ModifyDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    def modify_dbinstance_net_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceNetExpireTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_net_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_net_expire_time_with_options(request, runtime)

    def modify_dbinstance_network_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetworkTypeResponse(),
            self.do_rpcrequest('ModifyDBInstanceNetworkType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSSLResponse(),
            self.do_rpcrequest('ModifyDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def modify_dbinstance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSpecResponse(),
            self.do_rpcrequest('ModifyDBInstanceSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    def modify_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceTDEResponse(),
            self.do_rpcrequest('ModifyDBInstanceTDE', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceVpcAuthModeResponse(),
            self.do_rpcrequest('ModifyInstanceVpcAuthMode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_auth_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    def modify_node_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecResponse(),
            self.do_rpcrequest('ModifyNodeSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_node_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    def modify_node_spec_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecBatchResponse(),
            self.do_rpcrequest('ModifyNodeSpecBatch', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_node_spec_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_batch_with_options(request, runtime)

    def modify_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyParametersResponse(),
            self.do_rpcrequest('ModifyParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyResourceGroupResponse(),
            self.do_rpcrequest('ModifyResourceGroup', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    def modify_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityGroupConfigurationResponse(),
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def release_node_private_network_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse(),
            self.do_rpcrequest('ReleaseNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_node_private_network_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_node_private_network_address_with_options(request, runtime)

    def release_public_network_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleasePublicNetworkAddressResponse(),
            self.do_rpcrequest('ReleasePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_network_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    def renew_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.RenewDBInstanceResponse(),
            self.do_rpcrequest('RenewDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_dbinstance_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def restore_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.RestoreDBInstanceResponse(),
            self.do_rpcrequest('RestoreDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_dbinstance_with_options(request, runtime)

    def switch_dbinstance_hawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.SwitchDBInstanceHAResponse(),
            self.do_rpcrequest('SwitchDBInstanceHA', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_ha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def transform_to_pre_paid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.TransformToPrePaidResponse(),
            self.do_rpcrequest('TransformToPrePaid', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_to_pre_paid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceEngineVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceEngineVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_engine_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)
