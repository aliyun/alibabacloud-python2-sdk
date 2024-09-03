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
        """
        @summary Unpublishes a DataService Studio API.
        

        @param request: AbolishDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AbolishDataServiceApiResponse
        """
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
        """
        @summary Unpublishes a DataService Studio API.
        

        @param request: AbolishDataServiceApiRequest

        @return: AbolishDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abolish_data_service_api_with_options(request, runtime)

    def add_meta_collection_entity_with_options(self, request, runtime):
        """
        @summary Adds an entity to a collection.
        

        @param request: AddMetaCollectionEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddMetaCollectionEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection_qualified_name):
            query['CollectionQualifiedName'] = request.collection_qualified_name
        if not UtilClient.is_unset(request.entity_qualified_name):
            query['EntityQualifiedName'] = request.entity_qualified_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
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
        """
        @summary Adds an entity to a collection.
        

        @param request: AddMetaCollectionEntityRequest

        @return: AddMetaCollectionEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_meta_collection_entity_with_options(request, runtime)

    def add_project_member_to_role_with_options(self, request, runtime):
        """
        @summary Assigns a role to a member of a DataWorks workspace. Before you call this operation, you must add your account to a DataWorks workspace as a member.
        
        @description For information about how to add an account to a DataWorks workspace as a member, see [Manage members and roles](https://help.aliyun.com/document_detail/136941.html).
        

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
        @summary Assigns a role to a member of a DataWorks workspace. Before you call this operation, you must add your account to a DataWorks workspace as a member.
        
        @description For information about how to add an account to a DataWorks workspace as a member, see [Manage members and roles](https://help.aliyun.com/document_detail/136941.html).
        

        @param request: AddProjectMemberToRoleRequest

        @return: AddProjectMemberToRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_project_member_to_role_with_options(request, runtime)

    def add_recognize_rule_with_options(self, request, runtime):
        """
        @summary Adds a sensitive field that is defined based on the category and sensitivity level of data in Data Security Guard.
        

        @param request: AddRecognizeRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddRecognizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.col_exclude):
            body['ColExclude'] = request.col_exclude
        if not UtilClient.is_unset(request.col_scan):
            body['ColScan'] = request.col_scan
        if not UtilClient.is_unset(request.comment_scan):
            body['CommentScan'] = request.comment_scan
        if not UtilClient.is_unset(request.content_scan):
            body['ContentScan'] = request.content_scan
        if not UtilClient.is_unset(request.hit_threshold):
            body['HitThreshold'] = request.hit_threshold
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.level_name):
            body['LevelName'] = request.level_name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_parent):
            body['NodeParent'] = request.node_parent
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.recognize_rules):
            body['RecognizeRules'] = request.recognize_rules
        if not UtilClient.is_unset(request.recognize_rules_type):
            body['RecognizeRulesType'] = request.recognize_rules_type
        if not UtilClient.is_unset(request.sensitive_description):
            body['SensitiveDescription'] = request.sensitive_description
        if not UtilClient.is_unset(request.sensitive_name):
            body['SensitiveName'] = request.sensitive_name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRecognizeRule',
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
            dataworks_public_20200518_models.AddRecognizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_recognize_rule(self, request):
        """
        @summary Adds a sensitive field that is defined based on the category and sensitivity level of data in Data Security Guard.
        

        @param request: AddRecognizeRuleRequest

        @return: AddRecognizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_recognize_rule_with_options(request, runtime)

    def add_to_meta_category_with_options(self, request, runtime):
        """
        @summary Adds a metatable to a specified category.
        

        @param request: AddToMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddToMetaCategoryResponse
        """
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
        """
        @summary Adds a metatable to a specified category.
        

        @param request: AddToMetaCategoryRequest

        @return: AddToMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_to_meta_category_with_options(request, runtime)

    def approve_permission_apply_order_with_options(self, request, runtime):
        """
        @summary Processes a permission request order.
        

        @param request: ApprovePermissionApplyOrderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApprovePermissionApplyOrderResponse
        """
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
        """
        @summary Processes a permission request order.
        

        @param request: ApprovePermissionApplyOrderRequest

        @return: ApprovePermissionApplyOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_permission_apply_order_with_options(request, runtime)

    def callback_extension_with_options(self, request, runtime):
        """
        @summary Sends the processing result of an extension point event by an extension to DataWorks.
        

        @param request: CallbackExtensionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CallbackExtensionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_message):
            body['CheckMessage'] = request.check_message
        if not UtilClient.is_unset(request.check_result):
            body['CheckResult'] = request.check_result
        if not UtilClient.is_unset(request.extension_code):
            body['ExtensionCode'] = request.extension_code
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CallbackExtension',
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
            dataworks_public_20200518_models.CallbackExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def callback_extension(self, request):
        """
        @summary Sends the processing result of an extension point event by an extension to DataWorks.
        

        @param request: CallbackExtensionRequest

        @return: CallbackExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.callback_extension_with_options(request, runtime)

    def change_resource_manager_resource_group_with_options(self, request, runtime):
        """
        @summary Changes the resource group to which a resource belongs.
        

        @param request: ChangeResourceManagerResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChangeResourceManagerResourceGroupResponse
        """
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
        """
        @summary Changes the resource group to which a resource belongs.
        

        @param request: ChangeResourceManagerResourceGroupRequest

        @return: ChangeResourceManagerResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_manager_resource_group_with_options(request, runtime)

    def check_file_deployment_with_options(self, request, runtime):
        """
        @summary Returns the check events of a file. After you commit your file that is created on the DataStudio page, the system checks the file and returns check events before the system deploys the file. You must determine whether the check can be continued based on the events. You can call this operation to return the check events for the file that you want to deploy to DataWorks.
        

        @param request: CheckFileDeploymentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckFileDeploymentResponse
        """
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
        """
        @summary Returns the check events of a file. After you commit your file that is created on the DataStudio page, the system checks the file and returns check events before the system deploys the file. You must determine whether the check can be continued based on the events. You can call this operation to return the check events for the file that you want to deploy to DataWorks.
        

        @param request: CheckFileDeploymentRequest

        @return: CheckFileDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_file_deployment_with_options(request, runtime)

    def check_meta_partition_with_options(self, request, runtime):
        """
        @summary Checks whether a partition in a MaxCompute metatable exists.
        

        @param request: CheckMetaPartitionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckMetaPartitionResponse
        """
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
        """
        @summary Checks whether a partition in a MaxCompute metatable exists.
        

        @param request: CheckMetaPartitionRequest

        @return: CheckMetaPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_meta_partition_with_options(request, runtime)

    def check_meta_table_with_options(self, request, runtime):
        """
        @summary Checks whether a metatable exists.
        

        @param request: CheckMetaTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckMetaTableResponse
        """
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
        """
        @summary Checks whether a metatable exists.
        

        @param request: CheckMetaTableRequest

        @return: CheckMetaTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_with_options(request, runtime)

    def create_baseline_with_options(self, request, runtime):
        """
        @summary Creates a baseline.
        

        @param request: CreateBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBaselineResponse
        """
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
        """
        @summary Creates a baseline.
        

        @param request: CreateBaselineRequest

        @return: CreateBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_baseline_with_options(request, runtime)

    def create_business_with_options(self, request, runtime):
        """

        @param request: CreateBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBusinessResponse
        """
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
        """

        @param request: CreateBusinessRequest

        @return: CreateBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_business_with_options(request, runtime)

    def create_connection_with_options(self, request, runtime):
        """
        @deprecated OpenAPI CreateConnection is deprecated
        
        @summary Adds a data source.
        

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
        @deprecated OpenAPI CreateConnection is deprecated
        
        @summary Adds a data source.
        

        @param request: CreateConnectionRequest

        @return: CreateConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    def create_dialarm_rule_with_options(self, tmp_req, runtime):
        """
        @summary Creates an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param tmp_req: CreateDIAlarmRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.CreateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.notification_settings_shrink):
            body['NotificationSettings'] = request.notification_settings_shrink
        if not UtilClient.is_unset(request.trigger_conditions_shrink):
            body['TriggerConditions'] = request.trigger_conditions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDIAlarmRule',
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
            dataworks_public_20200518_models.CreateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dialarm_rule(self, request):
        """
        @summary Creates an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param request: CreateDIAlarmRuleRequest

        @return: CreateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dialarm_rule_with_options(request, runtime)

    def create_dijob_with_options(self, tmp_req, runtime):
        """
        @summary Creates a synchronization task of a new version in Data Integration. The following types of synchronization tasks are supported: real-time synchronization of all data in a MySQL database to Hologres and batch synchronization of all data in a MySQL database to Hive.
        

        @param tmp_req: CreateDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.CreateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_data_source_settings):
            request.destination_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_data_source_settings, 'DestinationDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.source_data_source_settings):
            request.source_data_source_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_data_source_settings, 'SourceDataSourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.system_debug):
            query['SystemDebug'] = request.system_debug
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_data_source_settings_shrink):
            body['DestinationDataSourceSettings'] = request.destination_data_source_settings_shrink
        if not UtilClient.is_unset(request.destination_data_source_type):
            body['DestinationDataSourceType'] = request.destination_data_source_type
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not UtilClient.is_unset(request.migration_type):
            body['MigrationType'] = request.migration_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not UtilClient.is_unset(request.source_data_source_settings_shrink):
            body['SourceDataSourceSettings'] = request.source_data_source_settings_shrink
        if not UtilClient.is_unset(request.source_data_source_type):
            body['SourceDataSourceType'] = request.source_data_source_type
        if not UtilClient.is_unset(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not UtilClient.is_unset(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDIJob',
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
            dataworks_public_20200518_models.CreateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dijob(self, request):
        """
        @summary Creates a synchronization task of a new version in Data Integration. The following types of synchronization tasks are supported: real-time synchronization of all data in a MySQL database to Hologres and batch synchronization of all data in a MySQL database to Hive.
        

        @param request: CreateDIJobRequest

        @return: CreateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dijob_with_options(request, runtime)

    def create_disync_task_with_options(self, request, runtime):
        """
        @summary Creates a data synchronization task.
        

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
        @summary Creates a data synchronization task.
        

        @param request: CreateDISyncTaskRequest

        @return: CreateDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_disync_task_with_options(request, runtime)

    def create_dag_complement_with_options(self, request, runtime):
        """
        @deprecated OpenAPI CreateDagComplement is deprecated
        

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
        @deprecated OpenAPI CreateDagComplement is deprecated
        

        @param request: CreateDagComplementRequest

        @return: CreateDagComplementResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dag_complement_with_options(request, runtime)

    def create_dag_test_with_options(self, request, runtime):
        """
        @deprecated OpenAPI CreateDagTest is deprecated
        

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
        @deprecated OpenAPI CreateDagTest is deprecated
        

        @param request: CreateDagTestRequest

        @return: CreateDagTestResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dag_test_with_options(request, runtime)

    def create_data_service_api_with_options(self, request, runtime):
        """
        @summary Creates an API.
        

        @param request: CreateDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataServiceApiResponse
        """
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
        if not UtilClient.is_unset(request.request_content_type):
            body['RequestContentType'] = request.request_content_type
        if not UtilClient.is_unset(request.request_method):
            body['RequestMethod'] = request.request_method
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.response_content_type):
            body['ResponseContentType'] = request.response_content_type
        if not UtilClient.is_unset(request.script_details):
            body['ScriptDetails'] = request.script_details
        if not UtilClient.is_unset(request.sql_mode):
            body['SqlMode'] = request.sql_mode
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
        """
        @summary Creates an API.
        

        @param request: CreateDataServiceApiRequest

        @return: CreateDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    def create_data_service_api_authority_with_options(self, request, runtime):
        """
        @summary Grants the access permissions on an API in DataService Studio.
        

        @param request: CreateDataServiceApiAuthorityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataServiceApiAuthorityResponse
        """
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
        """
        @summary Grants the access permissions on an API in DataService Studio.
        

        @param request: CreateDataServiceApiAuthorityRequest

        @return: CreateDataServiceApiAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_authority_with_options(request, runtime)

    def create_data_service_folder_with_options(self, request, runtime):
        """
        @summary Creates a folder in DataService Studio.
        

        @param request: CreateDataServiceFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataServiceFolderResponse
        """
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
        """
        @summary Creates a folder in DataService Studio.
        

        @param request: CreateDataServiceFolderRequest

        @return: CreateDataServiceFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_folder_with_options(request, runtime)

    def create_data_service_group_with_options(self, request, runtime):
        """
        @summary Creates a business process.
        

        @param request: CreateDataServiceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataServiceGroupResponse
        """
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
        """
        @summary Creates a business process.
        

        @param request: CreateDataServiceGroupRequest

        @return: CreateDataServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_group_with_options(request, runtime)

    def create_data_source_with_options(self, request, runtime):
        """
        @summary Adds a data source to DataWorks.
        

        @param request: CreateDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataSourceResponse
        """
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
        """
        @summary Adds a data source to DataWorks.
        

        @param request: CreateDataSourceRequest

        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    def create_export_migration_with_options(self, request, runtime):
        """
        @summary Creates an export task. You can use this operation to create an export task but cannot use this operation to start the created export task.
        

        @param request: CreateExportMigrationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateExportMigrationResponse
        """
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
        """
        @summary Creates an export task. You can use this operation to create an export task but cannot use this operation to start the created export task.
        

        @param request: CreateExportMigrationRequest

        @return: CreateExportMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_export_migration_with_options(request, runtime)

    def create_file_with_options(self, request, runtime):
        """
        @summary Creates a file in DataStudio. You cannot call this operation to create files for Data Integration nodes.
        

        @param request: CreateFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not UtilClient.is_unset(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
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
        if not UtilClient.is_unset(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
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
        if not UtilClient.is_unset(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
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
        """
        @summary Creates a file in DataStudio. You cannot call this operation to create files for Data Integration nodes.
        

        @param request: CreateFileRequest

        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        """
        @summary The operation that you want to perform. Set the value to *CreateFolder**.
        

        @param request: CreateFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFolderResponse
        """
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
        """
        @summary The operation that you want to perform. Set the value to *CreateFolder**.
        

        @param request: CreateFolderRequest

        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_import_migration_with_options(self, request, runtime):
        """
        @summary Creates an import task. The import task contains the import packages of data sources, nodes, and tables.
        
        @description The import package must be uploaded. Example of the upload method:
        Config config = new Config();
        config.setAccessKeyId(accessId);
        config.setAccessKeySecret(accessKey);
        config.setEndpoint(popEndpoint);
        config.setRegionId(regionId);
        
        Client client = new Client(config);
        CreateImportMigrationAdvanceRequest request = new CreateImportMigrationAdvanceRequest();
        request.setName("test_migration_api_" + System.currentTimeMillis());
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
        @summary Creates an import task. The import task contains the import packages of data sources, nodes, and tables.
        
        @description The import package must be uploaded. Example of the upload method:
        Config config = new Config();
        config.setAccessKeyId(accessId);
        config.setAccessKeySecret(accessKey);
        config.setEndpoint(popEndpoint);
        config.setRegionId(regionId);
        
        Client client = new Client(config);
        CreateImportMigrationAdvanceRequest request = new CreateImportMigrationAdvanceRequest();
        request.setName("test_migration_api_" + System.currentTimeMillis());
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
            product='dataworks-public',
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
        @deprecated OpenAPI CreateManualDag is deprecated
        
        @summary Triggers a manually triggered workflow to run. Before you call this operation, make sure that the manually triggered workflow is committed and deployed. You can find the manually triggered workflow on the Operation Center page only after the manually triggered workflow is committed and deployed.
        

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
        @deprecated OpenAPI CreateManualDag is deprecated
        
        @summary Triggers a manually triggered workflow to run. Before you call this operation, make sure that the manually triggered workflow is committed and deployed. You can find the manually triggered workflow on the Operation Center page only after the manually triggered workflow is committed and deployed.
        

        @param request: CreateManualDagRequest

        @return: CreateManualDagResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    def create_meta_category_with_options(self, request, runtime):
        """
        @summary Creates a category.
        

        @param request: CreateMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMetaCategoryResponse
        """
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
        """
        @summary Creates a category.
        

        @param request: CreateMetaCategoryRequest

        @return: CreateMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_meta_category_with_options(request, runtime)

    def create_meta_collection_with_options(self, request, runtime):
        """
        @summary Creates a collection.
        
        @description Collections are classified into various types. The names of collections of the same type must be different.
        

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
        @summary Creates a collection.
        
        @description Collections are classified into various types. The names of collections of the same type must be different.
        

        @param request: CreateMetaCollectionRequest

        @return: CreateMetaCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_meta_collection_with_options(request, runtime)

    def create_permission_apply_order_with_options(self, request, runtime):
        """
        @summary Creates a permission request order.
        

        @param request: CreatePermissionApplyOrderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePermissionApplyOrderResponse
        """
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
        """
        @summary Creates a permission request order.
        

        @param request: CreatePermissionApplyOrderRequest

        @return: CreatePermissionApplyOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_permission_apply_order_with_options(request, runtime)

    def create_project_with_options(self, tmp_req, runtime):
        """
        @summary Creates a DataWorks workspace.
        

        @param tmp_req: CreateProjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_development):
            query['DisableDevelopment'] = request.disable_development
        if not UtilClient.is_unset(request.is_allow_download):
            query['IsAllowDownload'] = request.is_allow_download
        if not UtilClient.is_unset(request.project_description):
            query['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_identifier):
            query['ProjectIdentifier'] = request.project_identifier
        if not UtilClient.is_unset(request.project_mode):
            query['ProjectMode'] = request.project_mode
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
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
            dataworks_public_20200518_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        """
        @summary Creates a DataWorks workspace.
        

        @param request: CreateProjectRequest

        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def create_project_member_with_options(self, request, runtime):
        """
        @summary Adds a user to a DataWorks workspace.
        

        @param request: CreateProjectMemberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProjectMemberResponse
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
        """
        @summary Adds a user to a DataWorks workspace.
        

        @param request: CreateProjectMemberRequest

        @return: CreateProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    def create_quality_entity_with_options(self, request, runtime):
        """
        @summary Creates a partition filter expression.
        

        @param request: CreateQualityEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateQualityEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_level):
            body['EntityLevel'] = request.entity_level
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Creates a partition filter expression.
        

        @param request: CreateQualityEntityRequest

        @return: CreateQualityEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_entity_with_options(request, runtime)

    def create_quality_follower_with_options(self, request, runtime):
        """
        @summary Creates a subscriber for a partition filter expression.
        

        @param request: CreateQualityFollowerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateQualityFollowerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_mode):
            body['AlarmMode'] = request.alarm_mode
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Creates a subscriber for a partition filter expression.
        

        @param request: CreateQualityFollowerRequest

        @return: CreateQualityFollowerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_follower_with_options(request, runtime)

    def create_quality_relative_node_with_options(self, request, runtime):
        """
        @summary Associates a node with a partition filter expression.
        

        @param request: CreateQualityRelativeNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateQualityRelativeNodeResponse
        """
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
        """
        @summary Associates a node with a partition filter expression.
        

        @param request: CreateQualityRelativeNodeRequest

        @return: CreateQualityRelativeNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_relative_node_with_options(request, runtime)

    def create_quality_rule_with_options(self, request, runtime):
        """
        @summary Creates a monitoring rule.
        

        @param request: CreateQualityRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateQualityRuleResponse
        """
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
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        if not UtilClient.is_unset(request.task_setting):
            body['TaskSetting'] = request.task_setting
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
        """
        @summary Creates a monitoring rule.
        

        @param request: CreateQualityRuleRequest

        @return: CreateQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    def create_remind_with_options(self, request, runtime):
        """
        @summary Creates a custom alert rule.
        

        @param request: CreateRemindRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRemindResponse
        """
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
        """
        @summary Creates a custom alert rule.
        

        @param request: CreateRemindRequest

        @return: CreateRemindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_remind_with_options(request, runtime)

    def create_resource_file_with_options(self, request, runtime):
        """
        @summary 支持用户指定自己的文件（比如jar，py，arhive，file等）创建数据开发资源文件
        

        @param request: CreateResourceFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateResourceFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.file_description):
            body['FileDescription'] = request.file_description
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.origin_resource_name):
            body['OriginResourceName'] = request.origin_resource_name
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_to_calc_engine):
            body['RegisterToCalcEngine'] = request.register_to_calc_engine
        if not UtilClient.is_unset(request.resource_file):
            body['ResourceFile'] = request.resource_file
        if not UtilClient.is_unset(request.storage_url):
            body['StorageURL'] = request.storage_url
        if not UtilClient.is_unset(request.upload_mode):
            body['UploadMode'] = request.upload_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceFile',
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
            dataworks_public_20200518_models.CreateResourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_file(self, request):
        """
        @summary 支持用户指定自己的文件（比如jar，py，arhive，file等）创建数据开发资源文件
        

        @param request: CreateResourceFileRequest

        @return: CreateResourceFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_file_with_options(request, runtime)

    def create_resource_file_advance(self, request, runtime):
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
            product='dataworks-public',
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
        create_resource_file_req = dataworks_public_20200518_models.CreateResourceFileRequest()
        OpenApiUtilClient.convert(request, create_resource_file_req)
        if not UtilClient.is_unset(request.resource_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.resource_file_object,
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
            create_resource_file_req.resource_file = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        create_resource_file_resp = self.create_resource_file_with_options(create_resource_file_req, runtime)
        return create_resource_file_resp

    def create_table_with_options(self, request, runtime):
        """
        @summary Creates a MaxCompute table or view.
        

        @param request: CreateTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTableResponse
        """
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
        """
        @summary Creates a MaxCompute table or view.
        

        @param request: CreateTableRequest

        @return: CreateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    def create_table_level_with_options(self, request, runtime):
        """
        @summary Creates a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: CreateTableLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTableLevelResponse
        """
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
        """
        @summary Creates a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: CreateTableLevelRequest

        @return: CreateTableLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_table_level_with_options(request, runtime)

    def create_table_theme_with_options(self, request, runtime):
        """
        @summary Creates a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: CreateTableThemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTableThemeResponse
        """
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
        """
        @summary Creates a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: CreateTableThemeRequest

        @return: CreateTableThemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_table_theme_with_options(request, runtime)

    def create_udf_file_with_options(self, request, runtime):
        """

        @param request: CreateUdfFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUdfFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.cmd_description):
            body['CmdDescription'] = request.cmd_description
        if not UtilClient.is_unset(request.create_folder_if_not_exists):
            body['CreateFolderIfNotExists'] = request.create_folder_if_not_exists
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
        """

        @param request: CreateUdfFileRequest

        @return: CreateUdfFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    def delete_baseline_with_options(self, request, runtime):
        """
        @summary Deletes a baseline based on its ID. You can delete a baseline only if the nodes in the baseline does not have ancestor nodes. You can call the UpdateBaseline operation to delete the relationships between the nodes and their ancestor nodes.
        

        @param request: DeleteBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBaselineResponse
        """
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
        """
        @summary Deletes a baseline based on its ID. You can delete a baseline only if the nodes in the baseline does not have ancestor nodes. You can call the UpdateBaseline operation to delete the relationships between the nodes and their ancestor nodes.
        

        @param request: DeleteBaselineRequest

        @return: DeleteBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_baseline_with_options(request, runtime)

    def delete_business_with_options(self, request, runtime):
        """

        @param request: DeleteBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBusinessResponse
        """
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
        """

        @param request: DeleteBusinessRequest

        @return: DeleteBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    def delete_connection_with_options(self, request, runtime):
        """
        @deprecated OpenAPI DeleteConnection is deprecated
        
        @summary Removes a data source.
        

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
        @deprecated OpenAPI DeleteConnection is deprecated
        
        @summary Removes a data source.
        

        @param request: DeleteConnectionRequest

        @return: DeleteConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    def delete_dialarm_rule_with_options(self, request, runtime):
        """
        @summary Deletes an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks whose MigrationType is set to RealtimeIncremental.
        

        @param request: DeleteDIAlarmRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDIAlarmRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialarm_rule_id):
            body['DIAlarmRuleId'] = request.dialarm_rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDIAlarmRule',
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
            dataworks_public_20200518_models.DeleteDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dialarm_rule(self, request):
        """
        @summary Deletes an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks whose MigrationType is set to RealtimeIncremental.
        

        @param request: DeleteDIAlarmRuleRequest

        @return: DeleteDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dialarm_rule_with_options(request, runtime)

    def delete_dijob_with_options(self, request, runtime):
        """
        @summary Deletes a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        

        @param request: DeleteDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDIJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDIJob',
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
            dataworks_public_20200518_models.DeleteDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dijob(self, request):
        """
        @summary Deletes a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        

        @param request: DeleteDIJobRequest

        @return: DeleteDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dijob_with_options(request, runtime)

    def delete_disync_task_with_options(self, request, runtime):
        """
        @summary Deletes a synchronization task. You can call this operation to delete only a real-time synchronization task.
        
        @description If you want to delete a batch synchronization task, call the DeleteFile operation. For more information, see [Delete a synchronization task](https://help.aliyun.com/document_detail/321443.html).
        

        @param request: DeleteDISyncTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDISyncTaskResponse
        """
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
        """
        @summary Deletes a synchronization task. You can call this operation to delete only a real-time synchronization task.
        
        @description If you want to delete a batch synchronization task, call the DeleteFile operation. For more information, see [Delete a synchronization task](https://help.aliyun.com/document_detail/321443.html).
        

        @param request: DeleteDISyncTaskRequest

        @return: DeleteDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_disync_task_with_options(request, runtime)

    def delete_data_service_api_with_options(self, request, runtime):
        """
        @summary Deletes an API in DataService Studio.
        

        @param request: DeleteDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataServiceApiResponse
        """
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
        """
        @summary Deletes an API in DataService Studio.
        

        @param request: DeleteDataServiceApiRequest

        @return: DeleteDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_with_options(request, runtime)

    def delete_data_service_api_authority_with_options(self, request, runtime):
        """
        @summary Revokes the access permissions on an API.
        

        @param request: DeleteDataServiceApiAuthorityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataServiceApiAuthorityResponse
        """
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
        """
        @summary Revokes the access permissions on an API.
        

        @param request: DeleteDataServiceApiAuthorityRequest

        @return: DeleteDataServiceApiAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_authority_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        """
        @summary Removes a data source.
        

        @param request: DeleteDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataSourceResponse
        """
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
        """
        @summary Removes a data source.
        

        @param request: DeleteDataSourceRequest

        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        """
        @summary Deletes a file from DataStudio. If the file has been committed, an asynchronous process is triggered to delete the file in the scheduling system. The value of the DeploymentId parameter returned is used to call the GetDeployment operation to poll the status of the asynchronous process.
        

        @param request: DeleteFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFileResponse
        """
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
        """
        @summary Deletes a file from DataStudio. If the file has been committed, an asynchronous process is triggered to delete the file in the scheduling system. The value of the DeploymentId parameter returned is used to call the GetDeployment operation to poll the status of the asynchronous process.
        

        @param request: DeleteFileRequest

        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        """

        @param request: DeleteFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFolderResponse
        """
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
        """

        @param request: DeleteFolderRequest

        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_from_meta_category_with_options(self, request, runtime):
        """
        @summary Removes a table from a specified category.
        

        @param request: DeleteFromMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFromMetaCategoryResponse
        """
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
        """
        @summary Removes a table from a specified category.
        

        @param request: DeleteFromMetaCategoryRequest

        @return: DeleteFromMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_from_meta_category_with_options(request, runtime)

    def delete_lineage_relation_with_options(self, request, runtime):
        """
        @summary Deletes the lineage between entities. You can call this operation to delete only custom lineages that are registered by users.
        
        @description This operation is in the trial phase. Users who need to call this operation can apply for it. The users can call this operation after the administrator adds the users to the trial list.
        

        @param request: DeleteLineageRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLineageRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_entity_qualified_name):
            query['DestEntityQualifiedName'] = request.dest_entity_qualified_name
        if not UtilClient.is_unset(request.relationship_guid):
            query['RelationshipGuid'] = request.relationship_guid
        if not UtilClient.is_unset(request.relationship_type):
            query['RelationshipType'] = request.relationship_type
        if not UtilClient.is_unset(request.src_entity_qualified_name):
            query['SrcEntityQualifiedName'] = request.src_entity_qualified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLineageRelation',
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
            dataworks_public_20200518_models.DeleteLineageRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_lineage_relation(self, request):
        """
        @summary Deletes the lineage between entities. You can call this operation to delete only custom lineages that are registered by users.
        
        @description This operation is in the trial phase. Users who need to call this operation can apply for it. The users can call this operation after the administrator adds the users to the trial list.
        

        @param request: DeleteLineageRelationRequest

        @return: DeleteLineageRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lineage_relation_with_options(request, runtime)

    def delete_meta_category_with_options(self, request, runtime):
        """
        @summary Deletes a category.
        

        @param request: DeleteMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMetaCategoryResponse
        """
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
        """
        @summary Deletes a category.
        

        @param request: DeleteMetaCategoryRequest

        @return: DeleteMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_category_with_options(request, runtime)

    def delete_meta_collection_with_options(self, request, runtime):
        """
        @summary Deletes a collection.
        

        @param request: DeleteMetaCollectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMetaCollectionResponse
        """
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
        """
        @summary Deletes a collection.
        

        @param request: DeleteMetaCollectionRequest

        @return: DeleteMetaCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_collection_with_options(request, runtime)

    def delete_meta_collection_entity_with_options(self, request, runtime):
        """
        @summary Deletes an entity from a collection.
        

        @param request: DeleteMetaCollectionEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMetaCollectionEntityResponse
        """
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
        """
        @summary Deletes an entity from a collection.
        

        @param request: DeleteMetaCollectionEntityRequest

        @return: DeleteMetaCollectionEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_collection_entity_with_options(request, runtime)

    def delete_project_member_with_options(self, request, runtime):
        """
        @summary Removes a user from a DataWorks workspace.
        

        @param request: DeleteProjectMemberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteProjectMemberResponse
        """
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
        """
        @summary Removes a user from a DataWorks workspace.
        

        @param request: DeleteProjectMemberRequest

        @return: DeleteProjectMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    def delete_quality_entity_with_options(self, request, runtime):
        """
        @summary Deletes a partition filter expression.
        

        @param request: DeleteQualityEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQualityEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Deletes a partition filter expression.
        

        @param request: DeleteQualityEntityRequest

        @return: DeleteQualityEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_entity_with_options(request, runtime)

    def delete_quality_follower_with_options(self, request, runtime):
        """
        @summary Deletes a subscriber of a partition filter expression.
        
        @description In Data Quality, you must configure monitoring rules based on a partition filter expression. Data Quality uses these rules to detect changes in source data and dirty data generated during the process of extract, transform, and load (ETL). This way, you can prevent tasks from producing unexpected dirty data that affects the smooth running of tasks and business decision-making. You can go to the Manage Subscriptions page to add subscribers for a partition filter expression. When the monitoring rule that is created based on the partition filter expression is triggered, the subscribers can receive notifications and troubleshoot errors at the earliest opportunity. For more information, see [Configure monitoring rules](https://help.aliyun.com/document_detail/73690.html).
        

        @param request: DeleteQualityFollowerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQualityFollowerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.follower_id):
            body['FollowerId'] = request.follower_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        @summary Deletes a subscriber of a partition filter expression.
        
        @description In Data Quality, you must configure monitoring rules based on a partition filter expression. Data Quality uses these rules to detect changes in source data and dirty data generated during the process of extract, transform, and load (ETL). This way, you can prevent tasks from producing unexpected dirty data that affects the smooth running of tasks and business decision-making. You can go to the Manage Subscriptions page to add subscribers for a partition filter expression. When the monitoring rule that is created based on the partition filter expression is triggered, the subscribers can receive notifications and troubleshoot errors at the earliest opportunity. For more information, see [Configure monitoring rules](https://help.aliyun.com/document_detail/73690.html).
        

        @param request: DeleteQualityFollowerRequest

        @return: DeleteQualityFollowerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_follower_with_options(request, runtime)

    def delete_quality_relative_node_with_options(self, request, runtime):
        """

        @param request: DeleteQualityRelativeNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQualityRelativeNodeResponse
        """
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
        """

        @param request: DeleteQualityRelativeNodeRequest

        @return: DeleteQualityRelativeNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_relative_node_with_options(request, runtime)

    def delete_quality_rule_with_options(self, request, runtime):
        """
        @summary Deletes a monitoring rule.
        

        @param request: DeleteQualityRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Deletes a monitoring rule.
        

        @param request: DeleteQualityRuleRequest

        @return: DeleteQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    def delete_recognize_rule_with_options(self, request, runtime):
        """
        @summary Deletes sensitive field types.
        

        @param request: DeleteRecognizeRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRecognizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sensitive_id):
            body['SensitiveId'] = request.sensitive_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRecognizeRule',
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
            dataworks_public_20200518_models.DeleteRecognizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_recognize_rule(self, request):
        """
        @summary Deletes sensitive field types.
        

        @param request: DeleteRecognizeRuleRequest

        @return: DeleteRecognizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_recognize_rule_with_options(request, runtime)

    def delete_remind_with_options(self, request, runtime):
        """
        @summary Deletes a custom alert rule.
        

        @param request: DeleteRemindRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRemindResponse
        """
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
        """
        @summary Deletes a custom alert rule.
        

        @param request: DeleteRemindRequest

        @return: DeleteRemindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_remind_with_options(request, runtime)

    def delete_table_with_options(self, request, runtime):
        """

        @param request: DeleteTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableResponse
        """
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
        """

        @param request: DeleteTableRequest

        @return: DeleteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    def delete_table_level_with_options(self, request, runtime):
        """
        @summary Deletes a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: DeleteTableLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableLevelResponse
        """
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
        """
        @summary Deletes a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: DeleteTableLevelRequest

        @return: DeleteTableLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_table_level_with_options(request, runtime)

    def delete_table_theme_with_options(self, request, runtime):
        """
        @summary Deletes a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: DeleteTableThemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTableThemeResponse
        """
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
        """
        @summary Deletes a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: DeleteTableThemeRequest

        @return: DeleteTableThemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_table_theme_with_options(request, runtime)

    def deploy_disync_task_with_options(self, request, runtime):
        """
        @summary Deploys a real-time synchronization task.
        

        @param request: DeployDISyncTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeployDISyncTaskResponse
        """
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
        """
        @summary Deploys a real-time synchronization task.
        

        @param request: DeployDISyncTaskRequest

        @return: DeployDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_disync_task_with_options(request, runtime)

    def deploy_file_with_options(self, request, runtime):
        """
        @summary Deploys a file to the production environment.
        

        @param request: DeployFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeployFileResponse
        """
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
        """
        @summary Deploys a file to the production environment.
        

        @param request: DeployFileRequest

        @return: DeployFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    def desensitize_data_with_options(self, request, runtime):
        """
        @summary Masks data.
        

        @param request: DesensitizeDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DesensitizeDataResponse
        """
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
        """
        @summary Masks data.
        

        @param request: DesensitizeDataRequest

        @return: DesensitizeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.desensitize_data_with_options(request, runtime)

    def dsg_desens_plan_add_or_update_with_options(self, tmp_req, runtime):
        """
        @summary Adds or modifies a data masking rule.
        

        @param tmp_req: DsgDesensPlanAddOrUpdateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgDesensPlanAddOrUpdateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgDesensPlanAddOrUpdateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.desens_rules):
            request.desens_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.desens_rules, 'DesensRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.desens_rules_shrink):
            query['DesensRules'] = request.desens_rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgDesensPlanAddOrUpdate',
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
            dataworks_public_20200518_models.DsgDesensPlanAddOrUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_desens_plan_add_or_update(self, request):
        """
        @summary Adds or modifies a data masking rule.
        

        @param request: DsgDesensPlanAddOrUpdateRequest

        @return: DsgDesensPlanAddOrUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_desens_plan_add_or_update_with_options(request, runtime)

    def dsg_desens_plan_delete_with_options(self, tmp_req, runtime):
        """
        @summary Deletes a data masking rule created in Data Security Guard.
        

        @param tmp_req: DsgDesensPlanDeleteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgDesensPlanDeleteResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgDesensPlanDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgDesensPlanDelete',
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
            dataworks_public_20200518_models.DsgDesensPlanDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_desens_plan_delete(self, request):
        """
        @summary Deletes a data masking rule created in Data Security Guard.
        

        @param request: DsgDesensPlanDeleteRequest

        @return: DsgDesensPlanDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_desens_plan_delete_with_options(request, runtime)

    def dsg_desens_plan_query_list_with_options(self, request, runtime):
        """
        @summary Queries a list of data masking rules.
        

        @param request: DsgDesensPlanQueryListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgDesensPlanQueryListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgDesensPlanQueryList',
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
            dataworks_public_20200518_models.DsgDesensPlanQueryListResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_desens_plan_query_list(self, request):
        """
        @summary Queries a list of data masking rules.
        

        @param request: DsgDesensPlanQueryListRequest

        @return: DsgDesensPlanQueryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_desens_plan_query_list_with_options(request, runtime)

    def dsg_desens_plan_update_status_with_options(self, tmp_req, runtime):
        """
        @summary Modifies the status of a data masking rule.
        

        @param tmp_req: DsgDesensPlanUpdateStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgDesensPlanUpdateStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgDesensPlanUpdateStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgDesensPlanUpdateStatus',
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
            dataworks_public_20200518_models.DsgDesensPlanUpdateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_desens_plan_update_status(self, request):
        """
        @summary Modifies the status of a data masking rule.
        

        @param request: DsgDesensPlanUpdateStatusRequest

        @return: DsgDesensPlanUpdateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_desens_plan_update_status_with_options(request, runtime)

    def dsg_platform_query_projects_and_schema_from_meta_with_options(self, request, runtime):
        """
        @summary Queries a list of compute engines of different types in the current tenant.
        

        @param request: DsgPlatformQueryProjectsAndSchemaFromMetaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgPlatformQueryProjectsAndSchemaFromMetaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgPlatformQueryProjectsAndSchemaFromMeta',
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
            dataworks_public_20200518_models.DsgPlatformQueryProjectsAndSchemaFromMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_platform_query_projects_and_schema_from_meta(self, request):
        """
        @summary Queries a list of compute engines of different types in the current tenant.
        

        @param request: DsgPlatformQueryProjectsAndSchemaFromMetaRequest

        @return: DsgPlatformQueryProjectsAndSchemaFromMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_platform_query_projects_and_schema_from_meta_with_options(request, runtime)

    def dsg_query_default_templates_with_options(self, request, runtime):
        """
        @summary Queries a list of available sensitive field type templates and the data masking rules supported by the templates. You can refer to the response parameters of this operation to configure a data masking rule.
        

        @param request: DsgQueryDefaultTemplatesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgQueryDefaultTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgQueryDefaultTemplates',
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
            dataworks_public_20200518_models.DsgQueryDefaultTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_query_default_templates(self, request):
        """
        @summary Queries a list of available sensitive field type templates and the data masking rules supported by the templates. You can refer to the response parameters of this operation to configure a data masking rule.
        

        @param request: DsgQueryDefaultTemplatesRequest

        @return: DsgQueryDefaultTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_query_default_templates_with_options(request, runtime)

    def dsg_query_sens_result_with_options(self, request, runtime):
        """
        @summary Queries the identification results of sensitive data.
        
        @description The query capability of the API operation is similar to the query feature in Data Security Guard in the DataWorks console. The API operation can be used to query the identification results of sensitive data of a tenant based on the association with the tenant ID.
        You can search for a specific identification result based on filter conditions such as data source type and workspace.
        You can sort the identification results of sensitive data of a tenant based on the values of a field in ascending or descending order.
        This operation supports paged query.
        

        @param request: DsgQuerySensResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgQuerySensResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.col):
            body['Col'] = request.col
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.schema_name):
            body['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.sens_status):
            body['SensStatus'] = request.sens_status
        if not UtilClient.is_unset(request.sensitive_id):
            body['SensitiveId'] = request.sensitive_id
        if not UtilClient.is_unset(request.sensitive_name):
            body['SensitiveName'] = request.sensitive_name
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DsgQuerySensResult',
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
            dataworks_public_20200518_models.DsgQuerySensResultResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_query_sens_result(self, request):
        """
        @summary Queries the identification results of sensitive data.
        
        @description The query capability of the API operation is similar to the query feature in Data Security Guard in the DataWorks console. The API operation can be used to query the identification results of sensitive data of a tenant based on the association with the tenant ID.
        You can search for a specific identification result based on filter conditions such as data source type and workspace.
        You can sort the identification results of sensitive data of a tenant based on the values of a field in ascending or descending order.
        This operation supports paged query.
        

        @param request: DsgQuerySensResultRequest

        @return: DsgQuerySensResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_query_sens_result_with_options(request, runtime)

    def dsg_run_sens_identify_with_options(self, tmp_req, runtime):
        """
        @summary Starts a sensitive data identification task in Data Security Guard.
        

        @param tmp_req: DsgRunSensIdentifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgRunSensIdentifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgRunSensIdentifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.es_meta_params):
            request.es_meta_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.es_meta_params, 'EsMetaParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.es_meta_params_shrink):
            body['EsMetaParams'] = request.es_meta_params_shrink
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DsgRunSensIdentify',
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
            dataworks_public_20200518_models.DsgRunSensIdentifyResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_run_sens_identify(self, request):
        """
        @summary Starts a sensitive data identification task in Data Security Guard.
        

        @param request: DsgRunSensIdentifyRequest

        @return: DsgRunSensIdentifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_run_sens_identify_with_options(request, runtime)

    def dsg_scene_add_or_update_scene_with_options(self, tmp_req, runtime):
        """
        @summary Adds or modifies a level-2 data masking scenario.
        

        @param tmp_req: DsgSceneAddOrUpdateSceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgSceneAddOrUpdateSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgSceneAddOrUpdateSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'scenes', 'json')
        query = {}
        if not UtilClient.is_unset(request.scenes_shrink):
            query['scenes'] = request.scenes_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgSceneAddOrUpdateScene',
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
            dataworks_public_20200518_models.DsgSceneAddOrUpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_scene_add_or_update_scene(self, request):
        """
        @summary Adds or modifies a level-2 data masking scenario.
        

        @param request: DsgSceneAddOrUpdateSceneRequest

        @return: DsgSceneAddOrUpdateSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_scene_add_or_update_scene_with_options(request, runtime)

    def dsg_scene_query_scene_list_by_name_with_options(self, request, runtime):
        """
        @summary Queries a list of data masking scenarios.
        

        @param request: DsgSceneQuerySceneListByNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgSceneQuerySceneListByNameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgSceneQuerySceneListByName',
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
            dataworks_public_20200518_models.DsgSceneQuerySceneListByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_scene_query_scene_list_by_name(self, request):
        """
        @summary Queries a list of data masking scenarios.
        

        @param request: DsgSceneQuerySceneListByNameRequest

        @return: DsgSceneQuerySceneListByNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_scene_query_scene_list_by_name_with_options(request, runtime)

    def dsg_scened_delete_scene_with_options(self, tmp_req, runtime):
        """
        @summary Deletes a level-2 data masking scenario created in Data Security Guard.
        

        @param tmp_req: DsgScenedDeleteSceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgScenedDeleteSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgScenedDeleteSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgScenedDeleteScene',
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
            dataworks_public_20200518_models.DsgScenedDeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_scened_delete_scene(self, request):
        """
        @summary Deletes a level-2 data masking scenario created in Data Security Guard.
        

        @param request: DsgScenedDeleteSceneRequest

        @return: DsgScenedDeleteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_scened_delete_scene_with_options(request, runtime)

    def dsg_stop_sens_identify_with_options(self, request, runtime):
        """
        @summary Stops a sensitive data identification task.
        

        @param request: DsgStopSensIdentifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgStopSensIdentifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DsgStopSensIdentify',
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
            dataworks_public_20200518_models.DsgStopSensIdentifyResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_stop_sens_identify(self, request):
        """
        @summary Stops a sensitive data identification task.
        

        @param request: DsgStopSensIdentifyRequest

        @return: DsgStopSensIdentifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_stop_sens_identify_with_options(request, runtime)

    def dsg_user_group_add_or_update_with_options(self, tmp_req, runtime):
        """
        @summary Adds or modifies a user group.
        

        @param tmp_req: DsgUserGroupAddOrUpdateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgUserGroupAddOrUpdateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgUserGroupAddOrUpdateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_groups):
            request.user_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_groups, 'UserGroups', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_groups_shrink):
            query['UserGroups'] = request.user_groups_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgUserGroupAddOrUpdate',
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
            dataworks_public_20200518_models.DsgUserGroupAddOrUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_user_group_add_or_update(self, request):
        """
        @summary Adds or modifies a user group.
        

        @param request: DsgUserGroupAddOrUpdateRequest

        @return: DsgUserGroupAddOrUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_user_group_add_or_update_with_options(request, runtime)

    def dsg_user_group_delete_with_options(self, tmp_req, runtime):
        """
        @summary Deletes a user group configured in Data Security Guard.
        

        @param tmp_req: DsgUserGroupDeleteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgUserGroupDeleteResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgUserGroupDeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgUserGroupDelete',
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
            dataworks_public_20200518_models.DsgUserGroupDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_user_group_delete(self, request):
        """
        @summary Deletes a user group configured in Data Security Guard.
        

        @param request: DsgUserGroupDeleteRequest

        @return: DsgUserGroupDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_user_group_delete_with_options(request, runtime)

    def dsg_user_group_get_odps_role_groups_with_options(self, request, runtime):
        """
        @summary Queries a list of MaxCompute roles that can be selected by the members of a user group when the user group is created or modified by the tenant in Data Security Guard.
        

        @param request: DsgUserGroupGetOdpsRoleGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgUserGroupGetOdpsRoleGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgUserGroupGetOdpsRoleGroups',
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
            dataworks_public_20200518_models.DsgUserGroupGetOdpsRoleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_user_group_get_odps_role_groups(self, request):
        """
        @summary Queries a list of MaxCompute roles that can be selected by the members of a user group when the user group is created or modified by the tenant in Data Security Guard.
        

        @param request: DsgUserGroupGetOdpsRoleGroupsRequest

        @return: DsgUserGroupGetOdpsRoleGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_user_group_get_odps_role_groups_with_options(request, runtime)

    def dsg_user_group_query_list_with_options(self, request, runtime):
        """
        @summary Queries a list of user groups in Data Security Guard.
        

        @param request: DsgUserGroupQueryListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgUserGroupQueryListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgUserGroupQueryList',
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
            dataworks_public_20200518_models.DsgUserGroupQueryListResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_user_group_query_list(self, request):
        """
        @summary Queries a list of user groups in Data Security Guard.
        

        @param request: DsgUserGroupQueryListRequest

        @return: DsgUserGroupQueryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_user_group_query_list_with_options(request, runtime)

    def dsg_user_group_query_user_list_with_options(self, runtime):
        """
        @summary Queries a list of users or roles of the current tenant.
        

        @param request: DsgUserGroupQueryUserListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgUserGroupQueryUserListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DsgUserGroupQueryUserList',
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
            dataworks_public_20200518_models.DsgUserGroupQueryUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_user_group_query_user_list(self):
        """
        @summary Queries a list of users or roles of the current tenant.
        

        @return: DsgUserGroupQueryUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_user_group_query_user_list_with_options(runtime)

    def dsg_white_list_add_or_update_with_options(self, tmp_req, runtime):
        """
        @summary Adds or modifies a data masking whitelist.
        

        @param tmp_req: DsgWhiteListAddOrUpdateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgWhiteListAddOrUpdateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgWhiteListAddOrUpdateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.white_lists):
            request.white_lists_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.white_lists, 'WhiteLists', 'json')
        query = {}
        if not UtilClient.is_unset(request.white_lists_shrink):
            query['WhiteLists'] = request.white_lists_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgWhiteListAddOrUpdate',
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
            dataworks_public_20200518_models.DsgWhiteListAddOrUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_white_list_add_or_update(self, request):
        """
        @summary Adds or modifies a data masking whitelist.
        

        @param request: DsgWhiteListAddOrUpdateRequest

        @return: DsgWhiteListAddOrUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_white_list_add_or_update_with_options(request, runtime)

    def dsg_white_list_delete_list_with_options(self, tmp_req, runtime):
        """
        @summary Deletes a data masking whitelist configured in Data Security Guard.
        

        @param tmp_req: DsgWhiteListDeleteListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgWhiteListDeleteListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.DsgWhiteListDeleteListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgWhiteListDeleteList',
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
            dataworks_public_20200518_models.DsgWhiteListDeleteListResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_white_list_delete_list(self, request):
        """
        @summary Deletes a data masking whitelist configured in Data Security Guard.
        

        @param request: DsgWhiteListDeleteListRequest

        @return: DsgWhiteListDeleteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_white_list_delete_list_with_options(request, runtime)

    def dsg_white_list_query_list_with_options(self, request, runtime):
        """
        @summary Queries a data masking whitelist.
        

        @param request: DsgWhiteListQueryListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DsgWhiteListQueryListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DsgWhiteListQueryList',
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
            dataworks_public_20200518_models.DsgWhiteListQueryListResponse(),
            self.call_api(params, req, runtime)
        )

    def dsg_white_list_query_list(self, request):
        """
        @summary Queries a data masking whitelist.
        

        @param request: DsgWhiteListQueryListRequest

        @return: DsgWhiteListQueryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dsg_white_list_query_list_with_options(request, runtime)

    def edit_recognize_rule_with_options(self, request, runtime):
        """
        @summary Edits a sensitive field that is defined based on the category and sensitivity level of data in Data Security Guard.
        

        @param request: EditRecognizeRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EditRecognizeRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.col_exclude):
            body['ColExclude'] = request.col_exclude
        if not UtilClient.is_unset(request.col_scan):
            body['ColScan'] = request.col_scan
        if not UtilClient.is_unset(request.comment_scan):
            body['CommentScan'] = request.comment_scan
        if not UtilClient.is_unset(request.content_scan):
            body['ContentScan'] = request.content_scan
        if not UtilClient.is_unset(request.hit_threshold):
            body['HitThreshold'] = request.hit_threshold
        if not UtilClient.is_unset(request.level_name):
            body['LevelName'] = request.level_name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_parent):
            body['NodeParent'] = request.node_parent
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.recognize_rules):
            body['RecognizeRules'] = request.recognize_rules
        if not UtilClient.is_unset(request.recognize_rules_type):
            body['RecognizeRulesType'] = request.recognize_rules_type
        if not UtilClient.is_unset(request.sensitive_description):
            body['SensitiveDescription'] = request.sensitive_description
        if not UtilClient.is_unset(request.sensitive_id):
            body['SensitiveId'] = request.sensitive_id
        if not UtilClient.is_unset(request.sensitive_name):
            body['SensitiveName'] = request.sensitive_name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditRecognizeRule',
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
            dataworks_public_20200518_models.EditRecognizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_recognize_rule(self, request):
        """
        @summary Edits a sensitive field that is defined based on the category and sensitivity level of data in Data Security Guard.
        

        @param request: EditRecognizeRuleRequest

        @return: EditRecognizeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_recognize_rule_with_options(request, runtime)

    def establish_relation_table_to_business_with_options(self, request, runtime):
        """

        @param request: EstablishRelationTableToBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EstablishRelationTableToBusinessResponse
        """
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
        """

        @param request: EstablishRelationTableToBusinessRequest

        @return: EstablishRelationTableToBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    def export_data_sources_with_options(self, request, runtime):
        """
        @summary Exports a list of data sources.
        

        @param request: ExportDataSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportDataSourcesResponse
        """
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
        """
        @summary Exports a list of data sources.
        

        @param request: ExportDataSourcesRequest

        @return: ExportDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_data_sources_with_options(request, runtime)

    def generate_disync_task_config_for_creating_with_options(self, request, runtime):
        """
        @summary Generates an ID for an asynchronous thread that is used to create a synchronization task in Data Integration.
        
        @description DataWorks allows you to use the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to directly create a batch synchronization task in Data Integration. To create a real-time synchronization task or another type of synchronization task, you must first call the [GenerateDISyncTaskConfigForCreating](https://help.aliyun.com/document_detail/383463.html) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can use the parameters as request parameters of [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) and call the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to create a real-time synchronization task or another type of synchronization task. DataWorks allows you to create real-time synchronization tasks and other types of synchronization tasks in Data Integration only in asynchronous mode.
        

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
        @summary Generates an ID for an asynchronous thread that is used to create a synchronization task in Data Integration.
        
        @description DataWorks allows you to use the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to directly create a batch synchronization task in Data Integration. To create a real-time synchronization task or another type of synchronization task, you must first call the [GenerateDISyncTaskConfigForCreating](https://help.aliyun.com/document_detail/383463.html) operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can use the parameters as request parameters of [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) and call the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to create a real-time synchronization task or another type of synchronization task. DataWorks allows you to create real-time synchronization tasks and other types of synchronization tasks in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForCreatingRequest

        @return: GenerateDISyncTaskConfigForCreatingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_creating_with_options(request, runtime)

    def generate_disync_task_config_for_updating_with_options(self, request, runtime):
        """
        @summary Generates the JSON for an asynchronous thread that is used to update a real-time synchronization task in Data Integration.
        
        @description DataWorks allows you to use only the [UpdateDISyncTask](https://help.aliyun.com/document_detail/289109.html) operation to update a batch synchronization task in Data Integration. To update a real-time synchronization task, you must first call the GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the UpdateDISyncTask operation and use the parameters as request parameters to update a real-time synchronization task in Data Integration. DataWorks allows you to create or update real-time synchronization tasks in Data Integration only in asynchronous mode.
        

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
        @summary Generates the JSON for an asynchronous thread that is used to update a real-time synchronization task in Data Integration.
        
        @description DataWorks allows you to use only the [UpdateDISyncTask](https://help.aliyun.com/document_detail/289109.html) operation to update a batch synchronization task in Data Integration. To update a real-time synchronization task, you must first call the GenerateDISyncTaskConfigForUpdating operation to generate the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the UpdateDISyncTask operation and use the parameters as request parameters to update a real-time synchronization task in Data Integration. DataWorks allows you to create or update real-time synchronization tasks in Data Integration only in asynchronous mode.
        

        @param request: GenerateDISyncTaskConfigForUpdatingRequest

        @return: GenerateDISyncTaskConfigForUpdatingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_updating_with_options(request, runtime)

    def get_alert_message_with_options(self, request, runtime):
        """
        @summary Queries alert information based on the alert ID that is specified by the AlertId parameter.
        

        @param request: GetAlertMessageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAlertMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_id):
            body['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAlertMessage',
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
            dataworks_public_20200518_models.GetAlertMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alert_message(self, request):
        """
        @summary Queries alert information based on the alert ID that is specified by the AlertId parameter.
        

        @param request: GetAlertMessageRequest

        @return: GetAlertMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_alert_message_with_options(request, runtime)

    def get_baseline_with_options(self, request, runtime):
        """
        @summary Queries the information about a baseline based on its ID.
        

        @param request: GetBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetBaselineResponse
        """
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
        """
        @summary Queries the information about a baseline based on its ID.
        

        @param request: GetBaselineRequest

        @return: GetBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_with_options(request, runtime)

    def get_baseline_config_with_options(self, request, runtime):
        """
        @summary Queries the configurations of a baseline.
        

        @param request: GetBaselineConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetBaselineConfigResponse
        """
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
        """
        @summary Queries the configurations of a baseline.
        

        @param request: GetBaselineConfigRequest

        @return: GetBaselineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_config_with_options(request, runtime)

    def get_baseline_key_path_with_options(self, request, runtime):
        """
        @summary The information about the events that are associated with the instance.
        

        @param request: GetBaselineKeyPathRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetBaselineKeyPathResponse
        """
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
        """
        @summary The information about the events that are associated with the instance.
        

        @param request: GetBaselineKeyPathRequest

        @return: GetBaselineKeyPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_key_path_with_options(request, runtime)

    def get_baseline_status_with_options(self, request, runtime):
        """
        @summary Queries the details of a baseline instance.
        

        @param request: GetBaselineStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetBaselineStatusResponse
        """
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
        """
        @summary Queries the details of a baseline instance.
        

        @param request: GetBaselineStatusRequest

        @return: GetBaselineStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_status_with_options(request, runtime)

    def get_business_with_options(self, request, runtime):
        """

        @param request: GetBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetBusinessResponse
        """
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
        """

        @param request: GetBusinessRequest

        @return: GetBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    def get_ddljob_status_with_options(self, request, runtime):
        """
        @summary Queries the status of a table creation, update, or deletion task.
        

        @param request: GetDDLJobStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDDLJobStatusResponse
        """
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
        """
        @summary Queries the status of a table creation, update, or deletion task.
        

        @param request: GetDDLJobStatusRequest

        @return: GetDDLJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ddljob_status_with_options(request, runtime)

    def get_dialarm_rule_with_options(self, request, runtime):
        """
        @summary Queries the details of an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param request: GetDIAlarmRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDIAlarmRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialarm_rule_id):
            body['DIAlarmRuleId'] = request.dialarm_rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDIAlarmRule',
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
            dataworks_public_20200518_models.GetDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dialarm_rule(self, request):
        """
        @summary Queries the details of an alert rule for a Data Integration task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param request: GetDIAlarmRuleRequest

        @return: GetDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dialarm_rule_with_options(request, runtime)

    def get_dijob_with_options(self, request, runtime):
        """
        @summary Queries the information about a new-version synchronization task created in Data Integration. The following types of synchronization tasks are supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param request: GetDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDIJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        if not UtilClient.is_unset(request.with_details):
            body['WithDetails'] = request.with_details
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDIJob',
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
            dataworks_public_20200518_models.GetDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dijob(self, request):
        """
        @summary Queries the information about a new-version synchronization task created in Data Integration. The following types of synchronization tasks are supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param request: GetDIJobRequest

        @return: GetDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dijob_with_options(request, runtime)

    def get_disync_instance_info_with_options(self, request, runtime):
        """
        @summary Queries the status of a real-time synchronization task or a data synchronization solution.
        

        @param request: GetDISyncInstanceInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDISyncInstanceInfoResponse
        """
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
        """
        @summary Queries the status of a real-time synchronization task or a data synchronization solution.
        

        @param request: GetDISyncInstanceInfoRequest

        @return: GetDISyncInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_disync_instance_info_with_options(request, runtime)

    def get_disync_task_with_options(self, request, runtime):
        """
        @summary Queries the details of a real-time synchronization task or a data synchronization solution.
        

        @param request: GetDISyncTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDISyncTaskResponse
        """
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
        """
        @summary Queries the details of a real-time synchronization task or a data synchronization solution.
        

        @param request: GetDISyncTaskRequest

        @return: GetDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_with_options(request, runtime)

    def get_dag_with_options(self, request, runtime):
        """
        @summary Queries the information about a directed acyclic graph (DAG). You can call the GetDag operation to query the information about the DAG for a manually triggered workflow, a manually triggered node, or a data backfill instance. However, you cannot query the information about the DAG for an auto triggered node or an auto triggered workflow.
        
        @description Supported DAG types:
        MANUAL: DAG for a manually triggered workflow
        SMOKE_TEST: DAG for a smoke testing workflow
        SUPPLY_DATA: DAG for a data backfill instance
        BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        Supported DAG states:
        CREATED
        RUNNING
        FAILURE
        SUCCESS
        

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
        @summary Queries the information about a directed acyclic graph (DAG). You can call the GetDag operation to query the information about the DAG for a manually triggered workflow, a manually triggered node, or a data backfill instance. However, you cannot query the information about the DAG for an auto triggered node or an auto triggered workflow.
        
        @description Supported DAG types:
        MANUAL: DAG for a manually triggered workflow
        SMOKE_TEST: DAG for a smoke testing workflow
        SUPPLY_DATA: DAG for a data backfill instance
        BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        Supported DAG states:
        CREATED
        RUNNING
        FAILURE
        SUCCESS
        

        @param request: GetDagRequest

        @return: GetDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dag_with_options(request, runtime)

    def get_data_service_api_with_options(self, request, runtime):
        """
        @summary Queries the details of a DataService Studio API in the development state.
        

        @param request: GetDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServiceApiResponse
        """
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
        """
        @summary Queries the details of a DataService Studio API in the development state.
        

        @param request: GetDataServiceApiRequest

        @return: GetDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_with_options(request, runtime)

    def get_data_service_api_test_with_options(self, request, runtime):
        """
        @summary Queries the test results of an API in DataService Studio.
        

        @param request: GetDataServiceApiTestRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServiceApiTestResponse
        """
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
        """
        @summary Queries the test results of an API in DataService Studio.
        

        @param request: GetDataServiceApiTestRequest

        @return: GetDataServiceApiTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_test_with_options(request, runtime)

    def get_data_service_application_with_options(self, request, runtime):
        """
        @summary Queries the details of an application.
        

        @param request: GetDataServiceApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServiceApplicationResponse
        """
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
        """
        @summary Queries the details of an application.
        

        @param request: GetDataServiceApplicationRequest

        @return: GetDataServiceApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_application_with_options(request, runtime)

    def get_data_service_folder_with_options(self, request, runtime):
        """
        @summary Queries a folder.
        

        @param request: GetDataServiceFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServiceFolderResponse
        """
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
        """
        @summary Queries a folder.
        

        @param request: GetDataServiceFolderRequest

        @return: GetDataServiceFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_folder_with_options(request, runtime)

    def get_data_service_group_with_options(self, request, runtime):
        """
        @summary Queries a business process.
        

        @param request: GetDataServiceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServiceGroupResponse
        """
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
        """
        @summary Queries a business process.
        

        @param request: GetDataServiceGroupRequest

        @return: GetDataServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_group_with_options(request, runtime)

    def get_data_service_published_api_with_options(self, request, runtime):
        """
        @summary Queries the information about a DataService Studio API in the published state.
        

        @param request: GetDataServicePublishedApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataServicePublishedApiResponse
        """
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
        """
        @summary Queries the information about a DataService Studio API in the published state.
        

        @param request: GetDataServicePublishedApiRequest

        @return: GetDataServicePublishedApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_published_api_with_options(request, runtime)

    def get_data_source_meta_with_options(self, request, runtime):
        """
        @summary Queries the metadata of a specified data source.
        

        @param request: GetDataSourceMetaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataSourceMetaResponse
        """
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
        """
        @summary Queries the metadata of a specified data source.
        

        @param request: GetDataSourceMetaRequest

        @return: GetDataSourceMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_meta_with_options(request, runtime)

    def get_deployment_with_options(self, request, runtime):
        """
        @summary Queries the information about a deployment package.
        

        @param request: GetDeploymentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDeploymentResponse
        """
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
        """
        @summary Queries the information about a deployment package.
        

        @param request: GetDeploymentRequest

        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    def get_extension_with_options(self, request, runtime):
        """
        @summary Queries the details of an extension.
        

        @param request: GetExtensionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetExtensionResponse
        """
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
        """
        @summary Queries the details of an extension.
        

        @param request: GetExtensionRequest

        @return: GetExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_extension_with_options(request, runtime)

    def get_file_with_options(self, request, runtime):
        """
        @summary Queries the information about a file.
        

        @param request: GetFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFileResponse
        """
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
        """
        @summary Queries the information about a file.
        

        @param request: GetFileRequest

        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    def get_file_type_statistic_with_options(self, request, runtime):
        """
        @summary Queries the distribution of node types.
        

        @param request: GetFileTypeStatisticRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFileTypeStatisticResponse
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
        """
        @summary Queries the distribution of node types.
        

        @param request: GetFileTypeStatisticRequest

        @return: GetFileTypeStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_type_statistic_with_options(request, runtime)

    def get_file_version_with_options(self, request, runtime):
        """
        @summary Queries the information about a file version.
        

        @param request: GetFileVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFileVersionResponse
        """
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
        """
        @summary Queries the information about a file version.
        

        @param request: GetFileVersionRequest

        @return: GetFileVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    def get_folder_with_options(self, request, runtime):
        """

        @param request: GetFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFolderResponse
        """
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
        """

        @param request: GetFolderRequest

        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_ideevent_detail_with_options(self, request, runtime):
        """
        @summary Queries the data snapshot of an extension point based on the ID of a message in DataWorks OpenEvent when the related extension point event is triggered.
        

        @param request: GetIDEEventDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetIDEEventDetailResponse
        """
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
        """
        @summary Queries the data snapshot of an extension point based on the ID of a message in DataWorks OpenEvent when the related extension point event is triggered.
        

        @param request: GetIDEEventDetailRequest

        @return: GetIDEEventDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ideevent_detail_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        """
        @summary Queries the information about an instance.
        

        @param request: GetInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceResponse
        """
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
        """
        @summary Queries the information about an instance.
        

        @param request: GetInstanceRequest

        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_instance_consume_time_rank_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetInstanceConsumeTimeRank is deprecated
        
        @summary Queries the ranking of the running durations of instances.
        

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
        @deprecated OpenAPI GetInstanceConsumeTimeRank is deprecated
        
        @summary Queries the ranking of the running durations of instances.
        

        @param request: GetInstanceConsumeTimeRankRequest

        @return: GetInstanceConsumeTimeRankResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_consume_time_rank_with_options(request, runtime)

    def get_instance_count_trend_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetInstanceCountTrend is deprecated
        
        @summary Queries the quantity trend of auto triggered instances.
        

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
        @deprecated OpenAPI GetInstanceCountTrend is deprecated
        
        @summary Queries the quantity trend of auto triggered instances.
        

        @param request: GetInstanceCountTrendRequest

        @return: GetInstanceCountTrendResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_trend_with_options(request, runtime)

    def get_instance_error_rank_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetInstanceErrorRank is deprecated
        
        @summary Queries the ranking of nodes on which errors occur within the last month.
        

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
        @deprecated OpenAPI GetInstanceErrorRank is deprecated
        
        @summary Queries the ranking of nodes on which errors occur within the last month.
        

        @param request: GetInstanceErrorRankRequest

        @return: GetInstanceErrorRankResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_error_rank_with_options(request, runtime)

    def get_instance_log_with_options(self, request, runtime):
        """
        @summary Queries the logs of an instance.
        
        @description You may not obtain the instance logs that were generated more than seven days ago.
        

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
        @summary Queries the logs of an instance.
        
        @description You may not obtain the instance logs that were generated more than seven days ago.
        

        @param request: GetInstanceLogRequest

        @return: GetInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_log_with_options(request, runtime)

    def get_instance_status_count_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetInstanceStatusCount is deprecated
        
        @summary Queries the statistics of instances in different states.
        

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
        @deprecated OpenAPI GetInstanceStatusCount is deprecated
        
        @summary Queries the statistics of instances in different states.
        

        @param request: GetInstanceStatusCountRequest

        @return: GetInstanceStatusCountResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_count_with_options(request, runtime)

    def get_instance_status_statistic_with_options(self, request, runtime):
        """
        @summary Queries the number of instances that are in each state.
        

        @param request: GetInstanceStatusStatisticRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceStatusStatisticResponse
        """
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
        if not UtilClient.is_unset(request.scheduler_period):
            body['SchedulerPeriod'] = request.scheduler_period
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
        """
        @summary Queries the number of instances that are in each state.
        

        @param request: GetInstanceStatusStatisticRequest

        @return: GetInstanceStatusStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_statistic_with_options(request, runtime)

    def get_manual_dag_instances_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetManualDagInstances is deprecated
        
        @summary Queries the information about instances in a manually triggered workflow.
        

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
        @deprecated OpenAPI GetManualDagInstances is deprecated
        
        @summary Queries the information about instances in a manually triggered workflow.
        

        @param request: GetManualDagInstancesRequest

        @return: GetManualDagInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_manual_dag_instances_with_options(request, runtime)

    def get_meta_category_with_options(self, request, runtime):
        """
        @summary Queries the information about a category tree.
        

        @param request: GetMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaCategoryResponse
        """
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
        """
        @summary Queries the information about a category tree.
        

        @param request: GetMetaCategoryRequest

        @return: GetMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_category_with_options(request, runtime)

    def get_meta_collection_detail_with_options(self, request, runtime):
        """
        @summary Queries the information about a collection.
        

        @param request: GetMetaCollectionDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaCollectionDetailResponse
        """
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
        """
        @summary Queries the information about a collection.
        

        @param request: GetMetaCollectionDetailRequest

        @return: GetMetaCollectionDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_collection_detail_with_options(request, runtime)

    def get_meta_column_lineage_with_options(self, request, runtime):
        """
        @summary Queries the lineage of a field in a metatable.
        

        @param request: GetMetaColumnLineageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaColumnLineageResponse
        """
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
        """
        @summary Queries the lineage of a field in a metatable.
        

        @param request: GetMetaColumnLineageRequest

        @return: GetMetaColumnLineageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_column_lineage_with_options(request, runtime)

    def get_meta_dbinfo_with_options(self, request, runtime):
        """
        @summary Queries the basic metadata information about a compute engine instance.
        
        @description The ID of the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        You can log on to the [EMR console](https://emr.console.aliyun.com/?spm=a2c4g.11186623.0.0.965cc5c2GeiHet#/cn-hangzhou) to obtain the ID of the EMR cluster.
        

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
        @summary Queries the basic metadata information about a compute engine instance.
        
        @description The ID of the EMR cluster. This parameter is required only if you set the DataSourceType parameter to emr.
        You can log on to the [EMR console](https://emr.console.aliyun.com/?spm=a2c4g.11186623.0.0.965cc5c2GeiHet#/cn-hangzhou) to obtain the ID of the EMR cluster.
        

        @param request: GetMetaDBInfoRequest

        @return: GetMetaDBInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbinfo_with_options(request, runtime)

    def get_meta_dbtable_list_with_options(self, request, runtime):
        """
        @summary Queries metatables in a compute engine instance.
        

        @param request: GetMetaDBTableListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaDBTableListResponse
        """
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
        """
        @summary Queries metatables in a compute engine instance.
        

        @param request: GetMetaDBTableListRequest

        @return: GetMetaDBTableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbtable_list_with_options(request, runtime)

    def get_meta_table_basic_info_with_options(self, request, runtime):
        """
        @summary Queries the basic information about a metatable.
        

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
        @summary Queries the basic information about a metatable.
        

        @param request: GetMetaTableBasicInfoRequest

        @return: GetMetaTableBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_basic_info_with_options(request, runtime)

    def get_meta_table_change_log_with_options(self, request, runtime):
        """
        @summary Queries the change logs of a metatable.
        
        @description > This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: GetMetaTableChangeLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableChangeLogResponse
        """
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
        """
        @summary Queries the change logs of a metatable.
        
        @description > This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: GetMetaTableChangeLogRequest

        @return: GetMetaTableChangeLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_change_log_with_options(request, runtime)

    def get_meta_table_column_with_options(self, request, runtime):
        """
        @summary Queries the field information of a metatable.
        

        @param request: GetMetaTableColumnRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableColumnResponse
        """
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
        """
        @summary Queries the field information of a metatable.
        

        @param request: GetMetaTableColumnRequest

        @return: GetMetaTableColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    def get_meta_table_full_info_with_options(self, request, runtime):
        """
        @summary Queries the complete information about a metatable, including information about fields in the metatable.
        

        @param request: GetMetaTableFullInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableFullInfoResponse
        """
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
        """
        @summary Queries the complete information about a metatable, including information about fields in the metatable.
        

        @param request: GetMetaTableFullInfoRequest

        @return: GetMetaTableFullInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_full_info_with_options(request, runtime)

    def get_meta_table_intro_wiki_with_options(self, request, runtime):
        """
        @summary Queries the instructions on how to use a table.
        

        @param request: GetMetaTableIntroWikiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableIntroWikiResponse
        """
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
        """
        @summary Queries the instructions on how to use a table.
        

        @param request: GetMetaTableIntroWikiRequest

        @return: GetMetaTableIntroWikiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_intro_wiki_with_options(request, runtime)

    def get_meta_table_lineage_with_options(self, request, runtime):
        """
        @summary Queries the lineage of a metatable.
        

        @param request: GetMetaTableLineageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableLineageResponse
        """
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
        """
        @summary Queries the lineage of a metatable.
        

        @param request: GetMetaTableLineageRequest

        @return: GetMetaTableLineageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_lineage_with_options(request, runtime)

    def get_meta_table_list_by_category_with_options(self, request, runtime):
        """
        @summary Queries metatables in a specified category.
        

        @param request: GetMetaTableListByCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableListByCategoryResponse
        """
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
        """
        @summary Queries metatables in a specified category.
        

        @param request: GetMetaTableListByCategoryRequest

        @return: GetMetaTableListByCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_list_by_category_with_options(request, runtime)

    def get_meta_table_output_with_options(self, request, runtime):
        """
        @summary Queries the output information of a metatable.
        

        @param request: GetMetaTableOutputRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableOutputResponse
        """
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
        """
        @summary Queries the output information of a metatable.
        

        @param request: GetMetaTableOutputRequest

        @return: GetMetaTableOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_output_with_options(request, runtime)

    def get_meta_table_partition_with_options(self, tmp_req, runtime):
        """
        @summary Obtains a list of partitions in a metatable.
        
        @description You can call this operation to query only the partitions of a metatable in a MaxCompute or E-MapReduce (EMR) compute engine. If you query partitions of a metatable in an EMR compute engine, only DataLake clusters that use Data Lake Formation (DLF) to manage metadata and Hadoop clusters whose cluster version is earlier than 3.41.0 or 5.7.0 are supported.
        

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
        @summary Obtains a list of partitions in a metatable.
        
        @description You can call this operation to query only the partitions of a metatable in a MaxCompute or E-MapReduce (EMR) compute engine. If you query partitions of a metatable in an EMR compute engine, only DataLake clusters that use Data Lake Formation (DLF) to manage metadata and Hadoop clusters whose cluster version is earlier than 3.41.0 or 5.7.0 are supported.
        

        @param request: GetMetaTablePartitionRequest

        @return: GetMetaTablePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_partition_with_options(request, runtime)

    def get_meta_table_producing_tasks_with_options(self, request, runtime):
        """
        @summary 获取Table的产出任务列表
        

        @param request: GetMetaTableProducingTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableProducingTasksResponse
        """
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
        """
        @summary 获取Table的产出任务列表
        

        @param request: GetMetaTableProducingTasksRequest

        @return: GetMetaTableProducingTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_producing_tasks_with_options(request, runtime)

    def get_meta_table_theme_level_with_options(self, request, runtime):
        """
        @summary Queries the information about the themes and levels of a metatable.
        

        @param request: GetMetaTableThemeLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMetaTableThemeLevelResponse
        """
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
        """
        @summary Queries the information about the themes and levels of a metatable.
        

        @param request: GetMetaTableThemeLevelRequest

        @return: GetMetaTableThemeLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_theme_level_with_options(request, runtime)

    def get_migration_process_with_options(self, request, runtime):
        """
        @summary Queries the progress of a migration task.
        

        @param request: GetMigrationProcessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMigrationProcessResponse
        """
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
        """
        @summary Queries the progress of a migration task.
        

        @param request: GetMigrationProcessRequest

        @return: GetMigrationProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_migration_process_with_options(request, runtime)

    def get_migration_summary_with_options(self, request, runtime):
        """
        @summary Queries the information about a migration task.
        

        @param request: GetMigrationSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMigrationSummaryResponse
        """
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
        """
        @summary Queries the information about a migration task.
        

        @param request: GetMigrationSummaryRequest

        @return: GetMigrationSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_migration_summary_with_options(request, runtime)

    def get_node_with_options(self, request, runtime):
        """
        @summary Indicates whether the request is successful.
        

        @param request: GetNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeResponse
        """
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
        """
        @summary Indicates whether the request is successful.
        

        @param request: GetNodeRequest

        @return: GetNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    def get_node_children_with_options(self, request, runtime):
        """
        @summary Queries a list of instances.
        

        @param request: GetNodeChildrenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeChildrenResponse
        """
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
        """
        @summary Queries a list of instances.
        

        @param request: GetNodeChildrenRequest

        @return: GetNodeChildrenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_children_with_options(request, runtime)

    def get_node_code_with_options(self, request, runtime):
        """
        @summary Queries the code of a node.
        

        @param request: GetNodeCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeCodeResponse
        """
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
        """
        @summary Queries the code of a node.
        

        @param request: GetNodeCodeRequest

        @return: GetNodeCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_code_with_options(request, runtime)

    def get_node_on_baseline_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetNodeOnBaseline is deprecated
        
        @summary Queries the nodes associated with a baseline.
        

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
        @deprecated OpenAPI GetNodeOnBaseline is deprecated
        
        @summary Queries the nodes associated with a baseline.
        

        @param request: GetNodeOnBaselineRequest

        @return: GetNodeOnBaselineResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_on_baseline_with_options(request, runtime)

    def get_node_parents_with_options(self, request, runtime):
        """
        @summary Queries the ancestor nodes of a node.
        

        @param request: GetNodeParentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeParentsResponse
        """
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
        """
        @summary Queries the ancestor nodes of a node.
        

        @param request: GetNodeParentsRequest

        @return: GetNodeParentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_parents_with_options(request, runtime)

    def get_node_type_list_info_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetNodeTypeListInfo is deprecated
        
        @summary Queries the information about node types, including the code and name of a node type.
        

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
        @deprecated OpenAPI GetNodeTypeListInfo is deprecated
        
        @summary Queries the information about node types, including the code and name of a node type.
        

        @param request: GetNodeTypeListInfoRequest

        @return: GetNodeTypeListInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_type_list_info_with_options(request, runtime)

    def get_op_risk_data_with_options(self, request, runtime):
        """
        @summary Queries the records that are generated on a specified date for access to the high-risk sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetOpRiskDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOpRiskDataResponse
        """
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
        """
        @summary Queries the records that are generated on a specified date for access to the high-risk sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetOpRiskDataRequest

        @return: GetOpRiskDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_op_risk_data_with_options(request, runtime)

    def get_op_sensitive_data_with_options(self, request, runtime):
        """
        @summary Queries the records that are generated on a specified date for access to sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetOpSensitiveDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOpSensitiveDataResponse
        """
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
        """
        @summary Queries the records that are generated on a specified date for access to sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetOpSensitiveDataRequest

        @return: GetOpSensitiveDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_op_sensitive_data_with_options(request, runtime)

    def get_option_value_for_project_with_options(self, request, runtime):
        """
        @summary Queries the option settings of an extension in a workspace.
        

        @param request: GetOptionValueForProjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOptionValueForProjectResponse
        """
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
        """
        @summary Queries the option settings of an extension in a workspace.
        

        @param request: GetOptionValueForProjectRequest

        @return: GetOptionValueForProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_option_value_for_project_with_options(request, runtime)

    def get_permission_apply_order_detail_with_options(self, request, runtime):
        """
        @summary Queries the details of a permission request order.
        

        @param request: GetPermissionApplyOrderDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPermissionApplyOrderDetailResponse
        """
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
        """
        @summary Queries the details of a permission request order.
        

        @param request: GetPermissionApplyOrderDetailRequest

        @return: GetPermissionApplyOrderDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_permission_apply_order_detail_with_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        """
        @summary Queries the information about a DataWorks workspace.
        

        @param request: GetProjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_identifier):
            query['ProjectIdentifier'] = request.project_identifier
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
        """
        @summary Queries the information about a DataWorks workspace.
        

        @param request: GetProjectRequest

        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def get_project_detail_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetProjectDetail is deprecated
        
        @summary Queries the information about a DataWorks workspace.
        

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
        @deprecated OpenAPI GetProjectDetail is deprecated
        
        @summary Queries the information about a DataWorks workspace.
        

        @param request: GetProjectDetailRequest

        @return: GetProjectDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_detail_with_options(request, runtime)

    def get_quality_entity_with_options(self, request, runtime):
        """

        @param request: GetQualityEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetQualityEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_type):
            body['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.match_expression):
            body['MatchExpression'] = request.match_expression
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """

        @param request: GetQualityEntityRequest

        @return: GetQualityEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_entity_with_options(request, runtime)

    def get_quality_follower_with_options(self, request, runtime):
        """

        @param request: GetQualityFollowerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetQualityFollowerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """

        @param request: GetQualityFollowerRequest

        @return: GetQualityFollowerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_follower_with_options(request, runtime)

    def get_quality_rule_with_options(self, request, runtime):
        """
        @summary Queries the information about a monitoring rule.
        

        @param request: GetQualityRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetQualityRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Queries the information about a monitoring rule.
        

        @param request: GetQualityRuleRequest

        @return: GetQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    def get_remind_with_options(self, request, runtime):
        """
        @summary Queries the details of a custom alert rule.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=dataworks-public\\&api=GetRemind\\&type=RPC\\&version=2020-05-18)
        

        @param request: GetRemindRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRemindResponse
        """
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
        """
        @summary Queries the details of a custom alert rule.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=dataworks-public\\&api=GetRemind\\&type=RPC\\&version=2020-05-18)
        

        @param request: GetRemindRequest

        @return: GetRemindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_remind_with_options(request, runtime)

    def get_sensitive_data_with_options(self, request, runtime):
        """
        @summary Queries the latest sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetSensitiveDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSensitiveDataResponse
        """
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
        """
        @summary Queries the latest sensitive data in all the DataWorks workspaces of a tenant.
        

        @param request: GetSensitiveDataRequest

        @return: GetSensitiveDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sensitive_data_with_options(request, runtime)

    def get_success_instance_trend_with_options(self, request, runtime):
        """
        @deprecated OpenAPI GetSuccessInstanceTrend is deprecated
        
        @summary Queries the statistics of instances in different periods of a day.
        

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
        @deprecated OpenAPI GetSuccessInstanceTrend is deprecated
        
        @summary Queries the statistics of instances in different periods of a day.
        

        @param request: GetSuccessInstanceTrendRequest

        @return: GetSuccessInstanceTrendResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_success_instance_trend_with_options(request, runtime)

    def get_topic_with_options(self, request, runtime):
        """
        @summary Queries the information about an event.
        
        @description ***\
        

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
        @summary Queries the information about an event.
        
        @description ***\
        

        @param request: GetTopicRequest

        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    def get_topic_influence_with_options(self, request, runtime):
        """

        @param request: GetTopicInfluenceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTopicInfluenceResponse
        """
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
        """

        @param request: GetTopicInfluenceRequest

        @return: GetTopicInfluenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_influence_with_options(request, runtime)

    def import_data_sources_with_options(self, request, runtime):
        """
        @summary Imports data sources from your on-premises machine to a specific DataWorks workspace.
        
        @description You can import self-managed data sources or data sources that are exported from other DataWorks workspaces to a specific DataWorks workspace.
        To import a self-managed data source to a DataWorks workspace, the data source type must be supported by DataWorks. For more information about the types of data sources supported by DataWorks, see [Supported data stores](https://help.aliyun.com/document_detail/181656.html).
        For more information about how to export data sources from DataWorks workspaces to your on-premises machine, see [ExportDataSources](https://help.aliyun.com/document_detail/279570.html).
        

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
        @summary Imports data sources from your on-premises machine to a specific DataWorks workspace.
        
        @description You can import self-managed data sources or data sources that are exported from other DataWorks workspaces to a specific DataWorks workspace.
        To import a self-managed data source to a DataWorks workspace, the data source type must be supported by DataWorks. For more information about the types of data sources supported by DataWorks, see [Supported data stores](https://help.aliyun.com/document_detail/181656.html).
        For more information about how to export data sources from DataWorks workspaces to your on-premises machine, see [ExportDataSources](https://help.aliyun.com/document_detail/279570.html).
        

        @param request: ImportDataSourcesRequest

        @return: ImportDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_data_sources_with_options(request, runtime)

    def list_alert_messages_with_options(self, request, runtime):
        """
        @summary Queries a list of alerts.
        

        @param request: ListAlertMessagesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAlertMessagesResponse
        """
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
        """
        @summary Queries a list of alerts.
        

        @param request: ListAlertMessagesRequest

        @return: ListAlertMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alert_messages_with_options(request, runtime)

    def list_baseline_configs_with_options(self, request, runtime):
        """
        @summary Queries a list of baselines.
        

        @param request: ListBaselineConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListBaselineConfigsResponse
        """
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
        """
        @summary Queries a list of baselines.
        

        @param request: ListBaselineConfigsRequest

        @return: ListBaselineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_configs_with_options(request, runtime)

    def list_baseline_statuses_with_options(self, request, runtime):
        """
        @summary Queries a list of baseline instances.
        

        @param request: ListBaselineStatusesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListBaselineStatusesResponse
        """
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
        """
        @summary Queries a list of baseline instances.
        

        @param request: ListBaselineStatusesRequest

        @return: ListBaselineStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_statuses_with_options(request, runtime)

    def list_baselines_with_options(self, request, runtime):
        """
        @summary Obtains a list of baselines.
        

        @param request: ListBaselinesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListBaselinesResponse
        """
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
        """
        @summary Obtains a list of baselines.
        

        @param request: ListBaselinesRequest

        @return: ListBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baselines_with_options(request, runtime)

    def list_business_with_options(self, request, runtime):
        """
        @summary Queries a list of workflows.
        

        @param request: ListBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListBusinessResponse
        """
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
        """
        @summary Queries a list of workflows.
        

        @param request: ListBusinessRequest

        @return: ListBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    def list_calc_engines_with_options(self, request, runtime):
        """
        @summary Queries a list of compute engines that are associated with a DataWorks workspace.
        

        @param request: ListCalcEnginesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCalcEnginesResponse
        """
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
        """
        @summary Queries a list of compute engines that are associated with a DataWorks workspace.
        

        @param request: ListCalcEnginesRequest

        @return: ListCalcEnginesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_calc_engines_with_options(request, runtime)

    def list_cluster_configs_with_options(self, request, runtime):
        """
        @summary 列出集群的配置信息
        

        @param request: ListClusterConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClusterConfigsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterConfigs',
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
            dataworks_public_20200518_models.ListClusterConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_configs(self, request):
        """
        @summary 列出集群的配置信息
        

        @param request: ListClusterConfigsRequest

        @return: ListClusterConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_configs_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        """
        @summary 列出注册到 DataWorks 的集群的信息
        

        @param request: ListClustersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
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
            dataworks_public_20200518_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters(self, request):
        """
        @summary 列出注册到 DataWorks 的集群的信息
        

        @param request: ListClustersRequest

        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def list_connections_with_options(self, request, runtime):
        """
        @deprecated OpenAPI ListConnections is deprecated
        
        @summary Queries a list of data sources.
        

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
        @deprecated OpenAPI ListConnections is deprecated
        
        @summary Queries a list of data sources.
        

        @param request: ListConnectionsRequest

        @return: ListConnectionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    def list_dialarm_rules_with_options(self, request, runtime):
        """
        @summary Queries a list of alert rules for a new-version synchronization task. The following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param request: ListDIAlarmRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDIAlarmRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDIAlarmRules',
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
            dataworks_public_20200518_models.ListDIAlarmRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dialarm_rules(self, request):
        """
        @summary Queries a list of alert rules for a new-version synchronization task. The following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization.
        

        @param request: ListDIAlarmRulesRequest

        @return: ListDIAlarmRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialarm_rules_with_options(request, runtime)

    def list_dijobs_with_options(self, request, runtime):
        """
        @summary Queries a list of new-version synchronization tasks. The following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can call this operation to obtain only the basic information about the tasks. If you want to obtain the details of a task, call the GetDIJob operation.
        

        @param request: ListDIJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDIJobsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_data_source_type):
            body['DestinationDataSourceType'] = request.destination_data_source_type
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_data_source_type):
            body['SourceDataSourceType'] = request.source_data_source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDIJobs',
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
            dataworks_public_20200518_models.ListDIJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dijobs(self, request):
        """
        @summary Queries a list of new-version synchronization tasks. The following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        
        @description You can call this operation to obtain only the basic information about the tasks. If you want to obtain the details of a task, call the GetDIJob operation.
        

        @param request: ListDIJobsRequest

        @return: ListDIJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dijobs_with_options(request, runtime)

    def list_diproject_config_with_options(self, request, runtime):
        """
        @summary Queries the default global configurations of synchronization solutions in a specified DataWorks workspace.
        
        @description DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization tasks in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](https://help.aliyun.com/document_detail/199008.html).
        

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
        @summary Queries the default global configurations of synchronization solutions in a specified DataWorks workspace.
        
        @description DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization tasks in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](https://help.aliyun.com/document_detail/199008.html).
        

        @param request: ListDIProjectConfigRequest

        @return: ListDIProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_diproject_config_with_options(request, runtime)

    def list_dags_with_options(self, request, runtime):
        """
        @summary Queries the details of directed acyclic graphs (DAGs) for a single data backfill instance based on OpSeq.
        
        @description Supported DAG types:
        MANUAL: DAG for a manually triggered workflow
        SMOKE_TEST: DAG for a smoke testing workflow
        SUPPLY_DATA: DAG for a data backfill instance
        BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        Supported DAG states:
        CREATED: The DAG is created.
        RUNNING: The DAG is running.
        FAILURE: The DAG fails to run.
        SUCCESS: The DAG is successfully run.
        

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
        @summary Queries the details of directed acyclic graphs (DAGs) for a single data backfill instance based on OpSeq.
        
        @description Supported DAG types:
        MANUAL: DAG for a manually triggered workflow
        SMOKE_TEST: DAG for a smoke testing workflow
        SUPPLY_DATA: DAG for a data backfill instance
        BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        Supported DAG states:
        CREATED: The DAG is created.
        RUNNING: The DAG is running.
        FAILURE: The DAG fails to run.
        SUCCESS: The DAG is successfully run.
        

        @param request: ListDagsRequest

        @return: ListDagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dags_with_options(request, runtime)

    def list_data_service_api_authorities_with_options(self, request, runtime):
        """
        @summary Queries the APIs on which other users are granted the access permissions.
        

        @param request: ListDataServiceApiAuthoritiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceApiAuthoritiesResponse
        """
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
        """
        @summary Queries the APIs on which other users are granted the access permissions.
        

        @param request: ListDataServiceApiAuthoritiesRequest

        @return: ListDataServiceApiAuthoritiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_authorities_with_options(request, runtime)

    def list_data_service_api_test_with_options(self, request, runtime):
        """
        @summary Queries the test records of a DataService Studio API. This API operation allows you to query only the test records that are generated within the previous month.
        

        @param request: ListDataServiceApiTestRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceApiTestResponse
        """
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
        """
        @summary Queries the test records of a DataService Studio API. This API operation allows you to query only the test records that are generated within the previous month.
        

        @param request: ListDataServiceApiTestRequest

        @return: ListDataServiceApiTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_test_with_options(request, runtime)

    def list_data_service_apis_with_options(self, request, runtime):
        """
        @summary Queries a list of APIs in the development state.
        

        @param request: ListDataServiceApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceApisResponse
        """
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
        """
        @summary Queries a list of APIs in the development state.
        

        @param request: ListDataServiceApisRequest

        @return: ListDataServiceApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_apis_with_options(request, runtime)

    def list_data_service_applications_with_options(self, request, runtime):
        """
        @summary Queries the basic information of applications.
        

        @param request: ListDataServiceApplicationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceApplicationsResponse
        """
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
        """
        @summary Queries the basic information of applications.
        

        @param request: ListDataServiceApplicationsRequest

        @return: ListDataServiceApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_applications_with_options(request, runtime)

    def list_data_service_authorized_apis_with_options(self, request, runtime):
        """
        @summary Queries the APIs that you are authorized to access.
        

        @param request: ListDataServiceAuthorizedApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceAuthorizedApisResponse
        """
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
        """
        @summary Queries the APIs that you are authorized to access.
        

        @param request: ListDataServiceAuthorizedApisRequest

        @return: ListDataServiceAuthorizedApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_authorized_apis_with_options(request, runtime)

    def list_data_service_folders_with_options(self, request, runtime):
        """
        @summary Queries folders.
        

        @param request: ListDataServiceFoldersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceFoldersResponse
        """
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
        """
        @summary Queries folders.
        

        @param request: ListDataServiceFoldersRequest

        @return: ListDataServiceFoldersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_folders_with_options(request, runtime)

    def list_data_service_groups_with_options(self, request, runtime):
        """
        @summary Queries business processes.
        

        @param request: ListDataServiceGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServiceGroupsResponse
        """
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
        """
        @summary Queries business processes.
        

        @param request: ListDataServiceGroupsRequest

        @return: ListDataServiceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_groups_with_options(request, runtime)

    def list_data_service_published_apis_with_options(self, request, runtime):
        """
        @summary Queries a list of APIs in the published state.
        

        @param request: ListDataServicePublishedApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataServicePublishedApisResponse
        """
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
        """
        @summary Queries a list of APIs in the published state.
        

        @param request: ListDataServicePublishedApisRequest

        @return: ListDataServicePublishedApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    def list_data_sources_with_options(self, request, runtime):
        """
        @summary Queries the data sources added to a DataWorks workspace.
        

        @param request: ListDataSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataSourcesResponse
        """
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
        """
        @summary Queries the data sources added to a DataWorks workspace.
        

        @param request: ListDataSourcesRequest

        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    def list_deployments_with_options(self, request, runtime):
        """
        @summary Queries a list of deployment packages. This operation is equivalent to viewing a list of deployment packages on the Deployment Packages page of the DataWorks console.
        

        @param request: ListDeploymentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDeploymentsResponse
        """
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
        """
        @summary Queries a list of deployment packages. This operation is equivalent to viewing a list of deployment packages on the Deployment Packages page of the DataWorks console.
        

        @param request: ListDeploymentsRequest

        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployments_with_options(request, runtime)

    def list_enabled_extensions_for_project_with_options(self, request, runtime):
        """
        @summary Queries a list of built-in and custom extensions that are enabled in a workspace.
        
        @description For information about codes of extension point events, see [Development references: Extension point event codes](https://help.aliyun.com/document_detail/463357.html).
        

        @param request: ListEnabledExtensionsForProjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListEnabledExtensionsForProjectResponse
        """
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
        """
        @summary Queries a list of built-in and custom extensions that are enabled in a workspace.
        
        @description For information about codes of extension point events, see [Development references: Extension point event codes](https://help.aliyun.com/document_detail/463357.html).
        

        @param request: ListEnabledExtensionsForProjectRequest

        @return: ListEnabledExtensionsForProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_enabled_extensions_for_project_with_options(request, runtime)

    def list_entities_by_tags_with_options(self, tmp_req, runtime):
        """
        @summary Queries a list of entities by tag. Only entities of the maxcompute-table type are supported.
        

        @param tmp_req: ListEntitiesByTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListEntitiesByTagsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.ListEntitiesByTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntitiesByTags',
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
            dataworks_public_20200518_models.ListEntitiesByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_entities_by_tags(self, request):
        """
        @summary Queries a list of entities by tag. Only entities of the maxcompute-table type are supported.
        

        @param request: ListEntitiesByTagsRequest

        @return: ListEntitiesByTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_entities_by_tags_with_options(request, runtime)

    def list_entity_tags_with_options(self, request, runtime):
        """
        @summary Queries a list of tags of an entity. Only entities of the maxcompute-table type are supported.
        

        @param request: ListEntityTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListEntityTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntityTags',
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
            dataworks_public_20200518_models.ListEntityTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_entity_tags(self, request):
        """
        @summary Queries a list of tags of an entity. Only entities of the maxcompute-table type are supported.
        

        @param request: ListEntityTagsRequest

        @return: ListEntityTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_entity_tags_with_options(request, runtime)

    def list_extensions_with_options(self, request, runtime):
        """
        @summary Queries a list of extensions.
        

        @param request: ListExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExtensionsResponse
        """
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
        """
        @summary Queries a list of extensions.
        

        @param request: ListExtensionsRequest

        @return: ListExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_extensions_with_options(request, runtime)

    def list_file_type_with_options(self, request, runtime):
        """
        @summary Queries the information about node types, such as the code and name.
        

        @param request: ListFileTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFileTypeResponse
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
        """
        @summary Queries the information about node types, such as the code and name.
        

        @param request: ListFileTypeRequest

        @return: ListFileTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_file_type_with_options(request, runtime)

    def list_file_versions_with_options(self, request, runtime):
        """

        @param request: ListFileVersionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFileVersionsResponse
        """
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
        """

        @param request: ListFileVersionsRequest

        @return: ListFileVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    def list_files_with_options(self, request, runtime):
        """

        @param request: ListFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exact_file_name):
            body['ExactFileName'] = request.exact_file_name
        if not UtilClient.is_unset(request.file_folder_path):
            body['FileFolderPath'] = request.file_folder_path
        if not UtilClient.is_unset(request.file_id_in):
            body['FileIdIn'] = request.file_id_in
        if not UtilClient.is_unset(request.file_types):
            body['FileTypes'] = request.file_types
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.need_absolute_folder_path):
            body['NeedAbsoluteFolderPath'] = request.need_absolute_folder_path
        if not UtilClient.is_unset(request.need_content):
            body['NeedContent'] = request.need_content
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
        """

        @param request: ListFilesRequest

        @return: ListFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    def list_folders_with_options(self, request, runtime):
        """
        @summary Queries a list of folders.
        

        @param request: ListFoldersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFoldersResponse
        """
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
        """
        @summary Queries a list of folders.
        

        @param request: ListFoldersRequest

        @return: ListFoldersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    def list_inner_nodes_with_options(self, request, runtime):
        """
        @summary Queries information about inner nodes. For example, you can call this operation to query the inner nodes of a node group or a do-while node. You cannot call this operation to query the inner nodes of a PAI node.
        

        @param request: ListInnerNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInnerNodesResponse
        """
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
        """
        @summary Queries information about inner nodes. For example, you can call this operation to query the inner nodes of a node group or a do-while node. You cannot call this operation to query the inner nodes of a PAI node.
        

        @param request: ListInnerNodesRequest

        @return: ListInnerNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_inner_nodes_with_options(request, runtime)

    def list_instance_amount_with_options(self, request, runtime):
        """
        @summary Queries the trend of the number of auto triggered node instances within a specified period of time.
        

        @param request: ListInstanceAmountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceAmountResponse
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
        """
        @summary Queries the trend of the number of auto triggered node instances within a specified period of time.
        

        @param request: ListInstanceAmountRequest

        @return: ListInstanceAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_amount_with_options(request, runtime)

    def list_instance_history_with_options(self, request, runtime):
        """
        @summary Queries information about the historical records of all instances. One historical record is generated if an instance is rerun once.
        

        @param request: ListInstanceHistoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceHistoryResponse
        """
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
        """
        @summary Queries information about the historical records of all instances. One historical record is generated if an instance is rerun once.
        

        @param request: ListInstanceHistoryRequest

        @return: ListInstanceHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_history_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        """
        @summary The ID of the directed acyclic graph (DAG). You can set this parameter to the value of the DagId parameter returned by the [RunCycleDagNodes](https://help.aliyun.com/document_detail/212961.html), [RunSmokeTest](https://help.aliyun.com/document_detail/212949.html), or [RunManualDagNodes](https://help.aliyun.com/document_detail/212830.html) operation based on your business requirements. The RunManualDagNodes operation is used to backfill data, the RunSmokeTest operation is used to perform smoke testing, and the RunManualDagNodes operation is used to run nodes in a manually triggered workflow.
        

        @param request: ListInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstancesResponse
        """
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
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
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
        """
        @summary The ID of the directed acyclic graph (DAG). You can set this parameter to the value of the DagId parameter returned by the [RunCycleDagNodes](https://help.aliyun.com/document_detail/212961.html), [RunSmokeTest](https://help.aliyun.com/document_detail/212949.html), or [RunManualDagNodes](https://help.aliyun.com/document_detail/212830.html) operation based on your business requirements. The RunManualDagNodes operation is used to backfill data, the RunSmokeTest operation is used to perform smoke testing, and the RunManualDagNodes operation is used to run nodes in a manually triggered workflow.
        

        @param request: ListInstancesRequest

        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_lineage_with_options(self, request, runtime):
        """
        @summary Queries the ancestor or descendant lineage of an entity.
        

        @param request: ListLineageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLineageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.entity_qualified_name):
            query['EntityQualifiedName'] = request.entity_qualified_name
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
            action='ListLineage',
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
            dataworks_public_20200518_models.ListLineageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_lineage(self, request):
        """
        @summary Queries the ancestor or descendant lineage of an entity.
        

        @param request: ListLineageRequest

        @return: ListLineageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lineage_with_options(request, runtime)

    def list_manual_dag_instances_with_options(self, request, runtime):
        """
        @summary Queries the information about instances in a manually triggered workflow.
        

        @param request: ListManualDagInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListManualDagInstancesResponse
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
        """
        @summary Queries the information about instances in a manually triggered workflow.
        

        @param request: ListManualDagInstancesRequest

        @return: ListManualDagInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_manual_dag_instances_with_options(request, runtime)

    def list_measure_data_with_options(self, request, runtime):
        """
        @summary 查询DataWorks计量数据
        

        @param request: ListMeasureDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMeasureDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_code):
            query['ComponentCode'] = request.component_code
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMeasureData',
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
            dataworks_public_20200518_models.ListMeasureDataResponse(),
            self.call_api(params, req, runtime)
        )

    def list_measure_data(self, request):
        """
        @summary 查询DataWorks计量数据
        

        @param request: ListMeasureDataRequest

        @return: ListMeasureDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_measure_data_with_options(request, runtime)

    def list_meta_collection_entities_with_options(self, request, runtime):
        """
        @summary Queries the entities in a collection.
        

        @param request: ListMetaCollectionEntitiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMetaCollectionEntitiesResponse
        """
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
        """
        @summary Queries the entities in a collection.
        

        @param request: ListMetaCollectionEntitiesRequest

        @return: ListMetaCollectionEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_meta_collection_entities_with_options(request, runtime)

    def list_meta_collections_with_options(self, request, runtime):
        """
        @summary Queries information about collections. Collections include data albums that are displayed on the Data Map page and categories that are created in the data albums. You can call this API operation to query collections by type.
        
        @description The type can be ALBUM or ALBUM_CATEGORY. ALBUM indicates data albums. ALBUM_CATEGORY indicates categories.
        

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
        @summary Queries information about collections. Collections include data albums that are displayed on the Data Map page and categories that are created in the data albums. You can call this API operation to query collections by type.
        
        @description The type can be ALBUM or ALBUM_CATEGORY. ALBUM indicates data albums. ALBUM_CATEGORY indicates categories.
        

        @param request: ListMetaCollectionsRequest

        @return: ListMetaCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_meta_collections_with_options(request, runtime)

    def list_meta_dbwith_options(self, request, runtime):
        """
        @summary Queries a list of metadatabases.
        

        @param request: ListMetaDBRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMetaDBResponse
        """
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
        """
        @summary Queries a list of metadatabases.
        

        @param request: ListMetaDBRequest

        @return: ListMetaDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_meta_dbwith_options(request, runtime)

    def list_migrations_with_options(self, request, runtime):
        """
        @summary Queries a list of migration tasks.
        

        @param request: ListMigrationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMigrationsResponse
        """
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
        """
        @summary Queries a list of migration tasks.
        

        @param request: ListMigrationsRequest

        @return: ListMigrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_migrations_with_options(request, runtime)

    def list_node_iowith_options(self, request, runtime):
        """
        @deprecated OpenAPI ListNodeIO is deprecated
        
        @summary Queries the information about one level of ancestor or descendant nodes of a node.
        

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
        @deprecated OpenAPI ListNodeIO is deprecated
        
        @summary Queries the information about one level of ancestor or descendant nodes of a node.
        

        @param request: ListNodeIORequest

        @return: ListNodeIOResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_iowith_options(request, runtime)

    def list_node_input_or_output_with_options(self, request, runtime):
        """
        @summary Queries the input and output information about a node. Only the ancestor or descendant nodes at the nearest level can be queried each time.
        

        @param request: ListNodeInputOrOutputRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodeInputOrOutputResponse
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
        """
        @summary Queries the input and output information about a node. Only the ancestor or descendant nodes at the nearest level can be queried each time.
        

        @param request: ListNodeInputOrOutputRequest

        @return: ListNodeInputOrOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_input_or_output_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        """
        @summary The ID of the workspace.
        

        @param request: ListNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodesResponse
        """
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
        if not UtilClient.is_unset(request.scheduler_type):
            body['SchedulerType'] = request.scheduler_type
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
        """
        @summary The ID of the workspace.
        

        @param request: ListNodesRequest

        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_nodes_by_baseline_with_options(self, request, runtime):
        """
        @summary Queries nodes in a baseline.
        

        @param request: ListNodesByBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodesByBaselineResponse
        """
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
        """
        @summary Queries nodes in a baseline.
        

        @param request: ListNodesByBaselineRequest

        @return: ListNodesByBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_baseline_with_options(request, runtime)

    def list_nodes_by_output_with_options(self, request, runtime):
        """
        @summary Queries nodes based on the output of the nodes.
        

        @param request: ListNodesByOutputRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodesByOutputResponse
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
        """
        @summary Queries nodes based on the output of the nodes.
        

        @param request: ListNodesByOutputRequest

        @return: ListNodesByOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_output_with_options(request, runtime)

    def list_permission_apply_orders_with_options(self, request, runtime):
        """
        @summary Queries a list of permission request orders.
        

        @param request: ListPermissionApplyOrdersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPermissionApplyOrdersResponse
        """
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
        """
        @summary Queries a list of permission request orders.
        

        @param request: ListPermissionApplyOrdersRequest

        @return: ListPermissionApplyOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permission_apply_orders_with_options(request, runtime)

    def list_program_type_count_with_options(self, request, runtime):
        """
        @deprecated OpenAPI ListProgramTypeCount is deprecated
        
        @summary Queries the distribution of different types of nodes.
        

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
        @deprecated OpenAPI ListProgramTypeCount is deprecated
        
        @summary Queries the distribution of different types of nodes.
        

        @param request: ListProgramTypeCountRequest

        @return: ListProgramTypeCountResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_program_type_count_with_options(request, runtime)

    def list_project_ids_with_options(self, request, runtime):
        """
        @summary Queries the IDs of the workspaces on which a specific Alibaba Cloud account or RAM user has permissions in a specific region.
        
        @description An Alibaba Cloud account can assume a role such as the developer, O\\&M engineer, or workspace administrator role in a workspace. For more information, see [Manage members and roles](https://help.aliyun.com/document_detail/136941.html).
        

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
        @summary Queries the IDs of the workspaces on which a specific Alibaba Cloud account or RAM user has permissions in a specific region.
        
        @description An Alibaba Cloud account can assume a role such as the developer, O\\&M engineer, or workspace administrator role in a workspace. For more information, see [Manage members and roles](https://help.aliyun.com/document_detail/136941.html).
        

        @param request: ListProjectIdsRequest

        @return: ListProjectIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_ids_with_options(request, runtime)

    def list_project_members_with_options(self, request, runtime):
        """
        @summary Queries a list of existing members in a DataWorks workspace.
        

        @param request: ListProjectMembersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProjectMembersResponse
        """
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
        """
        @summary Queries a list of existing members in a DataWorks workspace.
        

        @param request: ListProjectMembersRequest

        @return: ListProjectMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    def list_project_roles_with_options(self, request, runtime):
        """
        @summary Queries a list of roles in a DataWorks workspace.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=dataworks-public\\&api=ListProjectRoles\\&type=RPC\\&version=2020-05-18)
        

        @param request: ListProjectRolesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProjectRolesResponse
        """
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
        """
        @summary Queries a list of roles in a DataWorks workspace.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=dataworks-public\\&api=ListProjectRoles\\&type=RPC\\&version=2020-05-18)
        

        @param request: ListProjectRolesRequest

        @return: ListProjectRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    def list_projects_with_options(self, tmp_req, runtime):
        """
        @summary Queries a list of DataWorks workspaces of the tenant to which a user belongs.
        

        @param tmp_req: ListProjectsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProjectsResponse
        """
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
        """
        @summary Queries a list of DataWorks workspaces of the tenant to which a user belongs.
        

        @param request: ListProjectsRequest

        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_quality_results_by_entity_with_options(self, request, runtime):
        """
        @summary Queries a list of historical check results based on a partition filter expression.
        
        @description ***\
        

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
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        @summary Queries a list of historical check results based on a partition filter expression.
        
        @description ***\
        

        @param request: ListQualityResultsByEntityRequest

        @return: ListQualityResultsByEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_entity_with_options(request, runtime)

    def list_quality_results_by_rule_with_options(self, request, runtime):
        """
        @summary Queries monitoring results after the data quality of a data source or a compute engine is monitored based on monitoring rules.
        

        @param request: ListQualityResultsByRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListQualityResultsByRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Queries monitoring results after the data quality of a data source or a compute engine is monitored based on monitoring rules.
        

        @param request: ListQualityResultsByRuleRequest

        @return: ListQualityResultsByRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_rule_with_options(request, runtime)

    def list_quality_rules_with_options(self, request, runtime):
        """
        @summary Queries monitoring rules based on a partition filter expression.
        

        @param request: ListQualityRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListQualityRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Queries monitoring rules based on a partition filter expression.
        

        @param request: ListQualityRulesRequest

        @return: ListQualityRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    def list_ref_disync_tasks_with_options(self, request, runtime):
        """
        @summary Queries synchronization tasks in Data Integration that use a specific data source.
        

        @param request: ListRefDISyncTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRefDISyncTasksResponse
        """
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
        """
        @summary Queries synchronization tasks in Data Integration that use a specific data source.
        

        @param request: ListRefDISyncTasksRequest

        @return: ListRefDISyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ref_disync_tasks_with_options(request, runtime)

    def list_reminds_with_options(self, request, runtime):
        """
        @summary Queries a list of custom alert rules.
        

        @param request: ListRemindsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRemindsResponse
        """
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
        """
        @summary Queries a list of custom alert rules.
        

        @param request: ListRemindsRequest

        @return: ListRemindsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_reminds_with_options(request, runtime)

    def list_resource_groups_with_options(self, tmp_req, runtime):
        """
        @summary Queries a list of resource groups of a specific type.
        

        @param tmp_req: ListResourceGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceGroupsResponse
        """
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
        """
        @summary Queries a list of resource groups of a specific type.
        

        @param request: ListResourceGroupsRequest

        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_shift_personnels_with_options(self, request, runtime):
        """
        @summary Queries a list of on-duty engineers in a shift schedule.
        

        @param request: ListShiftPersonnelsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListShiftPersonnelsResponse
        """
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
        """
        @summary Queries a list of on-duty engineers in a shift schedule.
        

        @param request: ListShiftPersonnelsRequest

        @return: ListShiftPersonnelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shift_personnels_with_options(request, runtime)

    def list_shift_schedules_with_options(self, request, runtime):
        """
        @summary Queries a list of shift schedules in Operation Center.
        

        @param request: ListShiftSchedulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListShiftSchedulesResponse
        """
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
        """
        @summary Queries a list of shift schedules in Operation Center.
        

        @param request: ListShiftSchedulesRequest

        @return: ListShiftSchedulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shift_schedules_with_options(request, runtime)

    def list_success_instance_amount_with_options(self, request, runtime):
        """
        @summary Queries the trend of the number of auto triggered node instances that are successfully run every hour on the hour of the current day.
        

        @param request: ListSuccessInstanceAmountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSuccessInstanceAmountResponse
        """
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
        """
        @summary Queries the trend of the number of auto triggered node instances that are successfully run every hour on the hour of the current day.
        

        @param request: ListSuccessInstanceAmountRequest

        @return: ListSuccessInstanceAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_success_instance_amount_with_options(request, runtime)

    def list_table_level_with_options(self, request, runtime):
        """
        @summary Queries a list of table levels. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: ListTableLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTableLevelResponse
        """
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
        """
        @summary Queries a list of table levels. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: ListTableLevelRequest

        @return: ListTableLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_table_level_with_options(request, runtime)

    def list_table_theme_with_options(self, request, runtime):
        """
        @summary Queries a list of table themes. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: ListTableThemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTableThemeResponse
        """
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
        """
        @summary Queries a list of table themes. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: ListTableThemeRequest

        @return: ListTableThemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_table_theme_with_options(request, runtime)

    def list_tables_with_options(self, request, runtime):
        """
        @summary 分页获取租户下面的数据源类型粒度的表名称
        

        @param request: ListTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
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
            dataworks_public_20200518_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tables(self, request):
        """
        @summary 分页获取租户下面的数据源类型粒度的表名称
        

        @param request: ListTablesRequest

        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    def list_topics_with_options(self, request, runtime):
        """
        @summary Queries events.
        

        @param request: ListTopicsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTopicsResponse
        """
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
        """
        @summary Queries events.
        

        @param request: ListTopicsRequest

        @return: ListTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    def mount_directory_with_options(self, request, runtime):
        """
        @summary Adds a directory to the left-side navigation pane of DataAnalysis.
        

        @param request: MountDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MountDirectoryResponse
        """
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
        """
        @summary Adds a directory to the left-side navigation pane of DataAnalysis.
        

        @param request: MountDirectoryRequest

        @return: MountDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mount_directory_with_options(request, runtime)

    def offline_node_with_options(self, request, runtime):
        """
        @summary Undeploys a node.
        

        @param request: OfflineNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OfflineNodeResponse
        """
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
        """
        @summary Undeploys a node.
        

        @param request: OfflineNodeRequest

        @return: OfflineNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.offline_node_with_options(request, runtime)

    def publish_data_service_api_with_options(self, request, runtime):
        """
        @summary Publishes an API.
        

        @param request: PublishDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishDataServiceApiResponse
        """
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
        """
        @summary Publishes an API.
        

        @param request: PublishDataServiceApiRequest

        @return: PublishDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    def query_disync_task_config_process_result_with_options(self, request, runtime):
        """
        @summary Queries the execution results of an asynchronous task.
        
        @description DataWorks allows you to call only the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to create a batch synchronization task or the [UpdateDISyncTask](https://help.aliyun.com/document_detail/289109.html) operation to update a batch synchronization task in Data Integration. To create or update a real-time synchronization task, you must first call the [GenerateDISyncTaskConfigForCreating](https://help.aliyun.com/document_detail/383463.html) or [GenerateDISyncTaskConfigForUpdating](https://help.aliyun.com/document_detail/383464.html) operation to obtain the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask or UpdateDISyncTask operation and use the parameters as request parameters to create or update a real-time synchronization task. DataWorks allows you to create or update real-time synchronization tasks in Data Integration only in asynchronous mode.
        

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
        @summary Queries the execution results of an asynchronous task.
        
        @description DataWorks allows you to call only the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) operation to create a batch synchronization task or the [UpdateDISyncTask](https://help.aliyun.com/document_detail/289109.html) operation to update a batch synchronization task in Data Integration. To create or update a real-time synchronization task, you must first call the [GenerateDISyncTaskConfigForCreating](https://help.aliyun.com/document_detail/383463.html) or [GenerateDISyncTaskConfigForUpdating](https://help.aliyun.com/document_detail/383464.html) operation to obtain the ID of an asynchronous thread and call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. Then, you can call the CreateDISyncTask or UpdateDISyncTask operation and use the parameters as request parameters to create or update a real-time synchronization task. DataWorks allows you to create or update real-time synchronization tasks in Data Integration only in asynchronous mode.
        

        @param request: QueryDISyncTaskConfigProcessResultRequest

        @return: QueryDISyncTaskConfigProcessResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_disync_task_config_process_result_with_options(request, runtime)

    def query_default_template_with_options(self, request, runtime):
        """
        @summary Queries the default data category and data sensitivity level template defined by Data Security Guard.
        

        @param request: QueryDefaultTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryDefaultTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDefaultTemplate',
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
            dataworks_public_20200518_models.QueryDefaultTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def query_default_template(self, request):
        """
        @summary Queries the default data category and data sensitivity level template defined by Data Security Guard.
        

        @param request: QueryDefaultTemplateRequest

        @return: QueryDefaultTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_default_template_with_options(request, runtime)

    def query_public_model_engine_with_options(self, request, runtime):
        """
        @summary Queries information about objects that are created in Data Modeling by using fast modeling language (FML) statements.
        
        @description    Each time you call this API operation, you must use FML statements to query information about objects that are created in Data Modeling.
        The information about the objects can be queried by page, except for data layers, business processes, and data domains. You can add an offset to the end of an FML statement. The num LIMIT num statement specifies the offset when the information about the objects is queried, and the number of pages to return each time. The offset value must be a multiple of the number of pages.
        A maximum of 1,000 entries can be returned each time you call this API operation.
        

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
        @summary Queries information about objects that are created in Data Modeling by using fast modeling language (FML) statements.
        
        @description    Each time you call this API operation, you must use FML statements to query information about objects that are created in Data Modeling.
        The information about the objects can be queried by page, except for data layers, business processes, and data domains. You can add an offset to the end of an FML statement. The num LIMIT num statement specifies the offset when the information about the objects is queried, and the number of pages to return each time. The offset value must be a multiple of the number of pages.
        A maximum of 1,000 entries can be returned each time you call this API operation.
        

        @param request: QueryPublicModelEngineRequest

        @return: QueryPublicModelEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_public_model_engine_with_options(request, runtime)

    def query_recognize_data_by_rule_type_with_options(self, request, runtime):
        """
        @summary Queries the type of a sensitive data identification rule.
        

        @param request: QueryRecognizeDataByRuleTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRecognizeDataByRuleTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.recognize_rules_type):
            body['RecognizeRulesType'] = request.recognize_rules_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRecognizeDataByRuleType',
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
            dataworks_public_20200518_models.QueryRecognizeDataByRuleTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_recognize_data_by_rule_type(self, request):
        """
        @summary Queries the type of a sensitive data identification rule.
        

        @param request: QueryRecognizeDataByRuleTypeRequest

        @return: QueryRecognizeDataByRuleTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_recognize_data_by_rule_type_with_options(request, runtime)

    def query_recognize_rule_detail_with_options(self, request, runtime):
        """
        @summary Queries the details of a specified sensitive field in Data Security Guard.
        

        @param request: QueryRecognizeRuleDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRecognizeRuleDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sensitive_name):
            body['SensitiveName'] = request.sensitive_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRecognizeRuleDetail',
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
            dataworks_public_20200518_models.QueryRecognizeRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_recognize_rule_detail(self, request):
        """
        @summary Queries the details of a specified sensitive field in Data Security Guard.
        

        @param request: QueryRecognizeRuleDetailRequest

        @return: QueryRecognizeRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_recognize_rule_detail_with_options(request, runtime)

    def query_recognize_rules_type_with_options(self, runtime):
        """
        @summary Queries the built-in sensitive data identification rule that is used to configure a sensitive field.
        

        @param request: QueryRecognizeRulesTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryRecognizeRulesTypeResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryRecognizeRulesType',
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
            dataworks_public_20200518_models.QueryRecognizeRulesTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_recognize_rules_type(self):
        """
        @summary Queries the built-in sensitive data identification rule that is used to configure a sensitive field.
        

        @return: QueryRecognizeRulesTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_recognize_rules_type_with_options(runtime)

    def query_sens_classification_with_options(self, request, runtime):
        """
        @summary Queries data categories.
        

        @param request: QuerySensClassificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuerySensClassificationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySensClassification',
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
            dataworks_public_20200518_models.QuerySensClassificationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sens_classification(self, request):
        """
        @summary Queries data categories.
        

        @param request: QuerySensClassificationRequest

        @return: QuerySensClassificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sens_classification_with_options(request, runtime)

    def query_sens_level_with_options(self, request, runtime):
        """
        @summary Queries data sensitivity levels in Data Security Guard.
        

        @param request: QuerySensLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuerySensLevelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySensLevel',
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
            dataworks_public_20200518_models.QuerySensLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sens_level(self, request):
        """
        @summary Queries data sensitivity levels in Data Security Guard.
        

        @param request: QuerySensLevelRequest

        @return: QuerySensLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sens_level_with_options(request, runtime)

    def query_sens_node_info_with_options(self, request, runtime):
        """
        @summary Queries sensitive data identification rules.
        

        @param request: QuerySensNodeInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QuerySensNodeInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sensitive_name):
            body['SensitiveName'] = request.sensitive_name
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySensNodeInfo',
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
            dataworks_public_20200518_models.QuerySensNodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sens_node_info(self, request):
        """
        @summary Queries sensitive data identification rules.
        

        @param request: QuerySensNodeInfoRequest

        @return: QuerySensNodeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sens_node_info_with_options(request, runtime)

    def register_lineage_relation_with_options(self, tmp_req, runtime):
        """
        @summary Registers the lineage between self-managed entities to DataWorks.
        
        @description This operation is in the trial phase. Users who need to call this operation can apply for it. The users can call this operation after the administrator adds the users to the trial list.
        

        @param tmp_req: RegisterLineageRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterLineageRelationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.RegisterLineageRelationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lineage_relation_register_vo):
            request.lineage_relation_register_voshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lineage_relation_register_vo, 'LineageRelationRegisterVO', 'json')
        body = {}
        if not UtilClient.is_unset(request.lineage_relation_register_voshrink):
            body['LineageRelationRegisterVO'] = request.lineage_relation_register_voshrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterLineageRelation',
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
            dataworks_public_20200518_models.RegisterLineageRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def register_lineage_relation(self, request):
        """
        @summary Registers the lineage between self-managed entities to DataWorks.
        
        @description This operation is in the trial phase. Users who need to call this operation can apply for it. The users can call this operation after the administrator adds the users to the trial list.
        

        @param request: RegisterLineageRelationRequest

        @return: RegisterLineageRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_lineage_relation_with_options(request, runtime)

    def remove_entity_tags_with_options(self, tmp_req, runtime):
        """
        @summary Removes tags from an entity. Only entities of the maxcompute-table type are supported.
        

        @param tmp_req: RemoveEntityTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveEntityTagsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.RemoveEntityTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not UtilClient.is_unset(request.qualified_name):
            query['QualifiedName'] = request.qualified_name
        body = {}
        if not UtilClient.is_unset(request.tag_keys_shrink):
            body['TagKeys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveEntityTags',
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
            dataworks_public_20200518_models.RemoveEntityTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_entity_tags(self, request):
        """
        @summary Removes tags from an entity. Only entities of the maxcompute-table type are supported.
        

        @param request: RemoveEntityTagsRequest

        @return: RemoveEntityTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_entity_tags_with_options(request, runtime)

    def remove_project_member_from_role_with_options(self, request, runtime):
        """
        @summary Removes a role from a user in a DataWorks workspace.
        

        @param request: RemoveProjectMemberFromRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveProjectMemberFromRoleResponse
        """
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
        """
        @summary Removes a role from a user in a DataWorks workspace.
        

        @param request: RemoveProjectMemberFromRoleRequest

        @return: RemoveProjectMemberFromRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_project_member_from_role_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        """
        @summary Restarts an instance.
        

        @param request: RestartInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartInstanceResponse
        """
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
        """
        @summary Restarts an instance.
        

        @param request: RestartInstanceRequest

        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def resume_instance_with_options(self, request, runtime):
        """
        @summary Resumes a suspended instance.
        

        @param request: ResumeInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeInstanceResponse
        """
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
        """
        @summary Resumes a suspended instance.
        

        @param request: ResumeInstanceRequest

        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    def revoke_column_permission_with_options(self, request, runtime):
        """
        @summary Revokes permissions on table fields from a user.
        

        @param request: RevokeColumnPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeColumnPermissionResponse
        """
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
        """
        @summary Revokes permissions on table fields from a user.
        

        @param request: RevokeColumnPermissionRequest

        @return: RevokeColumnPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_column_permission_with_options(request, runtime)

    def revoke_table_permission_with_options(self, request, runtime):
        """
        @summary Revokes permissions on a table from a user.
        

        @param request: RevokeTablePermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeTablePermissionResponse
        """
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
        """
        @summary Revokes permissions on a table from a user.
        

        @param request: RevokeTablePermissionRequest

        @return: RevokeTablePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_table_permission_with_options(request, runtime)

    def run_cycle_dag_nodes_with_options(self, request, runtime):
        """
        @summary Creates a workflow to backfill data.
        
        @description For more information about data backfill, see [Backfill data](https://help.aliyun.com/document_detail/137937.html).
        

        @param request: RunCycleDagNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunCycleDagNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_notice_type):
            body['AlertNoticeType'] = request.alert_notice_type
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.biz_begin_time):
            body['BizBeginTime'] = request.biz_begin_time
        if not UtilClient.is_unset(request.biz_end_time):
            body['BizEndTime'] = request.biz_end_time
        if not UtilClient.is_unset(request.concurrent_runs):
            body['ConcurrentRuns'] = request.concurrent_runs
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
        @summary Creates a workflow to backfill data.
        
        @description For more information about data backfill, see [Backfill data](https://help.aliyun.com/document_detail/137937.html).
        

        @param request: RunCycleDagNodesRequest

        @return: RunCycleDagNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_cycle_dag_nodes_with_options(request, runtime)

    def run_manual_dag_nodes_with_options(self, request, runtime):
        """
        @summary Runs nodes in a manually triggered workflow. Before you call this operation, make sure that the manually triggered workflow is committed and deployed. You can find a manually triggered workflow in Operation Center only after the manually triggered workflow is committed and deployed.
        

        @param request: RunManualDagNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunManualDagNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_date):
            body['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.dag_parameters):
            body['DagParameters'] = request.dag_parameters
        if not UtilClient.is_unset(request.end_biz_date):
            body['EndBizDate'] = request.end_biz_date
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
        if not UtilClient.is_unset(request.start_biz_date):
            body['StartBizDate'] = request.start_biz_date
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
        """
        @summary Runs nodes in a manually triggered workflow. Before you call this operation, make sure that the manually triggered workflow is committed and deployed. You can find a manually triggered workflow in Operation Center only after the manually triggered workflow is committed and deployed.
        

        @param request: RunManualDagNodesRequest

        @return: RunManualDagNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_manual_dag_nodes_with_options(request, runtime)

    def run_smoke_test_with_options(self, request, runtime):
        """
        @summary Creates a workflow to perform smoke testing.
        

        @param request: RunSmokeTestRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunSmokeTestResponse
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
        """
        @summary Creates a workflow to perform smoke testing.
        

        @param request: RunSmokeTestRequest

        @return: RunSmokeTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_smoke_test_with_options(request, runtime)

    def run_trigger_node_with_options(self, request, runtime):
        """
        @summary Runs a manually triggered node.
        

        @param request: RunTriggerNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunTriggerNodeResponse
        """
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
        """
        @summary Runs a manually triggered node.
        

        @param request: RunTriggerNodeRequest

        @return: RunTriggerNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_trigger_node_with_options(request, runtime)

    def save_data_service_api_test_result_with_options(self, request, runtime):
        """
        @summary Saves the test results of an API.
        

        @param request: SaveDataServiceApiTestResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SaveDataServiceApiTestResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.auto_generate):
            body['AutoGenerate'] = request.auto_generate
        if not UtilClient.is_unset(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.result_sample):
            body['ResultSample'] = request.result_sample
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDataServiceApiTestResult',
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
            dataworks_public_20200518_models.SaveDataServiceApiTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    def save_data_service_api_test_result(self, request):
        """
        @summary Saves the test results of an API.
        

        @param request: SaveDataServiceApiTestResultRequest

        @return: SaveDataServiceApiTestResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_data_service_api_test_result_with_options(request, runtime)

    def scan_sensitive_data_with_options(self, request, runtime):
        """
        @summary Checks whether input data contains sensitive data.
        

        @param request: ScanSensitiveDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScanSensitiveDataResponse
        """
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
        """
        @summary Checks whether input data contains sensitive data.
        

        @param request: ScanSensitiveDataRequest

        @return: ScanSensitiveDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scan_sensitive_data_with_options(request, runtime)

    def search_meta_tables_with_options(self, request, runtime):
        """
        @summary Queries metatables based on specific conditions.
        
        @description You can call this operation to query only metatables in a MaxCompute or E-MapReduce (EMR) compute engine.
        

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
        @summary Queries metatables based on specific conditions.
        
        @description You can call this operation to query only metatables in a MaxCompute or E-MapReduce (EMR) compute engine.
        

        @param request: SearchMetaTablesRequest

        @return: SearchMetaTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_meta_tables_with_options(request, runtime)

    def search_nodes_by_output_with_options(self, request, runtime):
        """
        @deprecated OpenAPI SearchNodesByOutput is deprecated
        
        @summary Queries a node based on the output.
        

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
        @deprecated OpenAPI SearchNodesByOutput is deprecated
        
        @summary Queries a node based on the output.
        

        @param request: SearchNodesByOutputRequest

        @return: SearchNodesByOutputResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.search_nodes_by_output_with_options(request, runtime)

    def set_data_source_share_with_options(self, request, runtime):
        """
        @deprecated OpenAPI SetDataSourceShare is deprecated
        
        @summary Shares a data source to a specific DataWorks workspace or a specific user.
        

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
        @deprecated OpenAPI SetDataSourceShare is deprecated
        
        @summary Shares a data source to a specific DataWorks workspace or a specific user.
        

        @param request: SetDataSourceShareRequest

        @return: SetDataSourceShareResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_source_share_with_options(request, runtime)

    def set_entity_tags_with_options(self, tmp_req, runtime):
        """
        @summary Configures tags for an entity. Only entities of the maxcompute-table type are supported.
        

        @param tmp_req: SetEntityTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetEntityTagsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.SetEntityTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.qualified_name):
            query['QualifiedName'] = request.qualified_name
        body = {}
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetEntityTags',
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
            dataworks_public_20200518_models.SetEntityTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_entity_tags(self, request):
        """
        @summary Configures tags for an entity. Only entities of the maxcompute-table type are supported.
        

        @param request: SetEntityTagsRequest

        @return: SetEntityTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_entity_tags_with_options(request, runtime)

    def set_success_instance_with_options(self, request, runtime):
        """
        @summary Sets the state of a failed instance to successful.
        

        @param request: SetSuccessInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetSuccessInstanceResponse
        """
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
        """
        @summary Sets the state of a failed instance to successful.
        

        @param request: SetSuccessInstanceRequest

        @return: SetSuccessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_success_instance_with_options(request, runtime)

    def start_dijob_with_options(self, tmp_req, runtime):
        """
        @summary Starts a synchronization task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        

        @param tmp_req: StartDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.StartDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.realtime_start_settings):
            request.realtime_start_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.realtime_start_settings, 'RealtimeStartSettings', 'json')
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        if not UtilClient.is_unset(request.force_to_rerun):
            body['ForceToRerun'] = request.force_to_rerun
        if not UtilClient.is_unset(request.realtime_start_settings_shrink):
            body['RealtimeStartSettings'] = request.realtime_start_settings_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartDIJob',
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
            dataworks_public_20200518_models.StartDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dijob(self, request):
        """
        @summary Starts a synchronization task of a new version. Only the following type of task is supported: real-time data synchronization from a MySQL database to Hologres.
        

        @param request: StartDIJobRequest

        @return: StartDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dijob_with_options(request, runtime)

    def start_disync_instance_with_options(self, request, runtime):
        """
        @summary Starts a real-time synchronization task or a synchronization solution.
        

        @param request: StartDISyncInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartDISyncInstanceResponse
        """
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
        """
        @summary Starts a real-time synchronization task or a synchronization solution.
        

        @param request: StartDISyncInstanceRequest

        @return: StartDISyncInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_disync_instance_with_options(request, runtime)

    def start_migration_with_options(self, request, runtime):
        """
        @summary Starts a migration task.
        

        @param request: StartMigrationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartMigrationResponse
        """
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
        """
        @summary Starts a migration task.
        

        @param request: StartMigrationRequest

        @return: StartMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_migration_with_options(request, runtime)

    def stop_dijob_with_options(self, request, runtime):
        """
        @summary Stops a new-version synchronization task. The following type of synchronization task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param request: StopDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopDIJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopDIJob',
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
            dataworks_public_20200518_models.StopDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dijob(self, request):
        """
        @summary Stops a new-version synchronization task. The following type of synchronization task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param request: StopDIJobRequest

        @return: StopDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dijob_with_options(request, runtime)

    def stop_disync_instance_with_options(self, request, runtime):
        """
        @summary Stops a real-time synchronization task.
        

        @param request: StopDISyncInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopDISyncInstanceResponse
        """
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
        """
        @summary Stops a real-time synchronization task.
        

        @param request: StopDISyncInstanceRequest

        @return: StopDISyncInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_disync_instance_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        """
        @summary Terminates an instance.
        

        @param request: StopInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopInstanceResponse
        """
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
        """
        @summary Terminates an instance.
        

        @param request: StopInstanceRequest

        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def submit_data_service_api_with_options(self, request, runtime):
        """
        @summary Submits an API in DataService Studio.
        

        @param request: SubmitDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitDataServiceApiResponse
        """
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
            action='SubmitDataServiceApi',
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
            dataworks_public_20200518_models.SubmitDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_data_service_api(self, request):
        """
        @summary Submits an API in DataService Studio.
        

        @param request: SubmitDataServiceApiRequest

        @return: SubmitDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_data_service_api_with_options(request, runtime)

    def submit_file_with_options(self, request, runtime):
        """
        @summary Commits a file to the development environment of the scheduling system to generate a task.
        

        @param request: SubmitFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitFileResponse
        """
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
        """
        @summary Commits a file to the development environment of the scheduling system to generate a task.
        

        @param request: SubmitFileRequest

        @return: SubmitFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    def suspend_instance_with_options(self, request, runtime):
        """
        @summary Suspends an instance.
        

        @param request: SuspendInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SuspendInstanceResponse
        """
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
        """
        @summary Suspends an instance.
        

        @param request: SuspendInstanceRequest

        @return: SuspendInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_instance_with_options(request, runtime)

    def terminate_disync_instance_with_options(self, request, runtime):
        """
        @summary Undeploys a real-time synchronization task.
        

        @param request: TerminateDISyncInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TerminateDISyncInstanceResponse
        """
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
        """
        @summary Undeploys a real-time synchronization task.
        

        @param request: TerminateDISyncInstanceRequest

        @return: TerminateDISyncInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_disync_instance_with_options(request, runtime)

    def test_data_service_api_with_options(self, request, runtime):
        """
        @summary Tests a DataService Studio API in asynchronous mode. You can call the GetDataServiceApiTest operation to query the test result.
        

        @param request: TestDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TestDataServiceApiResponse
        """
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
        """
        @summary Tests a DataService Studio API in asynchronous mode. You can call the GetDataServiceApiTest operation to query the test result.
        

        @param request: TestDataServiceApiRequest

        @return: TestDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.test_data_service_api_with_options(request, runtime)

    def test_network_connection_with_options(self, request, runtime):
        """
        @summary Tests the network connectivity between a data source and a resource group.
        

        @param request: TestNetworkConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TestNetworkConnectionResponse
        """
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
        """
        @summary Tests the network connectivity between a data source and a resource group.
        

        @param request: TestNetworkConnectionRequest

        @return: TestNetworkConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.test_network_connection_with_options(request, runtime)

    def top_ten_elapsed_time_instance_with_options(self, request, runtime):
        """
        @summary Queries the ranking of the running durations of instances.
        

        @param request: TopTenElapsedTimeInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TopTenElapsedTimeInstanceResponse
        """
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
        """
        @summary Queries the ranking of the running durations of instances.
        

        @param request: TopTenElapsedTimeInstanceRequest

        @return: TopTenElapsedTimeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.top_ten_elapsed_time_instance_with_options(request, runtime)

    def top_ten_error_times_instance_with_options(self, request, runtime):
        """
        @summary Queries the ranking of nodes on which errors occur within the previous month.
        

        @param request: TopTenErrorTimesInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TopTenErrorTimesInstanceResponse
        """
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
        """
        @summary Queries the ranking of nodes on which errors occur within the previous month.
        

        @param request: TopTenErrorTimesInstanceRequest

        @return: TopTenErrorTimesInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.top_ten_error_times_instance_with_options(request, runtime)

    def umount_directory_with_options(self, request, runtime):
        """
        @summary Removes a directory from the left-side navigation pane of DataAnalysis.
        

        @param request: UmountDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UmountDirectoryResponse
        """
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
        """
        @summary Removes a directory from the left-side navigation pane of DataAnalysis.
        

        @param request: UmountDirectoryRequest

        @return: UmountDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.umount_directory_with_options(request, runtime)

    def update_baseline_with_options(self, tmp_req, runtime):
        """
        @summary 更新基线
        

        @param tmp_req: UpdateBaselineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBaselineResponse
        """
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
        """
        @summary 更新基线
        

        @param request: UpdateBaselineRequest

        @return: UpdateBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_baseline_with_options(request, runtime)

    def update_business_with_options(self, request, runtime):
        """
        @summary Updates a workflow.
        

        @param request: UpdateBusinessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBusinessResponse
        """
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
        """
        @summary Updates a workflow.
        

        @param request: UpdateBusinessRequest

        @return: UpdateBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    def update_cluster_configs_with_options(self, tmp_req, runtime):
        """
        @summary 更新集群的配置信息
        

        @param tmp_req: UpdateClusterConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateClusterConfigsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.UpdateClusterConfigsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_values):
            request.config_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_values, 'ConfigValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.config_values_shrink):
            body['ConfigValues'] = request.config_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterConfigs',
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
            dataworks_public_20200518_models.UpdateClusterConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster_configs(self, request):
        """
        @summary 更新集群的配置信息
        

        @param request: UpdateClusterConfigsRequest

        @return: UpdateClusterConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_configs_with_options(request, runtime)

    def update_connection_with_options(self, request, runtime):
        """
        @deprecated OpenAPI UpdateConnection is deprecated
        
        @summary Updates a data source.
        

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
        @deprecated OpenAPI UpdateConnection is deprecated
        
        @summary Updates a data source.
        

        @param request: UpdateConnectionRequest

        @return: UpdateConnectionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    def update_dialarm_rule_with_options(self, tmp_req, runtime):
        """
        @summary Updates an alert rule for a new-version synchronization task. The following type of task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization. You must update all fields in the alert rule.
        

        @param tmp_req: UpdateDIAlarmRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDIAlarmRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.UpdateDIAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification_settings):
            request.notification_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification_settings, 'NotificationSettings', 'json')
        if not UtilClient.is_unset(tmp_req.trigger_conditions):
            request.trigger_conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trigger_conditions, 'TriggerConditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.dialarm_rule_id):
            body['DIAlarmRuleId'] = request.dialarm_rule_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.notification_settings_shrink):
            body['NotificationSettings'] = request.notification_settings_shrink
        if not UtilClient.is_unset(request.trigger_conditions_shrink):
            body['TriggerConditions'] = request.trigger_conditions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDIAlarmRule',
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
            dataworks_public_20200518_models.UpdateDIAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dialarm_rule(self, request):
        """
        @summary Updates an alert rule for a new-version synchronization task. The following type of task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        
        @description You can configure alert rules only for tasks that can be used for real-time data synchronization. You must update all fields in the alert rule.
        

        @param request: UpdateDIAlarmRuleRequest

        @return: UpdateDIAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dialarm_rule_with_options(request, runtime)

    def update_dijob_with_options(self, tmp_req, runtime):
        """
        @summary Updates a new-version synchronization task. The following type of task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param tmp_req: UpdateDIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDIJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20200518_models.UpdateDIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_settings):
            request.job_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_settings, 'JobSettings', 'json')
        if not UtilClient.is_unset(tmp_req.resource_settings):
            request.resource_settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_settings, 'ResourceSettings', 'json')
        if not UtilClient.is_unset(tmp_req.table_mappings):
            request.table_mappings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_mappings, 'TableMappings', 'json')
        if not UtilClient.is_unset(tmp_req.transformation_rules):
            request.transformation_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transformation_rules, 'TransformationRules', 'json')
        body = {}
        if not UtilClient.is_unset(request.dijob_id):
            body['DIJobId'] = request.dijob_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.job_settings_shrink):
            body['JobSettings'] = request.job_settings_shrink
        if not UtilClient.is_unset(request.resource_settings_shrink):
            body['ResourceSettings'] = request.resource_settings_shrink
        if not UtilClient.is_unset(request.table_mappings_shrink):
            body['TableMappings'] = request.table_mappings_shrink
        if not UtilClient.is_unset(request.transformation_rules_shrink):
            body['TransformationRules'] = request.transformation_rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDIJob',
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
            dataworks_public_20200518_models.UpdateDIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dijob(self, request):
        """
        @summary Updates a new-version synchronization task. The following type of task is supported: real-time synchronization of all data in a MySQL database to Hologres.
        

        @param request: UpdateDIJobRequest

        @return: UpdateDIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dijob_with_options(request, runtime)

    def update_diproject_config_with_options(self, request, runtime):
        """
        @summary Modifies the default global configuration of synchronization solutions in a DataWorks workspace.
        
        @description DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization tasks in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](https://help.aliyun.com/document_detail/199008.html).
        

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
        @summary Modifies the default global configuration of synchronization solutions in a DataWorks workspace.
        
        @description DataWorks allows you to specify a default global configuration only for the processing rules of DDL messages in synchronization solutions. After you configure the *processing rules of DDL messages** in synchronization solutions, the configuration is used as the default global configuration and applies to all real-time synchronization tasks in the solutions. You can modify the **processing rules of DDL messages** based on your business requirements. For more information about how to configure a synchronization solution, see [Synchronization solutions](https://help.aliyun.com/document_detail/199008.html).
        

        @param request: UpdateDIProjectConfigRequest

        @return: UpdateDIProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_diproject_config_with_options(request, runtime)

    def update_disync_task_with_options(self, request, runtime):
        """
        @summary Updates a data synchronization task.
        

        @param request: UpdateDISyncTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDISyncTaskResponse
        """
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
        """
        @summary Updates a data synchronization task.
        

        @param request: UpdateDISyncTaskRequest

        @return: UpdateDISyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_disync_task_with_options(request, runtime)

    def update_data_service_api_with_options(self, request, runtime):
        """
        @summary Updates the information about an API in the development state in DataService Studio.
        

        @param request: UpdateDataServiceApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDataServiceApiResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Updates the information about an API in the development state in DataService Studio.
        

        @param request: UpdateDataServiceApiRequest

        @return: UpdateDataServiceApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_service_api_with_options(request, runtime)

    def update_data_source_with_options(self, request, runtime):
        """
        @summary Updates a data source.
        

        @param request: UpdateDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDataSourceResponse
        """
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
        """
        @summary Updates a data source.
        

        @param request: UpdateDataSourceRequest

        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    def update_file_with_options(self, request, runtime):
        """
        @summary Updates a file.
        
        @description When you debug or call this operation, you must specify new values for the specified parameters to ensure that the values are different from the original configurations of the file. For example, if the original value of a parameter is A, you must change the value of this parameter to B before you commit the node. If you set the parameter to A, an exception that indicates invalid data occurs.
        

        @param request: UpdateFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_settings):
            body['AdvancedSettings'] = request.advanced_settings
        if not UtilClient.is_unset(request.apply_schedule_immediately):
            body['ApplyScheduleImmediately'] = request.apply_schedule_immediately
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
        if not UtilClient.is_unset(request.ignore_parent_skip_running_property):
            body['IgnoreParentSkipRunningProperty'] = request.ignore_parent_skip_running_property
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
        @summary Updates a file.
        
        @description When you debug or call this operation, you must specify new values for the specified parameters to ensure that the values are different from the original configurations of the file. For example, if the original value of a parameter is A, you must change the value of this parameter to B before you commit the node. If you set the parameter to A, an exception that indicates invalid data occurs.
        

        @param request: UpdateFileRequest

        @return: UpdateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        """
        @summary Updates a folder.
        

        @param request: UpdateFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFolderResponse
        """
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
        """
        @summary Updates a folder.
        

        @param request: UpdateFolderRequest

        @return: UpdateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_ideevent_result_with_options(self, request, runtime):
        """
        @summary Returns the check result of an extension point event to DataStudio after the extension point event is triggered during data development and checked by an extension.
        

        @param request: UpdateIDEEventResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateIDEEventResultResponse
        """
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
        """
        @summary Returns the check result of an extension point event to DataStudio after the extension point event is triggered during data development and checked by an extension.
        

        @param request: UpdateIDEEventResultRequest

        @return: UpdateIDEEventResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ideevent_result_with_options(request, runtime)

    def update_meta_category_with_options(self, request, runtime):
        """
        @summary Updates a category.
        

        @param request: UpdateMetaCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMetaCategoryResponse
        """
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
        """
        @summary Updates a category.
        

        @param request: UpdateMetaCategoryRequest

        @return: UpdateMetaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_meta_category_with_options(request, runtime)

    def update_meta_collection_with_options(self, request, runtime):
        """
        @summary Updates the name and comment of a collection.
        
        @description Only the name and comment of a collection can be updated.
        

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
        @summary Updates the name and comment of a collection.
        
        @description Only the name and comment of a collection can be updated.
        

        @param request: UpdateMetaCollectionRequest

        @return: UpdateMetaCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_meta_collection_with_options(request, runtime)

    def update_meta_table_with_options(self, request, runtime):
        """
        @summary Updates the metadata information about a table.
        

        @param request: UpdateMetaTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMetaTableResponse
        """
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
        """
        @summary Updates the metadata information about a table.
        

        @param request: UpdateMetaTableRequest

        @return: UpdateMetaTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_with_options(request, runtime)

    def update_meta_table_intro_wiki_with_options(self, request, runtime):
        """
        @summary Updates the instructions on how to use a table. If no instruction on how to use the table is available, the instructions that are configured by calling this operation are added.
        

        @param request: UpdateMetaTableIntroWikiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMetaTableIntroWikiResponse
        """
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
        """
        @summary Updates the instructions on how to use a table. If no instruction on how to use the table is available, the instructions that are configured by calling this operation are added.
        

        @param request: UpdateMetaTableIntroWikiRequest

        @return: UpdateMetaTableIntroWikiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_intro_wiki_with_options(request, runtime)

    def update_node_owner_with_options(self, request, runtime):
        """
        @summary Changes the owner of a node.
        

        @param request: UpdateNodeOwnerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateNodeOwnerResponse
        """
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
        """
        @summary Changes the owner of a node.
        

        @param request: UpdateNodeOwnerRequest

        @return: UpdateNodeOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_node_owner_with_options(request, runtime)

    def update_node_run_mode_with_options(self, request, runtime):
        """
        @summary Freezes or unfreezes a node.
        

        @param request: UpdateNodeRunModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateNodeRunModeResponse
        """
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
        """
        @summary Freezes or unfreezes a node.
        

        @param request: UpdateNodeRunModeRequest

        @return: UpdateNodeRunModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_node_run_mode_with_options(request, runtime)

    def update_quality_follower_with_options(self, request, runtime):
        """
        @summary Updates a subscription relationship.
        

        @param request: UpdateQualityFollowerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateQualityFollowerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_mode):
            body['AlarmMode'] = request.alarm_mode
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.follower_id):
            body['FollowerId'] = request.follower_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        """
        @summary Updates a subscription relationship.
        

        @param request: UpdateQualityFollowerRequest

        @return: UpdateQualityFollowerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_quality_follower_with_options(request, runtime)

    def update_quality_rule_with_options(self, request, runtime):
        """
        @summary Updates a monitoring rule.
        

        @param request: UpdateQualityRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateQualityRuleResponse
        """
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
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
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
        if not UtilClient.is_unset(request.task_setting):
            body['TaskSetting'] = request.task_setting
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
        """
        @summary Updates a monitoring rule.
        

        @param request: UpdateQualityRuleRequest

        @return: UpdateQualityRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_quality_rule_with_options(request, runtime)

    def update_remind_with_options(self, request, runtime):
        """
        @summary Modifies a custom alert rule.
        

        @param request: UpdateRemindRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRemindResponse
        """
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
        """
        @summary Modifies a custom alert rule.
        

        @param request: UpdateRemindRequest

        @return: UpdateRemindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_remind_with_options(request, runtime)

    def update_table_with_options(self, request, runtime):
        """
        @summary Updates a MaxCompute table.
        

        @param request: UpdateTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableResponse
        """
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
        """
        @summary Updates a MaxCompute table.
        

        @param request: UpdateTableRequest

        @return: UpdateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    def update_table_add_column_with_options(self, request, runtime):
        """
        @summary Updates the fields in a MaxCompute table.
        

        @param request: UpdateTableAddColumnRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableAddColumnResponse
        """
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
        """
        @summary Updates the fields in a MaxCompute table.
        

        @param request: UpdateTableAddColumnRequest

        @return: UpdateTableAddColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_table_add_column_with_options(request, runtime)

    def update_table_level_with_options(self, request, runtime):
        """
        @summary Updates a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: UpdateTableLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableLevelResponse
        """
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
        """
        @summary Updates a table level. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: UpdateTableLevelRequest

        @return: UpdateTableLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_table_level_with_options(request, runtime)

    def update_table_model_info_with_options(self, request, runtime):
        """
        @summary Modifies the information about a table, such as the table folder, level, and category.
        

        @param request: UpdateTableModelInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableModelInfoResponse
        """
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
        """
        @summary Modifies the information about a table, such as the table folder, level, and category.
        

        @param request: UpdateTableModelInfoRequest

        @return: UpdateTableModelInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_table_model_info_with_options(request, runtime)

    def update_table_theme_with_options(self, request, runtime):
        """
        @summary Updates a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: UpdateTableThemeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTableThemeResponse
        """
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
        """
        @summary Updates a table theme. This operation will be replaced soon. We recommend that you do not call this operation.
        

        @param request: UpdateTableThemeRequest

        @return: UpdateTableThemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_table_theme_with_options(request, runtime)

    def update_udf_file_with_options(self, request, runtime):
        """

        @param request: UpdateUdfFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateUdfFileResponse
        """
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
        """

        @param request: UpdateUdfFileRequest

        @return: UpdateUdfFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)

    def update_workbench_event_result_with_options(self, request, runtime):
        """
        @summary Returns the processing result sent by an extension after a process in Operation Center is blocked by the extension.
        

        @param request: UpdateWorkbenchEventResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateWorkbenchEventResultResponse
        """
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
        """
        @summary Returns the processing result sent by an extension after a process in Operation Center is blocked by the extension.
        

        @param request: UpdateWorkbenchEventResultRequest

        @return: UpdateWorkbenchEventResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workbench_event_result_with_options(request, runtime)
