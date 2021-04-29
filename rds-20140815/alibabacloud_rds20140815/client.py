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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.AddTagsToResourceResponse(),
            self.do_rpcrequest('AddTagsToResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags_to_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def allocate_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateReadWriteSplittingConnectionResponse(),
            self.do_rpcrequest('AllocateReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_read_write_splitting_connection_with_options(request, runtime)

    def calculate_dbinstance_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CalculateDBInstanceWeightResponse(),
            self.do_rpcrequest('CalculateDBInstanceWeight', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def calculate_dbinstance_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    def cancel_import_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CancelImportResponse(),
            self.do_rpcrequest('CancelImport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_import(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    def check_account_name_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckAccountNameAvailableResponse(),
            self.do_rpcrequest('CheckAccountNameAvailable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_account_name_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_available_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCloudResourceAuthorizedResponse(),
            self.do_rpcrequest('CheckCloudResourceAuthorized', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def check_create_ddr_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCreateDdrDBInstanceResponse(),
            self.do_rpcrequest('CheckCreateDdrDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_create_ddr_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    def check_dbname_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckDBNameAvailableResponse(),
            self.do_rpcrequest('CheckDBNameAvailable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_dbname_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    def check_instance_exist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckInstanceExistResponse(),
            self.do_rpcrequest('CheckInstanceExist', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_instance_exist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    def clear_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ClearDedicatedHostResponse(),
            self.do_rpcrequest('ClearDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    def clone_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneDBInstanceResponse(),
            self.do_rpcrequest('CloneDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    def clone_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneParameterGroupResponse(),
            self.do_rpcrequest('CloneParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    def copy_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseResponse(),
            self.do_rpcrequest('CopyDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    def copy_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseBetweenInstancesResponse(),
            self.do_rpcrequest('CopyDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateBackupResponse(),
            self.do_rpcrequest('CreateBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDatabaseResponse(),
            self.do_rpcrequest('CreateDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBProxyEndpointAddressResponse(),
            self.do_rpcrequest('CreateDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    def create_ddr_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDdrInstanceResponse(),
            self.do_rpcrequest('CreateDdrInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ddr_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    def create_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostResponse(),
            self.do_rpcrequest('CreateDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    def create_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostAccountResponse(),
            self.do_rpcrequest('CreateDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    def create_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostGroupResponse(),
            self.do_rpcrequest('CreateDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    def create_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostUserResponse(),
            self.do_rpcrequest('CreateDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_user_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDiagnosticReportResponse(),
            self.do_rpcrequest('CreateDiagnosticReport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def create_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskResponse(),
            self.do_rpcrequest('CreateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    def create_migrate_task_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskForSQLServerResponse(),
            self.do_rpcrequest('CreateMigrateTaskForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_migrate_task_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_for_sqlserver_with_options(request, runtime)

    def create_online_database_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOnlineDatabaseTaskResponse(),
            self.do_rpcrequest('CreateOnlineDatabaseTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_online_database_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    def create_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateParameterGroupResponse(),
            self.do_rpcrequest('CreateParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    def create_read_only_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateReadOnlyDBInstanceResponse(),
            self.do_rpcrequest('CreateReadOnlyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_read_only_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    def create_temp_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateTempDBInstanceResponse(),
            self.do_rpcrequest('CreateTempDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_temp_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupResponse(),
            self.do_rpcrequest('DeleteBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    def delete_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupFileResponse(),
            self.do_rpcrequest('DeleteBackupFile', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    def delete_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDatabaseResponse(),
            self.do_rpcrequest('DeleteDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBProxyEndpointAddressResponse(),
            self.do_rpcrequest('DeleteDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    def delete_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostAccountResponse(),
            self.do_rpcrequest('DeleteDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    def delete_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostGroupResponse(),
            self.do_rpcrequest('DeleteDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    def delete_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteParameterGroupResponse(),
            self.do_rpcrequest('DeleteParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    def descibe_imports_from_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescibeImportsFromDatabaseResponse(),
            self.do_rpcrequest('DescibeImportsFromDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def descibe_imports_from_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActionEventPolicyResponse(),
            self.do_rpcrequest('DescribeActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    def describe_available_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableClassesResponse(),
            self.do_rpcrequest('DescribeAvailableClasses', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_classes_with_options(request, runtime)

    def describe_available_cross_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableCrossRegionResponse(),
            self.do_rpcrequest('DescribeAvailableCrossRegion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_cross_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    def describe_available_dedicated_host_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostClasses', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    def describe_available_dedicated_host_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    def describe_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableRecoveryTimeResponse(),
            self.do_rpcrequest('DescribeAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableZonesResponse(),
            self.do_rpcrequest('DescribeAvailableZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    def describe_backup_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupDatabaseResponse(),
            self.do_rpcrequest('DescribeBackupDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_backup_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupTasksResponse(),
            self.do_rpcrequest('DescribeBackupTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    def describe_binlog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBinlogFilesResponse(),
            self.do_rpcrequest('DescribeBinlogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_binlog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    def describe_character_set_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCharacterSetNameResponse(),
            self.do_rpcrequest('DescribeCharacterSetName', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_character_set_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    def describe_collation_time_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCollationTimeZonesResponse(),
            self.do_rpcrequest('DescribeCollationTimeZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_collation_time_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    def describe_cross_backup_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossBackupMetaListResponse(),
            self.do_rpcrequest('DescribeCrossBackupMetaList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_backup_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse(),
            self.do_rpcrequest('DescribeCrossRegionBackupDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_backup_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    def describe_cross_region_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupsResponse(),
            self.do_rpcrequest('DescribeCrossRegionBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    def describe_cross_region_log_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse(),
            self.do_rpcrequest('DescribeCrossRegionLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_log_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDatabasesResponse(),
            self.do_rpcrequest('DescribeDatabases', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceDetailResponse(),
            self.do_rpcrequest('DescribeDBInstanceDetail', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    def describe_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceHAConfigResponse(),
            self.do_rpcrequest('DescribeDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    def describe_dbinstance_iparray_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIPArrayListResponse(),
            self.do_rpcrequest('DescribeDBInstanceIPArrayList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_iparray_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIpHostnameResponse(),
            self.do_rpcrequest('DescribeDBInstanceIpHostname', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ip_hostname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    def describe_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMonitorResponse(),
            self.do_rpcrequest('DescribeDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoResponse(),
            self.do_rpcrequest('DescribeDBInstanceNetInfo', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_net_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePerformanceResponse(),
            self.do_rpcrequest('DescribeDBInstancePerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse(),
            self.do_rpcrequest('DescribeDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbinstances_as_csv_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesAsCsvResponse(),
            self.do_rpcrequest('DescribeDBInstancesAsCsv', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_as_csv(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByExpireTimeResponse(),
            self.do_rpcrequest('DescribeDBInstancesByExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_by_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    def describe_dbinstances_by_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByPerformanceResponse(),
            self.do_rpcrequest('DescribeDBInstancesByPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_by_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    def describe_dbinstances_for_clone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesForCloneResponse(),
            self.do_rpcrequest('DescribeDBInstancesForClone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_for_clone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceSSLResponse(),
            self.do_rpcrequest('DescribeDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceTDEResponse(),
            self.do_rpcrequest('DescribeDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    def describe_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyResponse(),
            self.do_rpcrequest('DescribeDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    def describe_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyEndpointResponse(),
            self.do_rpcrequest('DescribeDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    def describe_dbproxy_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyPerformanceResponse(),
            self.do_rpcrequest('DescribeDBProxyPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    def describe_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostAttributeResponse(),
            self.do_rpcrequest('DescribeDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    def describe_dedicated_host_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostGroupsResponse(),
            self.do_rpcrequest('DescribeDedicatedHostGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    def describe_dedicated_host_image_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse(),
            self.do_rpcrequest('DescribeDedicatedHostImageCategories', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_image_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_image_categories_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeDedicatedHosts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_detached_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDetachedBackupsResponse(),
            self.do_rpcrequest('DescribeDetachedBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_detached_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDiagnosticReportListResponse(),
            self.do_rpcrequest('DescribeDiagnosticReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse(),
            self.do_rpcrequest('DescribeDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def describe_error_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeErrorLogsResponse(),
            self.do_rpcrequest('DescribeErrorLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_error_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeEventsResponse(),
            self.do_rpcrequest('DescribeEvents', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_hadiagnose_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHADiagnoseConfigResponse(),
            self.do_rpcrequest('DescribeHADiagnoseConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hadiagnose_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hadiagnose_config_with_options(request, runtime)

    def describe_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHASwitchConfigResponse(),
            self.do_rpcrequest('DescribeHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_instance_cross_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse(),
            self.do_rpcrequest('DescribeInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_cross_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    def describe_instance_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceKeywordsResponse(),
            self.do_rpcrequest('DescribeInstanceKeywords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    def describe_local_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse(),
            self.do_rpcrequest('DescribeLocalAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_local_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    def describe_log_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLogBackupFilesResponse(),
            self.do_rpcrequest('DescribeLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    def describe_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMetaListResponse(),
            self.do_rpcrequest('DescribeMetaList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    def describe_migrate_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTaskByIdResponse(),
            self.do_rpcrequest('DescribeMigrateTaskById', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migrate_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    def describe_migrate_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksResponse(),
            self.do_rpcrequest('DescribeMigrateTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migrate_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    def describe_migrate_tasks_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksForSQLServerResponse(),
            self.do_rpcrequest('DescribeMigrateTasksForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migrate_tasks_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_for_sqlserver_with_options(request, runtime)

    def describe_modify_parameter_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyParameterLogResponse(),
            self.do_rpcrequest('DescribeModifyParameterLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_modify_parameter_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    def describe_oss_downloads_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsResponse(),
            self.do_rpcrequest('DescribeOssDownloads', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_downloads(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    def describe_oss_downloads_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsForSQLServerResponse(),
            self.do_rpcrequest('DescribeOssDownloadsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_downloads_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_for_sqlserver_with_options(request, runtime)

    def describe_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupResponse(),
            self.do_rpcrequest('DescribeParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    def describe_parameter_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupsResponse(),
            self.do_rpcrequest('DescribeParameterGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterTemplatesResponse(),
            self.do_rpcrequest('DescribeParameterTemplates', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_rds_resource_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRdsResourceSettingsResponse(),
            self.do_rpcrequest('DescribeRdsResourceSettings', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_resource_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    def describe_read_dbinstance_delay_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeReadDBInstanceDelayResponse(),
            self.do_rpcrequest('DescribeReadDBInstanceDelay', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_read_dbinstance_delay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.DescribeRenewalPriceResponse(),
            self.do_rpcrequest('DescribeRenewalPrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_resource_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeResourceUsageResponse(),
            self.do_rpcrequest('DescribeResourceUsage', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecurityGroupConfigurationResponse(),
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_slow_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogsResponse(),
            self.do_rpcrequest('DescribeSlowLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    def describe_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorPolicyResponse(),
            self.do_rpcrequest('DescribeSQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    def describe_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorRetentionResponse(),
            self.do_rpcrequest('DescribeSQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    def describe_sqllog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogFilesResponse(),
            self.do_rpcrequest('DescribeSQLLogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    def describe_sqllog_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogRecordsResponse(),
            self.do_rpcrequest('DescribeSQLLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    def describe_sqllog_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportListResponse(),
            self.do_rpcrequest('DescribeSQLLogReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    def describe_sqllog_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportsResponse(),
            self.do_rpcrequest('DescribeSQLLogReports', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_reports_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTasksResponse(),
            self.do_rpcrequest('DescribeTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def destroy_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DestroyDBInstanceResponse(),
            self.do_rpcrequest('DestroyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    def drop_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.DropDedicatedHostUserResponse(),
            self.do_rpcrequest('DropDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    def evaluate_dedicated_host_instance_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse(),
            self.do_rpcrequest('EvaluateDedicatedHostInstanceResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def evaluate_dedicated_host_instance_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.evaluate_dedicated_host_instance_resource_with_options(request, runtime)

    def get_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDbProxyInstanceSslResponse(),
            self.do_rpcrequest('GetDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    def grant_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantAccountPrivilegeResponse(),
            self.do_rpcrequest('GrantAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    def grant_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantOperatorPermissionResponse(),
            self.do_rpcrequest('GrantOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    def import_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportDatabaseBetweenInstancesResponse(),
            self.do_rpcrequest('ImportDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def lock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.LockAccountResponse(),
            self.do_rpcrequest('LockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    def migrate_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateDBInstanceResponse(),
            self.do_rpcrequest('MigrateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    def migrate_security_ipmode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateSecurityIPModeResponse(),
            self.do_rpcrequest('MigrateSecurityIPMode', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_security_ipmode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateToOtherZoneResponse(),
            self.do_rpcrequest('MigrateToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActionEventPolicyResponse(),
            self.do_rpcrequest('ModifyActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_collation_time_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyCollationTimeZoneResponse(),
            self.do_rpcrequest('ModifyCollationTimeZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_collation_time_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    def modify_das_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDasInstanceConfigResponse(),
            self.do_rpcrequest('ModifyDasInstanceConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_das_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    def modify_dbdescription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBDescriptionResponse(),
            self.do_rpcrequest('ModifyDBDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbdescription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse(),
            self.do_rpcrequest('ModifyDBInstanceAutoUpgradeMinorVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_auto_upgrade_minor_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    def modify_dbinstance_connection_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionModeResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionMode', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionStringResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceHAConfigResponse(),
            self.do_rpcrequest('ModifyDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.ModifyDBInstanceMonitorResponse(),
            self.do_rpcrequest('ModifyDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceNetworkExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    def modify_dbinstance_network_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkTypeResponse(),
            self.do_rpcrequest('ModifyDBInstanceNetworkType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    def modify_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstancePayTypeResponse(),
            self.do_rpcrequest('ModifyDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse(),
            self.do_rpcrequest('ModifyDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    def modify_dbinstance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSpecResponse(),
            self.do_rpcrequest('ModifyDBInstanceSpec', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSSLResponse(),
            self.do_rpcrequest('ModifyDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def modify_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceTDEResponse(),
            self.do_rpcrequest('ModifyDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    def modify_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyResponse(),
            self.do_rpcrequest('ModifyDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    def modify_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointResponse(),
            self.do_rpcrequest('ModifyDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointAddressResponse(),
            self.do_rpcrequest('ModifyDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    def modify_dbproxy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyInstanceResponse(),
            self.do_rpcrequest('ModifyDBProxyInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDbProxyInstanceSslResponse(),
            self.do_rpcrequest('ModifyDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    def modify_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAccountResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostGroupAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    def modify_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostUserResponse(),
            self.do_rpcrequest('ModifyDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_user_with_options(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse(),
            self.do_rpcrequest('ModifyDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def modify_hadiagnose_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHADiagnoseConfigResponse(),
            self.do_rpcrequest('ModifyHADiagnoseConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hadiagnose_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hadiagnose_config_with_options(request, runtime)

    def modify_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHASwitchConfigResponse(),
            self.do_rpcrequest('ModifyHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def modify_instance_cross_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse(),
            self.do_rpcrequest('ModifyInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_cross_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterResponse(),
            self.do_rpcrequest('ModifyParameter', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterGroupResponse(),
            self.do_rpcrequest('ModifyParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse(),
            self.do_rpcrequest('ModifyReadonlyInstanceDelayReplicationTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_readonly_instance_delay_replication_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    def modify_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadWriteSplittingConnectionResponse(),
            self.do_rpcrequest('ModifyReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyResourceGroupResponse(),
            self.do_rpcrequest('ModifyResourceGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.ModifySecurityGroupConfigurationResponse(),
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorPolicyResponse(),
            self.do_rpcrequest('ModifySQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    def modify_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorRetentionResponse(),
            self.do_rpcrequest('ModifySQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    def purge_dbinstance_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.PurgeDBInstanceLogResponse(),
            self.do_rpcrequest('PurgeDBInstanceLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purge_dbinstance_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    def rebuild_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RebuildDBInstanceResponse(),
            self.do_rpcrequest('RebuildDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebuild_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    def recovery_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RecoveryDBInstanceResponse(),
            self.do_rpcrequest('RecoveryDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recovery_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    def release_instance_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstanceConnectionResponse(),
            self.do_rpcrequest('ReleaseInstanceConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstancePublicConnectionResponse(),
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def release_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse(),
            self.do_rpcrequest('ReleaseReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    def remove_tags_from_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RemoveTagsFromResourceResponse(),
            self.do_rpcrequest('RemoveTagsFromResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags_from_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def replace_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ReplaceDedicatedHostResponse(),
            self.do_rpcrequest('ReplaceDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    def reset_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountResponse(),
            self.do_rpcrequest('ResetAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def restart_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDedicatedHostResponse(),
            self.do_rpcrequest('RestartDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    def restore_ddr_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreDdrTableResponse(),
            self.do_rpcrequest('RestoreDdrTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_ddr_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    def restore_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreTableResponse(),
            self.do_rpcrequest('RestoreTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    def revoke_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeAccountPrivilegeResponse(),
            self.do_rpcrequest('RevokeAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    def revoke_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeOperatorPermissionResponse(),
            self.do_rpcrequest('RevokeOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    def start_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.StartDBInstanceResponse(),
            self.do_rpcrequest('StartDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    def stop_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.StopDBInstanceResponse(),
            self.do_rpcrequest('StopDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    def switch_dbinstance_hawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceHAResponse(),
            self.do_rpcrequest('SwitchDBInstanceHA', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_ha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    def switch_dbinstance_net_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceNetTypeResponse(),
            self.do_rpcrequest('SwitchDBInstanceNetType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_net_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    def switch_dbinstance_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceVpcResponse(),
            self.do_rpcrequest('SwitchDBInstanceVpc', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def terminate_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.TerminateMigrateTaskResponse(),
            self.do_rpcrequest('TerminateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    def transform_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.TransformDBInstancePayTypeResponse(),
            self.do_rpcrequest('TransformDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    def unlock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.UnlockAccountResponse(),
            self.do_rpcrequest('UnlockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.UpgradeDBInstanceEngineVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceEngineVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            rds_20140815_models.UpgradeDBInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBProxyInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbproxy_instance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)
