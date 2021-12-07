# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_drds20190123 import models as drds_20190123_models
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
            'ap-northeast-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'drds.ap-southeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'drds.aliyuncs.com',
            'cn-beijing-finance-pop': 'drds.aliyuncs.com',
            'cn-beijing-gov-1': 'drds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'drds.aliyuncs.com',
            'cn-chengdu': 'drds.aliyuncs.com',
            'cn-edge-1': 'drds.aliyuncs.com',
            'cn-fujian': 'drds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'drds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'drds.aliyuncs.com',
            'cn-hangzhou-finance': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'drds.aliyuncs.com',
            'cn-hangzhou-test-306': 'drds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'drds.aliyuncs.com',
            'cn-qingdao-nebula': 'drds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'drds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'drds.aliyuncs.com',
            'cn-shanghai-inner': 'drds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'drds.aliyuncs.com',
            'cn-shenzhen-inner': 'drds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'drds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'drds.aliyuncs.com',
            'cn-wuhan': 'drds.aliyuncs.com',
            'cn-yushanfang': 'drds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'drds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'drds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'drds.aliyuncs.com',
            'eu-central-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'drds.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'drds.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'drds.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('drds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeAccountPassword',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def change_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_account_password_with_options(request, runtime)

    def change_instance_azone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['DrdsRegionId'] = request.drds_region_id
        query['OriginAzoneId'] = request.origin_azone_id
        query['TargetAzoneId'] = request.target_azone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeInstanceAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    def change_instance_azone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_instance_azone_with_options(request, runtime)

    def change_instance_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RetainClassic'] = request.retain_classic
        query['SrcInstanceNetworkType'] = request.src_instance_network_type
        query['VpcId'] = request.vpc_id
        query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeInstanceNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def change_instance_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_instance_network_with_options(request, runtime)

    def check_drds_db_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckDrdsDbName',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            self.call_api(params, req, runtime)
        )

    def check_drds_db_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_drds_db_name_with_options(request, runtime)

    def check_expand_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckExpandStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def check_expand_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_expand_status_with_options(request, runtime)

    def check_rds_super_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbInstanceId'] = request.db_instance_id
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckRdsSuperAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckRdsSuperAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def check_rds_super_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_rds_super_account_with_options(request, runtime)

    def check_sql_audit_enable_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckSqlAuditEnableStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def check_sql_audit_enable_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_sql_audit_enable_status_with_options(request, runtime)

    def configure_drds_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstance'] = request.db_instance
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigureDrdsDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ConfigureDrdsDbInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_drds_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_drds_db_instances_with_options(request, runtime)

    def create_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbInstType'] = request.db_inst_type
        query['DbInstanceIsCreating'] = request.db_instance_is_creating
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Encode'] = request.encode
        query['InstDbName'] = request.inst_db_name
        query['Password'] = request.password
        query['RdsInstance'] = request.rds_instance
        query['RdsSuperAccount'] = request.rds_super_account
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    def create_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbwith_options(request, runtime)

    def create_drds_dbpre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbInstType'] = request.db_inst_type
        query['DbInstanceIsCreating'] = request.db_instance_is_creating
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Encode'] = request.encode
        query['InstDbName'] = request.inst_db_name
        query['Password'] = request.password
        query['RdsInstance'] = request.rds_instance
        query['RdsSuperAccount'] = request.rds_super_account
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsDBPreCheck',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def create_drds_dbpre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpre_check_with_options(request, runtime)

    def create_drds_dbpreview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbInstType'] = request.db_inst_type
        query['DbInstanceIsCreating'] = request.db_instance_is_creating
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['InstDbName'] = request.inst_db_name
        query['OrderId'] = request.order_id
        query['RdsInstance'] = request.rds_instance
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsDBPreview',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    def create_drds_dbpreview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpreview_with_options(request, runtime)

    def create_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Duration'] = request.duration
        query['InstanceSeries'] = request.instance_series
        query['IsAutoRenew'] = request.is_auto_renew
        query['MasterInstId'] = request.master_inst_id
        query['MySQLVersion'] = request.my_sqlversion
        query['PayType'] = request.pay_type
        query['PricingCycle'] = request.pricing_cycle
        query['Quantity'] = request.quantity
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Specification'] = request.specification
        query['Type'] = request.type
        query['VpcId'] = request.vpc_id
        query['VswitchId'] = request.vswitch_id
        query['ZoneId'] = request.zone_id
        query['isHa'] = request.is_ha
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_instance_with_options(request, runtime)

    def create_evaluate_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AvgQpsGrowthScale'] = request.avg_qps_growth_scale
        query['DataGrowthScale'] = request.data_growth_scale
        query['DbInfo'] = request.db_info
        query['EvaluateHours'] = request.evaluate_hours
        query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEvaluatePreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluatePreCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_evaluate_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_pre_check_task_with_options(request, runtime)

    def create_instance_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbPrivilege'] = request.db_privilege
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_account_with_options(request, runtime)

    def create_instance_internet_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_internet_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_internet_address_with_options(request, runtime)

    def create_order_for_rds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Params'] = request.params
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOrderForRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order_for_rds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_rds_with_options(request, runtime)

    def create_shard_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['SourceTableName'] = request.source_table_name
        query['TargetTableName'] = request.target_table_name
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_shard_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_shard_task_with_options(request, runtime)

    def describe_back_menu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackMenu',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_back_menu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_menu_with_options(request, runtime)

    def describe_backup_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PreferredRestoreTime'] = request.preferred_restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    def describe_backup_local_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_local(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_local_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupSets',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_sets_with_options(request, runtime)

    def describe_backup_times_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupTimes',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_times(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_times_with_options(request, runtime)

    def describe_broadcast_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageSize'] = request.page_size
        query['Query'] = request.query
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_broadcast_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_broadcast_tables_with_options(request, runtime)

    def describe_data_import_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataImportTaskReport',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTaskReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_import_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_task_report_with_options(request, runtime)

    def describe_db_instance_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbInstType'] = request.db_inst_type
        query['DbInstanceId'] = request.db_instance_id
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDbInstanceDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_db_instance_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instance_dbs_with_options(request, runtime)

    def describe_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instances_with_options(request, runtime)

    def describe_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbwith_options(request, runtime)

    def describe_drds_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstanceId'] = request.db_instance_id
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBCluster',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbcluster_with_options(request, runtime)

    def describe_drds_dbip_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_dbip_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbip_white_list_with_options(request, runtime)

    def describe_drds_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbs_with_options(request, runtime)

    def describe_drds_db_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstanceId'] = request.db_instance_id
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instance_with_options(request, runtime)

    def describe_drds_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instances_with_options(request, runtime)

    def describe_drds_db_rds_name_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbRdsNameList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db_rds_name_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_rds_name_list_with_options(request, runtime)

    def describe_drds_db_spec_and_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBName'] = request.dbname
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbSpecAndPrice',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db_spec_and_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_spec_and_price_with_options(request, runtime)

    def describe_drds_db_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_db_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_tasks_with_options(request, runtime)

    def describe_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_with_options(request, runtime)

    def describe_drds_instance_db_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['RegionId'] = request.region_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceDbMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instance_db_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_db_monitor_with_options(request, runtime)

    def describe_drds_instance_level_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceLevelTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instance_level_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_level_tasks_with_options(request, runtime)

    def describe_drds_instance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['PeriodMultiple'] = request.period_multiple
        query['RegionId'] = request.region_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_monitor_with_options(request, runtime)

    def describe_drds_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_version_with_options(request, runtime)

    def describe_drds_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['Expired'] = request.expired
        query['Mix'] = request.mix
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProductVersion'] = request.product_version
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Tag'] = request.tag
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instances_with_options(request, runtime)

    def describe_drds_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['ParamLevel'] = request.param_level
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_params_with_options(request, runtime)

    def describe_drds_rds_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsRdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_rds_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_rds_instances_with_options(request, runtime)

    def describe_drds_sharding_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DbNamePattern'] = request.db_name_pattern
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsShardingDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_sharding_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sharding_dbs_with_options(request, runtime)

    def describe_drds_slow_sqls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['ExeTime'] = request.exe_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSlowSqls',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_slow_sqls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_slow_sqls_with_options(request, runtime)

    def describe_drds_sql_audit_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSqlAuditStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_sql_audit_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sql_audit_status_with_options(request, runtime)

    def describe_drds_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drds_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_tasks_with_options(request, runtime)

    def describe_expand_logic_table_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeExpandLogicTableInfoList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_expand_logic_table_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_expand_logic_table_info_list_with_options(request, runtime)

    def describe_hi_store_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['HistoreInstanceId'] = request.histore_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHiStoreInstanceInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHiStoreInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hi_store_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_store_instance_info_with_options(request, runtime)

    def describe_hot_db_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotDbList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hot_db_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_db_list_with_options(request, runtime)

    def describe_inst_db_log_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstDbLogInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inst_db_log_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_log_info_with_options(request, runtime)

    def describe_inst_db_sls_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstDbSlsInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inst_db_sls_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_sls_info_with_options(request, runtime)

    def describe_instance_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAccounts',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_accounts_with_options(request, runtime)

    def describe_instance_menu_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMenuSwitch',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceMenuSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_menu_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_menu_switch_with_options(request, runtime)

    def describe_instance_switch_azone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_switch_azone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_azone_with_options(request, runtime)

    def describe_instance_switch_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_switch_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_network_with_options(request, runtime)

    def describe_pre_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePreCheckResult',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pre_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_result_with_options(request, runtime)

    def describe_rdsperformance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Keys'] = request.keys
        query['RdsInstanceId'] = request.rds_instance_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSPerformance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rdsperformance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsperformance_with_options(request, runtime)

    def describe_rds_commodity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CommodityCode'] = request.commodity_code
        query['DrdsInstanceId'] = request.drds_instance_id
        query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsCommodity',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_commodity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_commodity_with_options(request, runtime)

    def describe_rds_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RdsInstanceId'] = request.rds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_drds_dbwith_options(request, runtime)

    def describe_rds_performance_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RdsInstanceId'] = request.rds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsPerformanceSummary',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_performance_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_performance_summary_with_options(request, runtime)

    def describe_rds_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Params'] = request.params
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsPrice',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_price_with_options(request, runtime)

    def describe_rds_read_only_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RdsInstanceId'] = request.rds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsReadOnly',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsReadOnlyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_read_only(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_read_only_with_options(request, runtime)

    def describe_rds_super_account_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RdsInstance'] = request.rds_instance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsSuperAccountInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_super_account_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_super_account_instances_with_options(request, runtime)

    def describe_rds_vpc_for_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcForZone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsVpcForZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_vpc_for_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpc_for_zone_with_options(request, runtime)

    def describe_recycle_bin_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recycle_bin_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_status_with_options(request, runtime)

    def describe_recycle_bin_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recycle_bin_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_tables_with_options(request, runtime)

    def describe_restore_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupDbNames'] = request.backup_db_names
        query['BackupId'] = request.backup_id
        query['BackupLevel'] = request.backup_level
        query['BackupMode'] = request.backup_mode
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRestoreOrder',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_order_with_options(request, runtime)

    def describe_shard_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['SourceTableName'] = request.source_table_name
        query['TargetTableName'] = request.target_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_shard_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_info_with_options(request, runtime)

    def describe_shard_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageSize'] = request.page_size
        query['Query'] = request.query
        query['RegionId'] = request.region_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_shard_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_list_with_options(request, runtime)

    def describe_sql_flashbak_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSqlFlashbakTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sql_flashbak_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_flashbak_task_with_options(request, runtime)

    def describe_src_rds_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PartitionMapping'] = request.partition_mapping
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSrcRdsList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSrcRdsListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_src_rds_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_src_rds_list_with_options(request, runtime)

    def describe_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    def describe_table_list_by_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageSize'] = request.page_size
        query['Query'] = request.query
        query['RegionId'] = request.region_id
        query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTableListByType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_table_list_by_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_list_by_type_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PageSize'] = request.page_size
        query['Query'] = request.query
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def disable_sql_audit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_sql_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    def enable_instance_ipv_6address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableInstanceIpv6Address',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_instance_ipv_6address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_ipv_6address_with_options(request, runtime)

    def enable_sql_audit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['IsRecall'] = request.is_recall
        query['RecallEndTimestamp'] = request.recall_end_timestamp
        query['RecallStartTimestamp'] = request.recall_start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_sql_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    def enable_sql_flashback_match_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSqlFlashbackMatchSwitch',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_sql_flashback_match_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_flashback_match_switch_with_options(request, runtime)

    def flashback_recycle_bin_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FlashbackRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            self.call_api(params, req, runtime)
        )

    def flashback_recycle_bin_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.flashback_recycle_bin_table_with_options(request, runtime)

    def get_drds_db_rds_relation_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDrdsDbRdsRelationInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_drds_db_rds_relation_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_drds_db_rds_relation_info_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['NextToken'] = request.next_token
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUserReports',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ListUserReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_reports_with_options(request, runtime)

    def list_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['DrdsVer'] = request.drds_ver
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ListVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    def manage_private_rds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Params'] = request.params
        query['RdsAction'] = request.rds_action
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ManagePrivateRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            self.call_api(params, req, runtime)
        )

    def manage_private_rds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.manage_private_rds_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['Description'] = request.description
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbPrivilege'] = request.db_privilege
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    def modify_drds_instance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsInstanceDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_drds_instance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_instance_description_with_options(request, runtime)

    def modify_drds_ip_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupAttribute'] = request.group_attribute
        query['GroupName'] = request.group_name
        query['IpWhiteList'] = request.ip_white_list
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_drds_ip_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_ip_white_list_with_options(request, runtime)

    def modify_event_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EventId'] = request.event_id
        query['Region'] = request.region
        query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyEventTaskStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyEventTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_event_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_event_task_status_with_options(request, runtime)

    def modify_polar_db_read_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstanceId'] = request.db_instance_id
        query['DbName'] = request.db_name
        query['DbNodeIds'] = request.db_node_ids
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPolarDbReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_polar_db_read_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_polar_db_read_weight_with_options(request, runtime)

    def modify_rds_read_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['InstanceNames'] = request.instance_names
        query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRdsReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rds_read_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_rds_read_weight_with_options(request, runtime)

    def pre_check_sql_flashback_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PreCheckSqlFlashbackTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def pre_check_sql_flashback_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pre_check_sql_flashback_task_with_options(request, runtime)

    def put_restore_pre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupDbNames'] = request.backup_db_names
        query['BackupId'] = request.backup_id
        query['BackupLevel'] = request.backup_level
        query['BackupMode'] = request.backup_mode
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutRestorePreCheck',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.PutRestorePreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def put_restore_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_restore_pre_check_with_options(request, runtime)

    def put_start_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupDbNames'] = request.backup_db_names
        query['BackupLevel'] = request.backup_level
        query['BackupMode'] = request.backup_mode
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutStartBackup',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def put_start_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_start_backup_with_options(request, runtime)

    def rearrange_db_to_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ChooseRds'] = request.choose_rds
        query['ChooseSubDb'] = request.choose_sub_db
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['InstanceList'] = request.instance_list
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RearrangeDbToInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RearrangeDbToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def rearrange_db_to_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rearrange_db_to_instance_with_options(request, runtime)

    def refresh_drds_atom_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshDrdsAtomUrl',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_drds_atom_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_drds_atom_url_with_options(request, runtime)

    def release_instance_internet_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_internet_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_internet_address_with_options(request, runtime)

    def remove_backups_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveBackupsSet',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_backups_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_backups_set_with_options(request, runtime)

    def remove_drds_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDb',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_with_options(request, runtime)

    def remove_drds_db_failed_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDbFailedRecord',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_drds_db_failed_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_failed_record_with_options(request, runtime)

    def remove_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_instance_with_options(request, runtime)

    def remove_drds_mysql_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstanceId'] = request.db_instance_id
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Force'] = request.force
        query['RoDbInstanceId'] = request.ro_db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsMysql',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsMysqlResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_drds_mysql(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_mysql_with_options(request, runtime)

    def remove_instance_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_instance_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_instance_account_with_options(request, runtime)

    def remove_recycle_bin_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_recycle_bin_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_recycle_bin_table_with_options(request, runtime)

    def restart_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_drds_instance_with_options(request, runtime)

    def rollback_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RollbackInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_instance_version_with_options(request, runtime)

    def set_backup_local_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        query['LocalLogRetentionHours'] = request.local_log_retention_hours
        query['LocalLogRetentionSpace'] = request.local_log_retention_space
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            self.call_api(params, req, runtime)
        )

    def set_backup_local(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backup_local_with_options(request, runtime)

    def set_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupDbNames'] = request.backup_db_names
        query['BackupLevel'] = request.backup_level
        query['BackupLog'] = request.backup_log
        query['BackupMode'] = request.backup_mode
        query['DataBackupRetentionPeriod'] = request.data_backup_retention_period
        query['DrdsInstanceId'] = request.drds_instance_id
        query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        query['PreferredBackupEndTime'] = request.preferred_backup_end_time
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupStartTime'] = request.preferred_backup_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backup_policy_with_options(request, runtime)

    def setup_broadcast_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Active'] = request.active
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetupBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_broadcast_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_broadcast_tables_with_options(request, runtime)

    def setup_drds_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['DrdsInstanceId'] = request.drds_instance_id
        query['ParamLevel'] = request.param_level
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetupDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_drds_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_drds_params_with_options(request, runtime)

    def setup_recycle_bin_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['StatusAction'] = request.status_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetupRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_recycle_bin_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_recycle_bin_status_with_options(request, runtime)

    def setup_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AllowFullTableScan'] = request.allow_full_table_scan
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetupTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_table_with_options(request, runtime)

    def setup_table_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AllowFullTableScan'] = request.allow_full_table_scan
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetupTableAsync',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_table_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_table_async_with_options(request, runtime)

    def sql_compatibility_cancel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SqlCompatibilityCancel',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityCancelResponse(),
            self.call_api(params, req, runtime)
        )

    def sql_compatibility_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_cancel_with_options(request, runtime)

    def sql_compatibility_start_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PerformanceTest'] = request.performance_test
        query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SqlCompatibilityStart',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityStartResponse(),
            self.call_api(params, req, runtime)
        )

    def sql_compatibility_start(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_start_with_options(request, runtime)

    def start_restore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackupDbNames'] = request.backup_db_names
        query['BackupId'] = request.backup_id
        query['BackupLevel'] = request.backup_level
        query['BackupMode'] = request.backup_mode
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRestore',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            self.call_api(params, req, runtime)
        )

    def start_restore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_restore_with_options(request, runtime)

    def submit_clean_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['ExpandType'] = request.expand_type
        query['JobId'] = request.job_id
        query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitCleanTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_clean_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_task_with_options(request, runtime)

    def submit_hot_expand_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['TableList'] = request.table_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_hot_expand_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_pre_check_task_with_options(request, runtime)

    def submit_hot_expand_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['ExtendedMapping'] = request.extended_mapping
        query['InstanceDbMapping'] = request.instance_db_mapping
        query['Mapping'] = request.mapping
        query['SupperAccountMapping'] = request.supper_account_mapping
        query['TaskDesc'] = request.task_desc
        query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_hot_expand_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_task_with_options(request, runtime)

    def submit_smooth_expand_pre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbInstType'] = request.db_inst_type
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheck',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_smooth_expand_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_with_options(request, runtime)

    def submit_smooth_expand_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_smooth_expand_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_task_with_options(request, runtime)

    def submit_sql_flashback_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['RecallRestoreType'] = request.recall_restore_type
        query['RecallType'] = request.recall_type
        query['SqlPk'] = request.sql_pk
        query['SqlType'] = request.sql_type
        query['StartTime'] = request.start_time
        query['TableName'] = request.table_name
        query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSqlFlashbackTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_sql_flashback_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    def switch_global_broadcast_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchGlobalBroadcastType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_global_broadcast_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_global_broadcast_type_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_instance_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RetainClassic'] = request.retain_classic
        query['SrcInstanceNetworkType'] = request.src_instance_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_network_with_options(request, runtime)

    def update_private_rds_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['DBInstanceId'] = request.dbinstance_id
        query['DrdsInstanceId'] = request.drds_instance_id
        query['PrePayDuration'] = request.pre_pay_duration
        query['RdsClass'] = request.rds_class
        query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePrivateRdsClass',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            self.call_api(params, req, runtime)
        )

    def update_private_rds_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_private_rds_class_with_options(request, runtime)

    def update_resource_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroupAttribute',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_attribute_with_options(request, runtime)

    def upgrade_hi_store_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['HistoreInstanceId'] = request.histore_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeHiStoreInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_hi_store_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_hi_store_instance_with_options(request, runtime)

    def upgrade_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['Rpm'] = request.rpm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    def validate_shard_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        query['SourceTableName'] = request.source_table_name
        query['TargetTableName'] = request.target_table_name
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ValidateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_shard_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_shard_task_with_options(request, runtime)

    def describe_rds_inst_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='describeRdsInstInfos',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsInstInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_inst_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_inst_infos_with_options(request, runtime)
