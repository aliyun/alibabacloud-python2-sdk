# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_datalake20200710 import models as data_lake_20200710_models
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
            'ap-northeast-1': 'datalake-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'datalake-daily.aliyuncs.com',
            'ap-south-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-2': 'datalake-daily.aliyuncs.com',
            'ap-southeast-3': 'datalake-daily.aliyuncs.com',
            'ap-southeast-5': 'datalake-daily.aliyuncs.com',
            'cn-beijing': 'dlf.cn-beijing.aliyuncs.com',
            'cn-beijing-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'datalake-daily.aliyuncs.com',
            'cn-chengdu': 'datalake-daily.aliyuncs.com',
            'cn-edge-1': 'datalake-daily.aliyuncs.com',
            'cn-fujian': 'datalake-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou': 'dlf.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'datalake-daily.aliyuncs.com',
            'cn-hongkong': 'datalake-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'datalake-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-qingdao': 'datalake-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'datalake-daily.aliyuncs.com',
            'cn-shanghai': 'dlf.cn-shanghai.aliyuncs.com',
            'cn-shanghai-et15-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-inner': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen': 'dlf.cn-shenzhen.aliyuncs.com',
            'cn-shenzhen-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'datalake-daily.aliyuncs.com',
            'cn-wuhan': 'datalake-daily.aliyuncs.com',
            'cn-wulanchabu': 'datalake-daily.aliyuncs.com',
            'cn-yushanfang': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'datalake-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'datalake-daily.aliyuncs.com',
            'eu-central-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1-oxs': 'datalake-daily.aliyuncs.com',
            'me-east-1': 'datalake-daily.aliyuncs.com',
            'rus-west-1-pop': 'datalake-daily.aliyuncs.com',
            'us-east-1': 'datalake-daily.aliyuncs.com',
            'us-west-1': 'datalake-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('datalake', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_lock_with_options(self, request, headers, runtime):
        """
        @summary abort lock context with the lockid
        

        @param request: AbortLockRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: AbortLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/locks/abort',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.AbortLockResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_lock(self, request):
        """
        @summary abort lock context with the lockid
        

        @param request: AbortLockRequest

        @return: AbortLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_lock_with_options(request, headers, runtime)

    def batch_create_partitions_with_options(self, request, headers, runtime):
        """
        @summary 批量创建分区
        

        @param request: BatchCreatePartitionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchCreatePartitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreatePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_partitions(self, request):
        """
        @summary 批量创建分区
        

        @param request: BatchCreatePartitionsRequest

        @return: BatchCreatePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_partitions_with_options(request, headers, runtime)

    def batch_create_tables_with_options(self, request, headers, runtime):
        """
        @summary 批量创建表
        

        @param request: BatchCreateTablesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchCreateTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreateTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_tables(self, request):
        """
        @summary 批量创建表
        

        @param request: BatchCreateTablesRequest

        @return: BatchCreateTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_tables_with_options(request, headers, runtime)

    def batch_delete_partitions_with_options(self, request, headers, runtime):
        """
        @summary batch delete partitions
        

        @param request: BatchDeletePartitionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchDeletePartitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeletePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeletePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_partitions(self, request):
        """
        @summary batch delete partitions
        

        @param request: BatchDeletePartitionsRequest

        @return: BatchDeletePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_partitions_with_options(request, headers, runtime)

    def batch_delete_table_versions_with_options(self, request, headers, runtime):
        """
        @summary BatchDeleteTableVersions
        

        @param request: BatchDeleteTableVersionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchDeleteTableVersionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_ids):
            body['VersionIds'] = request.version_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/versions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_table_versions(self, request):
        """
        @summary BatchDeleteTableVersions
        

        @param request: BatchDeleteTableVersionsRequest

        @return: BatchDeleteTableVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_table_versions_with_options(request, headers, runtime)

    def batch_delete_tables_with_options(self, request, headers, runtime):
        """
        @summary BatchDeleteTables
        

        @param request: BatchDeleteTablesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchDeleteTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_tables(self, request):
        """
        @summary BatchDeleteTables
        

        @param request: BatchDeleteTablesRequest

        @return: BatchDeleteTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_tables_with_options(request, headers, runtime)

    def batch_get_partition_column_statistics_with_options(self, request, headers, runtime):
        """
        @summary Batch Get Partition Column Statistics
        

        @param request: BatchGetPartitionColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchGetPartitionColumnStatisticsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names):
            body['ColumnNames'] = request.column_names
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names):
            body['PartitionNames'] = request.partition_names
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/columnstatistics/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_partition_column_statistics(self, request):
        """
        @summary Batch Get Partition Column Statistics
        

        @param request: BatchGetPartitionColumnStatisticsRequest

        @return: BatchGetPartitionColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_partition_column_statistics_with_options(request, headers, runtime)

    def batch_get_partitions_with_options(self, request, headers, runtime):
        """
        @summary batch get partitions
        

        @param request: BatchGetPartitionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchGetPartitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_partitions(self, request):
        """
        @summary batch get partitions
        

        @param request: BatchGetPartitionsRequest

        @return: BatchGetPartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_partitions_with_options(request, headers, runtime)

    def batch_get_tables_with_options(self, request, headers, runtime):
        """
        @summary batch get tables
        

        @param request: BatchGetTablesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchGetTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_tables(self, request):
        """
        @summary batch get tables
        

        @param request: BatchGetTablesRequest

        @return: BatchGetTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_tables_with_options(request, headers, runtime)

    def batch_grant_permissions_with_options(self, request, headers, runtime):
        """
        @summary 批量授权
        

        @param request: BatchGrantPermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchGrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/batchgrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_grant_permissions(self, request):
        """
        @summary 批量授权
        

        @param request: BatchGrantPermissionsRequest

        @return: BatchGrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_grant_permissions_with_options(request, headers, runtime)

    def batch_revoke_permissions_with_options(self, request, headers, runtime):
        """
        @summary 批量取消授权
        

        @param request: BatchRevokePermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchRevokePermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/batchrevoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchRevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_revoke_permissions(self, request):
        """
        @summary 批量取消授权
        

        @param request: BatchRevokePermissionsRequest

        @return: BatchRevokePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_revoke_permissions_with_options(request, headers, runtime)

    def batch_update_partitions_with_options(self, request, headers, runtime):
        """
        @summary batch update partitions
        

        @param request: BatchUpdatePartitionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchUpdatePartitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/batchupdate',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdatePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_partitions(self, request):
        """
        @summary batch update partitions
        

        @param request: BatchUpdatePartitionsRequest

        @return: BatchUpdatePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_partitions_with_options(request, headers, runtime)

    def batch_update_tables_with_options(self, request, headers, runtime):
        """
        @summary 批量更新表
        

        @param request: BatchUpdateTablesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchUpdateTablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/batchupdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdateTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_tables(self, request):
        """
        @summary 批量更新表
        

        @param request: BatchUpdateTablesRequest

        @return: BatchUpdateTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_tables_with_options(request, headers, runtime)

    def cancel_query_with_options(self, request, headers, runtime):
        """
        @summary 取消查询任务
        

        @param request: CancelQueryRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/query/cancelQuery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CancelQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_query(self, request):
        """
        @summary 取消查询任务
        

        @param request: CancelQueryRequest

        @return: CancelQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_query_with_options(request, headers, runtime)

    def check_permissions_with_options(self, request, headers, runtime):
        """
        @summary Check permissions
        

        @param request: CheckPermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckPermissionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CheckPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CheckPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_permissions(self, request):
        """
        @summary Check permissions
        

        @param request: CheckPermissionsRequest

        @return: CheckPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_permissions_with_options(request, headers, runtime)

    def create_catalog_with_options(self, request, headers, runtime):
        """
        @summary 创建数据湖Catalog
        

        @param request: CreateCatalogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def create_catalog(self, request):
        """
        @summary 创建数据湖Catalog
        

        @param request: CreateCatalogRequest

        @return: CreateCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_catalog_with_options(request, headers, runtime)

    def create_database_with_options(self, request, headers, runtime):
        """
        @summary create database
        

        @param request: CreateDatabaseRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDatabaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_database(self, request):
        """
        @summary create database
        

        @param request: CreateDatabaseRequest

        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_database_with_options(request, headers, runtime)

    def create_function_with_options(self, request, headers, runtime):
        """
        @summary Create function
        

        @param request: CreateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function(self, request):
        """
        @summary Create function
        

        @param request: CreateFunctionRequest

        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    def create_lock_with_options(self, request, headers, runtime):
        """
        @summary create lock
        

        @param request: CreateLockRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock_obj_list):
            body['LockObjList'] = request.lock_obj_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/locks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateLockResponse(),
            self.call_api(params, req, runtime)
        )

    def create_lock(self, request):
        """
        @summary create lock
        

        @param request: CreateLockRequest

        @return: CreateLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_lock_with_options(request, headers, runtime)

    def create_partition_with_options(self, request, headers, runtime):
        """
        @summary Create Partition
        

        @param request: CreatePartitionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreatePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_partition(self, request):
        """
        @summary Create Partition
        

        @param request: CreatePartitionRequest

        @return: CreatePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_partition_with_options(request, headers, runtime)

    def create_role_with_options(self, request, headers, runtime):
        """
        @summary 创建数据糊角色
        

        @param request: CreateRoleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_role(self, request):
        """
        @summary 创建数据糊角色
        

        @param request: CreateRoleRequest

        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(request, headers, runtime)

    def create_table_with_options(self, request, headers, runtime):
        """
        @summary Create tables
        

        @param request: CreateTableRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_table(self, request):
        """
        @summary Create tables
        

        @param request: CreateTableRequest

        @return: CreateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_with_options(request, headers, runtime)

    def delete_catalog_with_options(self, request, headers, runtime):
        """
        @summary Delete Catalog by catalogId
        

        @param request: DeleteCatalogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_catalog(self, request):
        """
        @summary Delete Catalog by catalogId
        

        @param request: DeleteCatalogRequest

        @return: DeleteCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_catalog_with_options(request, headers, runtime)

    def delete_database_with_options(self, request, headers, runtime):
        """
        @summary Delete database by catalogId and database name
        

        @param request: DeleteDatabaseRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.cascade):
            query['Cascade'] = request.cascade
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_database(self, request):
        """
        @summary Delete database by catalogId and database name
        

        @param request: DeleteDatabaseRequest

        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_database_with_options(request, headers, runtime)

    def delete_function_with_options(self, request, headers, runtime):
        """
        @summary Delete function
        

        @param request: DeleteFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_function(self, request):
        """
        @summary Delete function
        

        @param request: DeleteFunctionRequest

        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(request, headers, runtime)

    def delete_partition_with_options(self, request, headers, runtime):
        """
        @summary delete partition
        

        @param request: DeletePartitionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_partition(self, request):
        """
        @summary delete partition
        

        @param request: DeletePartitionRequest

        @return: DeletePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_partition_with_options(request, headers, runtime)

    def delete_partition_column_statistics_with_options(self, tmp_req, headers, runtime):
        """
        @summary DeletePartitionColumnStatistics
        

        @param tmp_req: DeletePartitionColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePartitionColumnStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeletePartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_partition_column_statistics(self, request):
        """
        @summary DeletePartitionColumnStatistics
        

        @param request: DeletePartitionColumnStatisticsRequest

        @return: DeletePartitionColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_partition_column_statistics_with_options(request, headers, runtime)

    def delete_role_with_options(self, request, headers, runtime):
        """
        @summary 删除角色
        

        @param request: DeleteRoleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_role(self, request):
        """
        @summary 删除角色
        

        @param request: DeleteRoleRequest

        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    def delete_table_with_options(self, request, headers, runtime):
        """
        @summary delete table
        

        @param request: DeleteTableRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table(self, request):
        """
        @summary delete table
        

        @param request: DeleteTableRequest

        @return: DeleteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_with_options(request, headers, runtime)

    def delete_table_column_statistics_with_options(self, tmp_req, headers, runtime):
        """
        @summary DeleteTableColumnStatistics
        

        @param tmp_req: DeleteTableColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableColumnStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeleteTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table_column_statistics(self, request):
        """
        @summary DeleteTableColumnStatistics
        

        @param request: DeleteTableColumnStatisticsRequest

        @return: DeleteTableColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_column_statistics_with_options(request, headers, runtime)

    def delete_table_version_with_options(self, request, headers, runtime):
        """
        @summary delete table version
        

        @param request: DeleteTableVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/versions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table_version(self, request):
        """
        @summary delete table version
        

        @param request: DeleteTableVersionRequest

        @return: DeleteTableVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_version_with_options(request, headers, runtime)

    def deregister_location_with_options(self, request, headers, runtime):
        """
        @summary 取消注册Location
        

        @param request: DeregisterLocationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeregisterLocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/locations',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeregisterLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_location(self, request):
        """
        @summary 取消注册Location
        

        @param request: DeregisterLocationRequest

        @return: DeregisterLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deregister_location_with_options(request, headers, runtime)

    def describe_regions_with_options(self, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/service/describeRegions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        """

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    def get_async_task_status_with_options(self, request, headers, runtime):
        """
        @summary GetAsyncTaskStatus
        

        @param request: GetAsyncTaskStatusRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAsyncTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncTaskStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetAsyncTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_task_status(self, request):
        """
        @summary GetAsyncTaskStatus
        

        @param request: GetAsyncTaskStatusRequest

        @return: GetAsyncTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_status_with_options(request, headers, runtime)

    def get_catalog_with_options(self, request, headers, runtime):
        """
        @summary 获取Catalog
        

        @param request: GetCatalogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_catalog(self, request):
        """
        @summary 获取Catalog
        

        @param request: GetCatalogRequest

        @return: GetCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_with_options(request, headers, runtime)

    def get_catalog_settings_with_options(self, request, headers, runtime):
        """
        @summary 获取数据湖配置
        

        @param request: GetCatalogSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCatalogSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_catalog_settings(self, request):
        """
        @summary 获取数据湖配置
        

        @param request: GetCatalogSettingsRequest

        @return: GetCatalogSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_settings_with_options(request, headers, runtime)

    def get_database_with_options(self, request, headers, runtime):
        """
        @summary Get Database
        

        @param request: GetDatabaseRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_database(self, request):
        """
        @summary Get Database
        

        @param request: GetDatabaseRequest

        @return: GetDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_database_with_options(request, headers, runtime)

    def get_database_profile_with_options(self, request, headers, runtime):
        """
        @summary 获取库数据概览信息
        

        @param request: GetDatabaseProfileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDatabaseProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabaseProfile',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/metastorehouse/catalog/database/databaseprofile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetDatabaseProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_database_profile(self, request):
        """
        @summary 获取库数据概览信息
        

        @param request: GetDatabaseProfileRequest

        @return: GetDatabaseProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_database_profile_with_options(request, headers, runtime)

    def get_function_with_options(self, request, headers, runtime):
        """
        @summary Get Function
        

        @param request: GetFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function(self, request):
        """
        @summary Get Function
        

        @param request: GetFunctionRequest

        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(request, headers, runtime)

    def get_lifecycle_rule_with_options(self, request, headers, runtime):
        """
        @summary 获取生命周期规则
        

        @param request: GetLifecycleRuleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLifecycleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLifecycleRule',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/metastorehouse/lifecycle/rule/getLifecycleRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_lifecycle_rule(self, request):
        """
        @summary 获取生命周期规则
        

        @param request: GetLifecycleRuleRequest

        @return: GetLifecycleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_lifecycle_rule_with_options(request, headers, runtime)

    def get_lock_with_options(self, request, headers, runtime):
        """
        @summary get lock status
        

        @param request: GetLockRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/locks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetLockResponse(),
            self.call_api(params, req, runtime)
        )

    def get_lock(self, request):
        """
        @summary get lock status
        

        @param request: GetLockRequest

        @return: GetLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_lock_with_options(request, headers, runtime)

    def get_partition_with_options(self, request, headers, runtime):
        """
        @summary get partition
        

        @param request: GetPartitionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_partition(self, request):
        """
        @summary get partition
        

        @param request: GetPartitionRequest

        @return: GetPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_partition_with_options(request, headers, runtime)

    def get_partition_column_statistics_with_options(self, tmp_req, headers, runtime):
        """
        @summary Batch Get Partition Column Statistics
        

        @param tmp_req: GetPartitionColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPartitionColumnStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetPartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_partition_column_statistics(self, request):
        """
        @summary Batch Get Partition Column Statistics
        

        @param request: GetPartitionColumnStatisticsRequest

        @return: GetPartitionColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_partition_column_statistics_with_options(request, headers, runtime)

    def get_query_result_with_options(self, request, headers, runtime):
        """
        @summary 获取查询结果
        

        @param request: GetQueryResultRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryResult',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/query/getQueryResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_query_result(self, request):
        """
        @summary 获取查询结果
        

        @param request: GetQueryResultRequest

        @return: GetQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_query_result_with_options(request, headers, runtime)

    def get_region_status_with_options(self, request, headers, runtime):
        """

        @param request: GetRegionStatusRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRegionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/service/getRegionStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRegionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region_status(self, request):
        """

        @param request: GetRegionStatusRequest

        @return: GetRegionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_status_with_options(request, headers, runtime)

    def get_role_with_options(self, request, headers, runtime):
        """
        @summary GetRole
        

        @param request: GetRoleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role(self, request):
        """
        @summary GetRole
        

        @param request: GetRoleRequest

        @return: GetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_with_options(request, headers, runtime)

    def get_service_status_with_options(self, request, headers, runtime):
        """

        @param request: GetServiceStatusRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/service/getServiceStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_status(self, request):
        """

        @param request: GetServiceStatusRequest

        @return: GetServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_status_with_options(request, headers, runtime)

    def get_table_with_options(self, request, headers, runtime):
        """
        @summary Get table
        

        @param request: GetTableRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table(self, request):
        """
        @summary Get table
        

        @param request: GetTableRequest

        @return: GetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_with_options(request, headers, runtime)

    def get_table_column_statistics_with_options(self, tmp_req, headers, runtime):
        """
        @summary An example of API
        

        @param tmp_req: GetTableColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTableColumnStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_column_statistics(self, request):
        """
        @summary An example of API
        

        @param request: GetTableColumnStatisticsRequest

        @return: GetTableColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_column_statistics_with_options(request, headers, runtime)

    def get_table_profile_with_options(self, request, headers, runtime):
        """
        @summary 获取表数据概况信息
        

        @param request: GetTableProfileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTableProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableProfile',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/metastorehouse/catalog/database/tableprofile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_profile(self, request):
        """
        @summary 获取表数据概况信息
        

        @param request: GetTableProfileRequest

        @return: GetTableProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_profile_with_options(request, headers, runtime)

    def get_table_version_with_options(self, request, headers, runtime):
        """
        @summary Get table version
        

        @param request: GetTableVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTableVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_version(self, request):
        """
        @summary Get table version
        

        @param request: GetTableVersionRequest

        @return: GetTableVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_version_with_options(request, headers, runtime)

    def grant_permissions_with_options(self, request, headers, runtime):
        """
        @summary 赋予Principal资源的权限
        

        @param request: GrantPermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_permissions(self, request):
        """
        @summary 赋予Principal资源的权限
        

        @param request: GrantPermissionsRequest

        @return: GrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(request, headers, runtime)

    def grant_role_to_users_with_options(self, request, headers, runtime):
        """
        @summary Grant 单个角色给一个或多个用户
        

        @param request: GrantRoleToUsersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/grantusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_role_to_users(self, request):
        """
        @summary Grant 单个角色给一个或多个用户
        

        @param request: GrantRoleToUsersRequest

        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    def grant_roles_to_user_with_options(self, request, headers, runtime):
        """
        @summary Grant 一个或多个角色给一个用户
        

        @param request: GrantRolesToUserRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantRolesToUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRolesToUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/grantroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRolesToUserResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_roles_to_user(self, request):
        """
        @summary Grant 一个或多个角色给一个用户
        

        @param request: GrantRolesToUserRequest

        @return: GrantRolesToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_roles_to_user_with_options(request, headers, runtime)

    def list_catalogs_with_options(self, request, headers, runtime):
        """
        @summary ListCatalogs
        

        @param request: ListCatalogsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id_pattern):
            query['IdPattern'] = request.id_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_catalogs(self, request):
        """
        @summary ListCatalogs
        

        @param request: ListCatalogsRequest

        @return: ListCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(request, headers, runtime)

    def list_databases_with_options(self, request, headers, runtime):
        """
        @summary Get Databases List
        

        @param request: ListDatabasesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name_pattern):
            query['NamePattern'] = request.name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_databases(self, request):
        """
        @summary Get Databases List
        

        @param request: ListDatabasesRequest

        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_databases_with_options(request, headers, runtime)

    def list_function_names_with_options(self, request, headers, runtime):
        """
        @summary list function names
        

        @param request: ListFunctionNamesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFunctionNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_names(self, request):
        """
        @summary list function names
        

        @param request: ListFunctionNamesRequest

        @return: ListFunctionNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_names_with_options(request, headers, runtime)

    def list_functions_with_options(self, request, headers, runtime):
        """
        @summary list functions
        

        @param request: ListFunctionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_functions(self, request):
        """
        @summary list functions
        

        @param request: ListFunctionsRequest

        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    def list_partition_names_with_options(self, request, headers, runtime):
        """
        @summary partition names
        

        @param request: ListPartitionNamesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPartitionNamesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/names',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_partition_names(self, request):
        """
        @summary partition names
        

        @param request: ListPartitionNamesRequest

        @return: ListPartitionNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partition_names_with_options(request, headers, runtime)

    def list_partitions_with_options(self, request, headers, runtime):
        """
        @summary list partitions
        

        @param request: ListPartitionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPartitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_partitions(self, request):
        """
        @summary list partitions
        

        @param request: ListPartitionsRequest

        @return: ListPartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_with_options(request, headers, runtime)

    def list_partitions_by_expr_with_options(self, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPartitionsByExprResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPartitionsByExpr',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/listbyexpr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByExprResponse(),
            self.call_api(params, req, runtime)
        )

    def list_partitions_by_expr(self):
        """

        @return: ListPartitionsByExprResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_by_expr_with_options(headers, runtime)

    def list_partitions_by_filter_with_options(self, request, headers, runtime):
        """
        @summary list partitions by filter
        

        @param request: ListPartitionsByFilterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPartitionsByFilterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionsByFilter',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/listbyfilter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    def list_partitions_by_filter(self, request):
        """
        @summary list partitions by filter
        

        @param request: ListPartitionsByFilterRequest

        @return: ListPartitionsByFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_by_filter_with_options(request, headers, runtime)

    def list_partitions_profile_with_options(self, tmp_req, headers, runtime):
        """
        @summary 获取分区数据概况信息
        

        @param tmp_req: ListPartitionsProfileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPartitionsProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.ListPartitionsProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'simple')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPartitionsProfile',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/metastorehouse/catalog/database/tableprofile/partitionprofile/listPartitionsProfile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def list_partitions_profile(self, request):
        """
        @summary 获取分区数据概况信息
        

        @param request: ListPartitionsProfileRequest

        @return: ListPartitionsProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_profile_with_options(request, headers, runtime)

    def list_permissions_with_options(self, request, headers, runtime):
        """
        @summary 获取指定资源或指定Principal的权限信息
        

        @param request: ListPermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_list_user_role_permissions):
            body['IsListUserRolePermissions'] = request.is_list_user_role_permissions
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.meta_resource_type):
            body['MetaResourceType'] = request.meta_resource_type
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_permissions(self, request):
        """
        @summary 获取指定资源或指定Principal的权限信息
        

        @param request: ListPermissionsRequest

        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(request, headers, runtime)

    def list_role_users_with_options(self, request, headers, runtime):
        """
        @summary 查询用户角色列表
        

        @param request: ListRoleUsersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.user_name_pattern):
            query['UserNamePattern'] = request.user_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/roleusers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_role_users(self, request):
        """
        @summary 查询用户角色列表
        

        @param request: ListRoleUsersRequest

        @return: ListRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_role_users_with_options(request, headers, runtime)

    def list_roles_with_options(self, request, headers, runtime):
        """
        @summary ListRoles
        

        @param request: ListRolesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_roles(self, request):
        """
        @summary ListRoles
        

        @param request: ListRolesRequest

        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(request, headers, runtime)

    def list_table_names_with_options(self, request, headers, runtime):
        """
        @summary list table names
        

        @param request: ListTableNamesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTableNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_names(self, request):
        """
        @summary list table names
        

        @param request: ListTableNamesRequest

        @return: ListTableNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_names_with_options(request, headers, runtime)

    def list_table_versions_with_options(self, request, headers, runtime):
        """
        @summary List table versions
        

        @param request: ListTableVersionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTableVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/versions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_versions(self, request):
        """
        @summary List table versions
        

        @param request: ListTableVersionsRequest

        @return: ListTableVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_versions_with_options(request, headers, runtime)

    def list_tables_with_options(self, request, headers, runtime):
        """
        @summary list tables
        

        @param request: ListTablesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/databases/tables/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tables(self, request):
        """
        @summary list tables
        

        @param request: ListTablesRequest

        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(request, headers, runtime)

    def list_user_roles_with_options(self, request, headers, runtime):
        """
        @summary 查询用户角色列表
        

        @param request: ListUserRolesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListUserRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_arn):
            query['PrincipalArn'] = request.principal_arn
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/userroles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_roles(self, request):
        """
        @summary 查询用户角色列表
        

        @param request: ListUserRolesRequest

        @return: ListUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_roles_with_options(request, headers, runtime)

    def refresh_lock_with_options(self, request, headers, runtime):
        """
        @summary refresh to keep the lock alive
        

        @param request: RefreshLockRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefreshLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/locks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RefreshLockResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_lock(self, request):
        """
        @summary refresh to keep the lock alive
        

        @param request: RefreshLockRequest

        @return: RefreshLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_lock_with_options(request, headers, runtime)

    def register_location_with_options(self, request, headers, runtime):
        """
        @summary 注册Location
        

        @param request: RegisterLocationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterLocationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/locations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RegisterLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def register_location(self, request):
        """
        @summary 注册Location
        

        @param request: RegisterLocationRequest

        @return: RegisterLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.register_location_with_options(request, headers, runtime)

    def rename_partition_with_options(self, request, headers, runtime):
        """
        @summary rename partition
        

        @param request: RenamePartitionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenamePartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenamePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/rename',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenamePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def rename_partition(self, request):
        """
        @summary rename partition
        

        @param request: RenamePartitionRequest

        @return: RenamePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_partition_with_options(request, headers, runtime)

    def rename_table_with_options(self, request, headers, runtime):
        """
        @summary rename table
        

        @param request: RenameTableRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenameTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/rename',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenameTableResponse(),
            self.call_api(params, req, runtime)
        )

    def rename_table(self, request):
        """
        @summary rename table
        

        @param request: RenameTableRequest

        @return: RenameTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_table_with_options(request, headers, runtime)

    def revoke_permissions_with_options(self, request, headers, runtime):
        """
        @summary 取消Principal资源的权限
        

        @param request: RevokePermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokePermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_permissions(self, request):
        """
        @summary 取消Principal资源的权限
        

        @param request: RevokePermissionsRequest

        @return: RevokePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_permissions_with_options(request, headers, runtime)

    def revoke_role_from_users_with_options(self, request, headers, runtime):
        """
        @summary 批量将该角色从这些用户中revoke
        

        @param request: RevokeRoleFromUsersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeRoleFromUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRoleFromUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/revokeusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRoleFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_role_from_users(self, request):
        """
        @summary 批量将该角色从这些用户中revoke
        

        @param request: RevokeRoleFromUsersRequest

        @return: RevokeRoleFromUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_role_from_users_with_options(request, headers, runtime)

    def revoke_roles_from_user_with_options(self, request, headers, runtime):
        """
        @summary 批量Revoke该用户的角色
        

        @param request: RevokeRolesFromUserRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeRolesFromUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRolesFromUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles/revokeroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRolesFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_roles_from_user(self, request):
        """
        @summary 批量Revoke该用户的角色
        

        @param request: RevokeRolesFromUserRequest

        @return: RevokeRolesFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_roles_from_user_with_options(request, headers, runtime)

    def run_migration_workflow_with_options(self, request, headers, runtime):
        """
        @summary 运行元数据迁移任务
        

        @param request: RunMigrationWorkflowRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunMigrationWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/migration/workflow/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RunMigrationWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def run_migration_workflow(self, request):
        """
        @summary 运行元数据迁移任务
        

        @param request: RunMigrationWorkflowRequest

        @return: RunMigrationWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_migration_workflow_with_options(request, headers, runtime)

    def search_with_options(self, request, headers, runtime):
        """
        @summary DLF 元数据search
        

        @param request: SearchRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_type):
            body['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    def search(self, request):
        """
        @summary DLF 元数据search
        

        @param request: SearchRequest

        @return: SearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_with_options(request, headers, runtime)

    def search_across_catalog_with_options(self, request, headers, runtime):
        """
        @summary DLF 跨Catalog检索元数据
        

        @param request: SearchAcrossCatalogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchAcrossCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_ids):
            body['CatalogIds'] = request.catalog_ids
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_types):
            body['SearchTypes'] = request.search_types
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAcrossCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/search/search-across-catalog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchAcrossCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def search_across_catalog(self, request):
        """
        @summary DLF 跨Catalog检索元数据
        

        @param request: SearchAcrossCatalogRequest

        @return: SearchAcrossCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_across_catalog_with_options(request, headers, runtime)

    def stop_migration_workflow_with_options(self, request, headers, runtime):
        """
        @summary 停止元数据迁移任务
        

        @param request: StopMigrationWorkflowRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopMigrationWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/migration/workflow/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.StopMigrationWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_migration_workflow(self, request):
        """
        @summary 停止元数据迁移任务
        

        @param request: StopMigrationWorkflowRequest

        @return: StopMigrationWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_migration_workflow_with_options(request, headers, runtime)

    def submit_query_with_options(self, request, headers, runtime):
        """

        @param request: SubmitQueryRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['catalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.sql):
            body['sql'] = request.sql
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/query/submitQueryRequestBody',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SubmitQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_query(self, request):
        """

        @param request: SubmitQueryRequest

        @return: SubmitQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_query_with_options(request, headers, runtime)

    def un_lock_with_options(self, request, headers, runtime):
        """
        @summary unlock
        

        @param request: UnLockRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/locks',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UnLockResponse(),
            self.call_api(params, req, runtime)
        )

    def un_lock(self, request):
        """
        @summary unlock
        

        @param request: UnLockRequest

        @return: UnLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_lock_with_options(request, headers, runtime)

    def update_catalog_with_options(self, request, headers, runtime):
        """
        @summary 更新数据湖Catalog
        

        @param request: UpdateCatalogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def update_catalog(self, request):
        """
        @summary 更新数据湖Catalog
        

        @param request: UpdateCatalogRequest

        @return: UpdateCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_catalog_with_options(request, headers, runtime)

    def update_catalog_settings_with_options(self, request, headers, runtime):
        """
        @summary 获取数据湖配置
        

        @param request: UpdateCatalogSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCatalogSettingsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.catalog_settings):
            body['CatalogSettings'] = request.catalog_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/settings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_catalog_settings(self, request):
        """
        @summary 获取数据湖配置
        

        @param request: UpdateCatalogSettingsRequest

        @return: UpdateCatalogSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_catalog_settings_with_options(request, headers, runtime)

    def update_database_with_options(self, request, headers, runtime):
        """
        @summary Update database
        

        @param request: UpdateDatabaseRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDatabaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def update_database(self, request):
        """
        @summary Update database
        

        @param request: UpdateDatabaseRequest

        @return: UpdateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_database_with_options(request, headers, runtime)

    def update_function_with_options(self, request, headers, runtime):
        """
        @summary update function
        

        @param request: UpdateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/functions',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_function(self, request):
        """
        @summary update function
        

        @param request: UpdateFunctionRequest

        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_with_options(request, headers, runtime)

    def update_partition_column_statistics_with_options(self, request, headers, runtime):
        """
        @summary update partition columnstatistics
        

        @param request: UpdatePartitionColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePartitionColumnStatisticsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdatePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_partition_column_statistics(self, request):
        """
        @summary update partition columnstatistics
        

        @param request: UpdatePartitionColumnStatisticsRequest

        @return: UpdatePartitionColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_partition_column_statistics_with_options(request, headers, runtime)

    def update_permissions_with_options(self, request, headers, runtime):
        """
        @summary 赋予Principal资源的权限
        

        @param request: UpdatePermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/permissions/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_permissions(self, request):
        """
        @summary 赋予Principal资源的权限
        

        @param request: UpdatePermissionsRequest

        @return: UpdatePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_permissions_with_options(request, headers, runtime)

    def update_registered_location_with_options(self, request, headers, runtime):
        """
        @summary 修改Location
        

        @param request: UpdateRegisteredLocationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRegisteredLocationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location_id):
            body['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegisteredLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/webapi/locations',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRegisteredLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_registered_location(self, request):
        """
        @summary 修改Location
        

        @param request: UpdateRegisteredLocationRequest

        @return: UpdateRegisteredLocationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registered_location_with_options(request, headers, runtime)

    def update_role_with_options(self, request, headers, runtime):
        """
        @summary 更新角色
        

        @param request: UpdateRoleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_input):
            body['RoleInput'] = request.role_input
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/roles',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_role(self, request):
        """
        @summary 更新角色
        

        @param request: UpdateRoleRequest

        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    def update_role_users_with_options(self, request, headers, runtime):
        """
        @summary 更新Role中的Users
        

        @param request: UpdateRoleUsersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRoleUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/auth/updateroleusers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def update_role_users(self, request):
        """
        @summary 更新Role中的Users
        

        @param request: UpdateRoleUsersRequest

        @return: UpdateRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_users_with_options(request, headers, runtime)

    def update_table_with_options(self, request, headers, runtime):
        """
        @summary update table
        

        @param request: UpdateTableRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allow_partition_key_change):
            body['AllowPartitionKeyChange'] = request.allow_partition_key_change
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.skip_archive):
            body['SkipArchive'] = request.skip_archive
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table(self, request):
        """
        @summary update table
        

        @param request: UpdateTableRequest

        @return: UpdateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_with_options(request, headers, runtime)

    def update_table_column_statistics_with_options(self, request, headers, runtime):
        """
        @summary update table columnstatistics
        

        @param request: UpdateTableColumnStatisticsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableColumnStatisticsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdateTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/api/metastore/catalogs/databases/tables/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table_column_statistics(self, request):
        """
        @summary update table columnstatistics
        

        @param request: UpdateTableColumnStatisticsRequest

        @return: UpdateTableColumnStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_column_statistics_with_options(request, headers, runtime)
