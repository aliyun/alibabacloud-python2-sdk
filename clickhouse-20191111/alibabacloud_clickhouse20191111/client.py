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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def allocate_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    def check_clickhouse_to_rdswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckClickhouseToRDS',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckClickhouseToRDSResponse(),
            self.call_api(params, req, runtime)
        )

    def check_clickhouse_to_rds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_clickhouse_to_rdswith_options(request, runtime)

    def check_scale_out_balanced_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckScaleOutBalanced',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            self.call_api(params, req, runtime)
        )

    def check_scale_out_balanced(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    def check_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    def check_version_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CheckAccount'] = request.check_account
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckVersionTransfer',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckVersionTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def check_version_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_version_transfer_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_account_and_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccountAndAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account_and_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)

    def create_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DBClusterCategory'] = request.dbcluster_category
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterNetworkType'] = request.dbcluster_network_type
        query['DBClusterVersion'] = request.dbcluster_version
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['DbNodeStorageType'] = request.db_node_storage_type
        query['EncryptionKey'] = request.encryption_key
        query['EncryptionType'] = request.encryption_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UsedTime'] = request.used_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_ossstorage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ossstorage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    def create_ports_for_click_house_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PortType'] = request.port_type
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePortsForClickHouse',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ports_for_click_house(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    def create_rdsto_clickhouse_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        query['SynDbTables'] = request.syn_db_tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rdsto_clickhouse_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rdsto_clickhouse_db_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    def delete_lorne_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLorneTask',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_lorne_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_lorne_task_with_options(request, runtime)

    def delete_syndb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSyndb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteSyndbResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_syndb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_syndb_with_options(request, runtime)

    def describe_account_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_account_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_all_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    def describe_all_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSources',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceptLanguage'] = request.accept_language
        query['ChargeType'] = request.charge_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_columns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_columns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    def describe_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    def describe_dbcluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    def describe_dbcluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    def describe_dbcluster_net_info_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNetInfoItems',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_net_info_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    def describe_dbcluster_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    def describe_dbclusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterIds'] = request.dbcluster_ids
        query['DBClusterStatus'] = request.dbcluster_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbclusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    def describe_dbconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    def describe_log_hub_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogHubAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_hub_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    def describe_log_store_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreKeys',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_store_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    def describe_loghub_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ExportName'] = request.export_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLoghubDetail',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_loghub_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    def describe_lorne_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneLog',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lorne_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_log_with_options(request, runtime)

    def describe_lorne_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasks',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lorne_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_with_options(request, runtime)

    def describe_lorne_tasks_mcount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMCount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lorne_tasks_mcount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_mcount_with_options(request, runtime)

    def describe_lorne_tasks_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMetrics',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lorne_tasks_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_metrics_with_options(request, runtime)

    def describe_ossstorage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ossstorage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    def describe_process_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['InitialUser'] = request.initial_user
        query['Keyword'] = request.keyword
        query['Order'] = request.order
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_process_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    def describe_rdstables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rdstables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rdstables_with_options(request, runtime)

    def describe_rdsvpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSVpc',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rdsvpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsvpc_with_options(request, runtime)

    def describe_rdsschemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSschemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSschemasResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rdsschemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsschemas_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_slow_log_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_log_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    def describe_syn_db_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_syn_db_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_db_tables_with_options(request, runtime)

    def describe_syn_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbs',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_syn_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_dbs_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def describe_transfer_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTransferHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTransferHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_transfer_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_history_with_options(request, runtime)

    def kill_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def kill_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    def modify_account_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterId'] = request.dbcluster_id
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    def modify_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        query['DBClusterId'] = request.dbcluster_id
        query['ModifyMode'] = request.modify_mode
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    def modify_dbcluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbcluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    def modify_dbcluster_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbcluster_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    def modify_dbcluster_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    def modify_dbconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    def modify_rdsto_clickhouse_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsSynDb'] = request.rds_syn_db
        query['RdsSynTables'] = request.rds_syn_tables
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rdsto_clickhouse_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_rdsto_clickhouse_db_with_options(request, runtime)

    def operate_log_hub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['AccessSecret'] = request.access_secret
        query['Create'] = request.create
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['DeliverTime'] = request.deliver_time
        query['Description'] = request.description
        query['DomainUrl'] = request.domain_url
        query['FilterDirtyData'] = request.filter_dirty_data
        query['LogHubStores'] = request.log_hub_stores
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Password'] = request.password
        query['ProjectName'] = request.project_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        query['TaskId'] = request.task_id
        query['UseLorne'] = request.use_lorne
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLogHub',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_log_hub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    def operate_lorne_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['LorneStatus'] = request.lorne_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLorneTaskStatus',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_lorne_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_lorne_task_status_with_options(request, runtime)

    def release_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def search_rdstables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.SearchRDSTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_rdstables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_rdstables_with_options(request, runtime)

    def transfer_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransferVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.TransferVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_version_with_options(request, runtime)
