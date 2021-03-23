# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_r_kvstore20150101 import models as r_kvstore_20150101_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'r-kvstore.aliyuncs.com',
            'cn-beijing': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou': 'r-kvstore.aliyuncs.com',
            'cn-shanghai': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen': 'r-kvstore.aliyuncs.com',
            'cn-heyuan': 'r-kvstore.aliyuncs.com',
            'ap-southeast-1': 'r-kvstore.aliyuncs.com',
            'us-west-1': 'r-kvstore.aliyuncs.com',
            'us-east-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-finance': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-north-2-gov-1': 'r-kvstore.aliyuncs.com',
            'ap-northeast-2-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-gov-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-nu16-b01': 'r-kvstore.aliyuncs.com',
            'cn-edge-1': 'r-kvstore.aliyuncs.com',
            'cn-fujian': 'r-kvstore.aliyuncs.com',
            'cn-haidian-cm12-c01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-test-306': 'r-kvstore.aliyuncs.com',
            'cn-hongkong-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'r-kvstore.aliyuncs.com',
            'cn-qingdao-nebula': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et15-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et2-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-inner': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-inner': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'r-kvstore.aliyuncs.com',
            'cn-wuhan': 'r-kvstore.aliyuncs.com',
            'cn-wulanchabu': 'r-kvstore.aliyuncs.com',
            'cn-yushanfang': 'r-kvstore.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'r-kvstore.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'r-kvstore.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'r-kvstore.aliyuncs.com',
            'eu-west-1-oxs': 'r-kvstore.aliyuncs.com',
            'rus-west-1-pop': 'r-kvstore.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('r-kvstore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_sharding_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.AddShardingNodeResponse().from_map(
            self.do_rpcrequest('AddShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sharding_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sharding_node_with_options(request, runtime)

    def allocate_direct_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.AllocateDirectConnectionResponse().from_map(
            self.do_rpcrequest('AllocateDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_direct_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_direct_connection_with_options(request, runtime)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse().from_map(
            self.do_rpcrequest('AllocateInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateAccountResponse().from_map(
            self.do_rpcrequest('CreateAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateBackupResponse().from_map(
            self.do_rpcrequest('CreateBackup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_cache_analysis_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse().from_map(
            self.do_rpcrequest('CreateCacheAnalysisTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cache_analysis_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_task_with_options(request, runtime)

    def create_global_distribute_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse().from_map(
            self.do_rpcrequest('CreateGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_global_distribute_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_global_distribute_cache_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_tair_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateTairInstanceResponse().from_map(
            self.do_rpcrequest('CreateTairInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tair_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tair_instance_with_options(request, runtime)

    def create_user_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.CreateUserClusterHostResponse().from_map(
            self.do_rpcrequest('CreateUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_cluster_host_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DeleteAccountResponse().from_map(
            self.do_rpcrequest('DeleteAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_sharding_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DeleteShardingNodeResponse().from_map(
            self.do_rpcrequest('DeleteShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sharding_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sharding_node_with_options(request, runtime)

    def delete_user_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DeleteUserClusterHostResponse().from_map(
            self.do_rpcrequest('DeleteUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_cluster_host_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAccounts', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_active_operation_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeActiveOperationTaskResponse().from_map(
            self.do_rpcrequest('DescribeActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_with_options(request, runtime)

    def describe_audit_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeAuditRecordsResponse().from_map(
            self.do_rpcrequest('DescribeAuditRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_backup_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeBackupTasksResponse().from_map(
            self.do_rpcrequest('DescribeBackupTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    def describe_cache_analysis_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse().from_map(
            self.do_rpcrequest('DescribeCacheAnalysisReport', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_with_options(request, runtime)

    def describe_cache_analysis_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse().from_map(
            self.do_rpcrequest('DescribeCacheAnalysisReportList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_list_with_options(request, runtime)

    def describe_cluster_member_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeClusterMemberInfoResponse().from_map(
            self.do_rpcrequest('DescribeClusterMemberInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_member_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_member_info_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceNetInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_net_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedClusterInstanceList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_cluster_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    def describe_engine_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeEngineVersionResponse().from_map(
            self.do_rpcrequest('DescribeEngineVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_engine_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_engine_version_with_options(request, runtime)

    def describe_global_distribute_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse().from_map(
            self.do_rpcrequest('DescribeGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_global_distribute_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_global_distribute_cache_with_options(request, runtime)

    def describe_history_monitor_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse().from_map(
            self.do_rpcrequest('DescribeHistoryMonitorValues', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_history_monitor_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_monitor_values_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeInstanceConfigResponse().from_map(
            self.do_rpcrequest('DescribeInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_config_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeInstanceSSLResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    def describe_intranet_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeIntranetAttributeResponse().from_map(
            self.do_rpcrequest('DescribeIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_intranet_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_intranet_attribute_with_options(request, runtime)

    def describe_logic_instance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse().from_map(
            self.do_rpcrequest('DescribeLogicInstanceTopology', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_logic_instance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_logic_instance_topology_with_options(request, runtime)

    def describe_monitor_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeMonitorItemsResponse().from_map(
            self.do_rpcrequest('DescribeMonitorItems', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_monitor_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_items_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeParametersResponse().from_map(
            self.do_rpcrequest('DescribeParameters', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeParameterTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeParameterTemplates', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribePriceResponse().from_map(
            self.do_rpcrequest('DescribePrice', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_role_zone_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeRoleZoneInfoResponse().from_map(
            self.do_rpcrequest('DescribeRoleZoneInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_role_zone_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    def describe_running_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeRunningLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeRunningLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_running_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def describe_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeSecurityIpsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeSlowLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSlowLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_user_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeUserClusterHostResponse().from_map(
            self.do_rpcrequest('DescribeUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_cluster_host_with_options(request, runtime)

    def describe_user_cluster_host_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse().from_map(
            self.do_rpcrequest('DescribeUserClusterHostInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_cluster_host_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_cluster_host_instance_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def enable_additional_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.EnableAdditionalBandwidthResponse().from_map(
            self.do_rpcrequest('EnableAdditionalBandwidth', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_additional_bandwidth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_additional_bandwidth_with_options(request, runtime)

    def flush_expire_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.FlushExpireKeysResponse().from_map(
            self.do_rpcrequest('FlushExpireKeys', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flush_expire_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.flush_expire_keys_with_options(request, runtime)

    def flush_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.FlushInstanceResponse().from_map(
            self.do_rpcrequest('FlushInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flush_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.flush_instance_with_options(request, runtime)

    def grant_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.GrantAccountPrivilegeResponse().from_map(
            self.do_rpcrequest('GrantAccountPrivilege', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    def initialize_kvstore_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.InitializeKvstorePermissionResponse().from_map(
            self.do_rpcrequest('InitializeKvstorePermission', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initialize_kvstore_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initialize_kvstore_permission_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.MigrateToOtherZoneResponse().from_map(
            self.do_rpcrequest('MigrateToOtherZone', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyAccountDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyAccountDescription', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyAccountPasswordResponse().from_map(
            self.do_rpcrequest('ModifyAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    def modify_active_operation_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyActiveOperationTaskResponse().from_map(
            self.do_rpcrequest('ModifyActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_task_with_options(request, runtime)

    def modify_audit_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyAuditLogConfigResponse().from_map(
            self.do_rpcrequest('ModifyAuditLogConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def modify_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceConfigResponse().from_map(
            self.do_rpcrequest('ModifyInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    def modify_instance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMaintainTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    def modify_instance_major_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMajorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_major_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_major_version_with_options(request, runtime)

    def modify_instance_minor_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMinorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_minor_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_minor_version_with_options(request, runtime)

    def modify_instance_net_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceNetExpireTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_net_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_net_expire_time_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyInstanceSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_instance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceSSLResponse().from_map(
            self.do_rpcrequest('ModifyInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVpcAuthMode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_auth_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    def modify_intranet_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyIntranetAttributeResponse().from_map(
            self.do_rpcrequest('ModifyIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_intranet_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_intranet_attribute_with_options(request, runtime)

    def modify_node_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyNodeSpecResponse().from_map(
            self.do_rpcrequest('ModifyNodeSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_node_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyResourceGroupResponse().from_map(
            self.do_rpcrequest('ModifyResourceGroup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    def modify_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifySecurityIpsResponse().from_map(
            self.do_rpcrequest('ModifySecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_user_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ModifyUserClusterHostResponse().from_map(
            self.do_rpcrequest('ModifyUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_cluster_host_with_options(request, runtime)

    def release_direct_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ReleaseDirectConnectionResponse().from_map(
            self.do_rpcrequest('ReleaseDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_direct_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_direct_connection_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse().from_map(
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def replace_user_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ReplaceUserClusterHostResponse().from_map(
            self.do_rpcrequest('ReplaceUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_user_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_user_cluster_host_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.ResetAccountPasswordResponse().from_map(
            self.do_rpcrequest('ResetAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.RestartInstanceResponse().from_map(
            self.do_rpcrequest('RestartInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def restore_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.RestoreInstanceResponse().from_map(
            self.do_rpcrequest('RestoreInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_instance_with_options(request, runtime)

    def switch_instance_hawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.SwitchInstanceHAResponse().from_map(
            self.do_rpcrequest('SwitchInstanceHA', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_instance_ha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_hawith_options(request, runtime)

    def switch_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.SwitchNetworkResponse().from_map(
            self.do_rpcrequest('SwitchNetwork', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_network_with_options(request, runtime)

    def sync_dts_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.SyncDtsStatusResponse().from_map(
            self.do_rpcrequest('SyncDtsStatus', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_dts_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_dts_status_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def transform_to_pre_paid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.TransformToPrePaidResponse().from_map(
            self.do_rpcrequest('TransformToPrePaid', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_to_pre_paid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return r_kvstore_20150101_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
