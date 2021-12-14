# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20180601 import models as dataworks_public_20180601_models
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
            'ap-northeast-1': 'dataworks.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'dataworks.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'dataworks.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dataworks.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dataworks.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dataworks.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dataworks.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'dataworks.cn-chengdu.aliyuncs.com',
            'cn-hangzhou': 'dataworks.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dataworks.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'dataworks.aliyuncs.com',
            'cn-qingdao': 'dataworks.aliyuncs.com',
            'cn-shanghai': 'dataworks.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'dataworks.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'dataworks.aliyuncs.com',
            'eu-central-1': 'dataworks.eu-central-1.aliyuncs.com',
            'eu-west-1': 'dataworks.eu-west-1.aliyuncs.com',
            'me-east-1': 'dataworks.me-east-1.aliyuncs.com',
            'us-east-1': 'dataworks.us-east-1.aliyuncs.com',
            'us-west-1': 'dataworks.us-west-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dataworks.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dataworks.aliyuncs.com',
            'cn-shanghai-finance-1': 'dataworks.aliyuncs.com',
            'cn-north-2-gov-1': 'dataworks.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dataworks-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCallback',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.CheckCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def check_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_callback_with_options(request, runtime)

    def create_manual_dag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Bizdate'] = request.bizdate
        query['DagPara'] = request.dag_para
        query['FlowName'] = request.flow_name
        query['NodePara'] = request.node_para
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateManualDag',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.CreateManualDagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_manual_dag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    def create_real_time_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ActionType'] = request.action_type
        query['CreateResGroup'] = request.create_res_group
        query['DataSource'] = request.data_source
        query['DataworksVersion'] = request.dataworks_version
        query['FileId'] = request.file_id
        query['JobConfig'] = request.job_config
        query['ProjectId'] = request.project_id
        query['ResourceSpec'] = request.resource_spec
        query['TableRule'] = request.table_rule
        query['Tables'] = request.tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRealTimeProcess',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.CreateRealTimeProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def create_real_time_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_real_time_process_with_options(request, runtime)

    def delete_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDISyncTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DeleteDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disync_task_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def deploy_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployDISyncTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DeployDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_disync_task_with_options(request, runtime)

    def describe_emr_hive_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DatabaseName'] = request.database_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEmrHiveTable',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.DescribeEmrHiveTableResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_emr_hive_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_emr_hive_table_with_options(request, runtime)

    def get_disync_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDISyncInstanceInfo',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDISyncInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_disync_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_instance_info_with_options(request, runtime)

    def get_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDISyncTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_with_options(request, runtime)

    def get_switch_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SwitchName'] = request.switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSwitchValue',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.GetSwitchValueResponse(),
            self.call_api(params, req, runtime)
        )

    def get_switch_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_switch_value_with_options(request, runtime)

    def list_emr_hive_audit_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DatabaseName'] = request.database_name
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrHiveAuditLogs',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveAuditLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_emr_hive_audit_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_audit_logs_with_options(request, runtime)

    def list_emr_hive_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrHiveDatabases',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_emr_hive_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_databases_with_options(request, runtime)

    def list_emr_hive_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DatabaseName'] = request.database_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrHiveTables',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListEmrHiveTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_emr_hive_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_emr_hive_tables_with_options(request, runtime)

    def list_hive_column_lineages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ColumnName'] = request.column_name
        query['DatabaseName'] = request.database_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHiveColumnLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveColumnLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hive_column_lineages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hive_column_lineages_with_options(request, runtime)

    def list_hive_table_lineages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DatabaseName'] = request.database_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListHiveTableLineages',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListHiveTableLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hive_table_lineages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hive_table_lineages_with_options(request, runtime)

    def list_table_partitions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DatabaseName'] = request.database_name
        query['Order'] = request.order
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTablePartitions',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.ListTablePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_partitions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_partitions_with_options(request, runtime)

    def open_data_works_standard_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenDataWorksStandardService',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.OpenDataWorksStandardServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_data_works_standard_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_data_works_standard_service_with_options(request, runtime)

    def query_data_import_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SubUid'] = request.sub_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDataImportProcess',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.QueryDataImportProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def query_data_import_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_data_import_process_with_options(request, runtime)

    def query_data_import_process_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDataImportProcessStatus',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.QueryDataImportProcessStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_data_import_process_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_data_import_process_status_with_options(request, runtime)

    def query_real_time_process_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRealTimeProcessStatus',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.QueryRealTimeProcessStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_real_time_process_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_real_time_process_status_with_options(request, runtime)

    def search_manual_dag_node_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DagId'] = request.dag_id
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchManualDagNodeInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SearchManualDagNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def search_manual_dag_node_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_manual_dag_node_instance_with_options(request, runtime)

    def send_task_meta_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SendTaskMetaCallback',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.SendTaskMetaCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def send_task_meta_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_task_meta_callback_with_options(request, runtime)

    def start_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['StartParam'] = request.start_param
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDISyncInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StartDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disync_instance_with_options(request, runtime)

    def stop_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDISyncInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.StopDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disync_instance_with_options(request, runtime)

    def terminate_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TerminateDISyncInstance',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TerminateDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_disync_instance_with_options(request, runtime)

    def trigger_data_loader_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TriggerDataLoader',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.TriggerDataLoaderResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_data_loader(self):
        runtime = util_models.RuntimeOptions()
        return self.trigger_data_loader_with_options(runtime)

    def update_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['FileId'] = request.file_id
        query['ProjectId'] = request.project_id
        query['TaskContent'] = request.task_content
        query['TaskParam'] = request.task_param
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDISyncTask',
            version='2018-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20180601_models.UpdateDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_disync_task_with_options(request, runtime)
