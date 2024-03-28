# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mpserverless20190615 import models as mpserverless_20190615_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('mpserverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cors_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCorsDomain',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddCorsDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cors_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cors_domain_with_options(request, runtime)

    def add_dingtalk_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDingtalkOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dingtalk_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dingtalk_open_platform_config_with_options(request, runtime)

    def attach_web_hosting_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.private_key):
            body['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.server_certificate):
            body['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachWebHostingCertificate',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AttachWebHostingCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_web_hosting_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_web_hosting_certificate_with_options(request, runtime)

    def batch_delete_web_hosting_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_paths):
            body['FilePaths'] = request.file_paths
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteWebHostingFiles',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_web_hosting_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_web_hosting_files_with_options(request, runtime)

    def bind_web_hosting_custom_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_domain):
            body['CustomDomain'] = request.custom_domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindWebHostingCustomDomain',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BindWebHostingCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_web_hosting_custom_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_web_hosting_custom_domain_with_options(request, runtime)

    def check_mp_serverless_role_exists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMpServerlessRoleExists',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_mp_serverless_role_exists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_mp_serverless_role_exists_with_options(request, runtime)

    def create_dbexport_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBExportTask',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbexport_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbexport_task_with_options(request, runtime)

    def create_dbimport_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collection):
            body['Collection'] = request.collection
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBImportTask',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbimport_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbimport_task_with_options(request, runtime)

    def create_dbrestore_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_id):
            body['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.new_collections):
            body['NewCollections'] = request.new_collections
        if not UtilClient.is_unset(request.origin_collections):
            body['OriginCollections'] = request.origin_collections
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBRestoreTask',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbrestore_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbrestore_task_with_options(request, runtime)

    def create_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.runtime):
            body['Runtime'] = request.runtime
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_function_with_options(request, runtime)

    def create_function_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionDeployment',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_function_deployment_with_options(request, runtime)

    def create_space_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpace',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_space_with_options(request, runtime)

    def create_space_with_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.package_version):
            body['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.use_coupon):
            body['UseCoupon'] = request.use_coupon
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpaceWithOrder',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSpaceWithOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_space_with_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_space_with_order_with_options(request, runtime)

    def delete_ant_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ant_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_open_platform_config_with_options(request, runtime)

    def delete_cors_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCorsDomain',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteCorsDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cors_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cors_domain_with_options(request, runtime)

    def delete_dbcollection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBCollection',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDBCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbcollection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcollection_with_options(request, runtime)

    def delete_dingtalk_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDingtalkOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dingtalk_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dingtalk_open_platform_config_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def delete_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_function_with_options(request, runtime)

    def delete_space_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSpace',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_space_with_options(request, runtime)

    def delete_web_hosting_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWebHostingCertificate',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_hosting_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_hosting_certificate_with_options(request, runtime)

    def delete_web_hosting_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWebHostingFile',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_hosting_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_hosting_file_with_options(request, runtime)

    def delete_wechat_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWechatOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_wechat_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_wechat_open_platform_config_with_options(request, runtime)

    def deploy_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['DeploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeployFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_function_with_options(request, runtime)

    def describe_cdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCdnDomain',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_with_options(request, runtime)

    def describe_fcopen_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFCOpenStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFCOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fcopen_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_fcopen_status_with_options(runtime)

    def describe_file_upload_signed_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.filename):
            body['Filename'] = request.filename
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFileUploadSignedUrl',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_file_upload_signed_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_file_upload_signed_url_with_options(request, runtime)

    def describe_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_function_with_options(request, runtime)

    def describe_http_trigger_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHttpTriggerConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeHttpTriggerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_http_trigger_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_http_trigger_config_with_options(request, runtime)

    def describe_resource_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeResourceQuota',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeResourceQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_quota_with_options(request, runtime)

    def describe_resource_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    def describe_service_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collection_name):
            body['CollectionName'] = request.collection_name
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServicePolicy',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeServicePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_policy_with_options(request, runtime)

    def describe_space_client_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.detail):
            body['Detail'] = request.detail
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSpaceClientConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpaceClientConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_space_client_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_space_client_config_with_options(request, runtime)

    def describe_spaces_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mpserverless_20190615_models.DescribeSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.space_ids):
            request.space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.space_ids, 'SpaceIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.emas_workspace_id):
            body['EmasWorkspaceId'] = request.emas_workspace_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_ids_shrink):
            body['SpaceIds'] = request.space_ids_shrink
        if not UtilClient.is_unset(request.spec_code):
            body['SpecCode'] = request.spec_code
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSpaces',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_spaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_spaces_with_options(request, runtime)

    def describe_web_hosting_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWebHostingFile',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeWebHostingFileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_hosting_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_hosting_file_with_options(request, runtime)

    def enable_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extension_id):
            body['ExtensionId'] = request.extension_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableExtension',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.EnableExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_extension_with_options(request, runtime)

    def get_web_hosting_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_domain):
            body['CustomDomain'] = request.custom_domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebHostingCertificateDetail',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_web_hosting_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_certificate_detail_with_options(request, runtime)

    def get_web_hosting_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebHostingConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_web_hosting_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_config_with_options(request, runtime)

    def get_web_hosting_domain_verification_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebHostingDomainVerificationContent',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_web_hosting_domain_verification_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_domain_verification_content_with_options(request, runtime)

    def get_web_hosting_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebHostingStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_web_hosting_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_status_with_options(request, runtime)

    def get_web_hosting_upload_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWebHostingUploadCredential',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingUploadCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def get_web_hosting_upload_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_upload_credential_with_options(request, runtime)

    def list_cors_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCorsDomains',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListCorsDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cors_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cors_domains_with_options(request, runtime)

    def list_dingtalk_open_platform_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDingtalkOpenPlatformConfigs',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dingtalk_open_platform_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dingtalk_open_platform_configs_with_options(request, runtime)

    def list_extensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListExtensions',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_extensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_extensions_with_options(request, runtime)

    def list_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.auth_delta):
            body['AuthDelta'] = request.auth_delta
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFileResponse(),
            self.call_api(params, req, runtime)
        )

    def list_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_with_options(request, runtime)

    def list_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filter_by):
            body['FilterBy'] = request.filter_by
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_with_options(request, runtime)

    def list_function_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFunctionDeployment',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_deployment_with_options(request, runtime)

    def list_function_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFunctionLog',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_log_with_options(request, runtime)

    def list_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_open_platform_config_with_options(request, runtime)

    def list_space_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mpserverless_20190615_models.ListSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.space_ids):
            request.space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.space_ids, 'SpaceIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.emas_workspace_id):
            body['EmasWorkspaceId'] = request.emas_workspace_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.space_ids_shrink):
            body['SpaceIds'] = request.space_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSpace',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_space_with_options(request, runtime)

    def list_web_hosting_custom_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebHostingCustomDomains',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_web_hosting_custom_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_web_hosting_custom_domains_with_options(request, runtime)

    def list_web_hosting_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.marker):
            body['Marker'] = request.marker
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebHostingFiles',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_web_hosting_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_web_hosting_files_with_options(request, runtime)

    def modify_web_hosting_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allowed_ips):
            body['AllowedIps'] = request.allowed_ips
        if not UtilClient.is_unset(request.error_http_status):
            body['ErrorHttpStatus'] = request.error_http_status
        if not UtilClient.is_unset(request.error_path):
            body['ErrorPath'] = request.error_path
        if not UtilClient.is_unset(request.index_path):
            body['IndexPath'] = request.index_path
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyWebHostingConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ModifyWebHostingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_hosting_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_hosting_config_with_options(request, runtime)

    def open_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenService',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_service_with_options(request, runtime)

    def open_web_hosting_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenWebHostingService',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenWebHostingServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_web_hosting_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_web_hosting_service_with_options(request, runtime)

    def query_dbbackup_collections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_id):
            body['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDBBackupCollections',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dbbackup_collections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dbbackup_collections_with_options(request, runtime)

    def query_dbbackup_dump_times_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDBBackupDumpTimes',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupDumpTimesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dbbackup_dump_times(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dbbackup_dump_times_with_options(request, runtime)

    def query_dbexport_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDBExportTaskStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBExportTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dbexport_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dbexport_task_status_with_options(request, runtime)

    def query_dbimport_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDBImportTaskStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBImportTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dbimport_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dbimport_task_status_with_options(request, runtime)

    def query_dbrestore_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDBRestoreTaskStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dbrestore_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dbrestore_task_status_with_options(request, runtime)

    def query_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryServiceStatus',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_service_status_with_options(request, runtime)

    def query_space_consumption_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpaceConsumption',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QuerySpaceConsumptionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_space_consumption(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_space_consumption_with_options(request, runtime)

    def query_space_spec_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.spec_code):
            body['SpecCode'] = request.spec_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpaceSpecDetail',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QuerySpaceSpecDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_space_spec_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_space_spec_detail_with_options(request, runtime)

    def query_space_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            body['Interval'] = request.interval
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpaceUsage',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QuerySpaceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_space_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_space_usage_with_options(request, runtime)

    def refresh_web_hosting_custom_domain_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshWebHostingCustomDomainCache',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RefreshWebHostingCustomDomainCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_web_hosting_custom_domain_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_web_hosting_custom_domain_cache_with_options(request, runtime)

    def register_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterFile',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RegisterFileResponse(),
            self.call_api(params, req, runtime)
        )

    def register_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_file_with_options(request, runtime)

    def rename_dbcollection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_collection):
            body['NewCollection'] = request.new_collection
        if not UtilClient.is_unset(request.origin_collection):
            body['OriginCollection'] = request.origin_collection
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameDBCollection',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RenameDBCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def rename_dbcollection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rename_dbcollection_with_options(request, runtime)

    def reset_server_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetServerSecret',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ResetServerSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_server_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_server_secret_with_options(request, runtime)

    def run_dbcommand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDBCommand',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunDBCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def run_dbcommand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_dbcommand_with_options(request, runtime)

    def run_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def run_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_function_with_options(request, runtime)

    def save_ant_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_cert):
            body['AppCert'] = request.app_cert
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.private_key):
            body['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_cert):
            body['PublicCert'] = request.public_cert
        if not UtilClient.is_unset(request.public_key):
            body['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.root_cert):
            body['RootCert'] = request.root_cert
        if not UtilClient.is_unset(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAntOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_ant_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_ant_open_platform_config_with_options(request, runtime)

    def save_app_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_auth_token):
            body['AppAuthToken'] = request.app_auth_token
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.isv_app_id):
            body['IsvAppId'] = request.isv_app_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAppAuthToken',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAppAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def save_app_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_app_auth_token_with_options(request, runtime)

    def save_cdn_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_config):
            body['AuthConfig'] = request.auth_config
        if not UtilClient.is_unset(request.cors_config):
            body['CorsConfig'] = request.cors_config
        if not UtilClient.is_unset(request.ip_config):
            body['IpConfig'] = request.ip_config
        if not UtilClient.is_unset(request.referer_config):
            body['RefererConfig'] = request.referer_config
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.ua_config):
            body['UaConfig'] = request.ua_config
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCdnDomainConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_cdn_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_cdn_domain_config_with_options(request, runtime)

    def save_web_hosting_custom_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_redirect_type):
            body['ForceRedirectType'] = request.force_redirect_type
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveWebHostingCustomDomainConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_web_hosting_custom_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_hosting_custom_domain_config_with_options(request, runtime)

    def save_web_hosting_custom_domain_cors_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_allow_origin):
            body['AccessControlAllowOrigin'] = request.access_control_allow_origin
        if not UtilClient.is_unset(request.access_origin_control):
            body['AccessOriginControl'] = request.access_origin_control
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable_cors):
            body['EnableCors'] = request.enable_cors
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveWebHostingCustomDomainCorsConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_web_hosting_custom_domain_cors_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_hosting_custom_domain_cors_config_with_options(request, runtime)

    def save_wechat_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveWechatOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_wechat_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_wechat_open_platform_config_with_options(request, runtime)

    def unbind_web_hosting_custom_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_domain):
            body['CustomDomain'] = request.custom_domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindWebHostingCustomDomain',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_web_hosting_custom_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_web_hosting_custom_domain_with_options(request, runtime)

    def update_dingtalk_open_platform_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDingtalkOpenPlatformConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dingtalk_open_platform_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dingtalk_open_platform_config_with_options(request, runtime)

    def update_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.http_trigger_path):
            body['HttpTriggerPath'] = request.http_trigger_path
        if not UtilClient.is_unset(request.instance_concurrency):
            body['InstanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.runtime):
            body['Runtime'] = request.runtime
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timing_trigger_config):
            body['TimingTriggerConfig'] = request.timing_trigger_config
        if not UtilClient.is_unset(request.timing_trigger_user_payload):
            body['TimingTriggerUserPayload'] = request.timing_trigger_user_payload
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_function_with_options(request, runtime)

    def update_http_trigger_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_domain):
            body['CustomDomain'] = request.custom_domain
        if not UtilClient.is_unset(request.custom_domain_certificate):
            body['CustomDomainCertificate'] = request.custom_domain_certificate
        if not UtilClient.is_unset(request.custom_domain_private_key):
            body['CustomDomainPrivateKey'] = request.custom_domain_private_key
        if not UtilClient.is_unset(request.enable_service):
            body['EnableService'] = request.enable_service
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHttpTriggerConfig',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateHttpTriggerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_http_trigger_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_http_trigger_config_with_options(request, runtime)

    def update_service_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collection_name):
            body['CollectionName'] = request.collection_name
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServicePolicy',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateServicePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_policy_with_options(request, runtime)

    def update_space_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpace',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_space_with_options(request, runtime)

    def verify_web_hosting_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.verify_type):
            body['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyWebHostingDomainOwner',
            version='2019-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_web_hosting_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_web_hosting_domain_owner_with_options(request, runtime)
