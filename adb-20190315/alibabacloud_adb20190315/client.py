# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adb20190315 import models as adb_20190315_models
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
            'cn-qingdao': 'adb.aliyuncs.com',
            'cn-beijing': 'adb.aliyuncs.com',
            'cn-hangzhou': 'adb.aliyuncs.com',
            'cn-shanghai': 'adb.aliyuncs.com',
            'cn-shenzhen': 'adb.aliyuncs.com',
            'cn-hongkong': 'adb.aliyuncs.com',
            'ap-southeast-1': 'adb.aliyuncs.com',
            'us-west-1': 'adb.aliyuncs.com',
            'us-east-1': 'adb.aliyuncs.com',
            'cn-hangzhou-finance': 'adb.aliyuncs.com',
            'cn-north-2-gov-1': 'adb.aliyuncs.com',
            'ap-northeast-2-pop': 'adb.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'adb.aliyuncs.com',
            'cn-beijing-finance-pop': 'adb.aliyuncs.com',
            'cn-beijing-gov-1': 'adb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'adb.aliyuncs.com',
            'cn-edge-1': 'adb.aliyuncs.com',
            'cn-fujian': 'adb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'adb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'adb.aliyuncs.com',
            'cn-hangzhou-test-306': 'adb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'adb.aliyuncs.com',
            'cn-qingdao-nebula': 'adb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'adb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'adb.aliyuncs.com',
            'cn-shanghai-finance-1': 'adb.aliyuncs.com',
            'cn-shanghai-inner': 'adb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'adb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'adb.aliyuncs.com',
            'cn-shenzhen-inner': 'adb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'adb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'adb.aliyuncs.com',
            'cn-wuhan': 'adb.aliyuncs.com',
            'cn-yushanfang': 'adb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'adb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'adb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'adb.aliyuncs.com',
            'eu-west-1-oxs': 'adb.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'adb.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'adb.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('adb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.AllocateClusterPublicConnectionResponse(),
            self.do_rpcrequest('AllocateClusterPublicConnection', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    def bind_dbresource_pool_with_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.BindDBResourcePoolWithUserResponse(),
            self.do_rpcrequest('BindDBResourcePoolWithUser', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_dbresource_pool_with_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_dbresource_pool_with_user_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBClusterResponse(),
            self.do_rpcrequest('CreateDBCluster', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    def create_dbresource_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBResourcePoolResponse(),
            self.do_rpcrequest('CreateDBResourcePool', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbresource_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_pool_with_options(request, runtime)

    def create_elastic_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateElasticPlanResponse(),
            self.do_rpcrequest('CreateElasticPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_elastic_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_plan_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBClusterResponse(),
            self.do_rpcrequest('DeleteDBCluster', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    def delete_dbresource_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBResourcePoolResponse(),
            self.do_rpcrequest('DeleteDBResourcePool', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbresource_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_pool_with_options(request, runtime)

    def delete_elastic_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteElasticPlanResponse(),
            self.do_rpcrequest('DeleteElasticPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_elastic_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_plan_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_all_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllAccountsResponse(),
            self.do_rpcrequest('DescribeAllAccounts', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_accounts_with_options(request, runtime)

    def describe_all_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllDataSourceResponse(),
            self.do_rpcrequest('DescribeAllDataSource', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    def describe_audit_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogConfigResponse(),
            self.do_rpcrequest('DescribeAuditLogConfig', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    def describe_audit_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogRecordsResponse(),
            self.do_rpcrequest('DescribeAuditLogRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_records_with_options(request, runtime)

    def describe_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAutoRenewAttributeResponse(),
            self.do_rpcrequest('DescribeAutoRenewAttribute', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            adb_20190315_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_columns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeColumnsResponse(),
            self.do_rpcrequest('DescribeColumns', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_columns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    def describe_connection_count_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeConnectionCountRecordsResponse(),
            self.do_rpcrequest('DescribeConnectionCountRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_connection_count_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_count_records_with_options(request, runtime)

    def describe_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('DescribeDBClusterAccessWhiteList', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    def describe_dbcluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAttributeResponse(),
            self.do_rpcrequest('DescribeDBClusterAttribute', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    def describe_dbcluster_forecast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterForecastResponse(),
            self.do_rpcrequest('DescribeDBClusterForecast', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_forecast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_forecast_with_options(request, runtime)

    def describe_dbcluster_health_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterHealthReportResponse(),
            self.do_rpcrequest('DescribeDBClusterHealthReport', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_health_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_health_report_with_options(request, runtime)

    def describe_dbcluster_net_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterNetInfoResponse(),
            self.do_rpcrequest('DescribeDBClusterNetInfo', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_net_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_with_options(request, runtime)

    def describe_dbcluster_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterPerformanceResponse(),
            self.do_rpcrequest('DescribeDBClusterPerformance', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    def describe_dbcluster_resource_pool_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse(),
            self.do_rpcrequest('DescribeDBClusterResourcePoolPerformance', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_resource_pool_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_resource_pool_performance_with_options(request, runtime)

    def describe_dbclusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClustersResponse(),
            self.do_rpcrequest('DescribeDBClusters', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbclusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    def describe_dbresource_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBResourcePoolResponse(),
            self.do_rpcrequest('DescribeDBResourcePool', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbresource_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_pool_with_options(request, runtime)

    def describe_diagnosis_dimensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisDimensionsResponse(),
            self.do_rpcrequest('DescribeDiagnosisDimensions', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnosis_dimensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    def describe_diagnosis_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisRecordsResponse(),
            self.do_rpcrequest('DescribeDiagnosisRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnosis_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisSQLInfoResponse(),
            self.do_rpcrequest('DescribeDiagnosisSQLInfo', '2019-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_diagnosis_sqlinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    def describe_download_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDownloadRecordsResponse(),
            self.do_rpcrequest('DescribeDownloadRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_download_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    def describe_elastic_daily_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticDailyPlanResponse(),
            self.do_rpcrequest('DescribeElasticDailyPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elastic_daily_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_daily_plan_with_options(request, runtime)

    def describe_elastic_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticPlanResponse(),
            self.do_rpcrequest('DescribeElasticPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elastic_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plan_with_options(request, runtime)

    def describe_inclined_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeInclinedTablesResponse(),
            self.do_rpcrequest('DescribeInclinedTables', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_inclined_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inclined_tables_with_options(request, runtime)

    def describe_load_tasks_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLoadTasksRecordsResponse(),
            self.do_rpcrequest('DescribeLoadTasksRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_tasks_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_tasks_records_with_options(request, runtime)

    def describe_maintenance_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeMaintenanceActionResponse(),
            self.do_rpcrequest('DescribeMaintenanceAction', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_maintenance_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_maintenance_action_with_options(request, runtime)

    def describe_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeOperatorPermissionResponse(),
            self.do_rpcrequest('DescribeOperatorPermission', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_operator_permission_with_options(request, runtime)

    def describe_pattern_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribePatternPerformanceResponse(),
            self.do_rpcrequest('DescribePatternPerformance', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pattern_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pattern_performance_with_options(request, runtime)

    def describe_process_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeProcessListResponse(),
            self.do_rpcrequest('DescribeProcessList', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_process_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSchemasResponse(),
            self.do_rpcrequest('DescribeSchemas', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_slow_log_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSlowLogTrendResponse(),
            self.do_rpcrequest('DescribeSlowLogTrend', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    def describe_sql_pattern_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSqlPatternResponse(),
            self.do_rpcrequest('DescribeSqlPattern', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sql_pattern(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_pattern_with_options(request, runtime)

    def describe_sqlpattern_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPatternAttributeResponse(),
            self.do_rpcrequest('DescribeSQLPatternAttribute', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlpattern_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpattern_attribute_with_options(request, runtime)

    def describe_sqlpatterns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPatternsResponse(),
            self.do_rpcrequest('DescribeSQLPatterns', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlpatterns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpatterns_with_options(request, runtime)

    def describe_sqlplan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanResponse(),
            self.do_rpcrequest('DescribeSQLPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlplan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplan_with_options(request, runtime)

    def describe_sqlplan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanTaskResponse(),
            self.do_rpcrequest('DescribeSQLPlanTask', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlplan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplan_task_with_options(request, runtime)

    def describe_table_access_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableAccessCountResponse(),
            self.do_rpcrequest('DescribeTableAccessCount', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_access_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_access_count_with_options(request, runtime)

    def describe_table_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableDetailResponse(),
            self.do_rpcrequest('DescribeTableDetail', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_detail_with_options(request, runtime)

    def describe_table_partition_diagnose_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablePartitionDiagnoseResponse(),
            self.do_rpcrequest('DescribeTablePartitionDiagnose', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_partition_diagnose(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_partition_diagnose_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def describe_table_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableStatisticsResponse(),
            self.do_rpcrequest('DescribeTableStatistics', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_table_statistics_with_options(request, runtime)

    def describe_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTaskInfoResponse(),
            self.do_rpcrequest('DescribeTaskInfo', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_info_with_options(request, runtime)

    def download_diagnosis_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.DownloadDiagnosisRecordsResponse(),
            self.do_rpcrequest('DownloadDiagnosisRecords', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_diagnosis_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    def grant_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.GrantOperatorPermissionResponse(),
            self.do_rpcrequest('GrantOperatorPermission', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    def kill_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.KillProcessResponse(),
            self.do_rpcrequest('KillProcess', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_audit_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAuditLogConfigResponse(),
            self.do_rpcrequest('ModifyAuditLogConfig', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    def modify_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAutoRenewAttributeResponse(),
            self.do_rpcrequest('ModifyAutoRenewAttribute', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_cluster_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyClusterConnectionStringResponse(),
            self.do_rpcrequest('ModifyClusterConnectionString', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_connection_string(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_connection_string_with_options(request, runtime)

    def modify_dbcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResponse(),
            self.do_rpcrequest('ModifyDBCluster', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    def modify_dbcluster_access_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('ModifyDBClusterAccessWhiteList', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_access_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    def modify_dbcluster_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterDescriptionResponse(),
            self.do_rpcrequest('ModifyDBClusterDescription', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    def modify_dbcluster_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBClusterMaintainTime', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    def modify_dbcluster_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResourceGroupResponse(),
            self.do_rpcrequest('ModifyDBClusterResourceGroup', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_resource_group_with_options(request, runtime)

    def modify_dbresource_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBResourcePoolResponse(),
            self.do_rpcrequest('ModifyDBResourcePool', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbresource_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_pool_with_options(request, runtime)

    def modify_elastic_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyElasticPlanResponse(),
            self.do_rpcrequest('ModifyElasticPlan', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elastic_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_plan_with_options(request, runtime)

    def modify_log_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyLogBackupPolicyResponse(),
            self.do_rpcrequest('ModifyLogBackupPolicy', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_backup_policy_with_options(request, runtime)

    def modify_maintenance_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyMaintenanceActionResponse(),
            self.do_rpcrequest('ModifyMaintenanceAction', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_maintenance_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_maintenance_action_with_options(request, runtime)

    def release_cluster_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ReleaseClusterPublicConnectionResponse(),
            self.do_rpcrequest('ReleaseClusterPublicConnection', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def revoke_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.RevokeOperatorPermissionResponse(),
            self.do_rpcrequest('RevokeOperatorPermission', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unbind_dbresource_pool_with_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.UnbindDBResourcePoolWithUserResponse(),
            self.do_rpcrequest('UnbindDBResourcePoolWithUser', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_dbresource_pool_with_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_dbresource_pool_with_user_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            adb_20190315_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
