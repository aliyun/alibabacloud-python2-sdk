# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dms_enterprise20181101 import models as dms_enterprise_20181101_models
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
        self._endpoint = self.get_endpoint('dms-enterprise', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def submit_struct_sync_order_approval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse().from_map(
            self.do_rpcrequest('SubmitStructSyncOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_struct_sync_order_approval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_struct_sync_order_approval_with_options(request, runtime)

    def list_database_user_permssions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse().from_map(
            self.do_rpcrequest('ListDatabaseUserPermssions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_database_user_permssions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_database_user_permssions_with_options(request, runtime)

    def list_sensitive_columns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsResponse().from_map(
            self.do_rpcrequest('ListSensitiveColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sensitive_columns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_columns_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def submit_order_approval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SubmitOrderApprovalResponse().from_map(
            self.do_rpcrequest('SubmitOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_order_approval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_order_approval_with_options(request, runtime)

    def grant_user_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GrantUserPermissionResponse().from_map(
            self.do_rpcrequest('GrantUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_user_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permission_with_options(request, runtime)

    def get_meta_table_detail_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse().from_map(
            self.do_rpcrequest('GetMetaTableDetailInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_detail_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_detail_info_with_options(request, runtime)

    def get_data_correct_sqlfile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse().from_map(
            self.do_rpcrequest('GetDataCorrectSQLFile', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_sqlfile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_sqlfile_with_options(request, runtime)

    def create_free_lock_correct_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateFreeLockCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse().from_map(
            self.do_rpcrequest('CreateFreeLockCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_free_lock_correct_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_free_lock_correct_order_with_options(request, runtime)

    def create_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plugin_param):
            request.plugin_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plugin_param, 'PluginParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateOrderResponse().from_map(
            self.do_rpcrequest('CreateOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    def list_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabasesResponse().from_map(
            self.do_rpcrequest('ListDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    def list_user_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUserPermissionsResponse().from_map(
            self.do_rpcrequest('ListUserPermissions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_permissions_with_options(request, runtime)

    def list_work_flow_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse().from_map(
            self.do_rpcrequest('ListWorkFlowTemplates', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_work_flow_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_work_flow_templates_with_options(request, runtime)

    def get_data_export_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportOrderDetailResponse().from_map(
            self.do_rpcrequest('GetDataExportOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_export_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_export_order_detail_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListInstancesResponse().from_map(
            self.do_rpcrequest('ListInstances', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def get_user_upload_file_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetUserUploadFileJobResponse().from_map(
            self.do_rpcrequest('GetUserUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_upload_file_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_upload_file_job_with_options(request, runtime)

    def get_struct_sync_job_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetStructSyncJobDetailResponse().from_map(
            self.do_rpcrequest('GetStructSyncJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_struct_sync_job_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_job_detail_with_options(request, runtime)

    def create_upload_ossfile_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateUploadOSSFileJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_target):
            request.upload_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.upload_target), 'UploadTarget', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse().from_map(
            self.do_rpcrequest('CreateUploadOSSFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_ossfile_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upload_ossfile_job_with_options(request, runtime)

    def search_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchDatabaseResponse().from_map(
            self.do_rpcrequest('SearchDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_database_with_options(request, runtime)

    def sync_database_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncDatabaseMetaResponse().from_map(
            self.do_rpcrequest('SyncDatabaseMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_database_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_database_meta_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def execute_struct_sync_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteStructSyncResponse().from_map(
            self.do_rpcrequest('ExecuteStructSync', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_struct_sync(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_struct_sync_with_options(request, runtime)

    def get_data_correct_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse().from_map(
            self.do_rpcrequest('GetDataCorrectOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_order_detail_with_options(request, runtime)

    def list_columns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListColumnsResponse().from_map(
            self.do_rpcrequest('ListColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_columns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_columns_with_options(request, runtime)

    def revoke_user_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RevokeUserPermissionResponse().from_map(
            self.do_rpcrequest('RevokeUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_user_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_user_permission_with_options(request, runtime)

    def get_meta_table_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableColumnResponse().from_map(
            self.do_rpcrequest('GetMetaTableColumn', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    def enable_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.EnableUserResponse().from_map(
            self.do_rpcrequest('EnableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_user_with_options(request, runtime)

    def update_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateInstanceResponse().from_map(
            self.do_rpcrequest('UpdateInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    def execute_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteScriptResponse().from_map(
            self.do_rpcrequest('ExecuteScript', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_script_with_options(request, runtime)

    def list_dbtask_sqljob_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse().from_map(
            self.do_rpcrequest('ListDBTaskSQLJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dbtask_sqljob_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbtask_sqljob_detail_with_options(request, runtime)

    def disable_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DisableUserResponse().from_map(
            self.do_rpcrequest('DisableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_user_with_options(request, runtime)

    def get_approval_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetApprovalDetailResponse().from_map(
            self.do_rpcrequest('GetApprovalDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_approval_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_approval_detail_with_options(request, runtime)

    def get_user_active_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetUserActiveTenantResponse().from_map(
            self.do_rpcrequest('GetUserActiveTenant', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_active_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_active_tenant_with_options(request, runtime)

    def register_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterUserResponse().from_map(
            self.do_rpcrequest('RegisterUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_user_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetInstanceResponse().from_map(
            self.do_rpcrequest('GetInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_perm_apply_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse().from_map(
            self.do_rpcrequest('GetPermApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_perm_apply_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_perm_apply_order_detail_with_options(request, runtime)

    def list_indexes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListIndexesResponse().from_map(
            self.do_rpcrequest('ListIndexes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_indexes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_indexes_with_options(request, runtime)

    def list_logic_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicTablesResponse().from_map(
            self.do_rpcrequest('ListLogicTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_logic_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_logic_tables_with_options(request, runtime)

    def get_table_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetTableTopologyResponse().from_map(
            self.do_rpcrequest('GetTableTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_table_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_table_topology_with_options(request, runtime)

    def get_data_export_download_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportDownloadURLResponse().from_map(
            self.do_rpcrequest('GetDataExportDownloadURL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_export_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_export_download_urlwith_options(request, runtime)

    def create_data_cron_clear_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCronClearOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateDataCronClearOrderResponse().from_map(
            self.do_rpcrequest('CreateDataCronClearOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_cron_clear_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_cron_clear_order_with_options(request, runtime)

    def create_publish_group_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreatePublishGroupTaskResponse().from_map(
            self.do_rpcrequest('CreatePublishGroupTask', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_publish_group_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_publish_group_task_with_options(request, runtime)

    def get_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDatabaseResponse().from_map(
            self.do_rpcrequest('GetDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    def get_owner_apply_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse().from_map(
            self.do_rpcrequest('GetOwnerApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_owner_apply_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_owner_apply_order_detail_with_options(request, runtime)

    def get_op_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOpLogResponse().from_map(
            self.do_rpcrequest('GetOpLog', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_op_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_op_log_with_options(request, runtime)

    def search_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchTableResponse().from_map(
            self.do_rpcrequest('SearchTable', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_table_with_options(request, runtime)

    def list_dbtask_sqljob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDBTaskSQLJobResponse().from_map(
            self.do_rpcrequest('ListDBTaskSQLJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dbtask_sqljob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbtask_sqljob_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def get_data_cron_clear_task_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse().from_map(
            self.do_rpcrequest('GetDataCronClearTaskDetailList', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_cron_clear_task_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_cron_clear_task_detail_list_with_options(request, runtime)

    def get_struct_sync_job_analyze_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse().from_map(
            self.do_rpcrequest('GetStructSyncJobAnalyzeResult', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_struct_sync_job_analyze_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_job_analyze_result_with_options(request, runtime)

    def approve_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ApproveOrderResponse().from_map(
            self.do_rpcrequest('ApproveOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.approve_order_with_options(request, runtime)

    def get_data_correct_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse().from_map(
            self.do_rpcrequest('GetDataCorrectTaskDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_task_detail_with_options(request, runtime)

    def create_upload_file_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateUploadFileJobResponse().from_map(
            self.do_rpcrequest('CreateUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_file_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upload_file_job_with_options(request, runtime)

    def list_logic_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicDatabasesResponse().from_map(
            self.do_rpcrequest('ListLogicDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_logic_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_logic_databases_with_options(request, runtime)

    def create_data_import_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataImportOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateDataImportOrderResponse().from_map(
            self.do_rpcrequest('CreateDataImportOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_import_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_import_order_with_options(request, runtime)

    def close_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CloseOrderResponse().from_map(
            self.do_rpcrequest('CloseOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_order_with_options(request, runtime)

    def sync_instance_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncInstanceMetaResponse().from_map(
            self.do_rpcrequest('SyncInstanceMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_instance_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_instance_meta_with_options(request, runtime)

    def list_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListOrdersResponse().from_map(
            self.do_rpcrequest('ListOrders', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_orders_with_options(request, runtime)

    def get_order_base_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOrderBaseInfoResponse().from_map(
            self.do_rpcrequest('GetOrderBaseInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_order_base_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_order_base_info_with_options(request, runtime)

    def list_user_tenants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUserTenantsResponse().from_map(
            self.do_rpcrequest('ListUserTenants', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_tenants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_tenants_with_options(request, runtime)

    def set_owners_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SetOwnersResponse().from_map(
            self.do_rpcrequest('SetOwners', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_owners(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_owners_with_options(request, runtime)

    def create_data_correct_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateDataCorrectOrderResponse().from_map(
            self.do_rpcrequest('CreateDataCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_correct_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_correct_order_with_options(request, runtime)

    def get_logic_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetLogicDatabaseResponse().from_map(
            self.do_rpcrequest('GetLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_logic_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_logic_database_with_options(request, runtime)

    def get_data_correct_backup_files_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.GetDataCorrectBackupFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse().from_map(
            self.do_rpcrequest('GetDataCorrectBackupFiles', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_backup_files_with_options(request, runtime)

    def register_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterInstanceResponse().from_map(
            self.do_rpcrequest('RegisterInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_instance_with_options(request, runtime)

    def create_struct_sync_order_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateStructSyncOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateStructSyncOrderResponse().from_map(
            self.do_rpcrequest('CreateStructSyncOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_struct_sync_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_struct_sync_order_with_options(request, runtime)

    def execute_data_export_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataExportResponse().from_map(
            self.do_rpcrequest('ExecuteDataExport', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_data_export(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_data_export_with_options(request, runtime)

    def execute_data_correct_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataCorrectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataCorrectResponse().from_map(
            self.do_rpcrequest('ExecuteDataCorrect', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_data_correct(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_data_correct_with_options(request, runtime)

    def list_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListTablesResponse().from_map(
            self.do_rpcrequest('ListTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    def list_work_flow_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowNodesResponse().from_map(
            self.do_rpcrequest('ListWorkFlowNodes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_work_flow_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_work_flow_nodes_with_options(request, runtime)

    def get_struct_sync_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse().from_map(
            self.do_rpcrequest('GetStructSyncOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_struct_sync_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_order_detail_with_options(request, runtime)

    def list_sensitive_columns_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse().from_map(
            self.do_rpcrequest('ListSensitiveColumnsDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sensitive_columns_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_columns_detail_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def get_struct_sync_exec_sql_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse().from_map(
            self.do_rpcrequest('GetStructSyncExecSqlDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_struct_sync_exec_sql_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_exec_sql_detail_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def get_table_dbtopology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetTableDBTopologyResponse().from_map(
            self.do_rpcrequest('GetTableDBTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_table_dbtopology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_table_dbtopology_with_options(request, runtime)
