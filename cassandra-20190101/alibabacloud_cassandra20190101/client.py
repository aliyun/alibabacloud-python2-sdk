# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cassandra20190101 import models as cassandra_20190101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cassandra', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_public_contact_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicContactPoints',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.AllocatePublicContactPointsResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_public_contact_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_contact_points_with_options(request, runtime)

    def create_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.retention_period):
            query['RetentionPeriod'] = request.retention_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.data_center_name):
            query['DataCenterName'] = request.data_center_name
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_data_center_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_name):
            query['DataCenterName'] = request.data_center_name
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCenter',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.CreateDataCenterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_center(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_center_with_options(request, runtime)

    def delete_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DeleteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_plan_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_data_center_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataCenter',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DeleteDataCenterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_center(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_center_with_options(request, runtime)

    def delete_node_tool_execution_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodeToolExecutionHistory',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_node_tool_execution_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_node_tool_execution_history_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_with_options(request, runtime)

    def describe_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_with_options(request, runtime)

    def describe_backup_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlans',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plans_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    def describe_cluster_dashboard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterDashboard',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeClusterDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_dashboard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_dashboard_with_options(request, runtime)

    def describe_cluster_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterStatus',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeClusterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_status_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    def describe_contact_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactPoints',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeContactPointsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contact_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_points_with_options(request, runtime)

    def describe_data_center_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCenter',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeDataCenterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_center(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_center_with_options(request, runtime)

    def describe_data_centers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCenters',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeDataCentersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_centers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_centers_with_options(request, runtime)

    def describe_deleted_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeletedClusters',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeDeletedClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deleted_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deleted_clusters_with_options(request, runtime)

    def describe_instance_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_with_options(request, runtime)

    def describe_ip_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_whitelist_with_options(request, runtime)

    def describe_ip_whitelist_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhitelistGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeIpWhitelistGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_whitelist_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_whitelist_groups_with_options(request, runtime)

    def describe_node_tool_execution_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeToolExecutionHistories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_tool_execution_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_tool_execution_histories_with_options(request, runtime)

    def describe_node_tool_execution_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dc_id):
            query['DcId'] = request.dc_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeToolExecutionHistory',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_tool_execution_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_tool_execution_history_with_options(request, runtime)

    def describe_parameter_modification_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeParameterModificationHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_modification_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_histories_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.DescribeSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    def execute_node_tool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arguments):
            query['Arguments'] = request.arguments
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.execute_nodes):
            query['ExecuteNodes'] = request.execute_nodes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteNodeTool',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ExecuteNodeToolResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_node_tool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_node_tool_with_options(request, runtime)

    def get_cms_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCmsUrl',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.GetCmsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cms_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cms_url_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    def modify_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    def modify_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.retention_period):
            query['RetentionPeriod'] = request.retention_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_with_options(request, runtime)

    def modify_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.confirm_product_offline):
            query['ConfirmProductOffline'] = request.confirm_product_offline
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_with_options(request, runtime)

    def modify_data_center_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.data_center_name):
            query['DataCenterName'] = request.data_center_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataCenter',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyDataCenterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_data_center(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_data_center_with_options(request, runtime)

    def modify_instance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    def modify_instance_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_type_with_options(request, runtime)

    def modify_ip_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_whitelist_with_options(request, runtime)

    def modify_ip_whitelist_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhitelistGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyIpWhitelistGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_whitelist_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_whitelist_group_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ModifySecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_groups_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def purge_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.PurgeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def purge_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purge_cluster_with_options(request, runtime)

    def reboot_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.RebootClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def reboot_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_cluster_with_options(request, runtime)

    def release_public_contact_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicContactPoints',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ReleasePublicContactPointsResponse(),
            self.call_api(params, req, runtime)
        )

    def release_public_contact_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_public_contact_points_with_options(request, runtime)

    def resize_disk_size_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDiskSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ResizeDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    def resize_disk_size(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_size_with_options(request, runtime)

    def resize_node_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_center_id):
            query['DataCenterId'] = request.data_center_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeNodeCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.ResizeNodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    def resize_node_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_node_count_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        ***\
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        ***\
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def un_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def un_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    def upgrade_cluster_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClusterVersion',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cassandra_20190101_models.UpgradeClusterVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cluster_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_version_with_options(request, runtime)
