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
from RPC import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AbolishDataServiceApiResponse(),
            self.do_rpcrequest('AbolishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abolish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abolish_data_service_api_with_options(request, runtime)

    def add_project_member_to_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddProjectMemberToRoleResponse(),
            self.do_rpcrequest('AddProjectMemberToRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_project_member_to_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_project_member_to_role_with_options(request, runtime)

    def add_to_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddToMetaCategoryResponse(),
            self.do_rpcrequest('AddToMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_to_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_to_meta_category_with_options(request, runtime)

    def approve_permission_apply_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse(),
            self.do_rpcrequest('ApprovePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_permission_apply_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.approve_permission_apply_order_with_options(request, runtime)

    def check_engine_meta_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaPartitionResponse(),
            self.do_rpcrequest('CheckEngineMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_engine_meta_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_engine_meta_partition_with_options(request, runtime)

    def check_engine_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaTableResponse(),
            self.do_rpcrequest('CheckEngineMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_engine_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_engine_meta_table_with_options(request, runtime)

    def check_file_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckFileDeploymentResponse(),
            self.do_rpcrequest('CheckFileDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_file_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_file_deployment_with_options(request, runtime)

    def check_meta_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaPartitionResponse(),
            self.do_rpcrequest('CheckMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_partition_with_options(request, runtime)

    def check_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableResponse(),
            self.do_rpcrequest('CheckMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_with_options(request, runtime)

    def check_meta_table_task_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableTaskResponse(),
            self.do_rpcrequest('CheckMetaTableTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_table_task(self):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_task_with_options(runtime)

    def create_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateBusinessResponse(),
            self.do_rpcrequest('CreateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_business_with_options(request, runtime)

    def create_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateConnectionResponse(),
            self.do_rpcrequest('CreateConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    def create_dag_complement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagComplementResponse(),
            self.do_rpcrequest('CreateDagComplement', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dag_complement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dag_complement_with_options(request, runtime)

    def create_dag_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagTestResponse(),
            self.do_rpcrequest('CreateDagTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dag_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dag_test_with_options(request, runtime)

    def create_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiResponse(),
            self.do_rpcrequest('CreateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    def create_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse(),
            self.do_rpcrequest('CreateDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_authority_with_options(request, runtime)

    def create_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceFolderResponse(),
            self.do_rpcrequest('CreateDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_folder_with_options(request, runtime)

    def create_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceGroupResponse(),
            self.do_rpcrequest('CreateDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_group_with_options(request, runtime)

    def create_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataSourceResponse(),
            self.do_rpcrequest('CreateDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    def create_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDISyncTaskResponse(),
            self.do_rpcrequest('CreateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disync_task_with_options(request, runtime)

    def create_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFileResponse(),
            self.do_rpcrequest('CreateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFolderResponse(),
            self.do_rpcrequest('CreateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_import_migration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateImportMigrationResponse(),
            self.do_rpcrequest('CreateImportMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_import_migration(self, request):
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
        auth_config = rpc_models.Config(
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
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.package_file_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            create_import_migration_req.package_file = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.bucket), TeaConverter.to_unicode(auth_response.endpoint), TeaConverter.to_unicode(auth_response.object_key))
        create_import_migration_resp = self.create_import_migration_with_options(create_import_migration_req, runtime)
        return create_import_migration_resp

    def create_manual_dag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateManualDagResponse(),
            self.do_rpcrequest('CreateManualDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_manual_dag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    def create_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateMetaCategoryResponse(),
            self.do_rpcrequest('CreateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_meta_category_with_options(request, runtime)

    def create_permission_apply_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreatePermissionApplyOrderResponse(),
            self.do_rpcrequest('CreatePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_permission_apply_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_permission_apply_order_with_options(request, runtime)

    def create_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateProjectMemberResponse(),
            self.do_rpcrequest('CreateProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    def create_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityEntityResponse(),
            self.do_rpcrequest('CreateQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_entity_with_options(request, runtime)

    def create_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityFollowerResponse(),
            self.do_rpcrequest('CreateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_follower_with_options(request, runtime)

    def create_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRelativeNodeResponse(),
            self.do_rpcrequest('CreateQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_relative_node_with_options(request, runtime)

    def create_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRuleResponse(),
            self.do_rpcrequest('CreateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    def create_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateRemindResponse(),
            self.do_rpcrequest('CreateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_remind_with_options(request, runtime)

    def create_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableResponse(),
            self.do_rpcrequest('CreateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    def create_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableLevelResponse(),
            self.do_rpcrequest('CreateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_level_with_options(request, runtime)

    def create_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableThemeResponse(),
            self.do_rpcrequest('CreateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_theme_with_options(request, runtime)

    def create_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateUdfFileResponse(),
            self.do_rpcrequest('CreateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    def create_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateViewResponse(),
            self.do_rpcrequest('CreateView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_view_with_options(request, runtime)

    def delete_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteBusinessResponse(),
            self.do_rpcrequest('DeleteBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    def delete_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteConnectionResponse(),
            self.do_rpcrequest('DeleteConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    def delete_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiResponse(),
            self.do_rpcrequest('DeleteDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_with_options(request, runtime)

    def delete_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse(),
            self.do_rpcrequest('DeleteDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_authority_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataSourceResponse(),
            self.do_rpcrequest('DeleteDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDISyncTaskResponse(),
            self.do_rpcrequest('DeleteDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disync_task_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFileResponse(),
            self.do_rpcrequest('DeleteFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFolderResponse(),
            self.do_rpcrequest('DeleteFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_from_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFromMetaCategoryResponse(),
            self.do_rpcrequest('DeleteFromMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_from_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_from_meta_category_with_options(request, runtime)

    def delete_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCategoryResponse(),
            self.do_rpcrequest('DeleteMetaCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_category_with_options(request, runtime)

    def delete_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteProjectMemberResponse(),
            self.do_rpcrequest('DeleteProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    def delete_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityEntityResponse(),
            self.do_rpcrequest('DeleteQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_entity_with_options(request, runtime)

    def delete_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityFollowerResponse(),
            self.do_rpcrequest('DeleteQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_follower_with_options(request, runtime)

    def delete_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse(),
            self.do_rpcrequest('DeleteQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_relative_node_with_options(request, runtime)

    def delete_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRuleResponse(),
            self.do_rpcrequest('DeleteQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    def delete_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteRemindResponse(),
            self.do_rpcrequest('DeleteRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_remind_with_options(request, runtime)

    def delete_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableResponse(),
            self.do_rpcrequest('DeleteTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    def delete_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableLevelResponse(),
            self.do_rpcrequest('DeleteTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_level_with_options(request, runtime)

    def delete_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableThemeResponse(),
            self.do_rpcrequest('DeleteTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_theme_with_options(request, runtime)

    def delete_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteViewResponse(),
            self.do_rpcrequest('DeleteView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_view_with_options(request, runtime)

    def deploy_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployDISyncTaskResponse(),
            self.do_rpcrequest('DeployDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_disync_task_with_options(request, runtime)

    def deploy_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployFileResponse(),
            self.do_rpcrequest('DeployFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    def desensitize_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DesensitizeDataResponse(),
            self.do_rpcrequest('DesensitizeData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def desensitize_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.desensitize_data_with_options(request, runtime)

    def establish_relation_table_to_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse(),
            self.do_rpcrequest('EstablishRelationTableToBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def establish_relation_table_to_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    def export_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportConnectionsResponse(),
            self.do_rpcrequest('ExportConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def export_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_connections_with_options(request, runtime)

    def export_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDataSourcesResponse(),
            self.do_rpcrequest('ExportDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def export_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_data_sources_with_options(request, runtime)

    def export_disync_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDISyncTasksResponse(),
            self.do_rpcrequest('ExportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_disync_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_disync_tasks_with_options(request, runtime)

    def generate_disync_task_config_for_creating_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse(),
            self.do_rpcrequest('GenerateDISyncTaskConfigForCreating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_disync_task_config_for_creating(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_creating_with_options(request, runtime)

    def generate_disync_task_config_for_updating_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse(),
            self.do_rpcrequest('GenerateDISyncTaskConfigForUpdating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_disync_task_config_for_updating(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_updating_with_options(request, runtime)

    def get_baseline_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineConfigResponse(),
            self.do_rpcrequest('GetBaselineConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_config_with_options(request, runtime)

    def get_baseline_key_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineKeyPathResponse(),
            self.do_rpcrequest('GetBaselineKeyPath', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_key_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_key_path_with_options(request, runtime)

    def get_baseline_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineStatusResponse(),
            self.do_rpcrequest('GetBaselineStatus', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_status_with_options(request, runtime)

    def get_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBusinessResponse(),
            self.do_rpcrequest('GetBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    def get_connection_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetConnectionMetaResponse(),
            self.do_rpcrequest('GetConnectionMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_connection_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_meta_with_options(request, runtime)

    def get_dag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDagResponse(),
            self.do_rpcrequest('GetDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dag_with_options(request, runtime)

    def get_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApiResponse(),
            self.do_rpcrequest('GetDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_with_options(request, runtime)

    def get_data_service_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApplicationResponse(),
            self.do_rpcrequest('GetDataServiceApplication', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_application_with_options(request, runtime)

    def get_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceFolderResponse(),
            self.do_rpcrequest('GetDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_folder_with_options(request, runtime)

    def get_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceGroupResponse(),
            self.do_rpcrequest('GetDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_group_with_options(request, runtime)

    def get_data_service_published_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServicePublishedApiResponse(),
            self.do_rpcrequest('GetDataServicePublishedApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_published_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_published_api_with_options(request, runtime)

    def get_data_source_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataSourceMetaResponse(),
            self.do_rpcrequest('GetDataSourceMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_source_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_meta_with_options(request, runtime)

    def get_ddljob_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDDLJobStatusResponse(),
            self.do_rpcrequest('GetDDLJobStatus', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ddljob_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ddljob_status_with_options(request, runtime)

    def get_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDeploymentResponse(),
            self.do_rpcrequest('GetDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    def get_disync_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncInstanceInfoResponse(),
            self.do_rpcrequest('GetDISyncInstanceInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_disync_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_instance_info_with_options(request, runtime)

    def get_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskResponse(),
            self.do_rpcrequest('GetDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_with_options(request, runtime)

    def get_disync_task_metric_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse(),
            self.do_rpcrequest('GetDISyncTaskMetricInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_disync_task_metric_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_metric_info_with_options(request, runtime)

    def get_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileResponse(),
            self.do_rpcrequest('GetFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    def get_file_type_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileTypeStatisticResponse(),
            self.do_rpcrequest('GetFileTypeStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_type_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_type_statistic_with_options(request, runtime)

    def get_file_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileVersionResponse(),
            self.do_rpcrequest('GetFileVersion', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    def get_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFolderResponse(),
            self.do_rpcrequest('GetFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceResponse(),
            self.do_rpcrequest('GetInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_instance_consume_time_rank_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse(),
            self.do_rpcrequest('GetInstanceConsumeTimeRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_consume_time_rank(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_consume_time_rank_with_options(request, runtime)

    def get_instance_count_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceCountTrendResponse(),
            self.do_rpcrequest('GetInstanceCountTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_count_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_trend_with_options(request, runtime)

    def get_instance_error_rank_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceErrorRankResponse(),
            self.do_rpcrequest('GetInstanceErrorRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_error_rank(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_error_rank_with_options(request, runtime)

    def get_instance_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceLogResponse(),
            self.do_rpcrequest('GetInstanceLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_log_with_options(request, runtime)

    def get_instance_status_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusCountResponse(),
            self.do_rpcrequest('GetInstanceStatusCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_status_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_count_with_options(request, runtime)

    def get_instance_status_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusStatisticResponse(),
            self.do_rpcrequest('GetInstanceStatusStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_status_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_statistic_with_options(request, runtime)

    def get_manual_dag_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetManualDagInstancesResponse(),
            self.do_rpcrequest('GetManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_manual_dag_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_manual_dag_instances_with_options(request, runtime)

    def get_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaCategoryResponse(),
            self.do_rpcrequest('GetMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_category_with_options(request, runtime)

    def get_meta_column_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaColumnLineageResponse(),
            self.do_rpcrequest('GetMetaColumnLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_column_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_column_lineage_with_options(request, runtime)

    def get_meta_dbinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBInfoResponse(),
            self.do_rpcrequest('GetMetaDBInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_dbinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbinfo_with_options(request, runtime)

    def get_meta_dbtable_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBTableListResponse(),
            self.do_rpcrequest('GetMetaDBTableList', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_dbtable_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbtable_list_with_options(request, runtime)

    def get_meta_table_basic_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableBasicInfoResponse(),
            self.do_rpcrequest('GetMetaTableBasicInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_basic_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_basic_info_with_options(request, runtime)

    def get_meta_table_change_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableChangeLogResponse(),
            self.do_rpcrequest('GetMetaTableChangeLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_change_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_change_log_with_options(request, runtime)

    def get_meta_table_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableColumnResponse(),
            self.do_rpcrequest('GetMetaTableColumn', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    def get_meta_table_full_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableFullInfoResponse(),
            self.do_rpcrequest('GetMetaTableFullInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_full_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_full_info_with_options(request, runtime)

    def get_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableIntroWikiResponse(),
            self.do_rpcrequest('GetMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_intro_wiki_with_options(request, runtime)

    def get_meta_table_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableLineageResponse(),
            self.do_rpcrequest('GetMetaTableLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_lineage_with_options(request, runtime)

    def get_meta_table_list_by_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableListByCategoryResponse(),
            self.do_rpcrequest('GetMetaTableListByCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_list_by_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_list_by_category_with_options(request, runtime)

    def get_meta_table_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableOutputResponse(),
            self.do_rpcrequest('GetMetaTableOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_output_with_options(request, runtime)

    def get_meta_table_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTablePartitionResponse(),
            self.do_rpcrequest('GetMetaTablePartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_partition_with_options(request, runtime)

    def get_meta_table_theme_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableThemeLevelResponse(),
            self.do_rpcrequest('GetMetaTableThemeLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_theme_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_theme_level_with_options(request, runtime)

    def get_migration_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMigrationProcessResponse(),
            self.do_rpcrequest('GetMigrationProcess', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_migration_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_migration_process_with_options(request, runtime)

    def get_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeResponse(),
            self.do_rpcrequest('GetNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    def get_node_children_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeChildrenResponse(),
            self.do_rpcrequest('GetNodeChildren', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_children(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_children_with_options(request, runtime)

    def get_node_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeCodeResponse(),
            self.do_rpcrequest('GetNodeCode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_code_with_options(request, runtime)

    def get_node_on_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeOnBaselineResponse(),
            self.do_rpcrequest('GetNodeOnBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_on_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_on_baseline_with_options(request, runtime)

    def get_node_parents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeParentsResponse(),
            self.do_rpcrequest('GetNodeParents', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_parents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_parents_with_options(request, runtime)

    def get_node_type_list_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeTypeListInfoResponse(),
            self.do_rpcrequest('GetNodeTypeListInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_type_list_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_type_list_info_with_options(request, runtime)

    def get_op_risk_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpRiskDataResponse(),
            self.do_rpcrequest('GetOpRiskData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_op_risk_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_op_risk_data_with_options(request, runtime)

    def get_op_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpSensitiveDataResponse(),
            self.do_rpcrequest('GetOpSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_op_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_op_sensitive_data_with_options(request, runtime)

    def get_permission_apply_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse(),
            self.do_rpcrequest('GetPermissionApplyOrderDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_permission_apply_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_permission_apply_order_detail_with_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def get_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectDetailResponse(),
            self.do_rpcrequest('GetProjectDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_detail_with_options(request, runtime)

    def get_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityEntityResponse(),
            self.do_rpcrequest('GetQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_entity_with_options(request, runtime)

    def get_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityFollowerResponse(),
            self.do_rpcrequest('GetQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_follower_with_options(request, runtime)

    def get_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityRuleResponse(),
            self.do_rpcrequest('GetQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    def get_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetRemindResponse(),
            self.do_rpcrequest('GetRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_remind_with_options(request, runtime)

    def get_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSensitiveDataResponse(),
            self.do_rpcrequest('GetSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sensitive_data_with_options(request, runtime)

    def get_success_instance_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSuccessInstanceTrendResponse(),
            self.do_rpcrequest('GetSuccessInstanceTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_success_instance_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_success_instance_trend_with_options(request, runtime)

    def get_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicResponse(),
            self.do_rpcrequest('GetTopic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    def get_topic_influence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicInfluenceResponse(),
            self.do_rpcrequest('GetTopicInfluence', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_influence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_influence_with_options(request, runtime)

    def import_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportConnectionsResponse(),
            self.do_rpcrequest('ImportConnections', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_connections_with_options(request, runtime)

    def import_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDataSourcesResponse(),
            self.do_rpcrequest('ImportDataSources', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_data_sources_with_options(request, runtime)

    def import_disync_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDISyncTasksResponse(),
            self.do_rpcrequest('ImportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_disync_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_disync_tasks_with_options(request, runtime)

    def list_alert_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListAlertMessagesResponse(),
            self.do_rpcrequest('ListAlertMessages', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_alert_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alert_messages_with_options(request, runtime)

    def list_baseline_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineConfigsResponse(),
            self.do_rpcrequest('ListBaselineConfigs', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_baseline_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_configs_with_options(request, runtime)

    def list_baseline_statuses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineStatusesResponse(),
            self.do_rpcrequest('ListBaselineStatuses', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_baseline_statuses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_statuses_with_options(request, runtime)

    def list_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBusinessResponse(),
            self.do_rpcrequest('ListBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    def list_calc_engines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListCalcEnginesResponse(),
            self.do_rpcrequest('ListCalcEngines', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_calc_engines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_calc_engines_with_options(request, runtime)

    def list_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListConnectionsResponse(),
            self.do_rpcrequest('ListConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    def list_data_service_api_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse(),
            self.do_rpcrequest('ListDataServiceApiAuthorities', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_api_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_authorities_with_options(request, runtime)

    def list_data_service_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApisResponse(),
            self.do_rpcrequest('ListDataServiceApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_apis_with_options(request, runtime)

    def list_data_service_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApplicationsResponse(),
            self.do_rpcrequest('ListDataServiceApplications', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_applications_with_options(request, runtime)

    def list_data_service_authorized_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse(),
            self.do_rpcrequest('ListDataServiceAuthorizedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_authorized_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_authorized_apis_with_options(request, runtime)

    def list_data_service_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceFoldersResponse(),
            self.do_rpcrequest('ListDataServiceFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_folders_with_options(request, runtime)

    def list_data_service_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceGroupsResponse(),
            self.do_rpcrequest('ListDataServiceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_groups_with_options(request, runtime)

    def list_data_service_published_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServicePublishedApisResponse(),
            self.do_rpcrequest('ListDataServicePublishedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_published_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    def list_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataSourcesResponse(),
            self.do_rpcrequest('ListDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    def list_diproject_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDIProjectConfigResponse(),
            self.do_rpcrequest('ListDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_diproject_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_diproject_config_with_options(request, runtime)

    def list_disync_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDISyncTasksResponse(),
            self.do_rpcrequest('ListDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_disync_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_disync_tasks_with_options(request, runtime)

    def list_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFilesResponse(),
            self.do_rpcrequest('ListFiles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    def list_file_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileTypeResponse(),
            self.do_rpcrequest('ListFileType', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_file_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_type_with_options(request, runtime)

    def list_file_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileVersionsResponse(),
            self.do_rpcrequest('ListFileVersions', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_file_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    def list_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFoldersResponse(),
            self.do_rpcrequest('ListFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    def list_instance_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstanceAmountResponse(),
            self.do_rpcrequest('ListInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instance_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_amount_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_manual_dag_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListManualDagInstancesResponse(),
            self.do_rpcrequest('ListManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_manual_dag_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_manual_dag_instances_with_options(request, runtime)

    def list_meta_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaDBResponse(),
            self.do_rpcrequest('ListMetaDB', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_meta_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_meta_dbwith_options(request, runtime)

    def list_node_input_or_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeInputOrOutputResponse(),
            self.do_rpcrequest('ListNodeInputOrOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_node_input_or_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_input_or_output_with_options(request, runtime)

    def list_node_iowith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeIOResponse(),
            self.do_rpcrequest('ListNodeIO', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_node_io(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_iowith_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesResponse(),
            self.do_rpcrequest('ListNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_nodes_by_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByBaselineResponse(),
            self.do_rpcrequest('ListNodesByBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_baseline_with_options(request, runtime)

    def list_nodes_by_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByOutputResponse(),
            self.do_rpcrequest('ListNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_output_with_options(request, runtime)

    def list_permission_apply_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListPermissionApplyOrdersResponse(),
            self.do_rpcrequest('ListPermissionApplyOrders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_permission_apply_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_permission_apply_orders_with_options(request, runtime)

    def list_program_type_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProgramTypeCountResponse(),
            self.do_rpcrequest('ListProgramTypeCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_program_type_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_program_type_count_with_options(request, runtime)

    def list_project_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectIdsResponse(),
            self.do_rpcrequest('ListProjectIds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_ids_with_options(request, runtime)

    def list_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectMembersResponse(),
            self.do_rpcrequest('ListProjectMembers', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    def list_project_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectRolesResponse(),
            self.do_rpcrequest('ListProjectRoles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_quality_results_by_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByEntityResponse(),
            self.do_rpcrequest('ListQualityResultsByEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_results_by_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_entity_with_options(request, runtime)

    def list_quality_results_by_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByRuleResponse(),
            self.do_rpcrequest('ListQualityResultsByRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_results_by_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_rule_with_options(request, runtime)

    def list_quality_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityRulesResponse(),
            self.do_rpcrequest('ListQualityRules', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    def list_ref_disync_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRefDISyncTasksResponse(),
            self.do_rpcrequest('ListRefDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ref_disync_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ref_disync_tasks_with_options(request, runtime)

    def list_reminds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRemindsResponse(),
            self.do_rpcrequest('ListReminds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_reminds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_reminds_with_options(request, runtime)

    def list_resource_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListResourceGroupsResponse(),
            self.do_rpcrequest('ListResourceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_success_instance_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListSuccessInstanceAmountResponse(),
            self.do_rpcrequest('ListSuccessInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_success_instance_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_success_instance_amount_with_options(request, runtime)

    def list_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableLevelResponse(),
            self.do_rpcrequest('ListTableLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_level_with_options(request, runtime)

    def list_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableThemeResponse(),
            self.do_rpcrequest('ListTableTheme', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_theme_with_options(request, runtime)

    def list_topics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTopicsResponse(),
            self.do_rpcrequest('ListTopics', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_topics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    def publish_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.PublishDataServiceApiResponse(),
            self.do_rpcrequest('PublishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    def query_disync_task_config_process_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse(),
            self.do_rpcrequest('QueryDISyncTaskConfigProcessResult', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_disync_task_config_process_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_disync_task_config_process_result_with_options(request, runtime)

    def query_public_model_engine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryPublicModelEngineResponse(),
            self.do_rpcrequest('QueryPublicModelEngine', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_public_model_engine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_public_model_engine_with_options(request, runtime)

    def remove_project_member_from_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse(),
            self.do_rpcrequest('RemoveProjectMemberFromRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_project_member_from_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_project_member_from_role_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RestartInstanceResponse(),
            self.do_rpcrequest('RestartInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def resume_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ResumeInstanceResponse(),
            self.do_rpcrequest('ResumeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    def revoke_column_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeColumnPermissionResponse(),
            self.do_rpcrequest('RevokeColumnPermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_column_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_column_permission_with_options(request, runtime)

    def revoke_table_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeTablePermissionResponse(),
            self.do_rpcrequest('RevokeTablePermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_table_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_table_permission_with_options(request, runtime)

    def run_cycle_dag_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunCycleDagNodesResponse(),
            self.do_rpcrequest('RunCycleDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cycle_dag_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cycle_dag_nodes_with_options(request, runtime)

    def run_manual_dag_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunManualDagNodesResponse(),
            self.do_rpcrequest('RunManualDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_manual_dag_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_manual_dag_nodes_with_options(request, runtime)

    def run_smoke_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunSmokeTestResponse(),
            self.do_rpcrequest('RunSmokeTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_smoke_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_smoke_test_with_options(request, runtime)

    def run_trigger_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunTriggerNodeResponse(),
            self.do_rpcrequest('RunTriggerNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_trigger_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_trigger_node_with_options(request, runtime)

    def scan_sensitive_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ScanSensitiveDataResponse(),
            self.do_rpcrequest('ScanSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def scan_sensitive_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scan_sensitive_data_with_options(request, runtime)

    def search_meta_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchMetaTablesResponse(),
            self.do_rpcrequest('SearchMetaTables', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_meta_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_meta_tables_with_options(request, runtime)

    def search_nodes_by_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchNodesByOutputResponse(),
            self.do_rpcrequest('SearchNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_nodes_by_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_nodes_by_output_with_options(request, runtime)

    def set_connection_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetConnectionShareResponse(),
            self.do_rpcrequest('SetConnectionShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_connection_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_connection_share_with_options(request, runtime)

    def set_data_source_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetDataSourceShareResponse(),
            self.do_rpcrequest('SetDataSourceShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_data_source_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_source_share_with_options(request, runtime)

    def set_success_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetSuccessInstanceResponse(),
            self.do_rpcrequest('SetSuccessInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_success_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_success_instance_with_options(request, runtime)

    def start_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartDISyncInstanceResponse(),
            self.do_rpcrequest('StartDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disync_instance_with_options(request, runtime)

    def start_migration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartMigrationResponse(),
            self.do_rpcrequest('StartMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_migration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_migration_with_options(request, runtime)

    def stop_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopDISyncInstanceResponse(),
            self.do_rpcrequest('StopDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disync_instance_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopInstanceResponse(),
            self.do_rpcrequest('StopInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def submit_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SubmitFileResponse(),
            self.do_rpcrequest('SubmitFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    def suspend_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SuspendInstanceResponse(),
            self.do_rpcrequest('SuspendInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_instance_with_options(request, runtime)

    def terminate_disync_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TerminateDISyncInstanceResponse(),
            self.do_rpcrequest('TerminateDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_disync_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_disync_instance_with_options(request, runtime)

    def test_network_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TestNetworkConnectionResponse(),
            self.do_rpcrequest('TestNetworkConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_network_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_network_connection_with_options(request, runtime)

    def top_ten_elapsed_time_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse(),
            self.do_rpcrequest('TopTenElapsedTimeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def top_ten_elapsed_time_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.top_ten_elapsed_time_instance_with_options(request, runtime)

    def top_ten_error_times_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse(),
            self.do_rpcrequest('TopTenErrorTimesInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def top_ten_error_times_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.top_ten_error_times_instance_with_options(request, runtime)

    def update_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateBusinessResponse(),
            self.do_rpcrequest('UpdateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    def update_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateConnectionResponse(),
            self.do_rpcrequest('UpdateConnection', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    def update_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataServiceApiResponse(),
            self.do_rpcrequest('UpdateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_service_api_with_options(request, runtime)

    def update_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataSourceResponse(),
            self.do_rpcrequest('UpdateDataSource', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    def update_diproject_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDIProjectConfigResponse(),
            self.do_rpcrequest('UpdateDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_diproject_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_diproject_config_with_options(request, runtime)

    def update_disync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDISyncTaskResponse(),
            self.do_rpcrequest('UpdateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_disync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_disync_task_with_options(request, runtime)

    def update_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFileResponse(),
            self.do_rpcrequest('UpdateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFolderResponse(),
            self.do_rpcrequest('UpdateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaCategoryResponse(),
            self.do_rpcrequest('UpdateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_category_with_options(request, runtime)

    def update_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableResponse(),
            self.do_rpcrequest('UpdateMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_with_options(request, runtime)

    def update_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse(),
            self.do_rpcrequest('UpdateMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_intro_wiki_with_options(request, runtime)

    def update_node_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeOwnerResponse(),
            self.do_rpcrequest('UpdateNodeOwner', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_node_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_node_owner_with_options(request, runtime)

    def update_node_run_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeRunModeResponse(),
            self.do_rpcrequest('UpdateNodeRunMode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_node_run_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_node_run_mode_with_options(request, runtime)

    def update_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityFollowerResponse(),
            self.do_rpcrequest('UpdateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_follower_with_options(request, runtime)

    def update_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityRuleResponse(),
            self.do_rpcrequest('UpdateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_rule_with_options(request, runtime)

    def update_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateRemindResponse(),
            self.do_rpcrequest('UpdateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_remind_with_options(request, runtime)

    def update_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableResponse(),
            self.do_rpcrequest('UpdateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    def update_table_add_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableAddColumnResponse(),
            self.do_rpcrequest('UpdateTableAddColumn', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_add_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_add_column_with_options(request, runtime)

    def update_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableLevelResponse(),
            self.do_rpcrequest('UpdateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_level_with_options(request, runtime)

    def update_table_model_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableModelInfoResponse(),
            self.do_rpcrequest('UpdateTableModelInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_model_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_model_info_with_options(request, runtime)

    def update_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableThemeResponse(),
            self.do_rpcrequest('UpdateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_theme_with_options(request, runtime)

    def update_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateUdfFileResponse(),
            self.do_rpcrequest('UpdateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)
