# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20200518 import models as dataworks_public_20200518_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


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

    def abolish_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbolishDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AbolishDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def abolish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abolish_data_service_api_with_options(request, runtime)

    def add_meta_collection_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection_qualified_name):
            query['CollectionQualifiedName'] = request.collection_qualified_name
        if not UtilClient.is_unset(request.entity_qualified_name):
            query['EntityQualifiedName'] = request.entity_qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMetaCollectionEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddMetaCollectionEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def add_meta_collection_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_meta_collection_entity_with_options(request, runtime)

    def add_project_member_to_role_with_options(self, request, runtime):
        """
        For more information about how to add your Alibaba Cloud account or a RAM user as a member of a DataWorks workspace, see [Add a member to a DataWorks workspace](~~136941~~).
        

        @param request: AddProjectMemberToRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddProjectMemberToRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_code):
            query['RoleCode'] = request.role_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddProjectMemberToRole',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddProjectMemberToRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_project_member_to_role(self, request):
        """
        For more information about how to add your Alibaba Cloud account or a RAM user as a member of a DataWorks workspace, see [Add a member to a DataWorks workspace](~~136941~~).
        

        @param request: AddProjectMemberToRoleRequest

        @return: AddProjectMemberToRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_project_member_to_role_with_options(request, runtime)

    def add_to_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddToMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddToMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_to_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_to_meta_category_with_options(request, runtime)

    def approve_permission_apply_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approve_action):
            query['ApproveAction'] = request.approve_action
        if not UtilClient.is_unset(request.approve_comment):
            query['ApproveComment'] = request.approve_comment
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApprovePermissionApplyOrder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def approve_permission_apply_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.approve_permission_apply_order_with_options(request, runtime)

    def change_resource_manager_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceManagerResourceGroup',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ChangeResourceManagerResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_manager_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_manager_resource_group_with_options(request, runtime)

    def check_file_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_detail_url):
            body['CheckDetailUrl'] = request.check_detail_url
        if not UtilClient.is_unset(request.checker_instance_id):
            body['CheckerInstanceId'] = request.checker_instance_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckFileDeployment',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckFileDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def check_file_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_file_deployment_with_options(request, runtime)

    def check_meta_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition):
            query['Partition'] = request.partition
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMetaPartition',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def check_meta_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_partition_with_options(request, runtime)

    def check_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMetaTable',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_with_options(request, runtime)

    def create_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_margin_threshold):
            body['AlertMarginThreshold'] = request.alert_margin_threshold
        if not UtilClient.is_unset(request.baseline_name):
            body['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.baseline_type):
            body['BaselineType'] = request.baseline_type
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.overtime_settings):
            body['OvertimeSettings'] = request.overtime_settings
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_baseline_with_options(request, runtime)

    def create_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def create_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_business_with_options(request, runtime)

    def create_connection_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConnectionResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConnection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_connection(self, request):
        """
        @deprecated
        

        @param request: CreateConnectionRequest

        @return: CreateConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    def create_disync_task_with_options(self, request, runtime):
        """
        DataWorks allows you to use only the CreateDISyncTask operation to create a batch synchronization node in Data Integration. To create a real-time synchronization node or a synchronization solution, you must first call the [GenerateDISyncTaskConfigForCreating](~~383463~~) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask operation and use the parameters as request parameters to create a real-time synchronization node or a synchronization solution in Data Integration.
        

        @param request: CreateDISyncTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDISyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_content):
            query['TaskContent'] = request.task_content
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_param):
            query['TaskParam'] = request.task_param
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDISyncTask',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_disync_task(self, request):
        """
        DataWorks allows you to use only the CreateDISyncTask operation to create a batch synchronization node in Data Integration. To create a real-time synchronization node or a synchronization solution, you must first call the [GenerateDISyncTaskConfigForCreating](~~383463~~) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask operation and use the parameters as request parameters to create a real-time synchronization node or a synchronization solution in Data Integration.
        

        @param request: CreateDISyncTaskRequest

        @return: CreateDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_disync_task_with_options(request, runtime)

    def create_dag_complement_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateDagComplementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDagComplementResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_begin_time):
            body['BizBeginTime'] = request.biz_begin_time
        if not UtilClient.is_unset(request.biz_end_time):
            body['BizEndTime'] = request.biz_end_time
        if not UtilClient.is_unset(request.end_biz_date):
            body['EndBizDate'] = request.end_biz_date
        if not UtilClient.is_unset(request.exclude_node_ids):
            body['ExcludeNodeIds'] = request.exclude_node_ids
        if not UtilClient.is_unset(request.include_node_ids):
            body['IncludeNodeIds'] = request.include_node_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_params):
            body['NodeParams'] = request.node_params
        if not UtilClient.is_unset(request.parallelism):
            body['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.root_node_id):
            body['RootNodeId'] = request.root_node_id
        if not UtilClient.is_unset(request.start_biz_date):
            body['StartBizDate'] = request.start_biz_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDagComplement',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagComplementResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dag_complement(self, request):
        """
        @deprecated
        

        @param request: CreateDagComplementRequest

        @return: CreateDagComplementResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dag_complement_with_options(request, runtime)

    def create_dag_test_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateDagTestRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDagTestResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_params):
            body['NodeParams'] = request.node_params
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDagTest',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagTestResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dag_test(self, request):
        """
        @deprecated
        

        @param request: CreateDagTestRequest

        @return: CreateDagTestResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dag_test_with_options(request, runtime)

    def create_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_description):
            body['ApiDescription'] = request.api_description
        if not UtilClient.is_unset(request.api_mode):
            body['ApiMode'] = request.api_mode
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.api_path):
            body['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.protocols):
            body['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.registration_details):
            body['RegistrationDetails'] = request.registration_details
        if not UtilClient.is_unset(request.request_method):
            body['RequestMethod'] = request.request_method
        if not UtilClient.is_unset(request.response_content_type):
            body['ResponseContentType'] = request.response_content_type
        if not UtilClient.is_unset(request.script_details):
            body['ScriptDetails'] = request.script_details
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.visible_range):
            body['VisibleRange'] = request.visible_range
        if not UtilClient.is_unset(request.wizard_details):
            body['WizardDetails'] = request.wizard_details
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    def create_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.authorized_project_id):
            body['AuthorizedProjectId'] = request.authorized_project_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataServiceApiAuthority',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_authority_with_options(request, runtime)

    def create_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_name):
            body['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataServiceFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_folder_with_options(request, runtime)

    def create_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_gateway_group_id):
            body['ApiGatewayGroupId'] = request.api_gateway_group_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataServiceGroup',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_group_with_options(request, runtime)

    def create_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    def create_export_migration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.export_mode):
            body['ExportMode'] = request.export_mode
        if not UtilClient.is_unset(request.export_object_status):
            body['ExportObjectStatus'] = request.export_object_status
        if not UtilClient.is_unset(request.incremental_since):
            body['IncrementalSince'] = request.incremental_since
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExportMigration',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateExportMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_export_migration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_export_migration_with_options(request, runtime)

    def create_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not UtilClient.is_unset(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not UtilClient.is_unset(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not UtilClient.is_unset(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not UtilClient.is_unset(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not UtilClient.is_unset(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not UtilClient.is_unset(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not UtilClient.is_unset(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not UtilClient.is_unset(request.file_description):
            body['FileDescription'] = request.file_description
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.input_list):
            body['InputList'] = request.input_list
        if not UtilClient.is_unset(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not UtilClient.is_unset(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.para_value):
            body['ParaValue'] = request.para_value
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not UtilClient.is_unset(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not UtilClient.is_unset(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not UtilClient.is_unset(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not UtilClient.is_unset(request.stop):
            body['Stop'] = request.stop
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_import_migration_with_options(self, request, runtime):
        """
        The import package must be uploaded. Example of the upload method:
        Config config = new Config();
        config.setAccessKeyId(accessId);
        config.setAccessKeySecret(accessKey);
        config.setEndpoint(popEndpoint);
        config.setRegionId(regionId);
        Client client = new Client(config);
        CreateImportMigrationAdvanceRequest request = new CreateImportMigrationAdvanceRequest();
        request.setName("test_migration_api\\_" + System.currentTimeMillis());
        request.setProjectId(123456L);
        request.setPackageType("DATAWORKS_MODEL");
        request.setPackageFileObject(new FileInputStream("/home/admin/Downloads/test.zip"));
        RuntimeOptions runtime = new RuntimeOptions();
        CreateImportMigrationResponse response = client.createImportMigrationAdvance(request, runtime);
        ...
        

        @param request: CreateImportMigrationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateImportMigrationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.calculate_engine_map):
            body['CalculateEngineMap'] = request.calculate_engine_map
        if not UtilClient.is_unset(request.commit_rule):
            body['CommitRule'] = request.commit_rule
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.package_file):
            body['PackageFile'] = request.package_file
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group_map):
            body['ResourceGroupMap'] = request.resource_group_map
        if not UtilClient.is_unset(request.workspace_map):
            body['WorkspaceMap'] = request.workspace_map
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImportMigration',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateImportMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_import_migration(self, request):
        """
        The import package must be uploaded. Example of the upload method:
        Config config = new Config();
        config.setAccessKeyId(accessId);
        config.setAccessKeySecret(accessKey);
        config.setEndpoint(popEndpoint);
        config.setRegionId(regionId);
        Client client = new Client(config);
        CreateImportMigrationAdvanceRequest request = new CreateImportMigrationAdvanceRequest();
        request.setName("test_migration_api\\_" + System.currentTimeMillis());
        request.setProjectId(123456L);
        request.setPackageType("DATAWORKS_MODEL");
        request.setPackageFileObject(new FileInputStream("/home/admin/Downloads/test.zip"));
        RuntimeOptions runtime = new RuntimeOptions();
        CreateImportMigrationResponse response = client.createImportMigrationAdvance(request, runtime);
        ...
        

        @param request: CreateImportMigrationRequest

        @return: CreateImportMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_import_migration_with_options(request, runtime)

    def create_import_migration_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            product='dataworks-public',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        create_import_migration_req = dataworks_public_20200518_models.CreateImportMigrationRequest()
        OpenApiUtilClient.convert(request, create_import_migration_req)
        if not UtilClient.is_unset(request.package_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.package_file_object,
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
            create_import_migration_req.package_file = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        create_import_migration_resp = self.create_import_migration_with_options(create_import_migration_req, runtime)
        return create_import_migration_resp

    def create_manual_dag_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateManualDagRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateManualDagResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.dag_parameters):
            body['DagParameters'] = request.dag_parameters
        if not UtilClient.is_unset(request.exclude_node_ids):
            body['ExcludeNodeIds'] = request.exclude_node_ids
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.include_node_ids):
            body['IncludeNodeIds'] = request.include_node_ids
        if not UtilClient.is_unset(request.node_parameters):
            body['NodeParameters'] = request.node_parameters
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateManualDag',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateManualDagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_manual_dag(self, request):
        """
        @deprecated
        

        @param request: CreateManualDagRequest

        @return: CreateManualDagResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    def create_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_meta_category_with_options(request, runtime)

    def create_meta_collection_with_options(self, request, runtime):
        """
        Collections are classified into various types. The names of collections of the same type must be different.
        

        @param request: CreateMetaCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMetaCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection_type):
            query['CollectionType'] = request.collection_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_qualified_name):
            query['ParentQualifiedName'] = request.parent_qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetaCollection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_meta_collection(self, request):
        """
        Collections are classified into various types. The names of collections of the same type must be different.
        

        @param request: CreateMetaCollectionRequest

        @return: CreateMetaCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_meta_collection_with_options(request, runtime)

    def create_permission_apply_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_object):
            query['ApplyObject'] = request.apply_object
        if not UtilClient.is_unset(request.apply_reason):
            query['ApplyReason'] = request.apply_reason
        if not UtilClient.is_unset(request.apply_user_ids):
            query['ApplyUserIds'] = request.apply_user_ids
        if not UtilClient.is_unset(request.deadline):
            query['Deadline'] = request.deadline
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.max_compute_project_name):
            query['MaxComputeProjectName'] = request.max_compute_project_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePermissionApplyOrder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreatePermissionApplyOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_permission_apply_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_permission_apply_order_with_options(request, runtime)

    def create_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_code):
            query['RoleCode'] = request.role_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProjectMember',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    def create_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_level):
            body['EntityLevel'] = request.entity_level
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_entity_with_options(request, runtime)

    def create_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_mode):
            body['AlarmMode'] = request.alarm_mode
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityFollower',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityFollowerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_follower_with_options(request, runtime)

    def create_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.target_node_project_id):
            body['TargetNodeProjectId'] = request.target_node_project_id
        if not UtilClient.is_unset(request.target_node_project_name):
            body['TargetNodeProjectName'] = request.target_node_project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityRelativeNode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRelativeNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_relative_node_with_options(request, runtime)

    def create_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_type):
            body['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.checker):
            body['Checker'] = request.checker
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.critical_threshold):
            body['CriticalThreshold'] = request.critical_threshold
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.expect_value):
            body['ExpectValue'] = request.expect_value
        if not UtilClient.is_unset(request.method_name):
            body['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.predict_type):
            body['PredictType'] = request.predict_type
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.property_type):
            body['PropertyType'] = request.property_type
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trend):
            body['Trend'] = request.trend
        if not UtilClient.is_unset(request.warning_threshold):
            body['WarningThreshold'] = request.warning_threshold
        if not UtilClient.is_unset(request.where_condition):
            body['WhereCondition'] = request.where_condition
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQualityRule',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    def create_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_interval):
            body['AlertInterval'] = request.alert_interval
        if not UtilClient.is_unset(request.alert_methods):
            body['AlertMethods'] = request.alert_methods
        if not UtilClient.is_unset(request.alert_targets):
            body['AlertTargets'] = request.alert_targets
        if not UtilClient.is_unset(request.alert_unit):
            body['AlertUnit'] = request.alert_unit
        if not UtilClient.is_unset(request.baseline_ids):
            body['BaselineIds'] = request.baseline_ids
        if not UtilClient.is_unset(request.biz_process_ids):
            body['BizProcessIds'] = request.biz_process_ids
        if not UtilClient.is_unset(request.detail):
            body['Detail'] = request.detail
        if not UtilClient.is_unset(request.dnd_end):
            body['DndEnd'] = request.dnd_end
        if not UtilClient.is_unset(request.max_alert_times):
            body['MaxAlertTimes'] = request.max_alert_times
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.remind_name):
            body['RemindName'] = request.remind_name
        if not UtilClient.is_unset(request.remind_type):
            body['RemindType'] = request.remind_type
        if not UtilClient.is_unset(request.remind_unit):
            body['RemindUnit'] = request.remind_unit
        if not UtilClient.is_unset(request.robot_urls):
            body['RobotUrls'] = request.robot_urls
        if not UtilClient.is_unset(request.webhooks):
            body['Webhooks'] = request.webhooks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRemind',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateRemindResponse(),
            self.call_api(params, req, runtime)
        )

    def create_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_remind_with_options(request, runtime)

    def create_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_guid):
            query['AppGuid'] = request.app_guid
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.external_table_type):
            query['ExternalTableType'] = request.external_table_type
        if not UtilClient.is_unset(request.has_part):
            query['HasPart'] = request.has_part
        if not UtilClient.is_unset(request.is_view):
            query['IsView'] = request.is_view
        if not UtilClient.is_unset(request.life_cycle):
            query['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.logical_level_id):
            query['LogicalLevelId'] = request.logical_level_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physics_level_id):
            query['PhysicsLevelId'] = request.physics_level_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['Columns'] = request.columns
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.themes):
            body['Themes'] = request.themes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    def create_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTableLevel',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_level_with_options(request, runtime)

    def create_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTableTheme',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableThemeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_theme_with_options(request, runtime)

    def create_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not UtilClient.is_unset(request.example):
            body['Example'] = request.example
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        if not UtilClient.is_unset(request.return_value):
            body['ReturnValue'] = request.return_value
        if not UtilClient.is_unset(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUdfFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateUdfFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    def delete_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_baseline_with_options(request, runtime)

    def delete_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_id):
            body['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    def delete_connection_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: DeleteConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConnectionResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_id):
            query['ConnectionId'] = request.connection_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_connection(self, request):
        """
        @deprecated
        

        @param request: DeleteConnectionRequest

        @return: DeleteConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    def delete_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDISyncTask',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disync_task_with_options(request, runtime)

    def delete_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_with_options(request, runtime)

    def delete_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.authorized_project_id):
            body['AuthorizedProjectId'] = request.authorized_project_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataServiceApiAuthority',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_authority_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_from_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFromMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFromMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_from_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_from_meta_category_with_options(request, runtime)

    def delete_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_category_with_options(request, runtime)

    def delete_meta_collection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualified_name):
            query['QualifiedName'] = request.qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetaCollection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_meta_collection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_collection_with_options(request, runtime)

    def delete_meta_collection_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection_qualified_name):
            query['CollectionQualifiedName'] = request.collection_qualified_name
        if not UtilClient.is_unset(request.entity_qualified_name):
            query['EntityQualifiedName'] = request.entity_qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetaCollectionEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCollectionEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_meta_collection_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_collection_entity_with_options(request, runtime)

    def delete_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProjectMember',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    def delete_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQualityEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_entity_with_options(request, runtime)

    def delete_quality_follower_with_options(self, request, runtime):
        """
        In Data Quality, you must configure monitoring rules based on a partition filter expression. Data Quality uses these rules to detect changes in source data and dirty data generated during the process of extract, transformation, load (ETL). Thereby, Data Quality automatically blocks the nodes that involve dirty data to stop dirty data from spreading downstream. This prevents nodes from producing unexpected dirty data that affects normal use and business decisions. You can go to the Manage Subscriptions page to add subscribers for a partition filter expression. When the monitoring rule described by the partition filter expression is triggered, the subscribers can receive notifications and troubleshoot errors in a timely manner. For more information, see [Configure monitoring rules for MaxCompute](~~73690~~).
        

        @param request: DeleteQualityFollowerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQualityFollowerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.follower_id):
            body['FollowerId'] = request.follower_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQualityFollower',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityFollowerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quality_follower(self, request):
        """
        In Data Quality, you must configure monitoring rules based on a partition filter expression. Data Quality uses these rules to detect changes in source data and dirty data generated during the process of extract, transformation, load (ETL). Thereby, Data Quality automatically blocks the nodes that involve dirty data to stop dirty data from spreading downstream. This prevents nodes from producing unexpected dirty data that affects normal use and business decisions. You can go to the Manage Subscriptions page to add subscribers for a partition filter expression. When the monitoring rule described by the partition filter expression is triggered, the subscribers can receive notifications and troubleshoot errors in a timely manner. For more information, see [Configure monitoring rules for MaxCompute](~~73690~~).
        

        @param request: DeleteQualityFollowerRequest

        @return: DeleteQualityFollowerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_follower_with_options(request, runtime)

    def delete_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.target_node_project_id):
            body['TargetNodeProjectId'] = request.target_node_project_id
        if not UtilClient.is_unset(request.target_node_project_name):
            body['TargetNodeProjectName'] = request.target_node_project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQualityRelativeNode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_relative_node_with_options(request, runtime)

    def delete_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQualityRule',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    def delete_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remind_id):
            body['RemindId'] = request.remind_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRemind',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteRemindResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_remind_with_options(request, runtime)

    def delete_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_guid):
            query['AppGuid'] = request.app_guid
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    def delete_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level_id):
            query['LevelId'] = request.level_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableLevel',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_level_with_options(request, runtime)

    def delete_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableTheme',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableThemeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_theme_with_options(request, runtime)

    def deploy_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployDISyncTask',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_disync_task_with_options(request, runtime)

    def deploy_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployFileResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    def desensitize_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesensitizeData',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DesensitizeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def desensitize_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.desensitize_data_with_options(request, runtime)

    def establish_relation_table_to_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_id):
            body['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.table_guid):
            body['TableGuid'] = request.table_guid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EstablishRelationTableToBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def establish_relation_table_to_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    def export_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDataSources',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def export_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_data_sources_with_options(request, runtime)

    def generate_disync_task_config_for_creating_with_options(self, request, runtime):
        """
        DataWorks allows you to use only the [CreateDISyncTask](~~278725~~) operation to create a batch synchronization node in Data Integration. To create a real-time synchronization node or a synchronization solution, you must first call the [GenerateDISyncTaskConfigForCreating](~~383463~~) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the [CreateDISyncTask](~~278725~~) operation and use the parameters as request parameters to create a real-time synchronization node or a synchronization solution in Data Integration.
        DataWorks allows you to create real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForCreatingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateDISyncTaskConfigForCreatingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_param):
            query['TaskParam'] = request.task_param
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDISyncTaskConfigForCreating',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_disync_task_config_for_creating(self, request):
        """
        DataWorks allows you to use only the [CreateDISyncTask](~~278725~~) operation to create a batch synchronization node in Data Integration. To create a real-time synchronization node or a synchronization solution, you must first call the [GenerateDISyncTaskConfigForCreating](~~383463~~) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the [CreateDISyncTask](~~278725~~) operation and use the parameters as request parameters to create a real-time synchronization node or a synchronization solution in Data Integration.
        DataWorks allows you to create real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForCreatingRequest

        @return: GenerateDISyncTaskConfigForCreatingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_creating_with_options(request, runtime)

    def generate_disync_task_config_for_updating_with_options(self, request, runtime):
        """
        DataWorks allows you to use only the [UpdateDISyncTask](~~289109~~) operation to update a batch synchronization node in Data Integration. To update a real-time synchronization node or a synchronization solution, you must first call the GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the UpdateDISyncTask operation and use the parameters as request parameters to update a real-time synchronization node or a synchronization solution in Data Integration. DataWorks allows you to update real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForUpdatingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateDISyncTaskConfigForUpdatingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_param):
            query['TaskParam'] = request.task_param
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDISyncTaskConfigForUpdating',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_disync_task_config_for_updating(self, request):
        """
        DataWorks allows you to use only the [UpdateDISyncTask](~~289109~~) operation to update a batch synchronization node in Data Integration. To update a real-time synchronization node or a synchronization solution, you must first call the GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the UpdateDISyncTask operation and use the parameters as request parameters to update a real-time synchronization node or a synchronization solution in Data Integration. DataWorks allows you to update real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForUpdatingRequest

        @return: GenerateDISyncTaskConfigForUpdatingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_updating_with_options(request, runtime)

    def get_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_with_options(request, runtime)

    def get_baseline_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaselineConfig',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_baseline_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_config_with_options(request, runtime)

    def get_baseline_key_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.in_group_id):
            body['InGroupId'] = request.in_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaselineKeyPath',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineKeyPathResponse(),
            self.call_api(params, req, runtime)
        )

    def get_baseline_key_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_key_path_with_options(request, runtime)

    def get_baseline_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.in_group_id):
            body['InGroupId'] = request.in_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaselineStatus',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_baseline_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_status_with_options(request, runtime)

    def get_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_id):
            body['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    def get_ddljob_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDDLJobStatus',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDDLJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ddljob_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ddljob_status_with_options(request, runtime)

    def get_disync_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDISyncInstanceInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_disync_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_instance_info_with_options(request, runtime)

    def get_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDISyncTask',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_with_options(request, runtime)

    def get_dag_with_options(self, request, runtime):
        """
        Supported DAG types:
        *   MANUAL: the DAG for a manually triggered workflow.
        *   SMOKE_TEST: the DAG for a smoke testing workflow.
        *   SUPPLY_DATA: the DAG for a data backfill instance.
        *   BUSINESS_PROCESS_DAG: the DAG for a one-time workflow.
        Supported DAG states:
        *   CREATED: The DAG is created.
        *   RUNNING: The DAG is running.
        *   FAILURE: The DAG fails to run.
        *   SUCCESS: The DAG successfully runs.
        

        @param request: GetDagRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dag_id):
            body['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDag',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dag(self, request):
        """
        Supported DAG types:
        *   MANUAL: the DAG for a manually triggered workflow.
        *   SMOKE_TEST: the DAG for a smoke testing workflow.
        *   SUPPLY_DATA: the DAG for a data backfill instance.
        *   BUSINESS_PROCESS_DAG: the DAG for a one-time workflow.
        Supported DAG states:
        *   CREATED: The DAG is created.
        *   RUNNING: The DAG is running.
        *   FAILURE: The DAG fails to run.
        *   SUCCESS: The DAG successfully runs.
        

        @param request: GetDagRequest

        @return: GetDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dag_with_options(request, runtime)

    def get_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_with_options(request, runtime)

    def get_data_service_api_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataServiceApiTest',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApiTestResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_api_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_test_with_options(request, runtime)

    def get_data_service_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataServiceApplication',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_application_with_options(request, runtime)

    def get_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataServiceFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_folder_with_options(request, runtime)

    def get_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataServiceGroup',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_group_with_options(request, runtime)

    def get_data_service_published_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataServicePublishedApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServicePublishedApiResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_service_published_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_published_api_with_options(request, runtime)

    def get_data_source_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datasource_name):
            query['DatasourceName'] = request.datasource_name
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceMeta',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataSourceMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_meta_with_options(request, runtime)

    def get_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['DeploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    def get_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extension_code):
            query['ExtensionCode'] = request.extension_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExtension',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_extension_with_options(request, runtime)

    def get_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    def get_file_type_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFileTypeStatistic',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileTypeStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_type_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_type_statistic_with_options(request, runtime)

    def get_file_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_version):
            body['FileVersion'] = request.file_version
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFileVersion',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    def get_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.folder_path):
            body['FolderPath'] = request.folder_path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_ideevent_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIDEEventDetail',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetIDEEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ideevent_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ideevent_detail_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_instance_consume_time_rank_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetInstanceConsumeTimeRankRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceConsumeTimeRankResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceConsumeTimeRank',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_consume_time_rank(self, request):
        """
        @deprecated
        

        @param request: GetInstanceConsumeTimeRankRequest

        @return: GetInstanceConsumeTimeRankResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_consume_time_rank_with_options(request, runtime)

    def get_instance_count_trend_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetInstanceCountTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceCountTrendResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceCountTrend',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceCountTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_count_trend(self, request):
        """
        @deprecated
        

        @param request: GetInstanceCountTrendRequest

        @return: GetInstanceCountTrendResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_trend_with_options(request, runtime)

    def get_instance_error_rank_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetInstanceErrorRankRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceErrorRankResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceErrorRank',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceErrorRankResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_error_rank(self, request):
        """
        @deprecated
        

        @param request: GetInstanceErrorRankRequest

        @return: GetInstanceErrorRankResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_error_rank_with_options(request, runtime)

    def get_instance_log_with_options(self, request, runtime):
        """
        You may not obtain the instance logs that were generated more than seven days ago.
        

        @param request: GetInstanceLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_history_id):
            body['InstanceHistoryId'] = request.instance_history_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceLog',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_log(self, request):
        """
        You may not obtain the instance logs that were generated more than seven days ago.
        

        @param request: GetInstanceLogRequest

        @return: GetInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_log_with_options(request, runtime)

    def get_instance_status_count_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetInstanceStatusCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceStatusCountResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceStatusCount',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_status_count(self, request):
        """
        @deprecated
        

        @param request: GetInstanceStatusCountRequest

        @return: GetInstanceStatusCountResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_count_with_options(request, runtime)

    def get_instance_status_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.dag_type):
            body['DagType'] = request.dag_type
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceStatusStatistic',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_status_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_statistic_with_options(request, runtime)

    def get_manual_dag_instances_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetManualDagInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetManualDagInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dag_id):
            body['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetManualDagInstances',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetManualDagInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_manual_dag_instances(self, request):
        """
        @deprecated
        

        @param request: GetManualDagInstancesRequest

        @return: GetManualDagInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_manual_dag_instances_with_options(request, runtime)

    def get_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_category_with_options(request, runtime)

    def get_meta_collection_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualified_name):
            query['QualifiedName'] = request.qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaCollectionDetail',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaCollectionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_collection_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_collection_detail_with_options(request, runtime)

    def get_meta_column_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.column_guid):
            query['ColumnGuid'] = request.column_guid
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaColumnLineage',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaColumnLineageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_column_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_column_lineage_with_options(request, runtime)

    def get_meta_dbinfo_with_options(self, request, runtime):
        """
        You can call this operation to query only the basic metadata information about a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param request: GetMetaDBInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaDBInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaDBInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_dbinfo(self, request):
        """
        You can call this operation to query only the basic metadata information about a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param request: GetMetaDBInfoRequest

        @return: GetMetaDBInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbinfo_with_options(request, runtime)

    def get_meta_dbtable_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_guid):
            query['AppGuid'] = request.app_guid
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaDBTableList',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBTableListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_dbtable_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbtable_list_with_options(request, runtime)

    def get_meta_table_basic_info_with_options(self, request, runtime):
        """
        ***\
        

        @param request: GetMetaTableBasicInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableBasicInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableBasicInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_basic_info(self, request):
        """
        ***\
        

        @param request: GetMetaTableBasicInfoRequest

        @return: GetMetaTableBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_basic_info_with_options(request, runtime)

    def get_meta_table_change_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_type):
            body['ChangeType'] = request.change_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.object_type):
            body['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.table_guid):
            body['TableGuid'] = request.table_guid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMetaTableChangeLog',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableChangeLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_change_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_change_log_with_options(request, runtime)

    def get_meta_table_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableColumn',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableColumnResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    def get_meta_table_full_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableFullInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableFullInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_full_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_full_info_with_options(request, runtime)

    def get_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.wiki_version):
            query['WikiVersion'] = request.wiki_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableIntroWiki',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableIntroWikiResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_intro_wiki_with_options(request, runtime)

    def get_meta_table_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.next_primary_key):
            query['NextPrimaryKey'] = request.next_primary_key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableLineage',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableLineageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_lineage_with_options(request, runtime)

    def get_meta_table_list_by_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableListByCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableListByCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_list_by_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_list_by_category_with_options(request, runtime)

    def get_meta_table_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableOutput',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_output_with_options(request, runtime)

    def get_meta_table_partition_with_options(self, tmp_req, runtime):
        """
        You can call this operation to query only the partitions of a metatable in a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param tmp_req: GetMetaTablePartitionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTablePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.GetMetaTablePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort_criterion):
            request.sort_criterion_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_criterion, 'SortCriterion', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_criterion_shrink):
            query['SortCriterion'] = request.sort_criterion_shrink
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTablePartition',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTablePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_partition(self, request):
        """
        You can call this operation to query only the partitions of a metatable in a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param request: GetMetaTablePartitionRequest

        @return: GetMetaTablePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_partition_with_options(request, runtime)

    def get_meta_table_producing_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableProducingTasks',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableProducingTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_producing_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_producing_tasks_with_options(request, runtime)

    def get_meta_table_theme_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableThemeLevel',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableThemeLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meta_table_theme_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_theme_level_with_options(request, runtime)

    def get_migration_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_id):
            body['MigrationId'] = request.migration_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMigrationProcess',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMigrationProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def get_migration_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_migration_process_with_options(request, runtime)

    def get_migration_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_id):
            body['MigrationId'] = request.migration_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMigrationSummary',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMigrationSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_migration_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_migration_summary_with_options(request, runtime)

    def get_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    def get_node_children_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeChildren',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_children(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_children_with_options(request, runtime)

    def get_node_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeCode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_code_with_options(request, runtime)

    def get_node_on_baseline_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetNodeOnBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeOnBaselineResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeOnBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeOnBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_on_baseline(self, request):
        """
        @deprecated
        

        @param request: GetNodeOnBaselineRequest

        @return: GetNodeOnBaselineResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_on_baseline_with_options(request, runtime)

    def get_node_parents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeParents',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeParentsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_parents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_parents_with_options(request, runtime)

    def get_node_type_list_info_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetNodeTypeListInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeTypeListInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeTypeListInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeTypeListInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_type_list_info(self, request):
        """
        @deprecated
        

        @param request: GetNodeTypeListInfoRequest

        @return: GetNodeTypeListInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_type_list_info_with_options(request, runtime)

    def get_op_risk_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpRiskData',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpRiskDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_op_risk_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_op_risk_data_with_options(request, runtime)

    def get_op_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpSensitiveData',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpSensitiveDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_op_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_op_sensitive_data_with_options(request, runtime)

    def get_option_value_for_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extension_code):
            body['ExtensionCode'] = request.extension_code
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOptionValueForProject',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOptionValueForProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_option_value_for_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_option_value_for_project_with_options(request, runtime)

    def get_permission_apply_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermissionApplyOrderDetail',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_permission_apply_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_permission_apply_order_detail_with_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def get_project_detail_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetProjectDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProjectDetailResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectDetail',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_detail(self, request):
        """
        @deprecated
        

        @param request: GetProjectDetailRequest

        @return: GetProjectDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_detail_with_options(request, runtime)

    def get_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQualityEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_entity_with_options(request, runtime)

    def get_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQualityFollower',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityFollowerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_follower_with_options(request, runtime)

    def get_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQualityRule',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    def get_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remind_id):
            body['RemindId'] = request.remind_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRemind',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetRemindResponse(),
            self.call_api(params, req, runtime)
        )

    def get_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_remind_with_options(request, runtime)

    def get_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSensitiveData',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSensitiveDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sensitive_data_with_options(request, runtime)

    def get_success_instance_trend_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetSuccessInstanceTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSuccessInstanceTrendResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSuccessInstanceTrend',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSuccessInstanceTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_success_instance_trend(self, request):
        """
        @deprecated
        

        @param request: GetSuccessInstanceTrendRequest

        @return: GetSuccessInstanceTrendResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_success_instance_trend_with_options(request, runtime)

    def get_topic_with_options(self, request, runtime):
        """
        ***\
        

        @param request: GetTopicRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTopicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopic',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic(self, request):
        """
        ***\
        

        @param request: GetTopicRequest

        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    def get_topic_influence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTopicInfluence',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicInfluenceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic_influence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_influence_with_options(request, runtime)

    def import_data_sources_with_options(self, request, runtime):
        """
        You can import self-managed data sources or data sources that are exported from other Dataworks workspaces to a specified DataWorks workspace.
        *   To import a self-managed data source to DataWorks, the data source type must be supported by DataWorks. For more information about the types of data sources supported by DataWorks, see [Supported data stores](~~181656~~).
        *   For more information about how to export data sources from DataWorks workspaces to on-premises devices, see [ExportDataSources](~~279570~~).
        

        @param request: ImportDataSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_sources):
            query['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDataSources',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_data_sources(self, request):
        """
        You can import self-managed data sources or data sources that are exported from other Dataworks workspaces to a specified DataWorks workspace.
        *   To import a self-managed data source to DataWorks, the data source type must be supported by DataWorks. For more information about the types of data sources supported by DataWorks, see [Supported data stores](~~181656~~).
        *   For more information about how to export data sources from DataWorks workspaces to on-premises devices, see [ExportDataSources](~~279570~~).
        

        @param request: ImportDataSourcesRequest

        @return: ImportDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_data_sources_with_options(request, runtime)

    def list_alert_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_methods):
            body['AlertMethods'] = request.alert_methods
        if not UtilClient.is_unset(request.alert_rule_types):
            body['AlertRuleTypes'] = request.alert_rule_types
        if not UtilClient.is_unset(request.alert_user):
            body['AlertUser'] = request.alert_user
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remind_id):
            body['RemindId'] = request.remind_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlertMessages',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListAlertMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alert_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alert_messages_with_options(request, runtime)

    def list_baseline_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_types):
            body['BaselineTypes'] = request.baseline_types
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.useflag):
            body['Useflag'] = request.useflag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBaselineConfigs',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_baseline_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_configs_with_options(request, runtime)

    def list_baseline_statuses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_types):
            body['BaselineTypes'] = request.baseline_types
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.finish_status):
            body['FinishStatus'] = request.finish_status
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBaselineStatuses',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_baseline_statuses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_statuses_with_options(request, runtime)

    def list_baselines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_types):
            body['BaselineTypes'] = request.baseline_types
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBaselines',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_baselines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baselines_with_options(request, runtime)

    def list_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def list_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    def list_calc_engines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.calc_engine_type):
            query['CalcEngineType'] = request.calc_engine_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCalcEngines',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListCalcEnginesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_calc_engines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_calc_engines_with_options(request, runtime)

    def list_connections_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListConnectionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConnectionsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnections',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connections(self, request):
        """
        @deprecated
        

        @param request: ListConnectionsRequest

        @return: ListConnectionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    def list_diproject_config_with_options(self, request, runtime):
        """
        DataWorks allows you to set the default global configuration for only the processing rules of DDL messages in sync solutions. After you configure the *processing rules of DDL messages** in sync solutions, the configuration is set as the default global configuration and applies to all real-time sync nodes. You can also modify the **processing rules of DDL messages** based on your business requirements. For more information, see [Sync solutions](~~199008~~).
        

        @param request: ListDIProjectConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDIProjectConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDIProjectConfig',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDIProjectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diproject_config(self, request):
        """
        DataWorks allows you to set the default global configuration for only the processing rules of DDL messages in sync solutions. After you configure the *processing rules of DDL messages** in sync solutions, the configuration is set as the default global configuration and applies to all real-time sync nodes. You can also modify the **processing rules of DDL messages** based on your business requirements. For more information, see [Sync solutions](~~199008~~).
        

        @param request: ListDIProjectConfigRequest

        @return: ListDIProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_diproject_config_with_options(request, runtime)

    def list_dags_with_options(self, request, runtime):
        """
        Supported DAG types:
        *   MANUAL: the DAG for a manually triggered workflow.
        *   SMOKE_TEST: the DAG for a smoke testing workflow.
        *   SUPPLY_DATA: the DAG for a data backfill instance.
        *   BUSINESS_PROCESS_DAG: the DAG for a one-time workflow.
        Supported DAG states:
        *   CREATED: The DAG is created.
        *   RUNNING: The DAG is running.
        *   FAILURE: The DAG fails to run.
        *   SUCCESS: The DAG successfully runs.
        

        @param request: ListDagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.op_seq):
            body['OpSeq'] = request.op_seq
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDags',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dags(self, request):
        """
        Supported DAG types:
        *   MANUAL: the DAG for a manually triggered workflow.
        *   SMOKE_TEST: the DAG for a smoke testing workflow.
        *   SUPPLY_DATA: the DAG for a data backfill instance.
        *   BUSINESS_PROCESS_DAG: the DAG for a one-time workflow.
        Supported DAG states:
        *   CREATED: The DAG is created.
        *   RUNNING: The DAG is running.
        *   FAILURE: The DAG fails to run.
        *   SUCCESS: The DAG successfully runs.
        

        @param request: ListDagsRequest

        @return: ListDagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dags_with_options(request, runtime)

    def list_data_service_api_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.api_name_keyword):
            body['ApiNameKeyword'] = request.api_name_keyword
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceApiAuthorities',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_api_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_authorities_with_options(request, runtime)

    def list_data_service_api_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataServiceApiTest',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApiTestResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_api_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_test_with_options(request, runtime)

    def list_data_service_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name_keyword):
            body['ApiNameKeyword'] = request.api_name_keyword
        if not UtilClient.is_unset(request.api_path_keyword):
            body['ApiPathKeyword'] = request.api_path_keyword
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceApis',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApisResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_apis_with_options(request, runtime)

    def list_data_service_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id_list):
            body['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceApplications',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_applications_with_options(request, runtime)

    def list_data_service_authorized_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.api_name_keyword):
            body['ApiNameKeyword'] = request.api_name_keyword
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceAuthorizedApis',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_authorized_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_authorized_apis_with_options(request, runtime)

    def list_data_service_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_name_keyword):
            body['FolderNameKeyword'] = request.folder_name_keyword
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceFolders',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceFoldersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_folders_with_options(request, runtime)

    def list_data_service_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name_keyword):
            body['GroupNameKeyword'] = request.group_name_keyword
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServiceGroups',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_groups_with_options(request, runtime)

    def list_data_service_published_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name_keyword):
            body['ApiNameKeyword'] = request.api_name_keyword
        if not UtilClient.is_unset(request.api_path_keyword):
            body['ApiPathKeyword'] = request.api_path_keyword
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataServicePublishedApis',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServicePublishedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_service_published_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    def list_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    def list_deployments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.end_create_time):
            body['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.end_execute_time):
            body['EndExecuteTime'] = request.end_execute_time
        if not UtilClient.is_unset(request.executor):
            body['Executor'] = request.executor
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deployments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_deployments_with_options(request, runtime)

    def list_enabled_extensions_for_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_code):
            body['EventCode'] = request.event_code
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEnabledExtensionsForProject',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListEnabledExtensionsForProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def list_enabled_extensions_for_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_enabled_extensions_for_project_with_options(request, runtime)

    def list_extensions_with_options(self, request, runtime):
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
            action='ListExtensions',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_extensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_extensions_with_options(request, runtime)

    def list_file_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFileType',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_file_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_type_with_options(request, runtime)

    def list_file_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFileVersions',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_file_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    def list_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_types):
            body['FileTypes'] = request.file_types
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.use_type):
            body['UseType'] = request.use_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    def list_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_path):
            body['ParentFolderPath'] = request.parent_folder_path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFolders',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFoldersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    def list_inner_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.outer_node_id):
            body['OuterNodeId'] = request.outer_node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_type):
            body['ProgramType'] = request.program_type
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInnerNodes',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInnerNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_inner_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_inner_nodes_with_options(request, runtime)

    def list_instance_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstanceAmount',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstanceAmountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_amount_with_options(request, runtime)

    def list_instance_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstanceHistory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstanceHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_history_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_bizdate):
            body['BeginBizdate'] = request.begin_bizdate
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.dag_id):
            body['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.end_bizdate):
            body['EndBizdate'] = request.end_bizdate
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_type):
            body['ProgramType'] = request.program_type
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_manual_dag_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dag_id):
            body['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListManualDagInstances',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListManualDagInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_manual_dag_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_manual_dag_instances_with_options(request, runtime)

    def list_meta_collection_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection_qualified_name):
            query['CollectionQualifiedName'] = request.collection_qualified_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMetaCollectionEntities',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaCollectionEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_meta_collection_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_meta_collection_entities_with_options(request, runtime)

    def list_meta_collections_with_options(self, request, runtime):
        """
        The type can be ALBUM or ALBUM_CATEGORY. ALBUM indicates data albums. ALBUM_CATEGORY indicates categories.
        

        @param request: ListMetaCollectionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMetaCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.administrator):
            query['Administrator'] = request.administrator
        if not UtilClient.is_unset(request.collection_type):
            query['CollectionType'] = request.collection_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.follower):
            query['Follower'] = request.follower
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_qualified_name):
            query['ParentQualifiedName'] = request.parent_qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMetaCollections',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_meta_collections(self, request):
        """
        The type can be ALBUM or ALBUM_CATEGORY. ALBUM indicates data albums. ALBUM_CATEGORY indicates categories.
        

        @param request: ListMetaCollectionsRequest

        @return: ListMetaCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_meta_collections_with_options(request, runtime)

    def list_meta_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMetaDB',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaDBResponse(),
            self.call_api(params, req, runtime)
        )

    def list_meta_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_meta_dbwith_options(request, runtime)

    def list_migrations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_type):
            body['MigrationType'] = request.migration_type
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMigrations',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMigrationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_migrations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_migrations_with_options(request, runtime)

    def list_node_iowith_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListNodeIORequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodeIOResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.io_type):
            body['IoType'] = request.io_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeIO',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeIOResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_io(self, request):
        """
        @deprecated
        

        @param request: ListNodeIORequest

        @return: ListNodeIOResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_iowith_options(request, runtime)

    def list_node_input_or_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.io_type):
            body['IoType'] = request.io_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeInputOrOutput',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeInputOrOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_input_or_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_input_or_output_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_type):
            body['ProgramType'] = request.program_type
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_nodes_by_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodesByBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes_by_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_baseline_with_options(request, runtime)

    def list_nodes_by_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outputs):
            body['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodesByOutput',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes_by_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_output_with_options(request, runtime)

    def list_permission_apply_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.flow_status):
            query['FlowStatus'] = request.flow_status
        if not UtilClient.is_unset(request.max_compute_project_name):
            query['MaxComputeProjectName'] = request.max_compute_project_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionApplyOrders',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListPermissionApplyOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_permission_apply_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_permission_apply_orders_with_options(request, runtime)

    def list_program_type_count_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListProgramTypeCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProgramTypeCountResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProgramTypeCount',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProgramTypeCountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_program_type_count(self, request):
        """
        @deprecated
        

        @param request: ListProgramTypeCountRequest

        @return: ListProgramTypeCountResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_program_type_count_with_options(request, runtime)

    def list_project_ids_with_options(self, request, runtime):
        """
        For example, an Alibaba Cloud account can assume the developer, O&M engineer, or workspace administrator role in a workspace. For more information, see [Manage members and roles](~~136941~~).
        

        @param request: ListProjectIdsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProjectIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectIds',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_ids(self, request):
        """
        For example, an Alibaba Cloud account can assume the developer, O&M engineer, or workspace administrator role in a workspace. For more information, see [Manage members and roles](~~136941~~).
        

        @param request: ListProjectIdsRequest

        @return: ListProjectIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_ids_with_options(request, runtime)

    def list_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    def list_project_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectRoles',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    def list_projects_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_quality_results_by_entity_with_options(self, request, runtime):
        """
        ***\
        

        @param request: ListQualityResultsByEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListQualityResultsByEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQualityResultsByEntity',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quality_results_by_entity(self, request):
        """
        ***\
        

        @param request: ListQualityResultsByEntityRequest

        @return: ListQualityResultsByEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_entity_with_options(request, runtime)

    def list_quality_results_by_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQualityResultsByRule',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quality_results_by_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_rule_with_options(request, runtime)

    def list_quality_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQualityRules',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quality_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    def list_ref_disync_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datasource_name):
            query['DatasourceName'] = request.datasource_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.ref_type):
            query['RefType'] = request.ref_type
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRefDISyncTasks',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRefDISyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ref_disync_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ref_disync_tasks_with_options(request, runtime)

    def list_reminds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_target):
            body['AlertTarget'] = request.alert_target
        if not UtilClient.is_unset(request.founder):
            body['Founder'] = request.founder
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remind_types):
            body['RemindTypes'] = request.remind_types
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReminds',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRemindsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_reminds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_reminds_with_options(request, runtime)

    def list_resource_groups_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.ListResourceGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_ext_key):
            query['BizExtKey'] = request.biz_ext_key
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.resource_group_type):
            query['ResourceGroupType'] = request.resource_group_type
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_shift_personnels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.shift_person_uid):
            body['ShiftPersonUID'] = request.shift_person_uid
        if not UtilClient.is_unset(request.shift_schedule_identifier):
            body['ShiftScheduleIdentifier'] = request.shift_schedule_identifier
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShiftPersonnels',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListShiftPersonnelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shift_personnels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_shift_personnels_with_options(request, runtime)

    def list_shift_schedules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shift_schedule_name):
            body['ShiftScheduleName'] = request.shift_schedule_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShiftSchedules',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListShiftSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shift_schedules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_shift_schedules_with_options(request, runtime)

    def list_success_instance_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSuccessInstanceAmount',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListSuccessInstanceAmountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_success_instance_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_success_instance_amount_with_options(request, runtime)

    def list_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableLevel',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_level_with_options(request, runtime)

    def list_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableTheme',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableThemeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_theme_with_options(request, runtime)

    def list_topics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.topic_statuses):
            body['TopicStatuses'] = request.topic_statuses
        if not UtilClient.is_unset(request.topic_types):
            body['TopicTypes'] = request.topic_types
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopics',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_topics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    def mount_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target_id):
            body['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_user_id):
            body['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MountDirectory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.MountDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def mount_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mount_directory_with_options(request, runtime)

    def offline_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineNode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.OfflineNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.offline_node_with_options(request, runtime)

    def publish_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.PublishDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    def query_disync_task_config_process_result_with_options(self, request, runtime):
        """
        DataWorks allows you to call only the [CreateDISyncTask](~~278725~~) or [UpdateDISyncTask](~~289109~~) operation to create or update a batch synchronization node in Data Integration. To create or update a real-time synchronization node or a synchronization solution, you must first call the GenerateDISyncTaskConfigForCreating or GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask or UpdateDISyncTask operation and use the parameters as request parameters to create or update a real-time synchronization node or a synchronization solution.
        DataWorks allows you to create or update real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: QueryDISyncTaskConfigProcessResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryDISyncTaskConfigProcessResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_process_id):
            query['AsyncProcessId'] = request.async_process_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDISyncTaskConfigProcessResult',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_disync_task_config_process_result(self, request):
        """
        DataWorks allows you to call only the [CreateDISyncTask](~~278725~~) or [UpdateDISyncTask](~~289109~~) operation to create or update a batch synchronization node in Data Integration. To create or update a real-time synchronization node or a synchronization solution, you must first call the GenerateDISyncTaskConfigForCreating or GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](~~383465~~) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask or UpdateDISyncTask operation and use the parameters as request parameters to create or update a real-time synchronization node or a synchronization solution.
        DataWorks allows you to create or update real-time synchronization nodes and synchronization solutions in Data Integration only in asynchronous mode.
        

        @param request: QueryDISyncTaskConfigProcessResultRequest

        @return: QueryDISyncTaskConfigProcessResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_disync_task_config_process_result_with_options(request, runtime)

    def query_public_model_engine_with_options(self, request, runtime):
        """
        You must use FML statements to query information about the data modeling engine when you call this operation.
        *   The information about the data modeling engine can be queried by page, except for data layers, business processes, and data domains. You can add an offset to the end of an FML statement.
        The num LIMIT num statement specifies the offset when the information about the data modeling engine is queried, and the number of pages to return each time. The offset value must be a multiple of the number of pages.
        *   A maximum of 1,000 entries can be returned each time you call the operation.
        

        @param request: QueryPublicModelEngineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryPublicModelEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPublicModelEngine',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryPublicModelEngineResponse(),
            self.call_api(params, req, runtime)
        )

    def query_public_model_engine(self, request):
        """
        You must use FML statements to query information about the data modeling engine when you call this operation.
        *   The information about the data modeling engine can be queried by page, except for data layers, business processes, and data domains. You can add an offset to the end of an FML statement.
        The num LIMIT num statement specifies the offset when the information about the data modeling engine is queried, and the number of pages to return each time. The offset value must be a multiple of the number of pages.
        *   A maximum of 1,000 entries can be returned each time you call the operation.
        

        @param request: QueryPublicModelEngineRequest

        @return: QueryPublicModelEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_public_model_engine_with_options(request, runtime)

    def remove_project_member_from_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_code):
            query['RoleCode'] = request.role_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveProjectMemberFromRole',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_project_member_from_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_project_member_from_role_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def resume_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    def revoke_column_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['Columns'] = request.columns
        if not UtilClient.is_unset(request.max_compute_project_name):
            query['MaxComputeProjectName'] = request.max_compute_project_name
        if not UtilClient.is_unset(request.revoke_user_id):
            query['RevokeUserId'] = request.revoke_user_id
        if not UtilClient.is_unset(request.revoke_user_name):
            query['RevokeUserName'] = request.revoke_user_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeColumnPermission',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeColumnPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_column_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_column_permission_with_options(request, runtime)

    def revoke_table_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actions):
            query['Actions'] = request.actions
        if not UtilClient.is_unset(request.max_compute_project_name):
            query['MaxComputeProjectName'] = request.max_compute_project_name
        if not UtilClient.is_unset(request.revoke_user_id):
            query['RevokeUserId'] = request.revoke_user_id
        if not UtilClient.is_unset(request.revoke_user_name):
            query['RevokeUserName'] = request.revoke_user_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeTablePermission',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeTablePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_table_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_table_permission_with_options(request, runtime)

    def run_cycle_dag_nodes_with_options(self, request, runtime):
        """
        For more information about data backfill, see [Backfill data](~~137937~~).
        

        @param request: RunCycleDagNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunCycleDagNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_begin_time):
            body['BizBeginTime'] = request.biz_begin_time
        if not UtilClient.is_unset(request.biz_end_time):
            body['BizEndTime'] = request.biz_end_time
        if not UtilClient.is_unset(request.end_biz_date):
            body['EndBizDate'] = request.end_biz_date
        if not UtilClient.is_unset(request.exclude_node_ids):
            body['ExcludeNodeIds'] = request.exclude_node_ids
        if not UtilClient.is_unset(request.include_node_ids):
            body['IncludeNodeIds'] = request.include_node_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_params):
            body['NodeParams'] = request.node_params
        if not UtilClient.is_unset(request.parallelism):
            body['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.root_node_id):
            body['RootNodeId'] = request.root_node_id
        if not UtilClient.is_unset(request.start_biz_date):
            body['StartBizDate'] = request.start_biz_date
        if not UtilClient.is_unset(request.start_future_instance_immediately):
            body['StartFutureInstanceImmediately'] = request.start_future_instance_immediately
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCycleDagNodes',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunCycleDagNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def run_cycle_dag_nodes(self, request):
        """
        For more information about data backfill, see [Backfill data](~~137937~~).
        

        @param request: RunCycleDagNodesRequest

        @return: RunCycleDagNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_cycle_dag_nodes_with_options(request, runtime)

    def run_manual_dag_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.dag_parameters):
            body['DagParameters'] = request.dag_parameters
        if not UtilClient.is_unset(request.exclude_node_ids):
            body['ExcludeNodeIds'] = request.exclude_node_ids
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.include_node_ids):
            body['IncludeNodeIds'] = request.include_node_ids
        if not UtilClient.is_unset(request.node_parameters):
            body['NodeParameters'] = request.node_parameters
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunManualDagNodes',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunManualDagNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def run_manual_dag_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_manual_dag_nodes_with_options(request, runtime)

    def run_smoke_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizdate):
            body['Bizdate'] = request.bizdate
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_params):
            body['NodeParams'] = request.node_params
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSmokeTest',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunSmokeTestResponse(),
            self.call_api(params, req, runtime)
        )

    def run_smoke_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_smoke_test_with_options(request, runtime)

    def run_trigger_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.cycle_time):
            body['CycleTime'] = request.cycle_time
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTriggerNode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunTriggerNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def run_trigger_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_trigger_node_with_options(request, runtime)

    def scan_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanSensitiveData',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ScanSensitiveDataResponse(),
            self.call_api(params, req, runtime)
        )

    def scan_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scan_sensitive_data_with_options(request, runtime)

    def search_meta_tables_with_options(self, request, runtime):
        """
        You can call this operation to query only metatables in a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param request: SearchMetaTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchMetaTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_guid):
            query['AppGuid'] = request.app_guid
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMetaTables',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchMetaTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_meta_tables(self, request):
        """
        You can call this operation to query only metatables in a MaxCompute or E-MapReduce (EMR) compute engine instance.
        

        @param request: SearchMetaTablesRequest

        @return: SearchMetaTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_meta_tables_with_options(request, runtime)

    def search_nodes_by_output_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: SearchNodesByOutputRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchNodesByOutputResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outputs):
            body['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchNodesByOutput',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchNodesByOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def search_nodes_by_output(self, request):
        """
        @deprecated
        

        @param request: SearchNodesByOutputRequest

        @return: SearchNodesByOutputResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.search_nodes_by_output_with_options(request, runtime)

    def set_data_source_share_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: SetDataSourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDataSourceShareResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datasource_name):
            query['DatasourceName'] = request.datasource_name
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_permissions):
            query['ProjectPermissions'] = request.project_permissions
        if not UtilClient.is_unset(request.user_permissions):
            query['UserPermissions'] = request.user_permissions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataSourceShare',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetDataSourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_source_share(self, request):
        """
        @deprecated
        

        @param request: SetDataSourceShareRequest

        @return: SetDataSourceShareResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_source_share_with_options(request, runtime)

    def set_success_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSuccessInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetSuccessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def set_success_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_success_instance_with_options(request, runtime)

    def start_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_param):
            query['StartParam'] = request.start_param
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDISyncInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disync_instance_with_options(request, runtime)

    def start_migration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.migration_id):
            body['MigrationId'] = request.migration_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartMigration',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    def start_migration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_migration_with_options(request, runtime)

    def stop_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDISyncInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disync_instance_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def submit_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.skip_all_deploy_file_extensions):
            body['SkipAllDeployFileExtensions'] = request.skip_all_deploy_file_extensions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SubmitFileResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    def suspend_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SuspendInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_instance_with_options(request, runtime)

    def terminate_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateDISyncInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TerminateDISyncInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_disync_instance_with_options(request, runtime)

    def test_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        body = {}
        if not UtilClient.is_unset(request.body_content):
            body['BodyContent'] = request.body_content
        if not UtilClient.is_unset(request.body_params):
            body['BodyParams'] = request.body_params
        if not UtilClient.is_unset(request.head_params):
            body['HeadParams'] = request.head_params
        if not UtilClient.is_unset(request.path_params):
            body['PathParams'] = request.path_params
        if not UtilClient.is_unset(request.query_param):
            body['QueryParam'] = request.query_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TestDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def test_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_data_service_api_with_options(request, runtime)

    def test_network_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datasource_name):
            query['DatasourceName'] = request.datasource_name
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestNetworkConnection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TestNetworkConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def test_network_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_network_connection_with_options(request, runtime)

    def top_ten_elapsed_time_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TopTenElapsedTimeInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def top_ten_elapsed_time_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.top_ten_elapsed_time_instance_with_options(request, runtime)

    def top_ten_error_times_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TopTenErrorTimesInstance',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def top_ten_error_times_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.top_ten_error_times_instance_with_options(request, runtime)

    def umount_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target_id):
            body['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_user_id):
            body['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UmountDirectory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UmountDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def umount_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.umount_directory_with_options(request, runtime)

    def update_baseline_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.UpdateBaselineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_settings):
            request.alert_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_settings, 'AlertSettings', 'json')
        if not UtilClient.is_unset(tmp_req.overtime_settings):
            request.overtime_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.overtime_settings, 'OvertimeSettings', 'json')
        body = {}
        if not UtilClient.is_unset(request.alert_enabled):
            body['AlertEnabled'] = request.alert_enabled
        if not UtilClient.is_unset(request.alert_margin_threshold):
            body['AlertMarginThreshold'] = request.alert_margin_threshold
        if not UtilClient.is_unset(request.alert_settings_shrink):
            body['AlertSettings'] = request.alert_settings_shrink
        if not UtilClient.is_unset(request.baseline_id):
            body['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_name):
            body['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.baseline_type):
            body['BaselineType'] = request.baseline_type
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.overtime_settings_shrink):
            body['OvertimeSettings'] = request.overtime_settings_shrink
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.remove_node_ids):
            body['RemoveNodeIds'] = request.remove_node_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBaseline',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_baseline_with_options(request, runtime)

    def update_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_id):
            body['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBusiness',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def update_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    def update_connection_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: UpdateConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateConnectionResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_id):
            query['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_connection(self, request):
        """
        @deprecated
        

        @param request: UpdateConnectionRequest

        @return: UpdateConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    def update_diproject_config_with_options(self, request, runtime):
        """
        DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization nodes in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](~~199008~~).
        

        @param request: UpdateDIProjectConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDIProjectConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.project_config):
            query['ProjectConfig'] = request.project_config
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDIProjectConfig',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDIProjectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_diproject_config(self, request):
        """
        DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization nodes in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](~~199008~~).
        

        @param request: UpdateDIProjectConfigRequest

        @return: UpdateDIProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_diproject_config_with_options(request, runtime)

    def update_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_content):
            query['TaskContent'] = request.task_content
        if not UtilClient.is_unset(request.task_param):
            query['TaskParam'] = request.task_param
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDISyncTask',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDISyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_disync_task_with_options(request, runtime)

    def update_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_description):
            body['ApiDescription'] = request.api_description
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_path):
            body['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.protocols):
            body['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.registration_details):
            body['RegistrationDetails'] = request.registration_details
        if not UtilClient.is_unset(request.request_method):
            body['RequestMethod'] = request.request_method
        if not UtilClient.is_unset(request.response_content_type):
            body['ResponseContentType'] = request.response_content_type
        if not UtilClient.is_unset(request.script_details):
            body['ScriptDetails'] = request.script_details
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.visible_range):
            body['VisibleRange'] = request.visible_range
        if not UtilClient.is_unset(request.wizard_details):
            body['WizardDetails'] = request.wizard_details
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataServiceApi',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_service_api_with_options(request, runtime)

    def update_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    def update_file_with_options(self, request, runtime):
        """
        When you debug or call this operation, you must specify new values for the specified parameters to ensure that the values are different from the original configurations of the file. For example, if the original value of a parameter is A, you must change the value of this parameter to B before you commit the node. If you set the parameter to A, an exception that indicates invalid data occurs.
        

        @param request: UpdateFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not UtilClient.is_unset(request.auto_parsing):
            body['AutoParsing'] = request.auto_parsing
        if not UtilClient.is_unset(request.auto_rerun_interval_millis):
            body['AutoRerunIntervalMillis'] = request.auto_rerun_interval_millis
        if not UtilClient.is_unset(request.auto_rerun_times):
            body['AutoRerunTimes'] = request.auto_rerun_times
        if not UtilClient.is_unset(request.connection_name):
            body['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.cron_express):
            body['CronExpress'] = request.cron_express
        if not UtilClient.is_unset(request.cycle_type):
            body['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.dependent_node_id_list):
            body['DependentNodeIdList'] = request.dependent_node_id_list
        if not UtilClient.is_unset(request.dependent_type):
            body['DependentType'] = request.dependent_type
        if not UtilClient.is_unset(request.end_effect_date):
            body['EndEffectDate'] = request.end_effect_date
        if not UtilClient.is_unset(request.file_description):
            body['FileDescription'] = request.file_description
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.input_list):
            body['InputList'] = request.input_list
        if not UtilClient.is_unset(request.input_parameters):
            body['InputParameters'] = request.input_parameters
        if not UtilClient.is_unset(request.output_list):
            body['OutputList'] = request.output_list
        if not UtilClient.is_unset(request.output_parameters):
            body['OutputParameters'] = request.output_parameters
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.para_value):
            body['ParaValue'] = request.para_value
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.rerun_mode):
            body['RerunMode'] = request.rerun_mode
        if not UtilClient.is_unset(request.resource_group_identifier):
            body['ResourceGroupIdentifier'] = request.resource_group_identifier
        if not UtilClient.is_unset(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        if not UtilClient.is_unset(request.start_effect_date):
            body['StartEffectDate'] = request.start_effect_date
        if not UtilClient.is_unset(request.start_immediately):
            body['StartImmediately'] = request.start_immediately
        if not UtilClient.is_unset(request.stop):
            body['Stop'] = request.stop
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_file(self, request):
        """
        When you debug or call this operation, you must specify new values for the specified parameters to ensure that the values are different from the original configurations of the file. For example, if the original value of a parameter is A, you must change the value of this parameter to B before you commit the node. If you set the parameter to A, an exception that indicates invalid data occurs.
        

        @param request: UpdateFileRequest

        @return: UpdateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.folder_name):
            body['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_ideevent_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_result):
            body['CheckResult'] = request.check_result
        if not UtilClient.is_unset(request.check_result_tip):
            body['CheckResultTip'] = request.check_result_tip
        if not UtilClient.is_unset(request.extension_code):
            body['ExtensionCode'] = request.extension_code
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIDEEventResult',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateIDEEventResultResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ideevent_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ideevent_result_with_options(request, runtime)

    def update_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetaCategory',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_category_with_options(request, runtime)

    def update_meta_collection_with_options(self, request, runtime):
        """
        Only the name and comment of a collection can be updated.
        

        @param request: UpdateMetaCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMetaCollectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.qualified_name):
            query['QualifiedName'] = request.qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMetaCollection',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meta_collection(self, request):
        """
        Only the name and comment of a collection can be updated.
        

        @param request: UpdateMetaCollectionRequest

        @return: UpdateMetaCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_meta_collection_with_options(request, runtime)

    def update_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption):
            query['Caption'] = request.caption
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.new_owner_id):
            query['NewOwnerId'] = request.new_owner_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        body = {}
        if not UtilClient.is_unset(request.added_labels):
            body['AddedLabels'] = request.added_labels
        if not UtilClient.is_unset(request.removed_labels):
            body['RemovedLabels'] = request.removed_labels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetaTable',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_with_options(request, runtime)

    def update_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetaTableIntroWiki',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_intro_wiki_with_options(request, runtime)

    def update_node_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNodeOwner',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_node_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_node_owner_with_options(request, runtime)

    def update_node_run_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.project_env):
            body['ProjectEnv'] = request.project_env
        if not UtilClient.is_unset(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNodeRunMode',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeRunModeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_node_run_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_node_run_mode_with_options(request, runtime)

    def update_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_mode):
            body['AlarmMode'] = request.alarm_mode
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.follower_id):
            body['FollowerId'] = request.follower_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQualityFollower',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityFollowerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_follower_with_options(request, runtime)

    def update_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_type):
            body['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.checker):
            body['Checker'] = request.checker
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.critical_threshold):
            body['CriticalThreshold'] = request.critical_threshold
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.expect_value):
            body['ExpectValue'] = request.expect_value
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.method_name):
            body['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.open_switch):
            body['OpenSwitch'] = request.open_switch
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.predict_type):
            body['PredictType'] = request.predict_type
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.property_type):
            body['PropertyType'] = request.property_type
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trend):
            body['Trend'] = request.trend
        if not UtilClient.is_unset(request.warning_threshold):
            body['WarningThreshold'] = request.warning_threshold
        if not UtilClient.is_unset(request.where_condition):
            body['WhereCondition'] = request.where_condition
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQualityRule',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_rule_with_options(request, runtime)

    def update_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_interval):
            body['AlertInterval'] = request.alert_interval
        if not UtilClient.is_unset(request.alert_methods):
            body['AlertMethods'] = request.alert_methods
        if not UtilClient.is_unset(request.alert_targets):
            body['AlertTargets'] = request.alert_targets
        if not UtilClient.is_unset(request.alert_unit):
            body['AlertUnit'] = request.alert_unit
        if not UtilClient.is_unset(request.baseline_ids):
            body['BaselineIds'] = request.baseline_ids
        if not UtilClient.is_unset(request.biz_process_ids):
            body['BizProcessIds'] = request.biz_process_ids
        if not UtilClient.is_unset(request.detail):
            body['Detail'] = request.detail
        if not UtilClient.is_unset(request.dnd_end):
            body['DndEnd'] = request.dnd_end
        if not UtilClient.is_unset(request.max_alert_times):
            body['MaxAlertTimes'] = request.max_alert_times
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.remind_id):
            body['RemindId'] = request.remind_id
        if not UtilClient.is_unset(request.remind_name):
            body['RemindName'] = request.remind_name
        if not UtilClient.is_unset(request.remind_type):
            body['RemindType'] = request.remind_type
        if not UtilClient.is_unset(request.remind_unit):
            body['RemindUnit'] = request.remind_unit
        if not UtilClient.is_unset(request.robot_urls):
            body['RobotUrls'] = request.robot_urls
        if not UtilClient.is_unset(request.use_flag):
            body['UseFlag'] = request.use_flag
        if not UtilClient.is_unset(request.webhooks):
            body['Webhooks'] = request.webhooks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRemind',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateRemindResponse(),
            self.call_api(params, req, runtime)
        )

    def update_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_remind_with_options(request, runtime)

    def update_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_guid):
            query['AppGuid'] = request.app_guid
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.create_if_not_exists):
            query['CreateIfNotExists'] = request.create_if_not_exists
        if not UtilClient.is_unset(request.external_table_type):
            query['ExternalTableType'] = request.external_table_type
        if not UtilClient.is_unset(request.has_part):
            query['HasPart'] = request.has_part
        if not UtilClient.is_unset(request.is_view):
            query['IsView'] = request.is_view
        if not UtilClient.is_unset(request.life_cycle):
            query['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.logical_level_id):
            query['LogicalLevelId'] = request.logical_level_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physics_level_id):
            query['PhysicsLevelId'] = request.physics_level_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['Columns'] = request.columns
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.themes):
            body['Themes'] = request.themes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTable',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    def update_table_add_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableAddColumn',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableAddColumnResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table_add_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_add_column_with_options(request, runtime)

    def update_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.level_id):
            query['LevelId'] = request.level_id
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTableLevel',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_level_with_options(request, runtime)

    def update_table_model_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.first_level_theme_id):
            query['FirstLevelThemeId'] = request.first_level_theme_id
        if not UtilClient.is_unset(request.level_id):
            query['LevelId'] = request.level_id
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        if not UtilClient.is_unset(request.second_level_theme_id):
            query['SecondLevelThemeId'] = request.second_level_theme_id
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTableModelInfo',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableModelInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table_model_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_model_info_with_options(request, runtime)

    def update_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTableTheme',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableThemeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_theme_with_options(request, runtime)

    def update_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not UtilClient.is_unset(request.example):
            body['Example'] = request.example
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.function_type):
            body['FunctionType'] = request.function_type
        if not UtilClient.is_unset(request.parameter_description):
            body['ParameterDescription'] = request.parameter_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            body['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        if not UtilClient.is_unset(request.return_value):
            body['ReturnValue'] = request.return_value
        if not UtilClient.is_unset(request.udf_description):
            body['UdfDescription'] = request.udf_description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUdfFile',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateUdfFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)

    def update_workbench_event_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_result):
            query['CheckResult'] = request.check_result
        if not UtilClient.is_unset(request.check_result_tip):
            query['CheckResultTip'] = request.check_result_tip
        if not UtilClient.is_unset(request.extension_code):
            query['ExtensionCode'] = request.extension_code
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkbenchEventResult',
            version='2020-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateWorkbenchEventResultResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workbench_event_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workbench_event_result_with_options(request, runtime)
