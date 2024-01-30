# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hbr20170908 import models as hbr_20170908_models
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
            'ap-northeast-2-pop': 'hbr.aliyuncs.com',
            'cn-beijing-finance-1': 'hbr.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbr.aliyuncs.com',
            'cn-beijing-gov-1': 'hbr.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbr.aliyuncs.com',
            'cn-edge-1': 'hbr.aliyuncs.com',
            'cn-fujian': 'hbr.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbr.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbr.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbr.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbr.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hbr.aliyuncs.com',
            'cn-qingdao-nebula': 'hbr.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-inner': 'hbr.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbr.aliyuncs.com',
            'cn-shenzhen-inner': 'hbr.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbr.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbr.aliyuncs.com',
            'cn-wuhan': 'hbr.aliyuncs.com',
            'cn-wulanchabu': 'hbr.aliyuncs.com',
            'cn-yushanfang': 'hbr.aliyuncs.com',
            'cn-zhangbei': 'hbr.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbr.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbr.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbr.aliyuncs.com',
            'eu-west-1-oxs': 'hbr.aliyuncs.com',
            'rus-west-1-pop': 'hbr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hbr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_container_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.AddContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def add_container_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_container_cluster_with_options(request, runtime)

    def attach_nas_file_system_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachNasFileSystem',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.AttachNasFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_nas_file_system(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_nas_file_system_with_options(request, runtime)

    def cancel_backup_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_backup_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_backup_job_with_options(request, runtime)

    def cancel_restore_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_restore_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_restore_job_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        """
        In the Hybrid Backup Recovery (HBR), you can use resource groups to manage resources such as backup vaults, backup clients, and SAP HANA instances.
        *   A resource is a cloud service entity that you create on Alibaba Cloud, such as an ECS instance, a backup vault, or an SAP HANA instance.
        *   You can sort resources owned by your Alibaba Cloud account into various resource groups. This facilitates resource management among multiple projects or applications within your Alibaba Cloud account and simplifies permission management.
        

        @param request: ChangeResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        """
        In the Hybrid Backup Recovery (HBR), you can use resource groups to manage resources such as backup vaults, backup clients, and SAP HANA instances.
        *   A resource is a cloud service entity that you create on Alibaba Cloud, such as an ECS instance, a backup vault, or an SAP HANA instance.
        *   You can sort resources owned by your Alibaba Cloud account into various resource groups. This facilitates resource management among multiple projects or applications within your Alibaba Cloud account and simplifies permission management.
        

        @param request: ChangeResourceGroupRequest

        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def check_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_role_type):
            query['CheckRoleType'] = request.check_role_type
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRole',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CheckRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def check_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_role_with_options(request, runtime)

    def create_backup_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_cluster_id):
            query['ContainerClusterId'] = request.container_cluster_id
        if not UtilClient.is_unset(request.container_resources):
            query['ContainerResources'] = request.container_resources
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.exclude):
            query['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            query['Include'] = request.include
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_job_with_options(request, runtime)

    def create_backup_plan_with_options(self, tmp_req, runtime):
        """
        A backup schedule defines the data source, backup policy, and other configurations. After you execute a backup schedule, a backup job is generated to record the backup progress and the backup result. If a backup job is complete, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup schedule.
        *   You can specify only one interval as a backup cycle in a backup schedule.
        *   Each backup schedule allows you to back up data to only one backup vault.
        

        @param tmp_req: CreateBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBackupPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_data_source_detail):
            request.dest_data_source_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_data_source_detail, 'DestDataSourceDetail', 'json')
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.dest_data_source_detail_shrink):
            query['DestDataSourceDetail'] = request.dest_data_source_detail_shrink
        if not UtilClient.is_unset(request.dest_data_source_id):
            query['DestDataSourceId'] = request.dest_data_source_id
        if not UtilClient.is_unset(request.dest_source_type):
            query['DestSourceType'] = request.dest_source_type
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        if not UtilClient.is_unset(request.speed_limit):
            body['SpeedLimit'] = request.speed_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_plan(self, request):
        """
        A backup schedule defines the data source, backup policy, and other configurations. After you execute a backup schedule, a backup job is generated to record the backup progress and the backup result. If a backup job is complete, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup schedule.
        *   You can specify only one interval as a backup cycle in a backup schedule.
        *   Each backup schedule allows you to back up data to only one backup vault.
        

        @param request: CreateBackupPlanRequest

        @return: CreateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    def create_clients_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Hybrid Backup Recovery (HBR). For more information, see [Billable items and billing methods](~~89062~~).
        

        @param request: CreateClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_clients(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and pricing of Hybrid Backup Recovery (HBR). For more information, see [Billable items and billing methods](~~89062~~).
        

        @param request: CreateClientsRequest

        @return: CreateClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_clients_with_options(request, runtime)

    def create_hana_backup_plan_with_options(self, request, runtime):
        """
        A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup plan.
        *   You can specify only one interval as a backup cycle in a backup plan.
        *   Each backup plan allows you to back up data to only one backup vault.
        

        @param request: CreateHanaBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hana_backup_plan(self, request):
        """
        A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup plan.
        *   You can specify only one interval as a backup cycle in a backup plan.
        *   Each backup plan allows you to back up data to only one backup vault.
        

        @param request: CreateHanaBackupPlanRequest

        @return: CreateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_backup_plan_with_options(request, runtime)

    def create_hana_instance_with_options(self, request, runtime):
        """
        To register an SAP HANA instance, you must configure the connection parameters of the SAP HANA instance. After the SAP HANA instance is registered, HBR installs an HBR client on the ECS instance that hosts the SAP HANA instance.
        

        @param request: CreateHanaInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hana_instance(self, request):
        """
        To register an SAP HANA instance, you must configure the connection parameters of the SAP HANA instance. After the SAP HANA instance is registered, HBR installs an HBR client on the ECS instance that hosts the SAP HANA instance.
        

        @param request: CreateHanaInstanceRequest

        @return: CreateHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_instance_with_options(request, runtime)

    def create_hana_restore_with_options(self, request, runtime):
        """
        If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](~~101178~~).
        

        @param request: CreateHanaRestoreRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHanaRestoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.check_access):
            query['CheckAccess'] = request.check_access
        if not UtilClient.is_unset(request.clear_log):
            query['ClearLog'] = request.clear_log
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.master_client_id):
            query['MasterClientId'] = request.master_client_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.sid_admin):
            query['SidAdmin'] = request.sid_admin
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_catalog):
            query['UseCatalog'] = request.use_catalog
        if not UtilClient.is_unset(request.use_delta):
            query['UseDelta'] = request.use_delta
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaRestore',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaRestoreResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hana_restore(self, request):
        """
        If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](~~101178~~).
        

        @param request: CreateHanaRestoreRequest

        @return: CreateHanaRestoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_restore_with_options(request, runtime)

    def create_policy_bindings_with_options(self, tmp_req, runtime):
        """
        You can bind data sources to only one policy in each request.
        *   Elastic Compute Service (ECS) instances can be bound to only one policy.
        

        @param tmp_req: CreatePolicyBindingsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePolicyBindingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_binding_list):
            request.policy_binding_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_binding_list, 'PolicyBindingList', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_binding_list_shrink):
            query['PolicyBindingList'] = request.policy_binding_list_shrink
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_policy_bindings(self, request):
        """
        You can bind data sources to only one policy in each request.
        *   Elastic Compute Service (ECS) instances can be bound to only one policy.
        

        @param request: CreatePolicyBindingsRequest

        @return: CreatePolicyBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_bindings_with_options(request, runtime)

    def create_policy_v2with_options(self, tmp_req, runtime):
        """
        A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        *   You can specify only one interval as a backup cycle in a backup policy.
        *   Each backup policy allows you to back up data to only one backup vault.
        

        @param tmp_req: CreatePolicyV2Request

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    def create_policy_v2(self, request):
        """
        A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        *   You can specify only one interval as a backup cycle in a backup policy.
        *   Each backup policy allows you to back up data to only one backup vault.
        

        @param request: CreatePolicyV2Request

        @return: CreatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_v2with_options(request, runtime)

    def create_replication_vault_with_options(self, request, runtime):
        """
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.
        

        @param request: CreateReplicationVaultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateReplicationVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not UtilClient.is_unset(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not UtilClient.is_unset(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReplicationVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateReplicationVaultResponse(),
            self.call_api(params, req, runtime)
        )

    def create_replication_vault(self, request):
        """
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.
        

        @param request: CreateReplicationVaultRequest

        @return: CreateReplicationVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_replication_vault_with_options(request, runtime)

    def create_restore_job_with_options(self, tmp_req, runtime):
        """
        You must create a restore job based on the specified backup snapshot and restore destination.
        *   The type of the data source from which you restore data must be the same as the type of the restore destination.
        

        @param tmp_req: CreateRestoreJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRestoreJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateRestoreJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.failback_detail):
            request.failback_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.failback_detail, 'FailbackDetail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        if not UtilClient.is_unset(tmp_req.udm_detail):
            request.udm_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.udm_detail, 'UdmDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.failback_detail_shrink):
            query['FailbackDetail'] = request.failback_detail_shrink
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not UtilClient.is_unset(request.target_container):
            query['TargetContainer'] = request.target_container
        if not UtilClient.is_unset(request.target_container_cluster_id):
            query['TargetContainerClusterId'] = request.target_container_cluster_id
        if not UtilClient.is_unset(request.target_create_time):
            query['TargetCreateTime'] = request.target_create_time
        if not UtilClient.is_unset(request.target_file_system_id):
            query['TargetFileSystemId'] = request.target_file_system_id
        if not UtilClient.is_unset(request.target_instance_name):
            query['TargetInstanceName'] = request.target_instance_name
        if not UtilClient.is_unset(request.target_prefix):
            query['TargetPrefix'] = request.target_prefix
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.target_time):
            query['TargetTime'] = request.target_time
        if not UtilClient.is_unset(request.udm_detail_shrink):
            query['UdmDetail'] = request.udm_detail_shrink
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_path):
            body['TargetPath'] = request.target_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_restore_job(self, request):
        """
        You must create a restore job based on the specified backup snapshot and restore destination.
        *   The type of the data source from which you restore data must be the same as the type of the restore destination.
        

        @param request: CreateRestoreJobRequest

        @return: CreateRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_restore_job_with_options(request, runtime)

    def create_temp_file_upload_url_with_options(self, request, runtime):
        """
        1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        

        @param request: CreateTempFileUploadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTempFileUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTempFileUploadUrl',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateTempFileUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_temp_file_upload_url(self, request):
        """
        1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        

        @param request: CreateTempFileUploadUrlRequest

        @return: CreateTempFileUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_temp_file_upload_url_with_options(request, runtime)

    def create_vault_with_options(self, request, runtime):
        """
        Each Alibaba Cloud account can create up to 100 backup vaults.
        *   After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        

        @param request: CreateVaultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vault(self, request):
        """
        Each Alibaba Cloud account can create up to 100 backup vaults.
        *   After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        

        @param request: CreateVaultRequest

        @return: CreateVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vault_with_options(request, runtime)

    def delete_backup_client_with_options(self, request, runtime):
        """
        You cannot delete an active backup client from which a heartbeat packet is received within the previous hour. After you call the UninstallBackupClients operation to uninstall a backup client, the status of the backup client changes to inactive.
        *   This operation deletes the resources that are related to the backup client. The following resources are included:
        *   Backup plans
        *   Backup jobs
        *   Backup files
        

        @param request: DeleteBackupClientRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBackupClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_client(self, request):
        """
        You cannot delete an active backup client from which a heartbeat packet is received within the previous hour. After you call the UninstallBackupClients operation to uninstall a backup client, the status of the backup client changes to inactive.
        *   This operation deletes the resources that are related to the backup client. The following resources are included:
        *   Backup plans
        *   Backup jobs
        *   Backup files
        

        @param request: DeleteBackupClientRequest

        @return: DeleteBackupClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_client_with_options(request, runtime)

    def delete_backup_client_resource_with_options(self, tmp_req, runtime):
        """
        This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        

        @param tmp_req: DeleteBackupClientResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBackupClientResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeleteBackupClientResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClientResource',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_client_resource(self, request):
        """
        This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        

        @param request: DeleteBackupClientResourceRequest

        @return: DeleteBackupClientResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_client_resource_with_options(request, runtime)

    def delete_backup_plan_with_options(self, request, runtime):
        """
        If you delete a backup plan, the backup jobs are also deleted.
        *   If you delete a backup plan, the created snapshot files are not deleted.
        

        @param request: DeleteBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.require_no_running_jobs):
            query['RequireNoRunningJobs'] = request.require_no_running_jobs
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_plan(self, request):
        """
        If you delete a backup plan, the backup jobs are also deleted.
        *   If you delete a backup plan, the created snapshot files are not deleted.
        

        @param request: DeleteBackupPlanRequest

        @return: DeleteBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_plan_with_options(request, runtime)

    def delete_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteClientResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_client_with_options(request, runtime)

    def delete_hana_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hana_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_hana_backup_plan_with_options(request, runtime)

    def delete_hana_instance_with_options(self, request, runtime):
        """
        If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the data in the HBR client of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        

        @param request: DeleteHanaInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hana_instance(self, request):
        """
        If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the data in the HBR client of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        

        @param request: DeleteHanaInstanceRequest

        @return: DeleteHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hana_instance_with_options(request, runtime)

    def delete_policy_binding_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeletePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_policy_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_binding_with_options(request, runtime)

    def delete_policy_v2with_options(self, request, runtime):
        """
        If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        

        @param request: DeletePolicyV2Request

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePolicyV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    def delete_policy_v2(self, request):
        """
        If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        

        @param request: DeletePolicyV2Request

        @return: DeletePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_v2with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        """
        If you delete the most recent backup file for a data source, you must set the `Force parameter to true`. Otherwise, an error occurs.
        

        @param request: DeleteSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot(self, request):
        """
        If you delete the most recent backup file for a data source, you must set the `Force parameter to true`. Otherwise, an error occurs.
        

        @param request: DeleteSnapshotRequest

        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_vault_with_options(self, request, runtime):
        """
        You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        *   After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include backup clients of earlier versions, backup plans, backup jobs, snapshots, and restore jobs.
        

        @param request: DeleteVaultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteVaultResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vault(self, request):
        """
        You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        *   After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include backup clients of earlier versions, backup plans, backup jobs, snapshots, and restore jobs.
        

        @param request: DeleteVaultRequest

        @return: DeleteVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vault_with_options(request, runtime)

    def describe_backup_clients_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            body['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_clients(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    def describe_backup_jobs_2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupJobs2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_jobs_2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_jobs_2with_options(request, runtime)

    def describe_backup_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plans_with_options(request, runtime)

    def describe_clients_with_options(self, request, runtime):
        """
        This operation is applicable only to SAP HANA backup. For backup clients of other data sources, call the DescribeBackupClients operation.
        

        @param request: DescribeClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_clients(self, request):
        """
        This operation is applicable only to SAP HANA backup. For backup clients of other data sources, call the DescribeBackupClients operation.
        

        @param request: DescribeClientsRequest

        @return: DescribeClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_clients_with_options(request, runtime)

    def describe_container_cluster_with_options(self, request, runtime):
        """
        You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        

        @param request: DescribeContainerClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_cluster(self, request):
        """
        You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        

        @param request: DescribeContainerClusterRequest

        @return: DescribeContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_cluster_with_options(request, runtime)

    def describe_cross_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossAccounts',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeCrossAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_accounts_with_options(request, runtime)

    def describe_hana_backup_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_backup_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backup_plans_with_options(request, runtime)

    def describe_hana_backup_setting_with_options(self, request, runtime):
        """
        If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        

        @param request: DescribeHanaBackupSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_backup_setting(self, request):
        """
        If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        

        @param request: DescribeHanaBackupSettingRequest

        @return: DescribeHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backup_setting_with_options(request, runtime)

    def describe_hana_backups_async_with_options(self, request, runtime):
        """
        After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the execution result of the asynchronous job.
        

        @param request: DescribeHanaBackupsAsyncRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHanaBackupsAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.include_differential):
            query['IncludeDifferential'] = request.include_differential
        if not UtilClient.is_unset(request.include_incremental):
            query['IncludeIncremental'] = request.include_incremental
        if not UtilClient.is_unset(request.include_log):
            query['IncludeLog'] = request.include_log
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_backint):
            query['UseBackint'] = request.use_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupsAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_backups_async(self, request):
        """
        After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the execution result of the asynchronous job.
        

        @param request: DescribeHanaBackupsAsyncRequest

        @return: DescribeHanaBackupsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backups_async_with_options(request, runtime)

    def describe_hana_databases_with_options(self, request, runtime):
        """
        After you register an SAP HANA instance and install a backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        

        @param request: DescribeHanaDatabasesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHanaDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaDatabases',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_databases(self, request):
        """
        After you register an SAP HANA instance and install a backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        

        @param request: DescribeHanaDatabasesRequest

        @return: DescribeHanaDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_databases_with_options(request, runtime)

    def describe_hana_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHanaInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_instances_with_options(request, runtime)

    def describe_hana_restores_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.restore_status):
            query['RestoreStatus'] = request.restore_status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRestores',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRestoresResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_restores(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_restores_with_options(request, runtime)

    def describe_hana_retention_setting_with_options(self, request, runtime):
        """
        If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        *   HBR deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        

        @param request: DescribeHanaRetentionSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hana_retention_setting(self, request):
        """
        If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        *   HBR deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        

        @param request: DescribeHanaRetentionSettingRequest

        @return: DescribeHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_retention_setting_with_options(request, runtime)

    def describe_ots_table_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not UtilClient.is_unset(request.ots_instances):
            body_flat['OtsInstances'] = request.ots_instances
        if not UtilClient.is_unset(request.snapshot_ids):
            body_flat['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOtsTableSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeOtsTableSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ots_table_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ots_table_snapshots_with_options(request, runtime)

    def describe_policies_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePoliciesV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePoliciesV2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_policies_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policies_v2with_options(request, runtime)

    def describe_policy_bindings_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_bindings_with_options(request, runtime)

    def describe_recoverable_ots_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoverableOtsInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRecoverableOtsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recoverable_ots_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recoverable_ots_instances_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_vault_count):
            query['NeedVaultCount'] = request.need_vault_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_restore_jobs_2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRestoreJobs2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_jobs_2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_jobs_2with_options(request, runtime)

    def describe_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    def describe_udm_snapshots_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeUdmSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_ids):
            request.snapshot_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_ids, 'SnapshotIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        body = {}
        if not UtilClient.is_unset(request.snapshot_ids_shrink):
            body['SnapshotIds'] = request.snapshot_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUdmSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeUdmSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_udm_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_udm_snapshots_with_options(request, runtime)

    def describe_vault_replication_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVaultReplicationRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultReplicationRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vault_replication_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vault_replication_regions_with_options(request, runtime)

    def describe_vaults_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVaults',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vaults(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vaults_with_options(request, runtime)

    def detach_nas_file_system_with_options(self, request, runtime):
        """
        If the request is successful, the mount target is deleted.
        *   After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        

        @param request: DetachNasFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachNasFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachNasFileSystem',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DetachNasFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_nas_file_system(self, request):
        """
        If the request is successful, the mount target is deleted.
        *   After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        

        @param request: DetachNasFileSystemRequest

        @return: DetachNasFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_nas_file_system_with_options(request, runtime)

    def disable_backup_plan_with_options(self, request, runtime):
        """
        If the request is successful, the specified backup plan is disabled. If you call the DescribeBackupPlans operation to query backup plans, the Disabled parameter is set to true for the backup plan.
        

        @param request: DisableBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_backup_plan(self, request):
        """
        If the request is successful, the specified backup plan is disabled. If you call the DescribeBackupPlans operation to query backup plans, the Disabled parameter is set to true for the backup plan.
        

        @param request: DisableBackupPlanRequest

        @return: DisableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_backup_plan_with_options(request, runtime)

    def disable_hana_backup_plan_with_options(self, request, runtime):
        """
        To enable the backup plan again, call the EnableHanaBackupPlan operation.
        

        @param request: DisableHanaBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_hana_backup_plan(self, request):
        """
        To enable the backup plan again, call the EnableHanaBackupPlan operation.
        

        @param request: DisableHanaBackupPlanRequest

        @return: DisableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_hana_backup_plan_with_options(request, runtime)

    def enable_backup_plan_with_options(self, request, runtime):
        """
        If the request is successful, the system enables the backup plan and backs up data based on the polices that are specified in the backup plan. If you call the DescribeBackupPlans operation to query backup plans, the Disabled parameter is automatically set to false for the backup plan.
        

        @param request: EnableBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_backup_plan(self, request):
        """
        If the request is successful, the system enables the backup plan and backs up data based on the polices that are specified in the backup plan. If you call the DescribeBackupPlans operation to query backup plans, the Disabled parameter is automatically set to false for the backup plan.
        

        @param request: EnableBackupPlanRequest

        @return: EnableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_plan_with_options(request, runtime)

    def enable_hana_backup_plan_with_options(self, request, runtime):
        """
        To disable the backup plan again, call the DisableHanaBackupPlan operation.
        

        @param request: EnableHanaBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_hana_backup_plan(self, request):
        """
        To disable the backup plan again, call the DisableHanaBackupPlan operation.
        

        @param request: EnableHanaBackupPlanRequest

        @return: EnableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_hana_backup_plan_with_options(request, runtime)

    def execute_backup_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecuteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_backup_plan_with_options(request, runtime)

    def execute_policy_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecutePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecutePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    def execute_policy_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_policy_v2with_options(request, runtime)

    def generate_ram_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.require_base_policy):
            query['RequireBasePolicy'] = request.require_base_policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateRamPolicy',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GenerateRamPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_ram_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_ram_policy_with_options(request, runtime)

    def get_temp_file_download_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.temp_file_key):
            query['TempFileKey'] = request.temp_file_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTempFileDownloadLink',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GetTempFileDownloadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_temp_file_download_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_temp_file_download_link_with_options(request, runtime)

    def install_backup_clients_with_options(self, tmp_req, runtime):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        *   You can call the [DescribeTask](~~431265~~) operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        

        @param tmp_req: InstallBackupClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.InstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.InstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def install_backup_clients(self, request):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        *   You can call the [DescribeTask](~~431265~~) operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        

        @param request: InstallBackupClientsRequest

        @return: InstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_backup_clients_with_options(request, runtime)

    def open_hbr_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenHbrService',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.OpenHbrServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_hbr_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_hbr_service_with_options(runtime)

    def search_historical_snapshots_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.SearchHistoricalSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchHistoricalSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.SearchHistoricalSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def search_historical_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_historical_snapshots_with_options(request, runtime)

    def start_hana_database_async_with_options(self, request, runtime):
        """
        To stop the database again, call the StopHanaDatabaseAsync operation.
        

        @param request: StartHanaDatabaseAsyncRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StartHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def start_hana_database_async(self, request):
        """
        To stop the database again, call the StopHanaDatabaseAsync operation.
        

        @param request: StartHanaDatabaseAsyncRequest

        @return: StartHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_hana_database_async_with_options(request, runtime)

    def stop_hana_database_async_with_options(self, request, runtime):
        """
        To start the database again, call the StartHanaDatabaseAsync operation.
        

        @param request: StopHanaDatabaseAsyncRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StopHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_hana_database_async(self, request):
        """
        To start the database again, call the StartHanaDatabaseAsync operation.
        

        @param request: StopHanaDatabaseAsyncRequest

        @return: StopHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_hana_database_async_with_options(request, runtime)

    def uninstall_backup_clients_with_options(self, tmp_req, runtime):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        *   You can call the DescribeTask operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        

        @param tmp_req: UninstallBackupClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UninstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_backup_clients(self, request):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        *   You can call the DescribeTask operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        

        @param request: UninstallBackupClientsRequest

        @return: UninstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_backup_clients_with_options(request, runtime)

    def uninstall_client_with_options(self, request, runtime):
        """
        If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        

        @param request: UninstallClientRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallClientResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_client(self, request):
        """
        If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        

        @param request: UninstallClientRequest

        @return: UninstallClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_client_with_options(request, runtime)

    def update_backup_plan_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.update_paths):
            query['UpdatePaths'] = request.update_paths
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_backup_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_backup_plan_with_options(request, runtime)

    def update_client_settings_with_options(self, request, runtime):
        """
        You can call this operation to update the configurations of both the old and new HBR clients.
        

        @param request: UpdateClientSettingsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateClientSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_on_partial_complete):
            query['AlertOnPartialComplete'] = request.alert_on_partial_complete
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.data_network_type):
            query['DataNetworkType'] = request.data_network_type
        if not UtilClient.is_unset(request.data_proxy_setting):
            query['DataProxySetting'] = request.data_proxy_setting
        if not UtilClient.is_unset(request.max_cpu_core):
            query['MaxCpuCore'] = request.max_cpu_core
        if not UtilClient.is_unset(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not UtilClient.is_unset(request.max_worker):
            query['MaxWorker'] = request.max_worker
        if not UtilClient.is_unset(request.proxy_host):
            query['ProxyHost'] = request.proxy_host
        if not UtilClient.is_unset(request.proxy_password):
            query['ProxyPassword'] = request.proxy_password
        if not UtilClient.is_unset(request.proxy_port):
            query['ProxyPort'] = request.proxy_port
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientSettings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateClientSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_client_settings(self, request):
        """
        You can call this operation to update the configurations of both the old and new HBR clients.
        

        @param request: UpdateClientSettingsRequest

        @return: UpdateClientSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_client_settings_with_options(request, runtime)

    def update_container_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.renew_token):
            query['RenewToken'] = request.renew_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_container_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_container_cluster_with_options(request, runtime)

    def update_hana_backup_plan_with_options(self, request, runtime):
        """
        A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup plan.
        *   You can specify only one interval as a backup cycle in a backup plan.
        *   Each backup plan allows you to back up data to only one backup vault.
        

        @param request: UpdateHanaBackupPlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hana_backup_plan(self, request):
        """
        A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        *   You can specify only one type of data source in a backup plan.
        *   You can specify only one interval as a backup cycle in a backup plan.
        *   Each backup plan allows you to back up data to only one backup vault.
        

        @param request: UpdateHanaBackupPlanRequest

        @return: UpdateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_backup_plan_with_options(request, runtime)

    def update_hana_backup_setting_with_options(self, request, runtime):
        """
        You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        

        @param request: UpdateHanaBackupSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_backup_parameter_file):
            query['CatalogBackupParameterFile'] = request.catalog_backup_parameter_file
        if not UtilClient.is_unset(request.catalog_backup_using_backint):
            query['CatalogBackupUsingBackint'] = request.catalog_backup_using_backint
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_backup_parameter_file):
            query['DataBackupParameterFile'] = request.data_backup_parameter_file
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.enable_auto_log_backup):
            query['EnableAutoLogBackup'] = request.enable_auto_log_backup
        if not UtilClient.is_unset(request.log_backup_parameter_file):
            query['LogBackupParameterFile'] = request.log_backup_parameter_file
        if not UtilClient.is_unset(request.log_backup_timeout):
            query['LogBackupTimeout'] = request.log_backup_timeout
        if not UtilClient.is_unset(request.log_backup_using_backint):
            query['LogBackupUsingBackint'] = request.log_backup_using_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hana_backup_setting(self, request):
        """
        You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        

        @param request: UpdateHanaBackupSettingRequest

        @return: UpdateHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_backup_setting_with_options(request, runtime)

    def update_hana_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hana_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_hana_instance_with_options(request, runtime)

    def update_hana_retention_setting_with_options(self, request, runtime):
        """
        If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        *   HBR deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        

        @param request: UpdateHanaRetentionSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hana_retention_setting(self, request):
        """
        If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        *   HBR deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        

        @param request: UpdateHanaRetentionSettingRequest

        @return: UpdateHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_retention_setting_with_options(request, runtime)

    def update_policy_binding_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_options):
            request.advanced_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_options, 'AdvancedOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_options_shrink):
            query['AdvancedOptions'] = request.advanced_options_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.policy_binding_description):
            query['PolicyBindingDescription'] = request.policy_binding_description
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_policy_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_policy_binding_with_options(request, runtime)

    def update_policy_v2with_options(self, tmp_req, runtime):
        """
        If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        

        @param tmp_req: UpdatePolicyV2Request

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    def update_policy_v2(self, request):
        """
        If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        

        @param request: UpdatePolicyV2Request

        @return: UpdatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.update_policy_v2with_options(request, runtime)

    def update_vault_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vault(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vault_with_options(request, runtime)

    def upgrade_backup_clients_with_options(self, tmp_req, runtime):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        *   You can call the DescribeTask operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes.
        

        @param tmp_req: UpgradeBackupClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpgradeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_backup_clients(self, request):
        """
        This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        *   You can call the DescribeTask operation to query the execution result of an asynchronous job.
        *   The timeout period of an asynchronous job is 15 minutes.
        

        @param request: UpgradeBackupClientsRequest

        @return: UpgradeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_clients_with_options(request, runtime)

    def upgrade_client_with_options(self, request, runtime):
        """
        You can call this operation to upgrade a backup client to the latest version. After the backup client is upgraded, the version of the backup client cannot be rolled back.
        

        @param request: UpgradeClientRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_client(self, request):
        """
        You can call this operation to upgrade a backup client to the latest version. After the backup client is upgraded, the version of the backup client cannot be rolled back.
        

        @param request: UpgradeClientRequest

        @return: UpgradeClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)
