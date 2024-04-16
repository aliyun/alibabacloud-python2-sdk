# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_miniapplcdp20200113 import models as miniapplcdp_20200113_models
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
        self._endpoint = self.get_endpoint('miniapplcdp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_create_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_data_json):
            query['ModelDataJson'] = request.model_data_json
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchCreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_model_with_options(request, runtime)

    def batch_delete_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_model_with_options(request, runtime)

    def batch_delete_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id_list):
            query['ResourceIdList'] = request.resource_id_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_resources_with_options(request, runtime)

    def batch_restore_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchRestoreModelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_restore_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_restore_model_with_options(request, runtime)

    def check_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def check_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    def clone_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneAppResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_app_with_options(request, runtime)

    def clone_model_from_commit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.target_module_id):
            query['TargetModuleId'] = request.target_module_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelFromCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelFromCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_model_from_commit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_model_from_commit_with_options(request, runtime)

    def clone_model_in_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelInModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelInModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_model_in_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_model_in_module_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous):
            query['Asynchronous'] = request.asynchronous
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.platform_version):
            query['PlatformVersion'] = request.platform_version
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.templated):
            query['Templated'] = request.templated
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_commit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.commit_type):
            query['CommitType'] = request.commit_type
        if not UtilClient.is_unset(request.main_module_commit_id):
            query['MainModuleCommitId'] = request.main_module_commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.rollback_to_commit_id):
            query['RollbackToCommitId'] = request.rollback_to_commit_id
        if not UtilClient.is_unset(request.rollback_type):
            query['RollbackType'] = request.rollback_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def create_commit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_commit_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_certificate):
            query['WithCertificate'] = request.with_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_link_entity_and_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.model_data):
            query['ModelData'] = request.model_data
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLinkEntityAndAssociation',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_link_entity_and_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_link_entity_and_association_with_options(request, runtime)

    def create_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.link_model_id):
            query['LinkModelId'] = request.link_model_id
        if not UtilClient.is_unset(request.link_module_id):
            query['LinkModuleId'] = request.link_module_id
        if not UtilClient.is_unset(request.linked):
            query['Linked'] = request.linked
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    def create_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.minimum_platform_version):
            query['MinimumPlatformVersion'] = request.minimum_platform_version
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.target_app_source):
            query['TargetAppSource'] = request.target_app_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_module_with_options(request, runtime)

    def create_module_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.publish_version):
            query['PublishVersion'] = request.publish_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModulePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModulePublishResponse(),
            self.call_api(params, req, runtime)
        )

    def create_module_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_module_publish_with_options(request, runtime)

    def create_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreatePublishResponse(),
            self.call_api(params, req, runtime)
        )

    def create_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_publish_with_options(request, runtime)

    def create_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_commit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_commit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_commit_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    def delete_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_module_with_options(request, runtime)

    def delete_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    def generate_app_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAppUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_app_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_app_user_password_with_options(request, runtime)

    def generate_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAuthToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_auth_token_with_options(request, runtime)

    def generate_upload_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.upload_token_type):
            query['UploadTokenType'] = request.upload_token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_upload_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_token_with_options(request, runtime)

    def get_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    def get_app_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppModelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_model_with_options(request, runtime)

    def get_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    def get_artifact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def get_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    def get_commit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_commit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_commit_with_options(request, runtime)

    def get_default_app_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultAppUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDefaultAppUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_app_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_default_app_user_with_options(request, runtime)

    def get_domain_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainCname',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_cname_with_options(request, runtime)

    def get_domain_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainOverview',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_overview_with_options(request, runtime)

    def get_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_environment_with_options(request, runtime)

    def get_history_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetHistoryStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_history_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_history_stats_with_options(request, runtime)

    def get_latest_commit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLatestCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetLatestCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_latest_commit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_latest_commit_with_options(request, runtime)

    def get_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_model_with_options(request, runtime)

    def get_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_module_with_options(request, runtime)

    def get_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetPublishResponse(),
            self.call_api(params, req, runtime)
        )

    def get_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_publish_with_options(request, runtime)

    def get_realtime_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetRealtimeStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_realtime_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_stats_with_options(request, runtime)

    def get_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def list_app_modules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppModulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_modules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_modules_with_options(request, runtime)

    def list_app_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    def list_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            query['AppStatus'] = request.app_status
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.main_module_id):
            query['MainModuleId'] = request.main_module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    def list_artifacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_artifacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    def list_commits_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommits',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_commits(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_commits_with_options(request, runtime)

    def list_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    def list_environment_overviews_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentOverviews',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environment_overviews(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_environment_overviews_with_options(request, runtime)

    def list_environments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_environments_with_options(request, runtime)

    def list_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_models_with_options(request, runtime)

    def list_models_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelsByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_models_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_models_by_page_with_options(request, runtime)

    def list_module_dependencies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleDependencies',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_dependencies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_module_dependencies_with_options(request, runtime)

    def list_module_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_types):
            query['SubTypes'] = request.sub_types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_module_models_with_options(request, runtime)

    def list_module_publish_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            query['ModuleVersion'] = request.module_version
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulePublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulePublishVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_publish_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_module_publish_versions_with_options(request, runtime)

    def list_module_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_module_resources_with_options(request, runtime)

    def list_modules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_modules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_modules_with_options(request, runtime)

    def list_modules_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_modules_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_modules_by_page_with_options(request, runtime)

    def list_publish_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_publish_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_publish_versions_with_options(request, runtime)

    def list_published_modules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_app_id):
            query['ExcludeAppId'] = request.exclude_app_id
        if not UtilClient.is_unset(request.exclude_module_id):
            query['ExcludeModuleId'] = request.exclude_module_id
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishedModulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_published_modules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_published_modules_with_options(request, runtime)

    def list_publishes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['PublishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishes',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_publishes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_publishes_with_options(request, runtime)

    def list_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    def list_resources_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_page_with_options(request, runtime)

    def reset_app_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ResetAppUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_app_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_app_user_password_with_options(request, runtime)

    def restore_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RestoreModelResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_model_with_options(request, runtime)

    def run_logic_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunLogicModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RunLogicModelResponse(),
            self.call_api(params, req, runtime)
        )

    def run_logic_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_logic_model_with_options(request, runtime)

    def set_environment_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEnvironmentDefaultDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def set_environment_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_environment_default_domain_with_options(request, runtime)

    def start_app_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StartAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    def start_app_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_app_server_with_options(request, runtime)

    def stop_app_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StopAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_app_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_app_server_with_options(request, runtime)

    def update_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    def update_app_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppModelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_model_with_options(request, runtime)

    def update_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_model_with_options(request, runtime)

    def update_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_module(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_module_with_options(request, runtime)

    def update_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    def update_resource_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceContent',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceContentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_content_with_options(request, runtime)

    def update_resource_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInfo',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_info_with_options(request, runtime)
