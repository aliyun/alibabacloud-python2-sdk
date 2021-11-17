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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            self.do_rpcrequest('ChangeAccountPassword', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_account_password_with_options(request, runtime)

    def change_instance_azone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            self.do_rpcrequest('ChangeInstanceAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_instance_azone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_instance_azone_with_options(request, runtime)

    def change_instance_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceNetworkResponse(),
            self.do_rpcrequest('ChangeInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_instance_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_instance_network_with_options(request, runtime)

    def check_connectivity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CheckConnectivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_info):
            request.db_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_info, 'DbInfo', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckConnectivityResponse(),
            self.do_rpcrequest('CheckConnectivity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_connectivity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_connectivity_with_options(request, runtime)

    def check_drds_db_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            self.do_rpcrequest('CheckDrdsDbName', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_drds_db_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_drds_db_name_with_options(request, runtime)

    def check_expand_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            self.do_rpcrequest('CheckExpandStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_expand_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_expand_status_with_options(request, runtime)

    def check_new_table_name_valid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckNewTableNameValidResponse(),
            self.do_rpcrequest('CheckNewTableNameValid', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_new_table_name_valid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_new_table_name_valid_with_options(request, runtime)

    def check_rds_super_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckRdsSuperAccountResponse(),
            self.do_rpcrequest('CheckRdsSuperAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_rds_super_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_rds_super_account_with_options(request, runtime)

    def check_sql_audit_enable_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            self.do_rpcrequest('CheckSqlAuditEnableStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_sql_audit_enable_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_sql_audit_enable_status_with_options(request, runtime)

    def configure_drds_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ConfigureDrdsDbInstancesResponse(),
            self.do_rpcrequest('ConfigureDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_drds_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_drds_db_instances_with_options(request, runtime)

    def create_custom_data_export_pre_check_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateCustomDataExportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_export_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_export_pre_check_task_with_options(request, runtime)

    def create_custom_data_export_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportTaskResponse(),
            self.do_rpcrequest('CreateCustomDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_export_task_with_options(request, runtime)

    def create_custom_data_import_pre_check_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateCustomDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_import_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_import_pre_check_task_with_options(request, runtime)

    def create_custom_data_import_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportTaskResponse(),
            self.do_rpcrequest('CreateCustomDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_import_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_import_task_with_options(request, runtime)

    def create_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            self.do_rpcrequest('CreateDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbwith_options(request, runtime)

    def create_drds_dbpre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreCheckResponse(),
            self.do_rpcrequest('CreateDrdsDBPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_dbpre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpre_check_with_options(request, runtime)

    def create_drds_dbpreview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreviewResponse(),
            self.do_rpcrequest('CreateDrdsDBPreview', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_dbpreview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpreview_with_options(request, runtime)

    def create_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            self.do_rpcrequest('CreateDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drds_instance_with_options(request, runtime)

    def create_evaluate_data_import_pre_check_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateEvaluateDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_data_import_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_data_import_pre_check_task_with_options(request, runtime)

    def create_evaluate_data_import_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportTaskResponse(),
            self.do_rpcrequest('CreateEvaluateDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_data_import_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_data_import_task_with_options(request, runtime)

    def create_evaluate_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluatePreCheckTaskResponse(),
            self.do_rpcrequest('CreateEvaluatePreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_pre_check_task_with_options(request, runtime)

    def create_evaluate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateTaskResponse(),
            self.do_rpcrequest('CreateEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_task_with_options(request, runtime)

    def create_instance_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            self.do_rpcrequest('CreateInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_account_with_options(request, runtime)

    def create_instance_internet_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            self.do_rpcrequest('CreateInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_internet_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_internet_address_with_options(request, runtime)

    def create_my_cat_evaluate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateMyCatEvaluateResponse(),
            self.do_rpcrequest('CreateMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_my_cat_evaluate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_my_cat_evaluate_with_options(request, runtime)

    def create_order_for_rds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            self.do_rpcrequest('CreateOrderForRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order_for_rds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_rds_with_options(request, runtime)

    def create_shard_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            self.do_rpcrequest('CreateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_shard_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_shard_task_with_options(request, runtime)

    def describe_back_menu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            self.do_rpcrequest('DescribeBackMenu', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_menu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_menu_with_options(request, runtime)

    def describe_backup_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            self.do_rpcrequest('DescribeBackupDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    def describe_backup_local_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            self.do_rpcrequest('DescribeBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_local(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_local_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            self.do_rpcrequest('DescribeBackupSets', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_sets_with_options(request, runtime)

    def describe_backup_times_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            self.do_rpcrequest('DescribeBackupTimes', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_times(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_times_with_options(request, runtime)

    def describe_batch_evaluate_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBatchEvaluateTaskReportResponse(),
            self.do_rpcrequest('DescribeBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_batch_evaluate_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_evaluate_task_report_with_options(request, runtime)

    def describe_broadcast_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            self.do_rpcrequest('DescribeBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_broadcast_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_broadcast_tables_with_options(request, runtime)

    def describe_can_expand_instance_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCanExpandInstanceDetailListResponse(),
            self.do_rpcrequest('DescribeCanExpandInstanceDetailList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_can_expand_instance_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_can_expand_instance_detail_list_with_options(request, runtime)

    def describe_custom_data_export_src_dst_tables_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataExportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse(),
            self.do_rpcrequest('DescribeCustomDataExportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_data_export_src_dst_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_data_export_src_dst_tables_with_options(request, runtime)

    def describe_custom_data_import_src_dst_tables_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataImportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse(),
            self.do_rpcrequest('DescribeCustomDataImportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_data_import_src_dst_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_data_import_src_dst_tables_with_options(request, runtime)

    def describe_data_export_pre_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportPreCheckResultResponse(),
            self.do_rpcrequest('DescribeDataExportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_pre_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_pre_check_result_with_options(request, runtime)

    def describe_data_export_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTaskReportResponse(),
            self.do_rpcrequest('DescribeDataExportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_task_report_with_options(request, runtime)

    def describe_data_export_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTasksResponse(),
            self.do_rpcrequest('DescribeDataExportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_tasks_with_options(request, runtime)

    def describe_data_import_pre_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportPreCheckResultResponse(),
            self.do_rpcrequest('DescribeDataImportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_pre_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_pre_check_result_with_options(request, runtime)

    def describe_data_import_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTaskReportResponse(),
            self.do_rpcrequest('DescribeDataImportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_task_report_with_options(request, runtime)

    def describe_data_import_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTasksResponse(),
            self.do_rpcrequest('DescribeDataImportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_tasks_with_options(request, runtime)

    def describe_db_instance_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            self.do_rpcrequest('DescribeDbInstanceDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_instance_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instance_dbs_with_options(request, runtime)

    def describe_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            self.do_rpcrequest('DescribeDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instances_with_options(request, runtime)

    def describe_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            self.do_rpcrequest('DescribeDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbwith_options(request, runtime)

    def describe_drds_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            self.do_rpcrequest('DescribeDrdsDBCluster', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbcluster_with_options(request, runtime)

    def describe_drds_dbip_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            self.do_rpcrequest('DescribeDrdsDBIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbip_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbip_white_list_with_options(request, runtime)

    def describe_drds_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            self.do_rpcrequest('DescribeDrdsDBs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbs_with_options(request, runtime)

    def describe_drds_db_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            self.do_rpcrequest('DescribeDrdsDbInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instance_with_options(request, runtime)

    def describe_drds_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instances_with_options(request, runtime)

    def describe_drds_db_rds_name_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            self.do_rpcrequest('DescribeDrdsDbRdsNameList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_rds_name_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_rds_name_list_with_options(request, runtime)

    def describe_drds_db_spec_and_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse(),
            self.do_rpcrequest('DescribeDrdsDbSpecAndPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_spec_and_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_spec_and_price_with_options(request, runtime)

    def describe_drds_db_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            self.do_rpcrequest('DescribeDrdsDbTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_tasks_with_options(request, runtime)

    def describe_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            self.do_rpcrequest('DescribeDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_with_options(request, runtime)

    def describe_drds_instance_db_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceDbMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_db_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_db_monitor_with_options(request, runtime)

    def describe_drds_instance_level_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceLevelTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_level_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_level_tasks_with_options(request, runtime)

    def describe_drds_instance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_monitor_with_options(request, runtime)

    def describe_drds_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_version_with_options(request, runtime)

    def describe_drds_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instances_with_options(request, runtime)

    def describe_drds_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            self.do_rpcrequest('DescribeDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_params_with_options(request, runtime)

    def describe_drds_rds_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsRdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_rds_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_rds_instances_with_options(request, runtime)

    def describe_drds_sharding_dbs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            self.do_rpcrequest('DescribeDrdsShardingDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_sharding_dbs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sharding_dbs_with_options(request, runtime)

    def describe_drds_slow_sqls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            self.do_rpcrequest('DescribeDrdsSlowSqls', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_slow_sqls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_slow_sqls_with_options(request, runtime)

    def describe_drds_sql_audit_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            self.do_rpcrequest('DescribeDrdsSqlAuditStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_sql_audit_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sql_audit_status_with_options(request, runtime)

    def describe_drds_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            self.do_rpcrequest('DescribeDrdsTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_tasks_with_options(request, runtime)

    def describe_evaluate_data_import_db_topologys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeEvaluateDataImportDbTopologysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse(),
            self.do_rpcrequest('DescribeEvaluateDataImportDbTopologys', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_data_import_db_topologys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_data_import_db_topologys_with_options(request, runtime)

    def describe_evaluate_pre_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluatePreCheckResultResponse(),
            self.do_rpcrequest('DescribeEvaluatePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_pre_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_pre_check_result_with_options(request, runtime)

    def describe_evaluate_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTaskReportResponse(),
            self.do_rpcrequest('DescribeEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_task_report_with_options(request, runtime)

    def describe_evaluate_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTasksResponse(),
            self.do_rpcrequest('DescribeEvaluateTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_tasks_with_options(request, runtime)

    def describe_expand_logic_table_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            self.do_rpcrequest('DescribeExpandLogicTableInfoList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_expand_logic_table_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_expand_logic_table_info_list_with_options(request, runtime)

    def describe_hi_store_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHiStoreInstanceInfoResponse(),
            self.do_rpcrequest('DescribeHiStoreInstanceInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hi_store_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_store_instance_info_with_options(request, runtime)

    def describe_hot_db_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            self.do_rpcrequest('DescribeHotDbList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_db_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_db_list_with_options(request, runtime)

    def describe_inst_db_log_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            self.do_rpcrequest('DescribeInstDbLogInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_inst_db_log_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_log_info_with_options(request, runtime)

    def describe_inst_db_sls_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            self.do_rpcrequest('DescribeInstDbSlsInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_inst_db_sls_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_sls_info_with_options(request, runtime)

    def describe_instance_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            self.do_rpcrequest('DescribeInstanceAccounts', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_accounts_with_options(request, runtime)

    def describe_instance_menu_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceMenuSwitchResponse(),
            self.do_rpcrequest('DescribeInstanceMenuSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_menu_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_menu_switch_with_options(request, runtime)

    def describe_instance_switch_azone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            self.do_rpcrequest('DescribeInstanceSwitchAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_switch_azone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_azone_with_options(request, runtime)

    def describe_instance_switch_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            self.do_rpcrequest('DescribeInstanceSwitchNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_switch_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_network_with_options(request, runtime)

    def describe_pre_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            self.do_rpcrequest('DescribePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pre_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_result_with_options(request, runtime)

    def describe_rdsperformance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            self.do_rpcrequest('DescribeRDSPerformance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rdsperformance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsperformance_with_options(request, runtime)

    def describe_rds_commodity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            self.do_rpcrequest('DescribeRdsCommodity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_commodity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_commodity_with_options(request, runtime)

    def describe_rds_drds_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsDrdsDBResponse(),
            self.do_rpcrequest('DescribeRdsDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_drds_dbwith_options(request, runtime)

    def describe_rds_performance_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            self.do_rpcrequest('DescribeRdsPerformanceSummary', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_performance_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_performance_summary_with_options(request, runtime)

    def describe_rds_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPriceResponse(),
            self.do_rpcrequest('DescribeRdsPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_price_with_options(request, runtime)

    def describe_rds_read_only_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsReadOnlyResponse(),
            self.do_rpcrequest('DescribeRdsReadOnly', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_read_only(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_read_only_with_options(request, runtime)

    def describe_rds_super_account_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            self.do_rpcrequest('DescribeRdsSuperAccountInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_super_account_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_super_account_instances_with_options(request, runtime)

    def describe_rds_vpc_for_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsVpcForZoneResponse(),
            self.do_rpcrequest('DescribeRdsVpcForZone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_vpc_for_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpc_for_zone_with_options(request, runtime)

    def describe_recycle_bin_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            self.do_rpcrequest('DescribeRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recycle_bin_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_status_with_options(request, runtime)

    def describe_recycle_bin_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            self.do_rpcrequest('DescribeRecycleBinTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recycle_bin_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_tables_with_options(request, runtime)

    def describe_restore_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            self.do_rpcrequest('DescribeRestoreOrder', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_restore_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_order_with_options(request, runtime)

    def describe_shard_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            self.do_rpcrequest('DescribeShardTaskInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shard_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_info_with_options(request, runtime)

    def describe_shard_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            self.do_rpcrequest('DescribeShardTaskList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shard_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_list_with_options(request, runtime)

    def describe_sql_flashbak_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            self.do_rpcrequest('DescribeSqlFlashbakTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sql_flashbak_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_flashbak_task_with_options(request, runtime)

    def describe_src_rds_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSrcRdsListResponse(),
            self.do_rpcrequest('DescribeSrcRdsList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_src_rds_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_src_rds_list_with_options(request, runtime)

    def describe_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            self.do_rpcrequest('DescribeTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    def describe_table_list_by_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            self.do_rpcrequest('DescribeTableListByType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_list_by_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_list_by_type_with_options(request, runtime)

    def describe_table_sharding_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableShardingInfoResponse(),
            self.do_rpcrequest('DescribeTableShardingInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_sharding_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_sharding_info_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def disable_sql_audit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            self.do_rpcrequest('DisableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_sql_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    def enable_instance_ipv_6address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            self.do_rpcrequest('EnableInstanceIpv6Address', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_ipv_6address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_ipv_6address_with_options(request, runtime)

    def enable_sql_audit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            self.do_rpcrequest('EnableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    def enable_sql_flashback_match_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            self.do_rpcrequest('EnableSqlFlashbackMatchSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_flashback_match_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_flashback_match_switch_with_options(request, runtime)

    def flashback_recycle_bin_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            self.do_rpcrequest('FlashbackRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flashback_recycle_bin_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.flashback_recycle_bin_table_with_options(request, runtime)

    def get_batch_evaluate_task_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetBatchEvaluateTaskReportResponse(),
            self.do_rpcrequest('GetBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_batch_evaluate_task_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_batch_evaluate_task_report_with_options(request, runtime)

    def get_drds_db_rds_relation_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            self.do_rpcrequest('GetDrdsDbRdsRelationInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_drds_db_rds_relation_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_drds_db_rds_relation_info_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListUserReportsResponse(),
            self.do_rpcrequest('ListUserReports', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_reports_with_options(request, runtime)

    def list_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListVersionsResponse(),
            self.do_rpcrequest('ListVersions', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    def manage_private_rds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            self.do_rpcrequest('ManagePrivateRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def manage_private_rds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.manage_private_rds_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            self.do_rpcrequest('ModifyAccountPrivilege', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    def modify_drds_instance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDrdsInstanceDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_drds_instance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_instance_description_with_options(request, runtime)

    def modify_drds_ip_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            self.do_rpcrequest('ModifyDrdsIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_drds_ip_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_ip_white_list_with_options(request, runtime)

    def modify_event_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyEventTaskStatusResponse(),
            self.do_rpcrequest('ModifyEventTaskStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_event_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_event_task_status_with_options(request, runtime)

    def modify_polar_db_read_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            self.do_rpcrequest('ModifyPolarDbReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_polar_db_read_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_polar_db_read_weight_with_options(request, runtime)

    def modify_rds_read_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            self.do_rpcrequest('ModifyRdsReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rds_read_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_rds_read_weight_with_options(request, runtime)

    def my_cat_connect_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatConnectTestResponse(),
            self.do_rpcrequest('MyCatConnectTest', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def my_cat_connect_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.my_cat_connect_test_with_options(request, runtime)

    def my_cat_custom_import_pre_check_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.MyCatCustomImportPreCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_map):
            request.table_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_map, 'TableMap', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatCustomImportPreCheckResponse(),
            self.do_rpcrequest('MyCatCustomImportPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def my_cat_custom_import_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.my_cat_custom_import_pre_check_with_options(request, runtime)

    def pre_check_modify_table_sharding_key_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse(),
            self.do_rpcrequest('PreCheckModifyTableShardingKeyParam', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pre_check_modify_table_sharding_key_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pre_check_modify_table_sharding_key_param_with_options(request, runtime)

    def pre_check_sql_flashback_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckSqlFlashbackTaskResponse(),
            self.do_rpcrequest('PreCheckSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pre_check_sql_flashback_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pre_check_sql_flashback_task_with_options(request, runtime)

    def precheck_my_cat_evaluate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PrecheckMyCatEvaluateResponse(),
            self.do_rpcrequest('PrecheckMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def precheck_my_cat_evaluate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.precheck_my_cat_evaluate_with_options(request, runtime)

    def put_restore_pre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutRestorePreCheckResponse(),
            self.do_rpcrequest('PutRestorePreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_restore_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_restore_pre_check_with_options(request, runtime)

    def put_start_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            self.do_rpcrequest('PutStartBackup', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_start_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_start_backup_with_options(request, runtime)

    def rearrange_db_to_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RearrangeDbToInstanceResponse(),
            self.do_rpcrequest('RearrangeDbToInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rearrange_db_to_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rearrange_db_to_instance_with_options(request, runtime)

    def refresh_drds_atom_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            self.do_rpcrequest('RefreshDrdsAtomUrl', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_drds_atom_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_drds_atom_url_with_options(request, runtime)

    def release_instance_internet_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            self.do_rpcrequest('ReleaseInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_internet_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_internet_address_with_options(request, runtime)

    def remove_backups_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            self.do_rpcrequest('RemoveBackupsSet', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_backups_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_backups_set_with_options(request, runtime)

    def remove_data_export_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataExportTaskResponse(),
            self.do_rpcrequest('RemoveDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_data_export_task_with_options(request, runtime)

    def remove_data_import_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataImportTaskResponse(),
            self.do_rpcrequest('RemoveDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_data_import_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_data_import_task_with_options(request, runtime)

    def remove_drds_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            self.do_rpcrequest('RemoveDrdsDb', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_with_options(request, runtime)

    def remove_drds_db_failed_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            self.do_rpcrequest('RemoveDrdsDbFailedRecord', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_db_failed_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_failed_record_with_options(request, runtime)

    def remove_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            self.do_rpcrequest('RemoveDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_instance_with_options(request, runtime)

    def remove_drds_mysql_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsMysqlResponse(),
            self.do_rpcrequest('RemoveDrdsMysql', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_mysql(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_mysql_with_options(request, runtime)

    def remove_evaluate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveEvaluateTaskResponse(),
            self.do_rpcrequest('RemoveEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_evaluate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_evaluate_task_with_options(request, runtime)

    def remove_instance_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            self.do_rpcrequest('RemoveInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_instance_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_instance_account_with_options(request, runtime)

    def remove_recycle_bin_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            self.do_rpcrequest('RemoveRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_recycle_bin_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_recycle_bin_table_with_options(request, runtime)

    def restart_drds_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            self.do_rpcrequest('RestartDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_drds_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_drds_instance_with_options(request, runtime)

    def rollback_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            self.do_rpcrequest('RollbackInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_instance_version_with_options(request, runtime)

    def set_backup_local_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            self.do_rpcrequest('SetBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backup_local(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backup_local_with_options(request, runtime)

    def set_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            self.do_rpcrequest('SetBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backup_policy_with_options(request, runtime)

    def setup_broadcast_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            self.do_rpcrequest('SetupBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_broadcast_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_broadcast_tables_with_options(request, runtime)

    def setup_drds_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            self.do_rpcrequest('SetupDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_drds_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_drds_params_with_options(request, runtime)

    def setup_recycle_bin_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            self.do_rpcrequest('SetupRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_recycle_bin_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_recycle_bin_status_with_options(request, runtime)

    def setup_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            self.do_rpcrequest('SetupTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_table_with_options(request, runtime)

    def setup_table_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableAsyncResponse(),
            self.do_rpcrequest('SetupTableAsync', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_table_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_table_async_with_options(request, runtime)

    def sql_compatibility_cancel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityCancelResponse(),
            self.do_rpcrequest('SqlCompatibilityCancel', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sql_compatibility_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_cancel_with_options(request, runtime)

    def sql_compatibility_start_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityStartResponse(),
            self.do_rpcrequest('SqlCompatibilityStart', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sql_compatibility_start(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_start_with_options(request, runtime)

    def start_evaluate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartEvaluateTaskResponse(),
            self.do_rpcrequest('StartEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_evaluate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_evaluate_task_with_options(request, runtime)

    def start_restore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            self.do_rpcrequest('StartRestore', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_restore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_restore_with_options(request, runtime)

    def stop_data_export_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataExportTaskResponse(),
            self.do_rpcrequest('StopDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_data_export_task_with_options(request, runtime)

    def stop_data_import_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataImportTaskResponse(),
            self.do_rpcrequest('StopDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_data_import_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_data_import_task_with_options(request, runtime)

    def stop_evaluate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopEvaluateTaskResponse(),
            self.do_rpcrequest('StopEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_evaluate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_evaluate_task_with_options(request, runtime)

    def submit_clean_table_sharding_key_modify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitCleanTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_clean_table_sharding_key_modify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_table_sharding_key_modify_with_options(request, runtime)

    def submit_clean_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            self.do_rpcrequest('SubmitCleanTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_clean_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_task_with_options(request, runtime)

    def submit_hot_expand_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            self.do_rpcrequest('SubmitHotExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_hot_expand_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_pre_check_task_with_options(request, runtime)

    def submit_hot_expand_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            self.do_rpcrequest('SubmitHotExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_hot_expand_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_task_with_options(request, runtime)

    def submit_rollback_sharding_key_modify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitRollbackShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitRollbackShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_rollback_sharding_key_modify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_rollback_sharding_key_modify_with_options(request, runtime)

    def submit_smooth_expand_pre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            self.do_rpcrequest('SubmitSmoothExpandPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_with_options(request, runtime)

    def submit_smooth_expand_pre_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            self.do_rpcrequest('SubmitSmoothExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_pre_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_task_with_options(request, runtime)

    def submit_smooth_expand_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandTaskResponse(),
            self.do_rpcrequest('SubmitSmoothExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_task_with_options(request, runtime)

    def submit_sql_flashback_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            self.do_rpcrequest('SubmitSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_sql_flashback_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    def submit_switch_table_sharding_key_modify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitSwitchTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_switch_table_sharding_key_modify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_switch_table_sharding_key_modify_with_options(request, runtime)

    def submit_switch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTaskResponse(),
            self.do_rpcrequest('SubmitSwitchTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_switch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_switch_task_with_options(request, runtime)

    def submit_table_sharding_key_modify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_table_sharding_key_modify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_table_sharding_key_modify_with_options(request, runtime)

    def switch_global_broadcast_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            self.do_rpcrequest('SwitchGlobalBroadcastType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_global_broadcast_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_global_broadcast_type_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_instance_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            self.do_rpcrequest('UpdateInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_network_with_options(request, runtime)

    def update_private_rds_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            self.do_rpcrequest('UpdatePrivateRdsClass', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_private_rds_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_private_rds_class_with_options(request, runtime)

    def update_resource_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            self.do_rpcrequest('UpdateResourceGroupAttribute', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_resource_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_attribute_with_options(request, runtime)

    def upgrade_hi_store_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            self.do_rpcrequest('UpgradeHiStoreInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_hi_store_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_hi_store_instance_with_options(request, runtime)

    def upgrade_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            self.do_rpcrequest('UpgradeInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    def validate_shard_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            self.do_rpcrequest('ValidateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_shard_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_shard_task_with_options(request, runtime)

    def describe_rds_inst_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsInstInfosResponse(),
            self.do_rpcrequest('describeRdsInstInfos', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_inst_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_inst_infos_with_options(request, runtime)
