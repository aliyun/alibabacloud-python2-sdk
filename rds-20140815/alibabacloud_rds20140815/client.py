# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds20140815 import models as rds_20140815_models
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
            'cn-qingdao': 'rds.aliyuncs.com',
            'cn-beijing': 'rds.aliyuncs.com',
            'cn-hangzhou': 'rds.aliyuncs.com',
            'cn-shanghai': 'rds.aliyuncs.com',
            'cn-shenzhen': 'rds.aliyuncs.com',
            'cn-heyuan': 'rds.aliyuncs.com',
            'cn-hongkong': 'rds.aliyuncs.com',
            'ap-southeast-1': 'rds.aliyuncs.com',
            'us-west-1': 'rds.aliyuncs.com',
            'us-east-1': 'rds.aliyuncs.com',
            'cn-shanghai-finance-1': 'rds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'rds.aliyuncs.com',
            'cn-north-2-gov-1': 'rds.aliyuncs.com',
            'ap-northeast-2-pop': 'rds.aliyuncs.com',
            'cn-beijing-finance-1': 'rds.aliyuncs.com',
            'cn-beijing-finance-pop': 'rds.aliyuncs.com',
            'cn-beijing-gov-1': 'rds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'rds.aliyuncs.com',
            'cn-edge-1': 'rds.aliyuncs.com',
            'cn-fujian': 'rds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'rds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'rds.aliyuncs.com',
            'cn-hangzhou-finance': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'rds.aliyuncs.com',
            'cn-hangzhou-test-306': 'rds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'rds.aliyuncs.com',
            'cn-qingdao-nebula': 'rds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'rds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'rds.aliyuncs.com',
            'cn-shanghai-inner': 'rds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'rds.aliyuncs.com',
            'cn-shenzhen-inner': 'rds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'rds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'rds.aliyuncs.com',
            'cn-wuhan': 'rds.aliyuncs.com',
            'cn-yushanfang': 'rds.aliyuncs.com',
            'cn-zhangbei': 'rds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'rds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'rds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'rds.aliyuncs.com',
            'eu-west-1-oxs': 'rds.aliyuncs.com',
            'rus-west-1-pop': 'rds.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_tags_to_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTagsToResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AddTagsToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags_to_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def allocate_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['NetType'] = request.net_type
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_read_write_splitting_connection_with_options(request, runtime)

    def calculate_dbinstance_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CalculateDBInstanceWeight',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CalculateDBInstanceWeightResponse(),
            self.call_api(params, req, runtime)
        )

    def calculate_dbinstance_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    def cancel_import_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ImportId'] = request.import_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelImport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CancelImportResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_import(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    def check_account_name_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckAccountNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckAccountNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_account_name_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_available_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def check_create_ddr_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCreateDdrDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCreateDdrDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_create_ddr_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    def check_dbname_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckDBNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckDBNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_dbname_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    def check_instance_exist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckInstanceExist',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckInstanceExistResponse(),
            self.call_api(params, req, runtime)
        )

    def check_instance_exist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    def clear_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ClearDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    def clone_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['DbNames'] = request.db_names
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['RestoreTable'] = request.restore_table
        query['TableMeta'] = request.table_meta
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    def clone_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TargetRegionId'] = request.target_region_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    def copy_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    def copy_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SyncUserPrivilege'] = request.sync_user_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AccountDescription'] = request.account_description
        query['AccountType'] = request.account_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupStrategy'] = request.backup_strategy
        query['BackupMethod'] = request.backup_method
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['CharacterSetName'] = request.character_set_name
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BusinessInfo'] = request.business_info
        query['EncryptionKey'] = request.encryption_key
        query['RoleARN'] = request.role_arn
        query['AutoRenew'] = request.auto_renew
        query['Category'] = request.category
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['DBParamGroupId'] = request.dbparam_group_id
        query['DBTimeZone'] = request.dbtime_zone
        query['DBIsIgnoreCase'] = request.dbis_ignore_case
        query['TargetMinorVersion'] = request.target_minor_version
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        query['DryRun'] = request.dry_run
        query['UserBackupId'] = request.user_backup_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    def create_ddr_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDdrInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDdrInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ddr_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    def create_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['HostName'] = request.host_name
        query['ZoneId'] = request.zone_id
        query['VSwitchId'] = request.v_switch_id
        query['HostClass'] = request.host_class
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['UsedTime'] = request.used_time
        query['ClientToken'] = request.client_token
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    def create_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    def create_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['VPCId'] = request.vpcid
        query['HostReplacePolicy'] = request.host_replace_policy
        query['ClientToken'] = request.client_token
        query['OpenPermission'] = request.open_permission
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    def create_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['UserPassword'] = request.user_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_user_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def create_gdn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['PrimaryInstanceName'] = request.primary_instance_name
        query['PrimaryInstanceRegion'] = request.primary_instance_region
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGdnInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gdn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gdn_instance_with_options(request, runtime)

    def create_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupMode'] = request.backup_mode
        query['IsOnlineDB'] = request.is_online_db
        query['CheckDBMode'] = request.check_dbmode
        query['OssObjectPositions'] = request.oss_object_positions
        query['OSSUrls'] = request.ossurls
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    def create_migrate_task_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['TaskType'] = request.task_type
        query['IsOnlineDB'] = request.is_online_db
        query['OSSUrls'] = request.ossurls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTaskForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_migrate_task_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_for_sqlserver_with_options(request, runtime)

    def create_online_database_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['MigrateTaskId'] = request.migrate_task_id
        query['CheckDBMode'] = request.check_dbmode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOnlineDatabaseTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOnlineDatabaseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_online_database_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    def create_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['Parameters'] = request.parameters
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    def create_read_only_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['GdnInstanceName'] = request.gdn_instance_name
        query['TddlBizType'] = request.tddl_biz_type
        query['TddlRegionConfig'] = request.tddl_region_config
        query['InstructionSetArch'] = request.instruction_set_arch
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateReadOnlyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_read_only_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    def create_temp_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTempDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateTempDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_temp_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    def delete_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['DBName'] = request.dbname
        query['BackupTime'] = request.backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    def delete_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    def delete_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    def delete_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    def delete_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    def delete_user_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_backup_file_with_options(request, runtime)

    def descibe_imports_from_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Engine'] = request.engine
        query['ImportId'] = request.import_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescibeImportsFromDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescibeImportsFromDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def descibe_imports_from_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    def describe_available_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_classes_with_options(request, runtime)

    def describe_available_cross_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableCrossRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_cross_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    def describe_available_dedicated_host_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_dedicated_host_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    def describe_available_dedicated_host_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_dedicated_host_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    def describe_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['CrossBackupId'] = request.cross_backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['DispenseMode'] = request.dispense_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['EngineVersion'] = request.engine_version
        query['CommodityCode'] = request.commodity_code
        query['DispenseMode'] = request.dispense_mode
        query['DBInstanceName'] = request.dbinstance_name
        query['Category'] = request.category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    def describe_backup_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['OwnerAccount'] = request.owner_account
        query['CompressType'] = request.compress_type
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_backup_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Flag'] = request.flag
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupJobId'] = request.backup_job_id
        query['BackupMode'] = request.backup_mode
        query['BackupJobStatus'] = request.backup_job_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    def describe_binlog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBinlogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBinlogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_binlog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    def describe_character_set_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Engine'] = request.engine
        query['RegionId'] = request.region_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSetName',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCharacterSetNameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_character_set_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    def describe_collation_time_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCollationTimeZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCollationTimeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_collation_time_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    def describe_cross_backup_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupSetId'] = request.backup_set_id
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossBackupMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossBackupMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_backup_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackupDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_backup_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    def describe_cross_region_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['CrossBackupId'] = request.cross_backup_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    def describe_cross_region_log_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_log_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBStatus'] = request.dbstatus
        query['OwnerAccount'] = request.owner_account
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Expired'] = request.expired
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDetail',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    def describe_dbinstance_encryption_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['EncryptionKey'] = request.encryption_key
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_encryption_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    def describe_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    def describe_dbinstance_iparray_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['WhitelistNetworkType'] = request.whitelist_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIpHostname',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIpHostnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_ip_hostname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    def describe_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Flag'] = request.flag
        query['DBInstanceNetRWSplitType'] = request.dbinstance_net_rwsplit_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_net_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Key'] = request.key
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['InstanceLevel'] = request.instance_level
        query['ConnectionString'] = request.connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbinstances_as_csv_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesAsCsv',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesAsCsvResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_as_csv(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['proxyId'] = request.proxy_id
        query['ExpirePeriod'] = request.expire_period
        query['Expired'] = request.expired
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_by_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    def describe_dbinstances_by_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['SortMethod'] = request.sort_method
        query['SortKey'] = request.sort_key
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_by_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    def describe_dbinstances_for_clone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['NodeType'] = request.node_type
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        query['CurrentInstanceId'] = request.current_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesForClone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesForCloneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_for_clone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_dbinstance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceStatus',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_status_with_options(request, runtime)

    def describe_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    def describe_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    def describe_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectString'] = request.dbproxy_connect_string
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    def describe_dbproxy_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['RegionId'] = request.region_id
        query['MetricsName'] = request.metrics_name
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    def describe_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    def describe_dedicated_host_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ImageCategory'] = request.image_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    def describe_dedicated_host_image_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['HostGroup'] = request.host_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostImageCategories',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_image_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_image_categories_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['OrderId'] = request.order_id
        query['HostType'] = request.host_type
        query['HostStatus'] = request.host_status
        query['AllocationStatus'] = request.allocation_status
        query['ZoneId'] = request.zone_id
        query['DedicatedHostId'] = request.dedicated_host_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_detached_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDetachedBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDetachedBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_detached_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def describe_error_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_error_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_hadiagnose_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hadiagnose_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hadiagnose_config_with_options(request, runtime)

    def describe_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_instance_cross_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_cross_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    def describe_instance_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeywords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    def describe_local_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLocalAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_local_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    def describe_log_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    def describe_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['RestoreType'] = request.restore_type
        query['BackupSetID'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    def describe_migrate_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTaskById',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migrate_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    def describe_migrate_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migrate_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    def describe_migrate_tasks_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasksForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migrate_tasks_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_for_sqlserver_with_options(request, runtime)

    def describe_modify_parameter_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_modify_parameter_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    def describe_oss_downloads_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloads',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_downloads(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    def describe_oss_downloads_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloadsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_downloads_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_for_sqlserver_with_options(request, runtime)

    def describe_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    def describe_parameter_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['Category'] = request.category
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['CommodityCode'] = request.commodity_code
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['InstanceUsedType'] = request.instance_used_type
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_rds_resource_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceNiche'] = request.resource_niche
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsResourceSettings',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRdsResourceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_resource_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    def describe_read_dbinstance_delay_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadInstanceId'] = request.read_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReadDBInstanceDelay',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeReadDBInstanceDelayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_read_dbinstance_delay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    def describe_region_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['InstanceUsedType'] = request.instance_used_type
        query['SpecifyCount'] = request.specify_count
        query['HostType'] = request.host_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegionInfos',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_region_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_region_infos_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['PayType'] = request.pay_type
        query['DBInstanceClass'] = request.dbinstance_class
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['OrderType'] = request.order_type
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_resource_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLHASH'] = request.sqlhash
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_slow_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['SortKey'] = request.sort_key
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    def describe_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    def describe_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    def describe_sqllog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['FileName'] = request.file_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    def describe_sqllog_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLId'] = request.sqlid
        query['QueryKeywords'] = request.query_keywords
        query['StartTime'] = request.start_time
        query['Database'] = request.database
        query['User'] = request.user
        query['Form'] = request.form
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    def describe_sqllog_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    def describe_sqllog_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReports',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_reports_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Status'] = request.status
        query['TaskAction'] = request.task_action
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def destroy_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DestroyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DestroyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def destroy_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    def drop_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DropDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    def evaluate_dedicated_host_instance_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DiskType'] = request.disk_type
        query['DiskSize'] = request.disk_size
        query['InstanceClassNames'] = request.instance_class_names
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EvaluateDedicatedHostInstanceResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def evaluate_dedicated_host_instance_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.evaluate_dedicated_host_instance_resource_with_options(request, runtime)

    def get_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    def get_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    def grant_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['AccountPrivilege'] = request.account_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    def grant_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ExpiredTime'] = request.expired_time
        query['Privileges'] = request.privileges
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    def import_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SourceDBInstanceId'] = request.source_dbinstance_id
        query['DBInfo'] = request.dbinfo
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    def import_user_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EngineVersion'] = request.engine_version
        query['BucketRegion'] = request.bucket_region
        query['BackupFile'] = request.backup_file
        query['Comment'] = request.comment
        query['RestoreSize'] = request.restore_size
        query['Retention'] = request.retention
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def import_user_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_user_backup_file_with_options(request, runtime)

    def list_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['CommodityCode'] = request.commodity_code
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_classes_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['BackupId'] = request.backup_id
        query['OssUrl'] = request.oss_url
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUserBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListUserBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_backup_files_with_options(request, runtime)

    def lock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.LockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    def migrate_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['ZoneIdForLog'] = request.zone_id_for_log
        query['ZoneIdForFollower'] = request.zone_id_for_follower
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    def migrate_security_ipmode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateSecurityIPMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateSecurityIPModeResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_security_ipmode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['ZoneId'] = request.zone_id
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['VSwitchId'] = request.v_switch_id
        query['Category'] = request.category
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountDescription'] = request.account_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EnableEventLog'] = request.enable_event_log
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['BackupLog'] = request.backup_log
        query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        query['OwnerAccount'] = request.owner_account
        query['EnableBackupLog'] = request.enable_backup_log
        query['LocalLogRetentionHours'] = request.local_log_retention_hours
        query['LocalLogRetentionSpace'] = request.local_log_retention_space
        query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        query['LogBackupFrequency'] = request.log_backup_frequency
        query['CompressType'] = request.compress_type
        query['ArchiveBackupRetentionPeriod'] = request.archive_backup_retention_period
        query['ArchiveBackupKeepPolicy'] = request.archive_backup_keep_policy
        query['ArchiveBackupKeepCount'] = request.archive_backup_keep_count
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        query['LogBackupLocalRetentionNumber'] = request.log_backup_local_retention_number
        query['Category'] = request.category
        query['BackupInterval'] = request.backup_interval
        query['BackupMethod'] = request.backup_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_collation_time_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Collation'] = request.collation
        query['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyCollationTimeZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyCollationTimeZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_collation_time_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    def modify_das_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDasInstanceConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDasInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_das_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    def modify_dbdescription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbdescription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AutoUpgradeMinorVersion'] = request.auto_upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgradeMinorVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_auto_upgrade_minor_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    def modify_dbinstance_connection_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_connection_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_connection_string(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceDescription'] = request.dbinstance_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SyncMode'] = request.sync_mode
        query['HAMode'] = request.hamode
        query['DbInstanceId'] = request.db_instance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    def modify_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_network_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    def modify_dbinstance_network_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RetainClassic'] = request.retain_classic
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['InstanceNetworkType'] = request.instance_network_type
        query['ReadWriteSplittingClassicExpiredDays'] = request.read_write_splitting_classic_expired_days
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['ReadWriteSplittingPrivateIpAddress'] = request.read_write_splitting_private_ip_address
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_network_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    def modify_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ProxyConfigurationKey'] = request.proxy_configuration_key
        query['ProxyConfigurationValue'] = request.proxy_configuration_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    def modify_dbinstance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['EngineVersion'] = request.engine_version
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Direction'] = request.direction
        query['SourceBiz'] = request.source_biz
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['OwnerAccount'] = request.owner_account
        query['SSLEnabled'] = request.sslenabled
        query['CAType'] = request.catype
        query['ServerCert'] = request.server_cert
        query['ServerKey'] = request.server_key
        query['ClientCAEnabled'] = request.client_caenabled
        query['ClientCACert'] = request.client_cacert
        query['ClientCrlEnabled'] = request.client_crl_enabled
        query['ClientCertRevocationList'] = request.client_cert_revocation_list
        query['ACL'] = request.acl
        query['ReplicationACL'] = request.replication_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def modify_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TDEStatus'] = request.tdestatus
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        query['EncryptionKey'] = request.encryption_key
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    def modify_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigDBProxyService'] = request.config_dbproxy_service
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['RegionId'] = request.region_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    def modify_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConfigDBProxyFeatures'] = request.config_dbproxy_features
        query['RegionId'] = request.region_id
        query['ReadOnlyInstanceMaxDelayTime'] = request.read_only_instance_max_delay_time
        query['ReadOnlyInstanceDistributionType'] = request.read_only_instance_distribution_type
        query['ReadOnlyInstanceWeight'] = request.read_only_instance_weight
        query['DBInstanceId'] = request.dbinstance_id
        query['DbEndpointOperator'] = request.db_endpoint_operator
        query['DbEndpointAliases'] = request.db_endpoint_aliases
        query['DbEndpointType'] = request.db_endpoint_type
        query['DbEndpointReadWriteMode'] = request.db_endpoint_read_write_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyNewConnectString'] = request.dbproxy_new_connect_string
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    def modify_dbproxy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['EffectiveTime'] = request.effective_time
        query['EffectiveSpecificTime'] = request.effective_specific_time
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbProxyEndpointId'] = request.db_proxy_endpoint_id
        query['DbProxyConnectString'] = request.db_proxy_connect_string
        query['DbProxySslEnabled'] = request.db_proxy_ssl_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    def modify_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostName'] = request.host_name
        query['AllocationStatus'] = request.allocation_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['HostReplacePolicy'] = request.host_replace_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostGroupAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    def modify_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['OldPassword'] = request.old_password
        query['NewPassword'] = request.new_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_user_with_options(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIpHosts'] = request.security_ip_hosts
        query['WhiteListGroupName'] = request.white_list_group_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def modify_hadiagnose_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TcpConnectionType'] = request.tcp_connection_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hadiagnose_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hadiagnose_config_with_options(request, runtime)

    def modify_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['HAConfig'] = request.haconfig
        query['ManualHATime'] = request.manual_hatime
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['Duration'] = request.duration
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def modify_instance_cross_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupType'] = request.cross_backup_type
        query['LogBackupEnabled'] = request.log_backup_enabled
        query['BackupEnabled'] = request.backup_enabled
        query['CrossBackupRegion'] = request.cross_backup_region
        query['RetentType'] = request.retent_type
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_cross_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Parameters'] = request.parameters
        query['Forcerestart'] = request.forcerestart
        query['OwnerAccount'] = request.owner_account
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        query['Parameters'] = request.parameters
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadSQLReplicationTime'] = request.read_sqlreplication_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadonlyInstanceDelayReplicationTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_readonly_instance_delay_replication_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    def modify_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    def modify_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIps'] = request.security_ips
        query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        query['SecurityIPType'] = request.security_iptype
        query['WhitelistNetworkType'] = request.whitelist_network_type
        query['ModifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLCollectorStatus'] = request.sqlcollector_status
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    def modify_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigValue'] = request.config_value
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    def purge_dbinstance_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PurgeDBInstanceLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.PurgeDBInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def purge_dbinstance_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    def rebuild_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['RebuildNodeType'] = request.rebuild_node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RebuildDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RebuildDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def rebuild_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    def recovery_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RecoveryDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RecoveryDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def recovery_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    def release_instance_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['InstanceNetworkType'] = request.instance_network_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstanceConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def release_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    def remove_tags_from_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RemoveTagsFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags_from_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['AutoPay'] = request.auto_pay
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def replace_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReplaceDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReplaceDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    def reset_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def restart_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    def restore_ddr_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['RestoreType'] = request.restore_type
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreDdrTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreDdrTableResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_ddr_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    def restore_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreTableResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    def revoke_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    def revoke_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    def start_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['TargetDBInstanceClass'] = request.target_dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['DBInstanceTransType'] = request.dbinstance_trans_type
        query['Storage'] = request.storage
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    def stop_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StopDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    def switch_dbinstance_hawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['NodeId'] = request.node_id
        query['Force'] = request.force
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_ha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    def switch_dbinstance_net_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['ConnectionStringType'] = request.connection_string_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_net_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    def switch_dbinstance_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceVpc',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def terminate_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TerminateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TerminateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    def transform_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransformDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TransformDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def transform_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    def unlock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnlockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UnlockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_user_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpdateUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_backup_file_with_options(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBProxyInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbproxy_instance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)
