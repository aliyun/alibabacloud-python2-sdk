# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20191111 import models as clickhouse_20191111_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'clickhouse.aliyuncs.com',
            'ap-southeast-1': 'clickhouse.aliyuncs.com',
            'cn-beijing': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-beijing-gov-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-nu16-b01': 'clickhouse.aliyuncs.com',
            'cn-edge-1': 'clickhouse.aliyuncs.com',
            'cn-fujian': 'clickhouse.aliyuncs.com',
            'cn-haidian-cm12-c01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-finance': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-test-306': 'clickhouse.aliyuncs.com',
            'cn-hongkong': 'clickhouse.aliyuncs.com',
            'cn-hongkong-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-north-2-gov-1': 'clickhouse.aliyuncs.com',
            'cn-qingdao': 'clickhouse.aliyuncs.com',
            'cn-qingdao-nebula': 'clickhouse.aliyuncs.com',
            'cn-shanghai': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et15-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et2-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shanghai-inner': 'clickhouse.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-inner': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'clickhouse.aliyuncs.com',
            'cn-wuhan': 'clickhouse.aliyuncs.com',
            'cn-yushanfang': 'clickhouse.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'clickhouse.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'clickhouse.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'clickhouse.aliyuncs.com',
            'eu-west-1-oxs': 'clickhouse.aliyuncs.com',
            'me-east-1': 'clickhouse.aliyuncs.com',
            'rus-west-1-pop': 'clickhouse.aliyuncs.com',
            'us-east-1': 'clickhouse.aliyuncs.com',
            'us-west-1': 'clickhouse.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('clickhouse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_account_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            self.do_rpcrequest('DescribeAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def describe_lorne_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            self.do_rpcrequest('DescribeLorneTasks', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_with_options(request, runtime)

    def describe_dbcluster_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            self.do_rpcrequest('DescribeDBClusterPerformance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    def modify_dbcluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            self.do_rpcrequest('ModifyDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def describe_dbcluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            self.do_rpcrequest('DescribeDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    def describe_ossstorage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            self.do_rpcrequest('DescribeOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ossstorage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def modify_dbconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            self.do_rpcrequest('ModifyDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    def create_ports_for_click_house_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            self.do_rpcrequest('CreatePortsForClickHouse', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ports_for_click_house(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    def delete_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            self.do_rpcrequest('DeleteDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    def describe_slow_log_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            self.do_rpcrequest('DescribeSlowLogTrend', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def release_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            self.do_rpcrequest('ReleaseClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def describe_log_store_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            self.do_rpcrequest('DescribeLogStoreKeys', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_store_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    def describe_process_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            self.do_rpcrequest('DescribeProcessList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_process_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    def create_ossstorage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            self.do_rpcrequest('CreateOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ossstorage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def describe_lorne_tasks_mcount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            self.do_rpcrequest('DescribeLorneTasksMCount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks_mcount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_mcount_with_options(request, runtime)

    def describe_dbconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            self.do_rpcrequest('DescribeDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    def modify_account_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            self.do_rpcrequest('ModifyAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    def describe_lorne_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            self.do_rpcrequest('DescribeLorneLog', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_log_with_options(request, runtime)

    def describe_all_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            self.do_rpcrequest('DescribeAllDataSources', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    def operate_lorne_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            self.do_rpcrequest('OperateLorneTaskStatus', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_lorne_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_lorne_task_status_with_options(request, runtime)

    def describe_dbcluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            self.do_rpcrequest('DescribeDBClusterAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    def delete_lorne_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            self.do_rpcrequest('DeleteLorneTask', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_lorne_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_lorne_task_with_options(request, runtime)

    def describe_dbclusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            self.do_rpcrequest('DescribeDBClusters', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbclusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    def operate_log_hub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            self.do_rpcrequest('OperateLogHub', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_log_hub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    def check_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            self.do_rpcrequest('CheckServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    def create_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            self.do_rpcrequest('CreateBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    def describe_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            self.do_rpcrequest('DescribeSchemas', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    def kill_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            self.do_rpcrequest('KillProcess', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    def modify_dbcluster_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBClusterMaintainTime', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('DescribeDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def modify_dbcluster_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            self.do_rpcrequest('ModifyDBClusterDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_columns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            self.do_rpcrequest('DescribeColumns', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_columns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_lorne_tasks_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            self.do_rpcrequest('DescribeLorneTasksMetrics', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_metrics_with_options(request, runtime)

    def check_scale_out_balanced_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            self.do_rpcrequest('CheckScaleOutBalanced', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_scale_out_balanced(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    def allocate_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            self.do_rpcrequest('AllocateClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    def describe_all_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            self.do_rpcrequest('DescribeAllDataSource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_dbcluster_net_info_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            self.do_rpcrequest('DescribeDBClusterNetInfoItems', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_net_info_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    def describe_loghub_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            self.do_rpcrequest('DescribeLoghubDetail', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_loghub_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    def modify_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            self.do_rpcrequest('ModifyDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    def describe_log_hub_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            self.do_rpcrequest('DescribeLogHubAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_hub_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    def modify_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('ModifyDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    def create_account_and_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            self.do_rpcrequest('CreateAccountAndAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account_and_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)
