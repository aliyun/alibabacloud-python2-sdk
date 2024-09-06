# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gpdb20160503 import models as gpdb_20160503_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'gpdb.aliyuncs.com',
            'cn-hangzhou': 'gpdb.aliyuncs.com',
            'cn-shanghai': 'gpdb.aliyuncs.com',
            'cn-shenzhen': 'gpdb.aliyuncs.com',
            'cn-hongkong': 'gpdb.aliyuncs.com',
            'ap-southeast-1': 'gpdb.aliyuncs.com',
            'us-west-1': 'gpdb.aliyuncs.com',
            'us-east-1': 'gpdb.aliyuncs.com',
            'cn-hangzhou-finance': 'gpdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'gpdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'gpdb.aliyuncs.com',
            'cn-qingdao': 'gpdb.aliyuncs.com',
            'cn-north-2-gov-1': 'gpdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gpdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        """
        @summary Allocates a public endpoint for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](https://help.aliyun.com/document_detail/204879.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: AllocateInstancePublicConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        """
        @summary Allocates a public endpoint for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](https://help.aliyun.com/document_detail/204879.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: AllocateInstancePublicConnectionRequest

        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def bind_dbresource_group_with_role_with_options(self, tmp_req, runtime):
        """
        @summary Binds a resource group to a database role.
        

        @param tmp_req: BindDBResourceGroupWithRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BindDBResourceGroupWithRoleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.BindDBResourceGroupWithRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_list):
            request.role_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourceGroupWithRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.BindDBResourceGroupWithRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_dbresource_group_with_role(self, request):
        """
        @summary Binds a resource group to a database role.
        

        @param request: BindDBResourceGroupWithRoleRequest

        @return: BindDBResourceGroupWithRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_dbresource_group_with_role_with_options(request, runtime)

    def cancel_upload_document_job_with_options(self, request, runtime):
        """
        @summary Cancels an asynchronous document upload job based on the job ID.
        
        @description This operation is related to the UploadDocumentAsync operation. You can call this operation to cancel a document upload job.
        >  If the canceling operation is complete, failed, or is canceled, you cannot call the operation again. The canceling operation only interrupts the document upload job. To remove the uploaded data, you must manually remove it or call the DeleteCollectionData operation. You can also call the document upload operation to overwrite the data by using the same FileName parameter.
        

        @param request: CancelUploadDocumentJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelUploadDocumentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelUploadDocumentJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CancelUploadDocumentJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_upload_document_job(self, request):
        """
        @summary Cancels an asynchronous document upload job based on the job ID.
        
        @description This operation is related to the UploadDocumentAsync operation. You can call this operation to cancel a document upload job.
        >  If the canceling operation is complete, failed, or is canceled, you cannot call the operation again. The canceling operation only interrupts the document upload job. To remove the uploaded data, you must manually remove it or call the DeleteCollectionData operation. You can also call the document upload operation to overwrite the data by using the same FileName parameter.
        

        @param request: CancelUploadDocumentJobRequest

        @return: CancelUploadDocumentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_upload_document_job_with_options(request, runtime)

    def cancel_upsert_collection_data_job_with_options(self, request, runtime):
        """
        @summary Cancels an asynchronous vector data upload job by using a job ID.
        
        @description This operation is related to the `UpsertCollectionDataAsync` operation. You can call this operation to cancel an upload job.
        >  If the canceling operation is complete, failed, or is canceled, you cannot call the operation again. The canceling operation only interrupts the upload job. To remove the uploaded data, you must manually remove it or call the DeleteCollectionData operation.
        

        @param request: CancelUpsertCollectionDataJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelUpsertCollectionDataJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelUpsertCollectionDataJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CancelUpsertCollectionDataJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_upsert_collection_data_job(self, request):
        """
        @summary Cancels an asynchronous vector data upload job by using a job ID.
        
        @description This operation is related to the `UpsertCollectionDataAsync` operation. You can call this operation to cancel an upload job.
        >  If the canceling operation is complete, failed, or is canceled, you cannot call the operation again. The canceling operation only interrupts the upload job. To remove the uploaded data, you must manually remove it or call the DeleteCollectionData operation.
        

        @param request: CancelUpsertCollectionDataJobRequest

        @return: CancelUpsertCollectionDataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_upsert_collection_data_job_with_options(request, runtime)

    def check_hadoop_data_source_with_options(self, request, runtime):
        """
        @summary Checks the configurations of a Hadoop data source.
        

        @param request: CheckHadoopDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckHadoopDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_dir):
            query['CheckDir'] = request.check_dir
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckHadoopDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_hadoop_data_source(self, request):
        """
        @summary Checks the configurations of a Hadoop data source.
        

        @param request: CheckHadoopDataSourceRequest

        @return: CheckHadoopDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_hadoop_data_source_with_options(request, runtime)

    def check_hadoop_net_connection_with_options(self, request, runtime):
        """
        @summary 检查hadoop集群网络连通性
        

        @param request: CheckHadoopNetConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckHadoopNetConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckHadoopNetConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckHadoopNetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def check_hadoop_net_connection(self, request):
        """
        @summary 检查hadoop集群网络连通性
        

        @param request: CheckHadoopNetConnectionRequest

        @return: CheckHadoopNetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_hadoop_net_connection_with_options(request, runtime)

    def check_jdbcsource_net_connection_with_options(self, request, runtime):
        """
        @summary Checks the network connectivity of a connection specified by a Java Database Connectivity (JDBC) connection string.
        

        @param request: CheckJDBCSourceNetConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckJDBCSourceNetConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.jdbc_connection_string):
            query['JdbcConnectionString'] = request.jdbc_connection_string
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckJDBCSourceNetConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckJDBCSourceNetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def check_jdbcsource_net_connection(self, request):
        """
        @summary Checks the network connectivity of a connection specified by a Java Database Connectivity (JDBC) connection string.
        

        @param request: CheckJDBCSourceNetConnectionRequest

        @return: CheckJDBCSourceNetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_jdbcsource_net_connection_with_options(request, runtime)

    def check_service_linked_role_with_options(self, request, runtime):
        """
        @summary Queries whether a service-linked role is created.
        

        @param request: CheckServiceLinkedRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_linked_role(self, request):
        """
        @summary Queries whether a service-linked role is created.
        

        @param request: CheckServiceLinkedRoleRequest

        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        """
        @summary Creates an initial account for an AnalyticDB for PostgreSQL instance.
        
        @description    Before you can use an AnalyticDB for PostgreSQL instance, you must create an initial account for the instance.
        You can call this operation to create only initial accounts. For information about how to create other types of accounts, see [Create a database account](https://help.aliyun.com/document_detail/50206.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        """
        @summary Creates an initial account for an AnalyticDB for PostgreSQL instance.
        
        @description    Before you can use an AnalyticDB for PostgreSQL instance, you must create an initial account for the instance.
        You can call this operation to create only initial accounts. For information about how to create other types of accounts, see [Create a database account](https://help.aliyun.com/document_detail/50206.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateAccountRequest

        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_collection_with_options(self, request, runtime):
        """
        @summary Creates a vector collection.
        

        @param request: CreateCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_collection(self, request):
        """
        @summary Creates a vector collection.
        

        @param request: CreateCollectionRequest

        @return: CreateCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_collection_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        """
        @summary Creates an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        

        @param request: CreateDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_sample_data):
            query['CreateSampleData'] = request.create_sample_data
        if not UtilClient.is_unset(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.serverless_mode):
            query['ServerlessMode'] = request.serverless_mode
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not UtilClient.is_unset(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance(self, request):
        """
        @summary Creates an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        

        @param request: CreateDBInstanceRequest

        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_dbinstance_plan_with_options(self, request, runtime):
        """
        @summary Creates a plan for an AnalyticDB for PostgreSQL instance.
        
        @description    The plan management feature is supported only for pay-as-you-go instances.
        When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: CreateDBInstancePlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance_plan(self, request):
        """
        @summary Creates a plan for an AnalyticDB for PostgreSQL instance.
        
        @description    The plan management feature is supported only for pay-as-you-go instances.
        When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: CreateDBInstancePlanRequest

        @return: CreateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_plan_with_options(request, runtime)

    def create_dbresource_group_with_options(self, request, runtime):
        """
        @summary Creates a resource group.
        

        @param request: CreateDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_config):
            query['ResourceGroupConfig'] = request.resource_group_config
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbresource_group(self, request):
        """
        @summary Creates a resource group.
        

        @param request: CreateDBResourceGroupRequest

        @return: CreateDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    def create_document_collection_with_options(self, request, runtime):
        """
        @summary Creates a document collection.
        

        @param request: CreateDocumentCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDocumentCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not UtilClient.is_unset(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_document_collection(self, request):
        """
        @summary Creates a document collection.
        

        @param request: CreateDocumentCollectionRequest

        @return: CreateDocumentCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_document_collection_with_options(request, runtime)

    def create_extensions_with_options(self, request, runtime):
        """
        @summary Install extensions.
        

        @param request: CreateExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnames):
            query['DBNames'] = request.dbnames
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExtensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_extensions(self, request):
        """
        @summary Install extensions.
        

        @param request: CreateExtensionsRequest

        @return: CreateExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_extensions_with_options(request, runtime)

    def create_external_data_service_with_options(self, request, runtime):
        """
        @summary Creates an external data service.
        

        @param request: CreateExternalDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateExternalDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExternalDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_external_data_service(self, request):
        """
        @summary Creates an external data service.
        

        @param request: CreateExternalDataServiceRequest

        @return: CreateExternalDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_external_data_service_with_options(request, runtime)

    def create_hadoop_data_source_with_options(self, request, runtime):
        """
        @summary Creates the configurations for a Hadoop data source.
        

        @param request: CreateHadoopDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHadoopDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not UtilClient.is_unset(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not UtilClient.is_unset(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not UtilClient.is_unset(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not UtilClient.is_unset(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not UtilClient.is_unset(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not UtilClient.is_unset(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHadoopDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hadoop_data_source(self, request):
        """
        @summary Creates the configurations for a Hadoop data source.
        

        @param request: CreateHadoopDataSourceRequest

        @return: CreateHadoopDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hadoop_data_source_with_options(request, runtime)

    def create_jdbcdata_source_with_options(self, request, runtime):
        """
        @summary Creates a Java Database Connectivity (JDBC) data source.
        

        @param request: CreateJDBCDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateJDBCDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not UtilClient.is_unset(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not UtilClient.is_unset(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJDBCDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_jdbcdata_source(self, request):
        """
        @summary Creates a Java Database Connectivity (JDBC) data source.
        

        @param request: CreateJDBCDataSourceRequest

        @return: CreateJDBCDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_jdbcdata_source_with_options(request, runtime)

    def create_namespace_with_options(self, request, runtime):
        """
        @summary Creates a vector namespace.
        

        @param request: CreateNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_namespace(self, request):
        """
        @summary Creates a vector namespace.
        

        @param request: CreateNamespaceRequest

        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    def create_sample_data_with_options(self, request, runtime):
        """
        @summary Creates a sample dataset for an AnalyticDB for PostgreSQL instance.
        
        @description    You can call this operation to create a sample dataset for an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to use or test your instance. For more information about query statements, see [Dataset information and query examples](https://help.aliyun.com/document_detail/452277.html).
        This operation is supported only for AnalyticDB for PostgreSQL V6.3.8.8 and V6.3.10.3 or later, excluding the versions from V6.3.9.0 to V6.3.10.2.
        

        @param request: CreateSampleDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sample_data(self, request):
        """
        @summary Creates a sample dataset for an AnalyticDB for PostgreSQL instance.
        
        @description    You can call this operation to create a sample dataset for an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to use or test your instance. For more information about query statements, see [Dataset information and query examples](https://help.aliyun.com/document_detail/452277.html).
        This operation is supported only for AnalyticDB for PostgreSQL V6.3.8.8 and V6.3.10.3 or later, excluding the versions from V6.3.9.0 to V6.3.10.2.
        

        @param request: CreateSampleDataRequest

        @return: CreateSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    def create_secret_with_options(self, request, runtime):
        """
        @summary Creates an access credential for an AnalyticDB for PostgreSQL instance by using the name and password of a database account.
        

        @param request: CreateSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.test_connection):
            query['TestConnection'] = request.test_connection
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def create_secret(self, request):
        """
        @summary Creates an access credential for an AnalyticDB for PostgreSQL instance by using the name and password of a database account.
        

        @param request: CreateSecretRequest

        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        """
        @summary Creates a service-linked role.
        

        @param request: CreateServiceLinkedRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        """
        @summary Creates a service-linked role.
        

        @param request: CreateServiceLinkedRoleRequest

        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def create_streaming_data_service_with_options(self, request, runtime):
        """
        @summary Creates a real-time data service.
        

        @param request: CreateStreamingDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateStreamingDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamingDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_streaming_data_service(self, request):
        """
        @summary Creates a real-time data service.
        

        @param request: CreateStreamingDataServiceRequest

        @return: CreateStreamingDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_streaming_data_service_with_options(request, runtime)

    def create_streaming_data_source_with_options(self, request, runtime):
        """
        @summary Creates a real-time data source.
        

        @param request: CreateStreamingDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateStreamingDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamingDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_streaming_data_source(self, request):
        """
        @summary Creates a real-time data source.
        

        @param request: CreateStreamingDataSourceRequest

        @return: CreateStreamingDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_streaming_data_source_with_options(request, runtime)

    def create_streaming_job_with_options(self, tmp_req, runtime):
        """
        @summary Creates the configurations for an external data source.
        

        @param tmp_req: CreateStreamingJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateStreamingJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.CreateStreamingJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_columns):
            request.dest_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not UtilClient.is_unset(tmp_req.match_columns):
            request.match_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not UtilClient.is_unset(tmp_req.src_columns):
            request.src_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not UtilClient.is_unset(tmp_req.update_columns):
            request.update_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.consistency):
            query['Consistency'] = request.consistency
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not UtilClient.is_unset(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not UtilClient.is_unset(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not UtilClient.is_unset(request.dest_table):
            query['DestTable'] = request.dest_table
        if not UtilClient.is_unset(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not UtilClient.is_unset(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.job_config):
            query['JobConfig'] = request.job_config
        if not UtilClient.is_unset(request.job_description):
            query['JobDescription'] = request.job_description
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not UtilClient.is_unset(request.try_run):
            query['TryRun'] = request.try_run
        if not UtilClient.is_unset(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not UtilClient.is_unset(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamingJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_streaming_job(self, request):
        """
        @summary Creates the configurations for an external data source.
        

        @param request: CreateStreamingJobRequest

        @return: CreateStreamingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_streaming_job_with_options(request, runtime)

    def create_vector_index_with_options(self, request, runtime):
        """
        @summary Creates a vector index.
        

        @param request: CreateVectorIndexRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVectorIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.external_storage):
            query['ExternalStorage'] = request.external_storage
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vector_index(self, request):
        """
        @summary Creates a vector index.
        

        @param request: CreateVectorIndexRequest

        @return: CreateVectorIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vector_index_with_options(request, runtime)

    def delete_collection_with_options(self, request, runtime):
        """
        @summary Deletes a vector collection.
        

        @param request: DeleteCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_collection(self, request):
        """
        @summary Deletes a vector collection.
        

        @param request: DeleteCollectionRequest

        @return: DeleteCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_collection_with_options(request, runtime)

    def delete_collection_data_with_options(self, request, runtime):
        """
        @summary Deletes vector data.
        

        @param request: DeleteCollectionDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCollectionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.collection_data):
            query['CollectionData'] = request.collection_data
        if not UtilClient.is_unset(request.collection_data_filter):
            query['CollectionDataFilter'] = request.collection_data_filter
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_collection_data(self, request):
        """
        @summary Deletes vector data.
        

        @param request: DeleteCollectionDataRequest

        @return: DeleteCollectionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_collection_data_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        """
        @summary Releases a pay-as-you-go AnalyticDB for PostgreSQL instance.
        
        @description    Subscription instances cannot be manually released. They are automatically released when they expire.
        You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance(self, request):
        """
        @summary Releases a pay-as-you-go AnalyticDB for PostgreSQL instance.
        
        @description    Subscription instances cannot be manually released. They are automatically released when they expire.
        You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDBInstanceRequest

        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_dbinstance_plan_with_options(self, request, runtime):
        """
        @summary Deletes a plan from an AnalyticDB for PostgreSQL instance.
        
        @description If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDBInstancePlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance_plan(self, request):
        """
        @summary Deletes a plan from an AnalyticDB for PostgreSQL instance.
        
        @description If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDBInstancePlanRequest

        @return: DeleteDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_plan_with_options(request, runtime)

    def delete_dbresource_group_with_options(self, request, runtime):
        """
        @summary Deletes a resource group.
        

        @param request: DeleteDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbresource_group(self, request):
        """
        @summary Deletes a resource group.
        

        @param request: DeleteDBResourceGroupRequest

        @return: DeleteDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    def delete_document_with_options(self, request, runtime):
        """
        @summary Deletes a document from a document collection.
        

        @param request: DeleteDocumentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_document(self, request):
        """
        @summary Deletes a document from a document collection.
        

        @param request: DeleteDocumentRequest

        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    def delete_document_collection_with_options(self, request, runtime):
        """
        @summary Deletes a document collection.
        

        @param request: DeleteDocumentCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDocumentCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_document_collection(self, request):
        """
        @summary Deletes a document collection.
        

        @param request: DeleteDocumentCollectionRequest

        @return: DeleteDocumentCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_document_collection_with_options(request, runtime)

    def delete_extension_with_options(self, request, runtime):
        """
        @summary Uninstall an extension.
        

        @param request: DeleteExtensionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteExtensionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnames):
            query['DBNames'] = request.dbnames
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExtension',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_extension(self, request):
        """
        @summary Uninstall an extension.
        

        @param request: DeleteExtensionRequest

        @return: DeleteExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_extension_with_options(request, runtime)

    def delete_external_data_service_with_options(self, request, runtime):
        """
        @summary Deletes an external data service.
        

        @param request: DeleteExternalDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteExternalDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExternalDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_external_data_service(self, request):
        """
        @summary Deletes an external data service.
        

        @param request: DeleteExternalDataServiceRequest

        @return: DeleteExternalDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_external_data_service_with_options(request, runtime)

    def delete_hadoop_data_source_with_options(self, request, runtime):
        """
        @summary 删除hadoop数据源
        

        @param request: DeleteHadoopDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteHadoopDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHadoopDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hadoop_data_source(self, request):
        """
        @summary 删除hadoop数据源
        

        @param request: DeleteHadoopDataSourceRequest

        @return: DeleteHadoopDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hadoop_data_source_with_options(request, runtime)

    def delete_jdbcdata_source_with_options(self, request, runtime):
        """
        @summary Deletes a Java Database Connectivity (JDBC) data source.
        

        @param request: DeleteJDBCDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteJDBCDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJDBCDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_jdbcdata_source(self, request):
        """
        @summary Deletes a Java Database Connectivity (JDBC) data source.
        

        @param request: DeleteJDBCDataSourceRequest

        @return: DeleteJDBCDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_jdbcdata_source_with_options(request, runtime)

    def delete_namespace_with_options(self, request, runtime):
        """
        @summary Deletes a namespace.
        

        @param request: DeleteNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_namespace(self, request):
        """
        @summary Deletes a namespace.
        

        @param request: DeleteNamespaceRequest

        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    def delete_secret_with_options(self, request, runtime):
        """
        @summary Deletes the access credentials of an AnalyticDB for PostgreSQL instance.
        

        @param request: DeleteSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_secret(self, request):
        """
        @summary Deletes the access credentials of an AnalyticDB for PostgreSQL instance.
        

        @param request: DeleteSecretRequest

        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    def delete_streaming_data_service_with_options(self, request, runtime):
        """
        @summary Deletes a real-time data service.
        

        @param request: DeleteStreamingDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteStreamingDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamingDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_streaming_data_service(self, request):
        """
        @summary Deletes a real-time data service.
        

        @param request: DeleteStreamingDataServiceRequest

        @return: DeleteStreamingDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_streaming_data_service_with_options(request, runtime)

    def delete_streaming_data_source_with_options(self, request, runtime):
        """
        @summary Deletes a real-time data source.
        

        @param request: DeleteStreamingDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteStreamingDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamingDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_streaming_data_source(self, request):
        """
        @summary Deletes a real-time data source.
        

        @param request: DeleteStreamingDataSourceRequest

        @return: DeleteStreamingDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_streaming_data_source_with_options(request, runtime)

    def delete_streaming_job_with_options(self, request, runtime):
        """
        @summary Deletes a real-time data service job.
        

        @param request: DeleteStreamingJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteStreamingJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamingJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_streaming_job(self, request):
        """
        @summary Deletes a real-time data service job.
        

        @param request: DeleteStreamingJobRequest

        @return: DeleteStreamingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_streaming_job_with_options(request, runtime)

    def delete_vector_index_with_options(self, request, runtime):
        """
        @summary Deletes a vector index.
        

        @param request: DeleteVectorIndexRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVectorIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vector_index(self, request):
        """
        @summary Deletes a vector index.
        

        @param request: DeleteVectorIndexRequest

        @return: DeleteVectorIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vector_index_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        """
        @summary Queries the information about database accounts for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeAccountsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accounts(self, request):
        """
        @summary Queries the information about database accounts for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeAccountsRequest

        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_active_sqlrecords_with_options(self, request, runtime):
        """
        @summary Queries active SQL records.
        

        @param request: DescribeActiveSQLRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeActiveSQLRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveSQLRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeActiveSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_active_sqlrecords(self, request):
        """
        @summary Queries active SQL records.
        

        @param request: DescribeActiveSQLRecordsRequest

        @return: DescribeActiveSQLRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_sqlrecords_with_options(request, runtime)

    def describe_available_resources_with_options(self, request, runtime):
        """
        @summary Queries the information about available resources of AnalyticDB for PostgreSQL.
        
        @description When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        

        @param request: DescribeAvailableResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAvailableResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resources(self, request):
        """
        @summary Queries the information about available resources of AnalyticDB for PostgreSQL.
        
        @description When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        

        @param request: DescribeAvailableResourcesRequest

        @return: DescribeAvailableResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resources_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        """
        @summary Queries the backup policy of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](https://help.aliyun.com/document_detail/210095.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        """
        @summary Queries the backup policy of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](https://help.aliyun.com/document_detail/210095.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeBackupPolicyRequest

        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_collection_with_options(self, request, runtime):
        """
        @summary Queries the information about a vector collection.
        

        @param request: DescribeCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_collection(self, request):
        """
        @summary Queries the information about a vector collection.
        

        @param request: DescribeCollectionRequest

        @return: DescribeCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_collection_with_options(request, runtime)

    def describe_dbcluster_node_with_options(self, request, runtime):
        """
        @summary Queries a list of nodes in an AnalyticDB for PostgreSQL instance.
        
        @description ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBClusterNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBClusterNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNode',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_node(self, request):
        """
        @summary Queries a list of nodes in an AnalyticDB for PostgreSQL instance.
        
        @description ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBClusterNodeRequest

        @return: DescribeDBClusterNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_node_with_options(request, runtime)

    def describe_dbcluster_performance_with_options(self, request, runtime):
        """
        @summary Queries the information about performance metrics of an AnalyticDB for PostgreSQL instance within a time range.
        
        @description You can query monitoring information only within the last 30 days.
        

        @param request: DescribeDBClusterPerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbcluster_performance(self, request):
        """
        @summary Queries the information about performance metrics of an AnalyticDB for PostgreSQL instance within a time range.
        
        @description You can query monitoring information only within the last 30 days.
        

        @param request: DescribeDBClusterPerformanceRequest

        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        """
        @summary Queries the information about an AnalyticDB for PostgreSQL instance.
        
        @description ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        """
        @summary Queries the information about an AnalyticDB for PostgreSQL instance.
        
        @description ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceAttributeRequest

        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_data_bloat_with_options(self, request, runtime):
        """
        @summary Queries the information about data bloat for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceDataBloatRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceDataBloatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataBloat',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataBloatResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_data_bloat(self, request):
        """
        @summary Queries the information about data bloat for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceDataBloatRequest

        @return: DescribeDBInstanceDataBloatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_bloat_with_options(request, runtime)

    def describe_dbinstance_data_skew_with_options(self, request, runtime):
        """
        @summary Queries the information about data skew for an AnalyticDB for PostgreSQL instance.
        
        @description To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceDataSkewRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceDataSkewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSkew',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataSkewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_data_skew(self, request):
        """
        @summary Queries the information about data skew for an AnalyticDB for PostgreSQL instance.
        
        @description To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceDataSkewRequest

        @return: DescribeDBInstanceDataSkewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_skew_with_options(request, runtime)

    def describe_dbinstance_diagnosis_summary_with_options(self, request, runtime):
        """
        @summary Queries the information about nodes in an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceDiagnosisSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_preferd):
            query['RolePreferd'] = request.role_preferd
        if not UtilClient.is_unset(request.start_status):
            query['StartStatus'] = request.start_status
        if not UtilClient.is_unset(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDiagnosisSummary',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_diagnosis_summary(self, request):
        """
        @summary Queries the information about nodes in an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceDiagnosisSummaryRequest

        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_diagnosis_summary_with_options(request, runtime)

    def describe_dbinstance_error_log_with_options(self, request, runtime):
        """
        @summary Queries the error logs of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceErrorLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceErrorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceErrorLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceErrorLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_error_log(self, request):
        """
        @summary Queries the error logs of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceErrorLogRequest

        @return: DescribeDBInstanceErrorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_error_log_with_options(request, runtime)

    def describe_dbinstance_iparray_list_with_options(self, request, runtime):
        """
        @summary Queries the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceIPArrayListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceIPArrayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(self, request):
        """
        @summary Queries the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstanceIPArrayListRequest

        @return: DescribeDBInstanceIPArrayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    def describe_dbinstance_index_usage_with_options(self, request, runtime):
        """
        @summary Queries the index usage of an AnalyticDB for PostgreSQL instance.
        
        @description Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDBInstanceIndexUsageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceIndexUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIndexUsage',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_index_usage(self, request):
        """
        @summary Queries the index usage of an AnalyticDB for PostgreSQL instance.
        
        @description Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDBInstanceIndexUsageRequest

        @return: DescribeDBInstanceIndexUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_index_usage_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        """
        @summary Queries the connection information of an instance.
        

        @param request: DescribeDBInstanceNetInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_net_info(self, request):
        """
        @summary Queries the connection information of an instance.
        

        @param request: DescribeDBInstanceNetInfoRequest

        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        """
        @summary Queries the information about performance metrics of an AnalyticDB for PostgreSQL instance within a time range.
        

        @param request: DescribeDBInstancePerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_performance(self, request):
        """
        @summary Queries the information about performance metrics of an AnalyticDB for PostgreSQL instance within a time range.
        

        @param request: DescribeDBInstancePerformanceRequest

        @return: DescribeDBInstancePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_dbinstance_plans_with_options(self, request, runtime):
        """
        @summary Queries the information about plans for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstancePlansRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancePlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_create_date):
            query['PlanCreateDate'] = request.plan_create_date
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePlans',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_plans(self, request):
        """
        @summary Queries the information about plans for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstancePlansRequest

        @return: DescribeDBInstancePlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_plans_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        """
        @summary Queries the SSL information about an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceSSLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_ssl(self, request):
        """
        @summary Queries the SSL information about an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceSSLRequest

        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_dbinstance_support_max_performance_with_options(self, request, runtime):
        """
        @summary Queries the maximum performance of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceSupportMaxPerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceSupportMaxPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSupportMaxPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_support_max_performance(self, request):
        """
        @summary Queries the maximum performance of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBInstanceSupportMaxPerformanceRequest

        @return: DescribeDBInstanceSupportMaxPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_support_max_performance_with_options(request, runtime)

    def describe_dbinstances_with_options(self, tmp_req, runtime):
        """
        @summary Queries a list of AnalyticDB for PostgreSQL instances.
        
        @description ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param tmp_req: DescribeDBInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.DescribeDBInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_categories):
            request.dbinstance_categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_categories, 'DBInstanceCategories', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_modes):
            request.dbinstance_modes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_modes, 'DBInstanceModes', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_statuses):
            request.dbinstance_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_statuses, 'DBInstanceStatuses', 'simple')
        if not UtilClient.is_unset(tmp_req.instance_deploy_types):
            request.instance_deploy_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_deploy_types, 'InstanceDeployTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_categories_shrink):
            query['DBInstanceCategories'] = request.dbinstance_categories_shrink
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_modes_shrink):
            query['DBInstanceModes'] = request.dbinstance_modes_shrink
        if not UtilClient.is_unset(request.dbinstance_statuses_shrink):
            query['DBInstanceStatuses'] = request.dbinstance_statuses_shrink
        if not UtilClient.is_unset(request.instance_deploy_types_shrink):
            query['InstanceDeployTypes'] = request.instance_deploy_types_shrink
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances(self, request):
        """
        @summary Queries a list of AnalyticDB for PostgreSQL instances.
        
        @description ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDBInstancesRequest

        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbresource_group_with_options(self, request, runtime):
        """
        @summary Queries the information about resource groups.
        

        @param request: DescribeDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbresource_group(self, request):
        """
        @summary Queries the information about resource groups.
        

        @param request: DescribeDBResourceGroupRequest

        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    def describe_dbresource_management_mode_with_options(self, request, runtime):
        """
        @summary Queries the resource management mode of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBResourceManagementModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBResourceManagementModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceManagementMode',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBResourceManagementModeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbresource_management_mode(self, request):
        """
        @summary Queries the resource management mode of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDBResourceManagementModeRequest

        @return: DescribeDBResourceManagementModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_management_mode_with_options(request, runtime)

    def describe_dbversion_infos_with_options(self, request, runtime):
        """
        @summary Queries the information about minor versions of AnalyticDB for PostgreSQL instances.
        

        @param request: DescribeDBVersionInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBVersionInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBVersionInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBVersionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbversion_infos(self, request):
        """
        @summary Queries the information about minor versions of AnalyticDB for PostgreSQL instances.
        

        @param request: DescribeDBVersionInfosRequest

        @return: DescribeDBVersionInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbversion_infos_with_options(request, runtime)

    def describe_data_backups_with_options(self, request, runtime):
        """
        @summary Queries a list of backup sets of full backup or point-in-time backup for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        

        @param request: DescribeDataBackupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_backups(self, request):
        """
        @summary Queries a list of backup sets of full backup or point-in-time backup for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        

        @param request: DescribeDataBackupsRequest

        @return: DescribeDataBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backups_with_options(request, runtime)

    def describe_data_re_distribute_info_with_options(self, request, runtime):
        """
        @summary Queries the data redistribution information about an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        

        @param request: DescribeDataReDistributeInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataReDistributeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataReDistributeInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataReDistributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_re_distribute_info(self, request):
        """
        @summary Queries the data redistribution information about an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        

        @param request: DescribeDataReDistributeInfoRequest

        @return: DescribeDataReDistributeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_re_distribute_info_with_options(request, runtime)

    def describe_data_share_instances_with_options(self, request, runtime):
        """
        @summary Queries the state of data sharing for AnalyticDB for PostgreSQL instances.
        
        @description Data sharing is supported only for instances in Serverless mode.
        

        @param request: DescribeDataShareInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataShareInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataShareInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataShareInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_share_instances(self, request):
        """
        @summary Queries the state of data sharing for AnalyticDB for PostgreSQL instances.
        
        @description Data sharing is supported only for instances in Serverless mode.
        

        @param request: DescribeDataShareInstancesRequest

        @return: DescribeDataShareInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_instances_with_options(request, runtime)

    def describe_data_share_performance_with_options(self, request, runtime):
        """
        @summary Queries the information about data sharing performance metrics.
        
        @description You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataSharePerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataSharePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSharePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataSharePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_share_performance(self, request):
        """
        @summary Queries the information about data sharing performance metrics.
        
        @description You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataSharePerformanceRequest

        @return: DescribeDataSharePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_performance_with_options(request, runtime)

    def describe_diagnosis_dimensions_with_options(self, request, runtime):
        """
        @summary Queries all databases and database accounts for an AnalyticDB for PostgreSQL instance.
        
        @description To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisDimensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosisDimensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnosis_dimensions(self, request):
        """
        @summary Queries all databases and database accounts for an AnalyticDB for PostgreSQL instance.
        
        @description To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisDimensionsRequest

        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(self, request, runtime):
        """
        @summary Queries the details of query execution on an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisMonitorPerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisMonitorPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnosis_monitor_performance(self, request):
        """
        @summary Queries the details of query execution on an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisMonitorPerformanceRequest

        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    def describe_diagnosis_records_with_options(self, request, runtime):
        """
        @summary Queries the information about SQL queries for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnosis_records(self, request):
        """
        @summary Queries the information about SQL queries for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDiagnosisRecordsRequest

        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(self, request, runtime):
        """
        @summary Queries the information about a query for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDiagnosisSQLInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosisSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.query_id):
            query['QueryID'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(self, request):
        """
        @summary Queries the information about a query for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDiagnosisSQLInfoRequest

        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    def describe_document_with_options(self, request, runtime):
        """
        @summary Queries the information about a document.
        

        @param request: DescribeDocumentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_document(self, request):
        """
        @summary Queries the information about a document.
        

        @param request: DescribeDocumentRequest

        @return: DescribeDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_document_with_options(request, runtime)

    def describe_download_records_with_options(self, request, runtime):
        """
        @summary Queries the download records of query diagnostic information for an AnalyticDB for PostgreSQL instance.
        
        @description You must call the [DownloadDiagnosisRecords](https://help.aliyun.com/document_detail/447700.html) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDownloadRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_records(self, request):
        """
        @summary Queries the download records of query diagnostic information for an AnalyticDB for PostgreSQL instance.
        
        @description You must call the [DownloadDiagnosisRecords](https://help.aliyun.com/document_detail/447700.html) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        

        @param request: DescribeDownloadRecordsRequest

        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    def describe_download_sqllogs_with_options(self, request, runtime):
        """
        @summary Queries the last five download records of slow query logs for an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDownloadSQLLogsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadSQLLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_sqllogs(self, request):
        """
        @summary Queries the last five download records of slow query logs for an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeDownloadSQLLogsRequest

        @return: DescribeDownloadSQLLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_sqllogs_with_options(request, runtime)

    def describe_external_data_service_with_options(self, request, runtime):
        """
        @summary Queries the information about an external data service.
        

        @param request: DescribeExternalDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExternalDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExternalDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_external_data_service(self, request):
        """
        @summary Queries the information about an external data service.
        

        @param request: DescribeExternalDataServiceRequest

        @return: DescribeExternalDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_external_data_service_with_options(request, runtime)

    def describe_hadoop_clusters_in_same_net_with_options(self, request, runtime):
        """
        @summary Queries E-MapReduce (EMR) Hadoop clusters in a specific virtual private cloud (VPC).
        

        @param request: DescribeHadoopClustersInSameNetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHadoopClustersInSameNetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHadoopClustersInSameNet',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHadoopClustersInSameNetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hadoop_clusters_in_same_net(self, request):
        """
        @summary Queries E-MapReduce (EMR) Hadoop clusters in a specific virtual private cloud (VPC).
        

        @param request: DescribeHadoopClustersInSameNetRequest

        @return: DescribeHadoopClustersInSameNetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hadoop_clusters_in_same_net_with_options(request, runtime)

    def describe_hadoop_configs_with_options(self, request, runtime):
        """
        @summary 获取hadoop配置信息
        

        @param request: DescribeHadoopConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHadoopConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHadoopConfigs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHadoopConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hadoop_configs(self, request):
        """
        @summary 获取hadoop配置信息
        

        @param request: DescribeHadoopConfigsRequest

        @return: DescribeHadoopConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hadoop_configs_with_options(request, runtime)

    def describe_hadoop_data_source_with_options(self, request, runtime):
        """
        @summary Obtains the configurations of a Hadoop data source.
        

        @param request: DescribeHadoopDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHadoopDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHadoopDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hadoop_data_source(self, request):
        """
        @summary Obtains the configurations of a Hadoop data source.
        

        @param request: DescribeHadoopDataSourceRequest

        @return: DescribeHadoopDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hadoop_data_source_with_options(request, runtime)

    def describe_health_status_with_options(self, request, runtime):
        """
        @summary Queries the health status of an AnalyticDB for PostgreSQL instance and its nodes.
        
        @description This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeHealthStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_health_status(self, request):
        """
        @summary Queries the health status of an AnalyticDB for PostgreSQL instance and its nodes.
        
        @description This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeHealthStatusRequest

        @return: DescribeHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    def describe_imvinfos_with_options(self, request, runtime):
        """
        @summary Queries the information about real-time materialized views of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeIMVInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeIMVInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.mvname):
            query['MVName'] = request.mvname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMVInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeIMVInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_imvinfos(self, request):
        """
        @summary Queries the information about real-time materialized views of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeIMVInfosRequest

        @return: DescribeIMVInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_imvinfos_with_options(request, runtime)

    def describe_jdbcdata_source_with_options(self, request, runtime):
        """
        @summary Queries the configurations of a Java Database Connectivity (JDBC) data source.
        

        @param request: DescribeJDBCDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeJDBCDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJDBCDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_jdbcdata_source(self, request):
        """
        @summary Queries the configurations of a Java Database Connectivity (JDBC) data source.
        

        @param request: DescribeJDBCDataSourceRequest

        @return: DescribeJDBCDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_jdbcdata_source_with_options(request, runtime)

    def describe_log_backups_with_options(self, request, runtime):
        """
        @summary Queries a list of log backups.
        

        @param request: DescribeLogBackupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLogBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeLogBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_backups(self, request):
        """
        @summary Queries a list of log backups.
        

        @param request: DescribeLogBackupsRequest

        @return: DescribeLogBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backups_with_options(request, runtime)

    def describe_modify_parameter_log_with_options(self, request, runtime):
        """
        @summary Queries the parameter modification logs of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeModifyParameterLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeModifyParameterLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_modify_parameter_log(self, request):
        """
        @summary Queries the parameter modification logs of an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeModifyParameterLogRequest

        @return: DescribeModifyParameterLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    def describe_namespace_with_options(self, request, runtime):
        """
        @summary Queries the information about a namespace.
        

        @param request: DescribeNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_namespace(self, request):
        """
        @summary Queries the information about a namespace.
        

        @param request: DescribeNamespaceRequest

        @return: DescribeNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_namespace_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        """
        @summary Queries the information about configuration parameters for an AnalyticDB for PostgreSQL instance.
        
        @description This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeParametersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters(self, request):
        """
        @summary Queries the information about configuration parameters for an AnalyticDB for PostgreSQL instance.
        
        @description This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeParametersRequest

        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_rds_vswitchs_with_options(self, request, runtime):
        """
        @summary Queries a list of vSwitches.
        
        @description When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRdsVSwitchsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRdsVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVSwitchs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_vswitchs(self, request):
        """
        @summary Queries a list of vSwitches.
        
        @description When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRdsVSwitchsRequest

        @return: DescribeRdsVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    def describe_rds_vpcs_with_options(self, request, runtime):
        """
        @summary Queries a list of VPCs.
        
        @description When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRdsVpcsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRdsVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_vpcs(self, request):
        """
        @summary Queries a list of VPCs.
        
        @description When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRdsVpcsRequest

        @return: DescribeRdsVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        """
        @summary Queries a list of regions and zones where AnalyticDB for PostgreSQL is available.
        
        @description Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRegionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        """
        @summary Queries a list of regions and zones where AnalyticDB for PostgreSQL is available.
        
        @description Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRegionsRequest

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_roles_with_options(self, request, runtime):
        """
        @summary Queries a list of roles.
        

        @param request: DescribeRolesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoles',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_roles(self, request):
        """
        @summary Queries a list of roles.
        

        @param request: DescribeRolesRequest

        @return: DescribeRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_roles_with_options(request, runtime)

    def describe_sqllog_count_with_options(self, request, runtime):
        """
        @summary Queries the number of audit logs for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        

        @param request: DescribeSQLLogCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogCount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_count(self, request):
        """
        @summary Queries the number of audit logs for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        

        @param request: DescribeSQLLogCountRequest

        @return: DescribeSQLLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_count_with_options(request, runtime)

    def describe_sqllogs_with_options(self, request, runtime):
        """
        @summary Queries the SQL execution logs of an AnalyticDB for PostgreSQL instance.
        
        @description > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](https://help.aliyun.com/document_detail/453722.html) operation.
        

        @param request: DescribeSQLLogsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllogs(self, request):
        """
        @summary Queries the SQL execution logs of an AnalyticDB for PostgreSQL instance.
        
        @description > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](https://help.aliyun.com/document_detail/453722.html) operation.
        

        @param request: DescribeSQLLogsRequest

        @return: DescribeSQLLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_with_options(request, runtime)

    def describe_sqllogs_v2with_options(self, request, runtime):
        """
        @summary Queries SQL logs within a specific time range.
        
        @description You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeSQLLogsV2Request

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLLogsV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogsV2',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsV2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllogs_v2(self, request):
        """
        @summary Queries SQL logs within a specific time range.
        
        @description You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeSQLLogsV2Request

        @return: DescribeSQLLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_v2with_options(request, runtime)

    def describe_sample_data_with_options(self, request, runtime):
        """
        @summary Queries whether a sample dataset is loaded to an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeSampleDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_data(self, request):
        """
        @summary Queries whether a sample dataset is loaded to an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeSampleDataRequest

        @return: DescribeSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_data_with_options(request, runtime)

    def describe_streaming_data_service_with_options(self, request, runtime):
        """
        @summary Queries a real-time data service.
        

        @param request: DescribeStreamingDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeStreamingDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamingDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_streaming_data_service(self, request):
        """
        @summary Queries a real-time data service.
        

        @param request: DescribeStreamingDataServiceRequest

        @return: DescribeStreamingDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_streaming_data_service_with_options(request, runtime)

    def describe_streaming_data_source_with_options(self, request, runtime):
        """
        @summary Queries a real-time data source.
        

        @param request: DescribeStreamingDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeStreamingDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamingDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_streaming_data_source(self, request):
        """
        @summary Queries a real-time data source.
        

        @param request: DescribeStreamingDataSourceRequest

        @return: DescribeStreamingDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_streaming_data_source_with_options(request, runtime)

    def describe_streaming_job_with_options(self, request, runtime):
        """
        @summary Queries a real-time data service.
        

        @param request: DescribeStreamingJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeStreamingJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamingJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_streaming_job(self, request):
        """
        @summary Queries a real-time data service.
        

        @param request: DescribeStreamingJobRequest

        @return: DescribeStreamingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_streaming_job_with_options(request, runtime)

    def describe_support_features_with_options(self, request, runtime):
        """
        @summary Queries the features that are supported by an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeSupportFeaturesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSupportFeaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportFeatures',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSupportFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_support_features(self, request):
        """
        @summary Queries the features that are supported by an AnalyticDB for PostgreSQL instance.
        

        @param request: DescribeSupportFeaturesRequest

        @return: DescribeSupportFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_support_features_with_options(request, runtime)

    def describe_table_with_options(self, request, runtime):
        """
        @summary Queries the information about a table.
        

        @param request: DescribeTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            query['Table'] = request.table
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTable',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTableResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_table(self, request):
        """
        @summary Queries the information about a table.
        

        @param request: DescribeTableRequest

        @return: DescribeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        """
        @summary Queries a list of tags for AnalyticDB for PostgreSQL instances.
        

        @param request: DescribeTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        """
        @summary Queries a list of tags for AnalyticDB for PostgreSQL instances.
        

        @param request: DescribeTagsRequest

        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_user_encryption_key_list_with_options(self, request, runtime):
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        

        @param request: DescribeUserEncryptionKeyListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeUserEncryptionKeyListResponse
        """
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
            action='DescribeUserEncryptionKeyList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_encryption_key_list(self, request):
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        

        @param request: DescribeUserEncryptionKeyListRequest

        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    def describe_waiting_sqlinfo_with_options(self, request, runtime):
        """
        @summary Queries the information about a lock-waiting query for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeWaitingSQLInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeWaitingSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.pid):
            query['PID'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_waiting_sqlinfo(self, request):
        """
        @summary Queries the information about a lock-waiting query for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeWaitingSQLInfoRequest

        @return: DescribeWaitingSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waiting_sqlinfo_with_options(request, runtime)

    def describe_waiting_sqlrecords_with_options(self, request, runtime):
        """
        @summary Queries the lock diagnostic records of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeWaitingSQLRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeWaitingSQLRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_waiting_sqlrecords(self, request):
        """
        @summary Queries the lock diagnostic records of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeWaitingSQLRecordsRequest

        @return: DescribeWaitingSQLRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waiting_sqlrecords_with_options(request, runtime)

    def disable_dbresource_group_with_options(self, request, runtime):
        """
        @summary Disables resource group management for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode. After you disable resource group management, the resource management method of the instance switches from resource group management to resource queue management.
        
        @description    You can call this operation only for AnalyticDB for PostgreSQL V6.0 instances in elastic storage mode whose minor version is V6.6.1.0 or later.
        You can call this operation to disable resource group management only for AnalyticDB for PostgreSQL instances that are in the **Running** state.
        **Note: When the resource management method is switched, your AnalyticDB for PostgreSQL instance restarts and becomes unavailable for approximately 5 minutes. To prevent your business from being affected, call this operation during off-peak hours.
        

        @param request: DisableDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DisableDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_dbresource_group(self, request):
        """
        @summary Disables resource group management for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode. After you disable resource group management, the resource management method of the instance switches from resource group management to resource queue management.
        
        @description    You can call this operation only for AnalyticDB for PostgreSQL V6.0 instances in elastic storage mode whose minor version is V6.6.1.0 or later.
        You can call this operation to disable resource group management only for AnalyticDB for PostgreSQL instances that are in the **Running** state.
        **Note: When the resource management method is switched, your AnalyticDB for PostgreSQL instance restarts and becomes unavailable for approximately 5 minutes. To prevent your business from being affected, call this operation during off-peak hours.
        

        @param request: DisableDBResourceGroupRequest

        @return: DisableDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_dbresource_group_with_options(request, runtime)

    def download_diagnosis_records_with_options(self, request, runtime):
        """
        @summary Downloads the query diagnostic information of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](https://help.aliyun.com/document_detail/447712.html) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DownloadDiagnosisRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DownloadDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def download_diagnosis_records(self, request):
        """
        @summary Downloads the query diagnostic information of an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](https://help.aliyun.com/document_detail/447712.html) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DownloadDiagnosisRecordsRequest

        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    def download_sqllogs_records_with_options(self, request, runtime):
        """
        @summary Download the slow query logs of an AnalyticDB for PostgreSQL instance.
        

        @param request: DownloadSQLLogsRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DownloadSQLLogsRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadSQLLogsRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadSQLLogsRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def download_sqllogs_records(self, request):
        """
        @summary Download the slow query logs of an AnalyticDB for PostgreSQL instance.
        

        @param request: DownloadSQLLogsRecordsRequest

        @return: DownloadSQLLogsRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_sqllogs_records_with_options(request, runtime)

    def enable_dbresource_group_with_options(self, request, runtime):
        """
        @summary Enables resource group management for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode. After resource group management is enabled, the resource management mode of the instance is changed from resource queue to resource group.
        
        @description    You can call this operation only for AnalyticDB for PostgreSQL V6.0 instances in elastic storage mode whose minor version is V6.6.1.0 or later.
        You can call this operation to enable resource group management only for AnalyticDB for PostgreSQL instances that are in the **Running** state.
        **Note: When the resource management mode is changed, your AnalyticDB for PostgreSQL instance is restarted and remains unavailable within 5 minutes. To prevent your business from being affected, call this operation during off-peak hours.
        

        @param request: EnableDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.EnableDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_dbresource_group(self, request):
        """
        @summary Enables resource group management for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode. After resource group management is enabled, the resource management mode of the instance is changed from resource queue to resource group.
        
        @description    You can call this operation only for AnalyticDB for PostgreSQL V6.0 instances in elastic storage mode whose minor version is V6.6.1.0 or later.
        You can call this operation to enable resource group management only for AnalyticDB for PostgreSQL instances that are in the **Running** state.
        **Note: When the resource management mode is changed, your AnalyticDB for PostgreSQL instance is restarted and remains unavailable within 5 minutes. To prevent your business from being affected, call this operation during off-peak hours.
        

        @param request: EnableDBResourceGroupRequest

        @return: EnableDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_dbresource_group_with_options(request, runtime)

    def execute_statement_with_options(self, tmp_req, runtime):
        """
        @summary Executes SQL statements.
        

        @param tmp_req: ExecuteStatementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExecuteStatementResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.ExecuteStatementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.sqls):
            request.sqls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sqls, 'Sqls', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.run_type):
            query['RunType'] = request.run_type
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.statement_name):
            query['StatementName'] = request.statement_name
        body = {}
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.sqls_shrink):
            body['Sqls'] = request.sqls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteStatement',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ExecuteStatementResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_statement(self, request):
        """
        @summary Executes SQL statements.
        

        @param request: ExecuteStatementRequest

        @return: ExecuteStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_statement_with_options(request, runtime)

    def get_secret_value_with_options(self, request, runtime):
        """
        @summary Queries the information about an access credential.
        

        @param request: GetSecretValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSecretValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretValue',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    def get_secret_value(self, request):
        """
        @summary Queries the information about an access credential.
        

        @param request: GetSecretValueRequest

        @return: GetSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    def get_upload_document_job_with_options(self, request, runtime):
        """
        @summary Queries the progress and result of an asynchronous document upload job based on the job ID.
        
        @description This operation is related to the UploadDocumentAsync operation. You can call the UploadDocumentAsync operation to create an upload job and obtain the job ID, and then call the GetUploadDocumentJob operation to query the execution information of the job.
        >  Suggestions:
        Determine whether the document upload job times out based on the document complexity and the number of tokens after chunking. In most cases, a job that lasts more than 2 hours is considered timeout.
        

        @param request: GetUploadDocumentJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetUploadDocumentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadDocumentJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GetUploadDocumentJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_upload_document_job(self, request):
        """
        @summary Queries the progress and result of an asynchronous document upload job based on the job ID.
        
        @description This operation is related to the UploadDocumentAsync operation. You can call the UploadDocumentAsync operation to create an upload job and obtain the job ID, and then call the GetUploadDocumentJob operation to query the execution information of the job.
        >  Suggestions:
        Determine whether the document upload job times out based on the document complexity and the number of tokens after chunking. In most cases, a job that lasts more than 2 hours is considered timeout.
        

        @param request: GetUploadDocumentJobRequest

        @return: GetUploadDocumentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_document_job_with_options(request, runtime)

    def get_upsert_collection_data_job_with_options(self, request, runtime):
        """
        @summary Queries the progress and result of an asynchronous vector data upload job by using a job ID.
        
        @description This operation is related to the `UpsertCollectionDataAsync` operation. You can call the `UpsertCollectionDataAsync` operation to create an upload job and obtain a job ID, and then call the GetUpsertCollectionDataJob operation to query the execution information of the job.
        >  We recommend that you evaluate the amount of time required for the upload job based on 1,000 data entries every second, and then query the job progress every 5 seconds. The timeout period can be set to 30 minutes after the evaluated amount of time.
        

        @param request: GetUpsertCollectionDataJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetUpsertCollectionDataJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUpsertCollectionDataJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GetUpsertCollectionDataJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_upsert_collection_data_job(self, request):
        """
        @summary Queries the progress and result of an asynchronous vector data upload job by using a job ID.
        
        @description This operation is related to the `UpsertCollectionDataAsync` operation. You can call the `UpsertCollectionDataAsync` operation to create an upload job and obtain a job ID, and then call the GetUpsertCollectionDataJob operation to query the execution information of the job.
        >  We recommend that you evaluate the amount of time required for the upload job based on 1,000 data entries every second, and then query the job progress every 5 seconds. The timeout period can be set to 30 minutes after the evaluated amount of time.
        

        @param request: GetUpsertCollectionDataJobRequest

        @return: GetUpsertCollectionDataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upsert_collection_data_job_with_options(request, runtime)

    def grant_collection_with_options(self, request, runtime):
        """
        @summary Grants vector collection permissions to a namespace.
        

        @param request: GrantCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.grant_to_namespace):
            query['GrantToNamespace'] = request.grant_to_namespace
        if not UtilClient.is_unset(request.grant_type):
            query['GrantType'] = request.grant_type
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GrantCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_collection(self, request):
        """
        @summary Grants vector collection permissions to a namespace.
        

        @param request: GrantCollectionRequest

        @return: GrantCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_collection_with_options(request, runtime)

    def handle_active_sqlrecord_with_options(self, request, runtime):
        """
        @summary Processes active queries.
        

        @param request: HandleActiveSQLRecordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: HandleActiveSQLRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleActiveSQLRecord',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.HandleActiveSQLRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def handle_active_sqlrecord(self, request):
        """
        @summary Processes active queries.
        

        @param request: HandleActiveSQLRecordRequest

        @return: HandleActiveSQLRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.handle_active_sqlrecord_with_options(request, runtime)

    def init_vector_database_with_options(self, request, runtime):
        """
        @summary Initializes vector databases.
        

        @param request: InitVectorDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InitVectorDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitVectorDatabase',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.InitVectorDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def init_vector_database(self, request):
        """
        @summary Initializes vector databases.
        

        @param request: InitVectorDatabaseRequest

        @return: InitVectorDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_vector_database_with_options(request, runtime)

    def list_collections_with_options(self, request, runtime):
        """
        @summary Queries a list of vector collections.
        

        @param request: ListCollectionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_collections(self, request):
        """
        @summary Queries a list of vector collections.
        

        @param request: ListCollectionsRequest

        @return: ListCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    def list_databases_with_options(self, request, runtime):
        """
        @summary Queries a list of databases.
        

        @param request: ListDatabasesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_databases(self, request):
        """
        @summary Queries a list of databases.
        

        @param request: ListDatabasesRequest

        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    def list_document_collections_with_options(self, request, runtime):
        """
        @summary Queries a list of document collections.
        

        @param request: ListDocumentCollectionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDocumentCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocumentCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_document_collections(self, request):
        """
        @summary Queries a list of document collections.
        

        @param request: ListDocumentCollectionsRequest

        @return: ListDocumentCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_document_collections_with_options(request, runtime)

    def list_documents_with_options(self, request, runtime):
        """
        @summary Queries a list of documents in a collection.
        

        @param request: ListDocumentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDocumentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocuments',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_documents(self, request):
        """
        @summary Queries a list of documents in a collection.
        

        @param request: ListDocumentsRequest

        @return: ListDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    def list_external_data_services_with_options(self, request, runtime):
        """
        @summary Queries a list of external data sources.
        

        @param request: ListExternalDataServicesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExternalDataServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ListExternalDataServices',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListExternalDataServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_external_data_services(self, request):
        """
        @summary Queries a list of external data sources.
        

        @param request: ListExternalDataServicesRequest

        @return: ListExternalDataServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_external_data_services_with_options(request, runtime)

    def list_external_data_sources_with_options(self, request, runtime):
        """
        @summary 获取实例外表配置列表
        

        @param request: ListExternalDataSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExternalDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ListExternalDataSources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListExternalDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_external_data_sources(self, request):
        """
        @summary 获取实例外表配置列表
        

        @param request: ListExternalDataSourcesRequest

        @return: ListExternalDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_external_data_sources_with_options(request, runtime)

    def list_instance_extensions_with_options(self, request, runtime):
        """
        @summary Queries a list of extensions.
        

        @param request: ListInstanceExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.install_status):
            query['InstallStatus'] = request.install_status
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
            action='ListInstanceExtensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListInstanceExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_extensions(self, request):
        """
        @summary Queries a list of extensions.
        

        @param request: ListInstanceExtensionsRequest

        @return: ListInstanceExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_extensions_with_options(request, runtime)

    def list_namespaces_with_options(self, request, runtime):
        """
        @summary Queries a list of namespaces.
        

        @param request: ListNamespacesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_namespaces(self, request):
        """
        @summary Queries a list of namespaces.
        

        @param request: ListNamespacesRequest

        @return: ListNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    def list_schemas_with_options(self, request, runtime):
        """
        @summary Queries a list of schemas.
        

        @param request: ListSchemasRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_pattern):
            query['SchemaPattern'] = request.schema_pattern
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemas',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_schemas(self, request):
        """
        @summary Queries a list of schemas.
        

        @param request: ListSchemasRequest

        @return: ListSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_schemas_with_options(request, runtime)

    def list_secrets_with_options(self, request, runtime):
        """
        @summary Queries a list of access credentials.
        

        @param request: ListSecretsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_secrets(self, request):
        """
        @summary Queries a list of access credentials.
        

        @param request: ListSecretsRequest

        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    def list_streaming_data_services_with_options(self, request, runtime):
        """
        @summary Queries the information about real-time data services.
        

        @param request: ListStreamingDataServicesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListStreamingDataServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ListStreamingDataServices',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListStreamingDataServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_streaming_data_services(self, request):
        """
        @summary Queries the information about real-time data services.
        

        @param request: ListStreamingDataServicesRequest

        @return: ListStreamingDataServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_streaming_data_services_with_options(request, runtime)

    def list_streaming_data_sources_with_options(self, request, runtime):
        """
        @summary Queries real-time service data sources.
        

        @param request: ListStreamingDataSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListStreamingDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ListStreamingDataSources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListStreamingDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_streaming_data_sources(self, request):
        """
        @summary Queries real-time service data sources.
        

        @param request: ListStreamingDataSourcesRequest

        @return: ListStreamingDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_streaming_data_sources_with_options(request, runtime)

    def list_streaming_jobs_with_options(self, request, runtime):
        """
        @summary Queries real-time data service jobs.
        

        @param request: ListStreamingJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListStreamingJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ListStreamingJobs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListStreamingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_streaming_jobs(self, request):
        """
        @summary Queries real-time data service jobs.
        

        @param request: ListStreamingJobsRequest

        @return: ListStreamingJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_streaming_jobs_with_options(request, runtime)

    def list_tables_with_options(self, request, runtime):
        """
        @summary Queries a list of tables in a database.
        

        @param request: ListTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table_pattern):
            query['TablePattern'] = request.table_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tables(self, request):
        """
        @summary Queries a list of tables in a database.
        

        @param request: ListTablesRequest

        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        @summary Queries a list of tags that are added to AnalyticDB for PostgreSQL instances.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        @summary Queries a list of tags that are added to AnalyticDB for PostgreSQL instances.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        """
        @summary Modifies the description of a database account for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyAccountDescriptionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_description(self, request):
        """
        @summary Modifies the description of a database account for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyAccountDescriptionRequest

        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        """
        @summary Configures the backup policy of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.enable_recovery_point):
            query['EnableRecoveryPoint'] = request.enable_recovery_point
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.recovery_point_period):
            query['RecoveryPointPeriod'] = request.recovery_point_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy(self, request):
        """
        @summary Configures the backup policy of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyBackupPolicyRequest

        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_dbinstance_config_with_options(self, request, runtime):
        """
        @summary Changes the threshold of computing resources and the wait period of idle resources for an AnalyticDB for PostgreSQL instance in Serverless automatic scheduling mode.
        

        @param request: ModifyDBInstanceConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_config(self, request):
        """
        @summary Changes the threshold of computing resources and the wait period of idle resources for an AnalyticDB for PostgreSQL instance in Serverless automatic scheduling mode.
        

        @param request: ModifyDBInstanceConfigRequest

        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        """
        @summary Changes the endpoint of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyDBInstanceConnectionStringRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_connection_string(self, request):
        """
        @summary Changes the endpoint of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyDBInstanceConnectionStringRequest

        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        """
        @summary Changes the description of an AnalyticDB for PostgreSQL instance.
        
        @description To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDBInstanceDescriptionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_description(self, request):
        """
        @summary Changes the description of an AnalyticDB for PostgreSQL instance.
        
        @description To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDBInstanceDescriptionRequest

        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        """
        @summary Modifies the maintenance window of an AnalyticDB for PostgreSQL instance.
        
        @description The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDBInstanceMaintainTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(self, request):
        """
        @summary Modifies the maintenance window of an AnalyticDB for PostgreSQL instance.
        
        @description The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDBInstanceMaintainTimeRequest

        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    def modify_dbinstance_resource_group_with_options(self, request, runtime):
        """
        @summary Moves an AnalyticDB for PostgreSQL instance to a resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        

        @param request: ModifyDBInstanceResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_resource_group(self, request):
        """
        @summary Moves an AnalyticDB for PostgreSQL instance to a resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        

        @param request: ModifyDBInstanceResourceGroupRequest

        @return: ModifyDBInstanceResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_resource_group_with_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        """
        @summary Enables, disables, or updates SSL encryption for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyDBInstanceSSLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_ssl(self, request):
        """
        @summary Enables, disables, or updates SSL encryption for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyDBInstanceSSLRequest

        @return: ModifyDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def modify_dbresource_group_with_options(self, tmp_req, runtime):
        """
        @summary Modifies the configurations of a resource group.
        

        @param tmp_req: ModifyDBResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.ModifyDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_group_items):
            request.resource_group_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_group_items, 'ResourceGroupItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_items_shrink):
            query['ResourceGroupItems'] = request.resource_group_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbresource_group(self, request):
        """
        @summary Modifies the configurations of a resource group.
        

        @param request: ModifyDBResourceGroupRequest

        @return: ModifyDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    def modify_external_data_service_with_options(self, request, runtime):
        """
        @summary Modifies an external data service.
        

        @param request: ModifyExternalDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyExternalDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyExternalDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyExternalDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_external_data_service(self, request):
        """
        @summary Modifies an external data service.
        

        @param request: ModifyExternalDataServiceRequest

        @return: ModifyExternalDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_external_data_service_with_options(request, runtime)

    def modify_hadoop_data_source_with_options(self, request, runtime):
        """
        @summary Modifies the configurations of a Hadoop data source.
        

        @param request: ModifyHadoopDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHadoopDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.emr_instance_id):
            query['EmrInstanceId'] = request.emr_instance_id
        if not UtilClient.is_unset(request.hdfsconf):
            query['HDFSConf'] = request.hdfsconf
        if not UtilClient.is_unset(request.hadoop_core_conf):
            query['HadoopCoreConf'] = request.hadoop_core_conf
        if not UtilClient.is_unset(request.hadoop_create_type):
            query['HadoopCreateType'] = request.hadoop_create_type
        if not UtilClient.is_unset(request.hadoop_hosts_address):
            query['HadoopHostsAddress'] = request.hadoop_hosts_address
        if not UtilClient.is_unset(request.hive_conf):
            query['HiveConf'] = request.hive_conf
        if not UtilClient.is_unset(request.map_reduce_conf):
            query['MapReduceConf'] = request.map_reduce_conf
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.yarn_conf):
            query['YarnConf'] = request.yarn_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHadoopDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyHadoopDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hadoop_data_source(self, request):
        """
        @summary Modifies the configurations of a Hadoop data source.
        

        @param request: ModifyHadoopDataSourceRequest

        @return: ModifyHadoopDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hadoop_data_source_with_options(request, runtime)

    def modify_jdbcdata_source_with_options(self, request, runtime):
        """
        @summary Modifies the configurations of a Java Database Connectivity (JDBC) data source.
        

        @param request: ModifyJDBCDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyJDBCDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.jdbcconnection_string):
            query['JDBCConnectionString'] = request.jdbcconnection_string
        if not UtilClient.is_unset(request.jdbcpassword):
            query['JDBCPassword'] = request.jdbcpassword
        if not UtilClient.is_unset(request.jdbcuser_name):
            query['JDBCUserName'] = request.jdbcuser_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyJDBCDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyJDBCDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_jdbcdata_source(self, request):
        """
        @summary Modifies the configurations of a Java Database Connectivity (JDBC) data source.
        

        @param request: ModifyJDBCDataSourceRequest

        @return: ModifyJDBCDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_jdbcdata_source_with_options(request, runtime)

    def modify_master_spec_with_options(self, request, runtime):
        """
        @summary Changes the specifications of coordinator node resources for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: ModifyMasterSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyMasterSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMasterSpec',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyMasterSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_master_spec(self, request):
        """
        @summary Changes the specifications of coordinator node resources for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: ModifyMasterSpecRequest

        @return: ModifyMasterSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_master_spec_with_options(request, runtime)

    def modify_parameters_with_options(self, request, runtime):
        """
        @summary Modifies the configuration parameters of an AnalyticDB for PostgreSQL instance.
        
        @description This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyParametersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.force_restart_instance):
            query['ForceRestartInstance'] = request.force_restart_instance
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameters(self, request):
        """
        @summary Modifies the configuration parameters of an AnalyticDB for PostgreSQL instance.
        
        @description This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyParametersRequest

        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    def modify_sqlcollector_policy_with_options(self, request, runtime):
        """
        @summary Enables or disables the SQL Explorer feature for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifySQLCollectorPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySQLCollectorPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_sqlcollector_policy(self, request):
        """
        @summary Enables or disables the SQL Explorer feature for an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifySQLCollectorPolicyRequest

        @return: ModifySQLCollectorPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for PostgreSQL instance.
        
        @description To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifySecurityIpsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_ips(self, request):
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for PostgreSQL instance.
        
        @description To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifySecurityIpsRequest

        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_streaming_data_service_with_options(self, request, runtime):
        """
        @summary Modifies a real-time data service.
        

        @param request: ModifyStreamingDataServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyStreamingDataServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_spec):
            query['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStreamingDataService',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyStreamingDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_streaming_data_service(self, request):
        """
        @summary Modifies a real-time data service.
        

        @param request: ModifyStreamingDataServiceRequest

        @return: ModifyStreamingDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_streaming_data_service_with_options(request, runtime)

    def modify_streaming_data_source_with_options(self, request, runtime):
        """
        @summary Modifies a real-time service data source.
        

        @param request: ModifyStreamingDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyStreamingDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_source_config):
            query['DataSourceConfig'] = request.data_source_config
        if not UtilClient.is_unset(request.data_source_description):
            query['DataSourceDescription'] = request.data_source_description
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStreamingDataSource',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyStreamingDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_streaming_data_source(self, request):
        """
        @summary Modifies a real-time service data source.
        

        @param request: ModifyStreamingDataSourceRequest

        @return: ModifyStreamingDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_streaming_data_source_with_options(request, runtime)

    def modify_streaming_job_with_options(self, tmp_req, runtime):
        """
        @summary 创建外部数据源配置
        

        @param tmp_req: ModifyStreamingJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyStreamingJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.ModifyStreamingJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_columns):
            request.dest_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_columns, 'DestColumns', 'json')
        if not UtilClient.is_unset(tmp_req.match_columns):
            request.match_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.match_columns, 'MatchColumns', 'json')
        if not UtilClient.is_unset(tmp_req.src_columns):
            request.src_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_columns, 'SrcColumns', 'json')
        if not UtilClient.is_unset(tmp_req.update_columns):
            request.update_columns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_columns, 'UpdateColumns', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.consistency):
            query['Consistency'] = request.consistency
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_columns_shrink):
            query['DestColumns'] = request.dest_columns_shrink
        if not UtilClient.is_unset(request.dest_database):
            query['DestDatabase'] = request.dest_database
        if not UtilClient.is_unset(request.dest_schema):
            query['DestSchema'] = request.dest_schema
        if not UtilClient.is_unset(request.dest_table):
            query['DestTable'] = request.dest_table
        if not UtilClient.is_unset(request.error_limit_count):
            query['ErrorLimitCount'] = request.error_limit_count
        if not UtilClient.is_unset(request.fallback_offset):
            query['FallbackOffset'] = request.fallback_offset
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.job_config):
            query['JobConfig'] = request.job_config
        if not UtilClient.is_unset(request.job_description):
            query['JobDescription'] = request.job_description
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.match_columns_shrink):
            query['MatchColumns'] = request.match_columns_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.src_columns_shrink):
            query['SrcColumns'] = request.src_columns_shrink
        if not UtilClient.is_unset(request.try_run):
            query['TryRun'] = request.try_run
        if not UtilClient.is_unset(request.update_columns_shrink):
            query['UpdateColumns'] = request.update_columns_shrink
        if not UtilClient.is_unset(request.write_mode):
            query['WriteMode'] = request.write_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStreamingJob',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyStreamingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_streaming_job(self, request):
        """
        @summary 创建外部数据源配置
        

        @param request: ModifyStreamingJobRequest

        @return: ModifyStreamingJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_streaming_job_with_options(request, runtime)

    def modify_vector_configuration_with_options(self, request, runtime):
        """
        @summary Modifies the vector engine optimization configuration of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyVectorConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyVectorConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVectorConfiguration',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyVectorConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vector_configuration(self, request):
        """
        @summary Modifies the vector engine optimization configuration of an AnalyticDB for PostgreSQL instance.
        

        @param request: ModifyVectorConfigurationRequest

        @return: ModifyVectorConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vector_configuration_with_options(request, runtime)

    def pause_data_redistribute_with_options(self, request, runtime):
        """
        @summary Pauses data redistribution.
        

        @param request: PauseDataRedistributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PauseDataRedistributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseDataRedistribute',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.PauseDataRedistributeResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_data_redistribute(self, request):
        """
        @summary Pauses data redistribution.
        

        @param request: PauseDataRedistributeRequest

        @return: PauseDataRedistributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_data_redistribute_with_options(request, runtime)

    def pause_instance_with_options(self, request, runtime):
        """
        @summary Pauses an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: PauseInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PauseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.PauseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_instance(self, request):
        """
        @summary Pauses an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: PauseInstanceRequest

        @return: PauseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_instance_with_options(request, runtime)

    def query_collection_data_with_options(self, tmp_req, runtime):
        """
        @summary Retrieves vector data.
        

        @param tmp_req: QueryCollectionDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryCollectionDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.QueryCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not UtilClient.is_unset(tmp_req.relational_table_filter):
            request.relational_table_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.relational_table_filter, 'RelationalTableFilter', 'json')
        if not UtilClient.is_unset(tmp_req.vector):
            request.vector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vector, 'Vector', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not UtilClient.is_unset(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not UtilClient.is_unset(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not UtilClient.is_unset(request.include_values):
            query['IncludeValues'] = request.include_values
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relational_table_filter_shrink):
            query['RelationalTableFilter'] = request.relational_table_filter_shrink
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.vector_shrink):
            query['Vector'] = request.vector_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_collection_data(self, request):
        """
        @summary Retrieves vector data.
        

        @param request: QueryCollectionDataRequest

        @return: QueryCollectionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_collection_data_with_options(request, runtime)

    def query_content_with_options(self, tmp_req, runtime):
        """
        @summary Retrieves vector data and metadata from a document collection by using natural statements.
        

        @param tmp_req: QueryContentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.QueryContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hybrid_search_args):
            request.hybrid_search_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hybrid_search_args, 'HybridSearchArgs', 'json')
        if not UtilClient.is_unset(tmp_req.recall_window):
            request.recall_window_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recall_window, 'RecallWindow', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.hybrid_search):
            query['HybridSearch'] = request.hybrid_search
        if not UtilClient.is_unset(request.hybrid_search_args_shrink):
            query['HybridSearchArgs'] = request.hybrid_search_args_shrink
        if not UtilClient.is_unset(request.include_file_url):
            query['IncludeFileUrl'] = request.include_file_url
        if not UtilClient.is_unset(request.include_metadata_fields):
            query['IncludeMetadataFields'] = request.include_metadata_fields
        if not UtilClient.is_unset(request.include_vector):
            query['IncludeVector'] = request.include_vector
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recall_window_shrink):
            query['RecallWindow'] = request.recall_window_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rerank_factor):
            query['RerankFactor'] = request.rerank_factor
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.use_full_text_retrieval):
            query['UseFullTextRetrieval'] = request.use_full_text_retrieval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContent',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryContentResponse(),
            self.call_api(params, req, runtime)
        )

    def query_content(self, request):
        """
        @summary Retrieves vector data and metadata from a document collection by using natural statements.
        

        @param request: QueryContentRequest

        @return: QueryContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_content_with_options(request, runtime)

    def query_content_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='gpdb',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        query_content_req = gpdb_20160503_models.QueryContentRequest()
        OpenApiUtilClient.convert(request, query_content_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            query_content_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        query_content_resp = self.query_content_with_options(query_content_req, runtime)
        return query_content_resp

    def rebalance_dbinstance_with_options(self, request, runtime):
        """
        @summary Rebalances an AnalyticDB for PostgreSQL instance.
        

        @param request: RebalanceDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RebalanceDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RebalanceDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def rebalance_dbinstance(self, request):
        """
        @summary Rebalances an AnalyticDB for PostgreSQL instance.
        

        @param request: RebalanceDBInstanceRequest

        @return: RebalanceDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebalance_dbinstance_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        """
        @summary Releases the public endpoint of an AnalyticDB for PostgreSQL instance.
        

        @param request: ReleaseInstancePublicConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_public_connection(self, request):
        """
        @summary Releases the public endpoint of an AnalyticDB for PostgreSQL instance.
        

        @param request: ReleaseInstancePublicConnectionRequest

        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def rerank_with_options(self, tmp_req, runtime):
        """
        @summary 通过模型对文档进行打分和重排序
        

        @param tmp_req: RerankRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RerankResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.RerankShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.max_chunks_per_doc):
            body['MaxChunksPerDoc'] = request.max_chunks_per_doc
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.return_documents):
            body['ReturnDocuments'] = request.return_documents
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Rerank',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RerankResponse(),
            self.call_api(params, req, runtime)
        )

    def rerank(self, request):
        """
        @summary 通过模型对文档进行打分和重排序
        

        @param request: RerankRequest

        @return: RerankResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rerank_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        """
        @summary Resets the password of a database account for an AnalyticDB for PostgreSQL instance.
        

        @param request: ResetAccountPasswordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account_password(self, request):
        """
        @summary Resets the password of a database account for an AnalyticDB for PostgreSQL instance.
        

        @param request: ResetAccountPasswordRequest

        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def reset_imvmonitor_data_with_options(self, request, runtime):
        """
        @summary Resets the IMV statistics.
        

        @param request: ResetIMVMonitorDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetIMVMonitorDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetIMVMonitorData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetIMVMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_imvmonitor_data(self, request):
        """
        @summary Resets the IMV statistics.
        

        @param request: ResetIMVMonitorDataRequest

        @return: ResetIMVMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_imvmonitor_data_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        """
        @summary Restarts an AnalyticDB for PostgreSQL instance.
        
        @description A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: RestartDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_dbinstance(self, request):
        """
        @summary Restarts an AnalyticDB for PostgreSQL instance.
        
        @description A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        

        @param request: RestartDBInstanceRequest

        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def resume_data_redistribute_with_options(self, request, runtime):
        """
        @summary Resumes data redistribution.
        

        @param request: ResumeDataRedistributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeDataRedistributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeDataRedistribute',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResumeDataRedistributeResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_data_redistribute(self, request):
        """
        @summary Resumes data redistribution.
        

        @param request: ResumeDataRedistributeRequest

        @return: ResumeDataRedistributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_data_redistribute_with_options(request, runtime)

    def resume_instance_with_options(self, request, runtime):
        """
        @summary Resumes an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ResumeInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_instance(self, request):
        """
        @summary Resumes an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](https://help.aliyun.com/document_detail/277424.html) and [Update the minor engine version](https://help.aliyun.com/document_detail/139271.html).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ResumeInstanceRequest

        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    def set_dbinstance_plan_status_with_options(self, request, runtime):
        """
        @summary Enables or disables a plan for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: SetDBInstancePlanStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDBInstancePlanStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_status):
            query['PlanStatus'] = request.plan_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDBInstancePlanStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDBInstancePlanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dbinstance_plan_status(self, request):
        """
        @summary Enables or disables a plan for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: SetDBInstancePlanStatusRequest

        @return: SetDBInstancePlanStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dbinstance_plan_status_with_options(request, runtime)

    def set_data_share_instance_with_options(self, tmp_req, runtime):
        """
        @summary Enables or disables data sharing for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param tmp_req: SetDataShareInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDataShareInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.SetDataShareInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataShareInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDataShareInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_share_instance(self, request):
        """
        @summary Enables or disables data sharing for an AnalyticDB for PostgreSQL instance.
        
        @description This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: SetDataShareInstanceRequest

        @return: SetDataShareInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_share_instance_with_options(request, runtime)

    def switch_dbinstance_net_type_with_options(self, request, runtime):
        """
        @summary Switches between the internal and public endpoints of an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not supported for AnalyticDB for PostgreSQL instances in elastic storage mode or Serverless mode.
        

        @param request: SwitchDBInstanceNetTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchDBInstanceNetTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_net_type(self, request):
        """
        @summary Switches between the internal and public endpoints of an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not supported for AnalyticDB for PostgreSQL instances in elastic storage mode or Serverless mode.
        

        @param request: SwitchDBInstanceNetTypeRequest

        @return: SwitchDBInstanceNetTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        @summary Creates and adds tags to AnalyticDB for PostgreSQL instances.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        @summary Creates and adds tags to AnalyticDB for PostgreSQL instances.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unbind_dbresource_group_with_role_with_options(self, tmp_req, runtime):
        """
        @summary Unbinds database roles from a resource group.
        

        @param tmp_req: UnbindDBResourceGroupWithRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnbindDBResourceGroupWithRoleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UnbindDBResourceGroupWithRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.role_list):
            request.role_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.role_list, 'RoleList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.role_list_shrink):
            query['RoleList'] = request.role_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourceGroupWithRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UnbindDBResourceGroupWithRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_dbresource_group_with_role(self, request):
        """
        @summary Unbinds database roles from a resource group.
        

        @param request: UnbindDBResourceGroupWithRoleRequest

        @return: UnbindDBResourceGroupWithRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_dbresource_group_with_role_with_options(request, runtime)

    def unload_sample_data_with_options(self, request, runtime):
        """
        @summary Releases a sample dataset from an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UnloadSampleDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnloadSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnloadSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UnloadSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def unload_sample_data(self, request):
        """
        @summary Releases a sample dataset from an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UnloadSampleDataRequest

        @return: UnloadSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unload_sample_data_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        @summary Removes tags from AnalyticDB for PostgreSQL instances. If the tags that you remove are not added to other instances, the tags are automatically deleted.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        @summary Removes tags from AnalyticDB for PostgreSQL instances. If the tags that you remove are not added to other instances, the tags are automatically deleted.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_collection_data_metadata_with_options(self, tmp_req, runtime):
        """
        @summary Updates metadata in the vector data.
        

        @param tmp_req: UpdateCollectionDataMetadataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCollectionDataMetadataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpdateCollectionDataMetadataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.metadata):
            request.metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.metadata_shrink):
            query['Metadata'] = request.metadata_shrink
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCollectionDataMetadata',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateCollectionDataMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_collection_data_metadata(self, request):
        """
        @summary Updates metadata in the vector data.
        

        @param request: UpdateCollectionDataMetadataRequest

        @return: UpdateCollectionDataMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_collection_data_metadata_with_options(request, runtime)

    def update_dbinstance_plan_with_options(self, request, runtime):
        """
        @summary Modifies a plan for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UpdateDBInstancePlanRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dbinstance_plan(self, request):
        """
        @summary Modifies a plan for an AnalyticDB for PostgreSQL instance.
        
        @description You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UpdateDBInstancePlanRequest

        @return: UpdateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_plan_with_options(request, runtime)

    def upgrade_dbinstance_with_options(self, request, runtime):
        """
        @summary Changes the configurations of an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: UpgradeDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance(self, request):
        """
        @summary Changes the configurations of an AnalyticDB for PostgreSQL instance.
        
        @description This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](https://help.aliyun.com/document_detail/35406.html) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        

        @param request: UpgradeDBInstanceRequest

        @return: UpgradeDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_with_options(request, runtime)

    def upgrade_dbversion_with_options(self, request, runtime):
        """
        @summary Upgrades the minor version of an AnalyticDB for PostgreSQL instance.
        

        @param request: UpgradeDBVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBVersion',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbversion(self, request):
        """
        @summary Upgrades the minor version of an AnalyticDB for PostgreSQL instance.
        

        @param request: UpgradeDBVersionRequest

        @return: UpgradeDBVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbversion_with_options(request, runtime)

    def upgrade_extensions_with_options(self, request, runtime):
        """
        @summary Updates extensions.
        

        @param request: UpgradeExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeExtensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_extensions(self, request):
        """
        @summary Updates extensions.
        

        @param request: UpgradeExtensionsRequest

        @return: UpgradeExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_extensions_with_options(request, runtime)

    def upload_document_async_with_options(self, tmp_req, runtime):
        """
        @summary Uploads a document in an asynchronous manner by using an on-premises file or an Internet-accessible file URL. After a document is uploaded, the server loads, chunks, embeds, and stores the document. A document can be up to 200 MB in size.
        
        @description The server loads and chunks a document based on the file extension, performs vectorization by using the embedding model that is specified when you call the CreateDocumentCollection operation, and then writes the document to the specified document collection. This operation supports multi-modal embedding for various formats of text and images.
        Related operations:
        You can call the GetUploadDocumentJob operation to query the progress and result of a document upload job.
        You can call the CancelUploadDocumentJob operation to cancel a document upload job.
        >
        After a document upload request is submitted, the request is queued for processing. Up to 20 documents in the Pending and Running states can be processed within a Resource Access Management (RAM) user or Alibaba Cloud account.
        A text document can be split into up to 100,000 chunks.
        If a document collection uses the OnePeace model, each RAM user or Alibaba Cloud account can upload and query up to 10,000 images.
        

        @param tmp_req: UploadDocumentAsyncRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadDocumentAsyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UploadDocumentAsyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metadata):
            request.metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        if not UtilClient.is_unset(tmp_req.separators):
            request.separators_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.separators, 'Separators', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.chunk_overlap):
            body['ChunkOverlap'] = request.chunk_overlap
        if not UtilClient.is_unset(request.chunk_size):
            body['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.document_loader_name):
            body['DocumentLoaderName'] = request.document_loader_name
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.separators_shrink):
            body['Separators'] = request.separators_shrink
        if not UtilClient.is_unset(request.text_splitter_name):
            body['TextSplitterName'] = request.text_splitter_name
        if not UtilClient.is_unset(request.zh_title_enhance):
            body['ZhTitleEnhance'] = request.zh_title_enhance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDocumentAsync',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UploadDocumentAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_document_async(self, request):
        """
        @summary Uploads a document in an asynchronous manner by using an on-premises file or an Internet-accessible file URL. After a document is uploaded, the server loads, chunks, embeds, and stores the document. A document can be up to 200 MB in size.
        
        @description The server loads and chunks a document based on the file extension, performs vectorization by using the embedding model that is specified when you call the CreateDocumentCollection operation, and then writes the document to the specified document collection. This operation supports multi-modal embedding for various formats of text and images.
        Related operations:
        You can call the GetUploadDocumentJob operation to query the progress and result of a document upload job.
        You can call the CancelUploadDocumentJob operation to cancel a document upload job.
        >
        After a document upload request is submitted, the request is queued for processing. Up to 20 documents in the Pending and Running states can be processed within a Resource Access Management (RAM) user or Alibaba Cloud account.
        A text document can be split into up to 100,000 chunks.
        If a document collection uses the OnePeace model, each RAM user or Alibaba Cloud account can upload and query up to 10,000 images.
        

        @param request: UploadDocumentAsyncRequest

        @return: UploadDocumentAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_document_async_with_options(request, runtime)

    def upload_document_async_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='gpdb',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_document_async_req = gpdb_20160503_models.UploadDocumentAsyncRequest()
        OpenApiUtilClient.convert(request, upload_document_async_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            upload_document_async_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        upload_document_async_resp = self.upload_document_async_with_options(upload_document_async_req, runtime)
        return upload_document_async_resp

    def upsert_chunks_with_options(self, tmp_req, runtime):
        """
        @summary Splits a document into chunks and uploads the vectorized chunks to a document collection.
        

        @param tmp_req: UpsertChunksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpsertChunksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertChunksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.text_chunks):
            request.text_chunks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_chunks, 'TextChunks', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.text_chunks_shrink):
            body['TextChunks'] = request.text_chunks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertChunks',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertChunksResponse(),
            self.call_api(params, req, runtime)
        )

    def upsert_chunks(self, request):
        """
        @summary Splits a document into chunks and uploads the vectorized chunks to a document collection.
        

        @param request: UpsertChunksRequest

        @return: UpsertChunksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upsert_chunks_with_options(request, runtime)

    def upsert_collection_data_with_options(self, tmp_req, runtime):
        """
        @summary Uploads vector data to a vector collection.
        

        @param tmp_req: UpsertCollectionDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpsertCollectionDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rows):
            request.rows_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rows, 'Rows', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.rows_shrink):
            body['Rows'] = request.rows_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def upsert_collection_data(self, request):
        """
        @summary Uploads vector data to a vector collection.
        

        @param request: UpsertCollectionDataRequest

        @return: UpsertCollectionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upsert_collection_data_with_options(request, runtime)

    def upsert_collection_data_async_with_options(self, request, runtime):
        """
        @summary Uploads vector data in an asynchronous manner by using an on-premises file or a password-free Internet-accessible file URL. The vector data can be up to 200 MB in size.
        
        @description This operation is the asynchronous operation of `UpsertCollectionData`. The `UpsertCollectionData` operation supports up to 10 MB of data, and this operation supports up to 200 MB of data.
        >  Related operations:
        You can call the GetUpsertCollectionDataJob operation to query the progress and result of an upload job.
        You can call the CancelUpsertCollectionDataJob operation to cancel an upload job.
        > You can upload data for the same collection only in a serial manner.
        

        @param request: UpsertCollectionDataAsyncRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpsertCollectionDataAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            body['NamespacePassword'] = request.namespace_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionDataAsync',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertCollectionDataAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def upsert_collection_data_async(self, request):
        """
        @summary Uploads vector data in an asynchronous manner by using an on-premises file or a password-free Internet-accessible file URL. The vector data can be up to 200 MB in size.
        
        @description This operation is the asynchronous operation of `UpsertCollectionData`. The `UpsertCollectionData` operation supports up to 10 MB of data, and this operation supports up to 200 MB of data.
        >  Related operations:
        You can call the GetUpsertCollectionDataJob operation to query the progress and result of an upload job.
        You can call the CancelUpsertCollectionDataJob operation to cancel an upload job.
        > You can upload data for the same collection only in a serial manner.
        

        @param request: UpsertCollectionDataAsyncRequest

        @return: UpsertCollectionDataAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upsert_collection_data_async_with_options(request, runtime)

    def upsert_collection_data_async_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='gpdb',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upsert_collection_data_async_req = gpdb_20160503_models.UpsertCollectionDataAsyncRequest()
        OpenApiUtilClient.convert(request, upsert_collection_data_async_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            upsert_collection_data_async_req.file_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        upsert_collection_data_async_resp = self.upsert_collection_data_async_with_options(upsert_collection_data_async_req, runtime)
        return upsert_collection_data_async_resp
