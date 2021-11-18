# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardbx20200202 import models as polardbx_20200202_models
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
            'ap-northeast-1': 'polardbx.aliyuncs.com',
            'ap-northeast-2-pop': 'polardbx.aliyuncs.com',
            'ap-south-1': 'polardbx.aliyuncs.com',
            'ap-southeast-2': 'polardbx.aliyuncs.com',
            'ap-southeast-3': 'polardbx.aliyuncs.com',
            'ap-southeast-5': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-1': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-pop': 'polardbx.aliyuncs.com',
            'cn-beijing-gov-1': 'polardbx.aliyuncs.com',
            'cn-beijing-nu16-b01': 'polardbx.aliyuncs.com',
            'cn-edge-1': 'polardbx.aliyuncs.com',
            'cn-fujian': 'polardbx.aliyuncs.com',
            'cn-haidian-cm12-c01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-finance': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'polardbx.aliyuncs.com',
            'cn-hangzhou-test-306': 'polardbx.aliyuncs.com',
            'cn-hongkong-finance-pop': 'polardbx.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'polardbx.aliyuncs.com',
            'cn-north-2-gov-1': 'polardbx.aliyuncs.com',
            'cn-qingdao-nebula': 'polardbx.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardbx.aliyuncs.com',
            'cn-shanghai-inner': 'polardbx.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-inner': 'polardbx.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardbx.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardbx.aliyuncs.com',
            'cn-wuhan': 'polardbx.aliyuncs.com',
            'cn-wulanchabu': 'polardbx.aliyuncs.com',
            'cn-yushanfang': 'polardbx.aliyuncs.com',
            'cn-zhangbei': 'polardbx.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'polardbx.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'polardbx.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'polardbx.aliyuncs.com',
            'eu-central-1': 'polardbx.aliyuncs.com',
            'eu-west-1': 'polardbx.aliyuncs.com',
            'eu-west-1-oxs': 'polardbx.aliyuncs.com',
            'me-east-1': 'polardbx.aliyuncs.com',
            'rus-west-1-pop': 'polardbx.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('polardbx', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def cancel_active_operation_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelActiveOperationTasksResponse(),
            self.do_rpcrequest('CancelActiveOperationTasks', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def cancel_active_operation_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    def cancel_polarx_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelPolarxOrderResponse(),
            self.do_rpcrequest('CancelPolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_polarx_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_polarx_order_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckCloudResourceAuthorizedResponse(),
            self.do_rpcrequest('CheckCloudResourceAuthorized', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            polardbx_20200202_models.CreateBackupResponse(),
            self.do_rpcrequest('CreateBackup', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBResponse(),
            self.do_rpcrequest('CreateDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_polarx_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreatePolarxOrderResponse(),
            self.do_rpcrequest('CreatePolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_polarx_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_polarx_order_with_options(request, runtime)

    def create_super_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSuperAccountResponse(),
            self.do_rpcrequest('CreateSuperAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_super_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_super_account_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBResponse(),
            self.do_rpcrequest('DeleteDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def describe_account_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAccountListResponse(),
            self.do_rpcrequest('DescribeAccountList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_list_with_options(request, runtime)

    def describe_active_operation_maintain_conf_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse(),
            self.do_rpcrequest('DescribeActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_maintain_conf(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    def describe_active_operation_task_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTaskCountResponse(),
            self.do_rpcrequest('DescribeActiveOperationTaskCount', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_set_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetListResponse(),
            self.do_rpcrequest('DescribeBackupSetList', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_backup_set_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_list_with_options(request, runtime)

    def describe_binary_log_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBinaryLogListResponse(),
            self.do_rpcrequest('DescribeBinaryLogList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_binary_log_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_binary_log_list_with_options(request, runtime)

    def describe_character_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCharacterSetResponse(),
            self.do_rpcrequest('DescribeCharacterSet', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_character_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceConfigResponse(),
            self.do_rpcrequest('DescribeDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_config_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceSSLResponse(),
            self.do_rpcrequest('DescribeDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            polardbx_20200202_models.DescribeDBInstanceTDEResponse(),
            self.do_rpcrequest('DescribeDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    def describe_dbinstance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTopologyResponse(),
            self.do_rpcrequest('DescribeDBInstanceTopology', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_topology_with_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbnode_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBNodePerformanceResponse(),
            self.do_rpcrequest('DescribeDBNodePerformance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbnode_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    def describe_db_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDbListResponse(),
            self.do_rpcrequest('DescribeDbList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_db_list_with_options(request, runtime)

    def describe_distribute_table_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDistributeTableListResponse(),
            self.do_rpcrequest('DescribeDistributeTableList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_distribute_table_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_distribute_table_list_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEventsResponse(),
            self.do_rpcrequest('DescribeEvents', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterTemplatesResponse(),
            self.do_rpcrequest('DescribeParameterTemplates', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            polardbx_20200202_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_polarx_data_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDataNodesResponse(),
            self.do_rpcrequest('DescribePolarxDataNodes', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_polarx_data_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_polarx_data_nodes_with_options(request, runtime)

    def describe_polarx_db_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDbInstancesResponse(),
            self.do_rpcrequest('DescribePolarxDbInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_polarx_db_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_polarx_db_instances_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def describe_scale_out_migrate_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse(),
            self.do_rpcrequest('DescribeScaleOutMigrateTaskList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scale_out_migrate_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scale_out_migrate_task_list_with_options(request, runtime)

    def describe_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSecurityIpsResponse(),
            self.do_rpcrequest('DescribeSecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTasksResponse(),
            self.do_rpcrequest('DescribeTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_user_encryption_key_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeUserEncryptionKeyListResponse(),
            self.do_rpcrequest('DescribeUserEncryptionKeyList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_encryption_key_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    def get_polarx_commodity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.GetPolarxCommodityResponse(),
            self.do_rpcrequest('GetPolarxCommodity', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_polarx_commodity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_polarx_commodity_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_active_operation_maintain_conf_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse(),
            self.do_rpcrequest('ModifyActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_maintain_conf(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    def modify_active_operation_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationTasksResponse(),
            self.do_rpcrequest('ModifyActiveOperationTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    def modify_dbinstance_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceClassResponse(),
            self.do_rpcrequest('ModifyDBInstanceClass', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    def modify_dbinstance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConfigResponse(),
            self.do_rpcrequest('ModifyDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_database_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDatabaseDescriptionResponse(),
            self.do_rpcrequest('ModifyDatabaseDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_database_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyParameterResponse(),
            self.do_rpcrequest('ModifyParameter', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseInstancePublicConnectionResponse(),
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def update_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateBackupPolicyResponse(),
            self.do_rpcrequest('UpdateBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_backup_policy_with_options(request, runtime)

    def update_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceSSLResponse(),
            self.do_rpcrequest('UpdateDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_sslwith_options(request, runtime)

    def update_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceTDEResponse(),
            self.do_rpcrequest('UpdateDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_tdewith_options(request, runtime)

    def update_polar_dbxinstance_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse(),
            self.do_rpcrequest('UpdatePolarDBXInstanceNode', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_polar_dbxinstance_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_polar_dbxinstance_node_with_options(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)
