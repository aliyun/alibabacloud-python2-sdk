# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops20210625 import models as devops_20210625_models
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
        self._endpoint = self.get_endpoint('devops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/members/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(group_id, request, headers, runtime)

    def add_pipeline_relations_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_ids):
            query['relObjectIds'] = request.rel_object_ids
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/pipelineRelations' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddPipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_pipeline_relations(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    def add_repository_member_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_repository_member(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_repository_member_with_options(repository_id, request, headers, runtime)

    def add_webhook_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_ssl_verification):
            body['enableSslVerification'] = request.enable_ssl_verification
        if not UtilClient.is_unset(request.merge_requests_events):
            body['mergeRequestsEvents'] = request.merge_requests_events
        if not UtilClient.is_unset(request.note_events):
            body['noteEvents'] = request.note_events
        if not UtilClient.is_unset(request.push_events):
            body['pushEvents'] = request.push_events
        if not UtilClient.is_unset(request.secret_token):
            body['secretToken'] = request.secret_token
        if not UtilClient.is_unset(request.tag_push_events):
            body['tagPushEvents'] = request.tag_push_events
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/webhooks/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def add_webhook(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_webhook_with_options(repository_id, request, headers, runtime)

    def create_branch_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_branch(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_branch_with_options(repository_id, request, headers, runtime)

    def create_deploy_key_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/keys/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_deploy_key(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_deploy_key_with_options(repository_id, request, headers, runtime)

    def create_file_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(repository_id, request, headers, runtime)

    def create_flow_tag_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tags' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_flow_tag(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_with_options(organization_id, request, headers, runtime)

    def create_flow_tag_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tagGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_flow_tag_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_group_with_options(organization_id, request, headers, runtime)

    def create_host_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    def create_oauth_token_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.login):
            body['login'] = request.login
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOAuthToken',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/login/oauth/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateOAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_oauth_token(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oauth_token_with_options(request, headers, runtime)

    def create_pipeline_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipeline(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(organization_id, request, headers, runtime)

    def create_pipeline_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipeline_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_group_with_options(organization_id, request, headers, runtime)

    def create_project_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_code):
            body['customCode'] = request.custom_code
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.template_identifier):
            body['templateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/createProject' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(organization_id, request, headers, runtime)

    def create_protectd_branch_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProtectdBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/protect_branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProtectdBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_protectd_branch(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_protectd_branch_with_options(repository_id, request, headers, runtime)

    def create_repository_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['createParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sync):
            query['sync'] = request.sync
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gitignore_type):
            body['gitignoreType'] = request.gitignore_type
        if not UtilClient.is_unset(request.import_account):
            body['importAccount'] = request.import_account
        if not UtilClient.is_unset(request.import_demo_project):
            body['importDemoProject'] = request.import_demo_project
        if not UtilClient.is_unset(request.import_repo_type):
            body['importRepoType'] = request.import_repo_type
        if not UtilClient.is_unset(request.import_token):
            body['importToken'] = request.import_token
        if not UtilClient.is_unset(request.import_token_encrypted):
            body['importTokenEncrypted'] = request.import_token_encrypted
        if not UtilClient.is_unset(request.import_url):
            body['importUrl'] = request.import_url
        if not UtilClient.is_unset(request.init_standard_service):
            body['initStandardService'] = request.init_standard_service
        if not UtilClient.is_unset(request.is_crypto_enabled):
            body['isCryptoEnabled'] = request.is_crypto_enabled
        if not UtilClient.is_unset(request.local_import_url):
            body['localImportUrl'] = request.local_import_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            body['namespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.readme_type):
            body['readmeType'] = request.readme_type
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    def create_repository_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_group_with_options(request, headers, runtime)

    def create_resource_member_with_options(self, organization_id, resource_type, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/%s/members' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_member(self, organization_id, resource_type, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_sprint_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.staff_ids):
            body['staffIds'] = request.staff_ids
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSprint',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sprints/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSprintResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sprint(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sprint_with_options(organization_id, request, headers, runtime)

    def create_ssh_key_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sshKey' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    def create_tag_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        if not UtilClient.is_unset(request.tag_name):
            body['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/tags/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(repository_id, request, headers, runtime)

    def create_test_case_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.testcase_step_content_info):
            body['testcaseStepContentInfo'] = request.testcase_step_content_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testcase' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_test_case(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_test_case_with_options(organization_id, request, headers, runtime)

    def create_user_key_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.expire_time):
            body['expireTime'] = request.expire_time
        if not UtilClient.is_unset(request.key_scope):
            body['keyScope'] = request.key_scope
        if not UtilClient.is_unset(request.public_key):
            body['publicKey'] = request.public_key
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/v3/user/keys/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateUserKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_key(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_key_with_options(request, headers, runtime)

    def create_variable_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_variable_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    def create_workitem_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.description_format):
            body['descriptionFormat'] = request.description_format
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.participant):
            body['participant'] = request.participant
        if not UtilClient.is_unset(request.space):
            body['space'] = request.space
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            body['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.sprint):
            body['sprint'] = request.sprint
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tracker):
            body['tracker'] = request.tracker
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.workitem_type):
            body['workitemType'] = request.workitem_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/create' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workitem(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_with_options(organization_id, request, headers, runtime)

    def create_workitem_comment_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/comment' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workitem_comment(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_comment_with_options(organization_id, request, headers, runtime)

    def create_workitem_estimate_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.spent_time):
            body['spentTime'] = request.spent_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/estimate' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemEstimateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workitem_estimate(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_estimate_with_options(organization_id, request, headers, runtime)

    def create_workitem_record_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_time):
            body['actualTime'] = request.actual_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gmt_end):
            body['gmtEnd'] = request.gmt_end
        if not UtilClient.is_unset(request.gmt_start):
            body['gmtStart'] = request.gmt_start
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemRecord',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/record' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workitem_record(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_record_with_options(organization_id, request, headers, runtime)

    def create_workitem_v2with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent_identifier):
            body['parentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.sprint_identifier):
            body['sprintIdentifier'] = request.sprint_identifier
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.trackers):
            body['trackers'] = request.trackers
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.versions):
            body['versions'] = request.versions
        if not UtilClient.is_unset(request.workitem_type_identifier):
            body['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemV2',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitem' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemV2Response(),
            self.call_api(params, req, runtime)
        )

    def create_workitem_v2(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_v2with_options(organization_id, request, headers, runtime)

    def create_workspace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    def delete_branch_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/branches/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_branch(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_branch_with_options(repository_id, request, headers, runtime)

    def delete_file_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(repository_id, request, headers, runtime)

    def delete_flow_tag_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tags/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_flow_tag(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_with_options(organization_id, id, headers, runtime)

    def delete_flow_tag_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tagGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_flow_tag_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_group_with_options(organization_id, id, headers, runtime)

    def delete_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/members/remove/aliyun_pk' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_member_with_options(group_id, request, headers, runtime)

    def delete_host_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    def delete_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_group_with_options(self, organization_id, group_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline_group(self, organization_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    def delete_pipeline_relations_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_id):
            query['relObjectId'] = request.rel_object_id
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/pipelineRelations' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline_relations(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    def delete_project_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(organization_id, request, headers, runtime)

    def delete_protected_branch_with_options(self, repository_id, protected_branch_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectedBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/protect_branches/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(protected_branch_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_protected_branch(self, repository_id, protected_branch_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_protected_branch_with_options(repository_id, protected_branch_id, request, headers, runtime)

    def delete_repository_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(repository_id, request, headers, runtime)

    def delete_repository_group_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_group(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_group_with_options(group_id, request, headers, runtime)

    def delete_repository_member_with_options(self, repository_id, aliyun_pk, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/members/delete/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(aliyun_pk))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_member(self, repository_id, aliyun_pk, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    def delete_repository_webhook_with_options(self, repository_id, hook_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/hooks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(hook_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_webhook(self, repository_id, hook_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_webhook_with_options(repository_id, hook_id, request, headers, runtime)

    def delete_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(account_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_member(self, organization_id, resource_type, resource_id, account_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_tag_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/tags/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(repository_id, request, headers, runtime)

    def delete_user_key_with_options(self, key_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/v3/user/keys/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(key_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteUserKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_key(self, key_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_key_with_options(key_id, request, headers, runtime)

    def delete_variable_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    def delete_workitem_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitem/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workitem(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_with_options(organization_id, request, headers, runtime)

    def delete_workitem_all_comment_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemAllComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/deleteAllComment' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workitem_all_comment(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_all_comment_with_options(organization_id, request, headers, runtime)

    def delete_workitem_comment_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/deleteComent' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workitem_comment(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_comment_with_options(organization_id, request, headers, runtime)

    def enable_deploy_key_with_options(self, repository_id, key_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeployKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/keys/%s/enable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(key_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.EnableDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_deploy_key(self, repository_id, key_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_deploy_key_with_options(repository_id, key_id, request, headers, runtime)

    def frozen_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s/frozen' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def frozen_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    def get_branch_info_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/branches/detail' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetBranchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_branch_info(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_branch_info_with_options(repository_id, request, headers, runtime)

    def get_codeup_organization_with_options(self, identity, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/organization/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(identity)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCodeupOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_codeup_organization(self, identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_codeup_organization_with_options(identity, request, headers, runtime)

    def get_compare_detail_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.max_diff_byte):
            query['maxDiffByte'] = request.max_diff_byte
        if not UtilClient.is_unset(request.max_diff_file):
            query['maxDiffFile'] = request.max_diff_file
        if not UtilClient.is_unset(request.merge_base):
            query['mergeBase'] = request.merge_base
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCompareDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/commits/compare/detail' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCompareDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_compare_detail(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compare_detail_with_options(repository_id, request, headers, runtime)

    def get_custom_field_option_with_options(self, organization_id, field_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomFieldOption',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/fields/%s/getCustomOption' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(field_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCustomFieldOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_custom_field_option(self, organization_id, field_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_field_option_with_options(organization_id, field_id, request, headers, runtime)

    def get_file_blobs_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files/blobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileBlobsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_blobs(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_blobs_with_options(repository_id, request, headers, runtime)

    def get_file_last_commit_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files/lastCommit' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileLastCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_last_commit(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_last_commit_with_options(repository_id, request, headers, runtime)

    def get_flow_tag_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tagGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_flow_tag_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_flow_tag_group_with_options(organization_id, id, headers, runtime)

    def get_group_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/get_detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_detail_with_options(request, headers, runtime)

    def get_host_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    def get_organization_member_with_options(self, organization_id, account_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(account_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organization_member(self, organization_id, account_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_member_with_options(organization_id, account_id, headers, runtime)

    def get_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_artifact_url_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/getArtifactDownloadUrl' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_artifact_url(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_artifact_url_with_options(organization_id, request, headers, runtime)

    def get_pipeline_emas_artifact_url_with_options(self, organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_connection_id):
            query['serviceConnectionId'] = request.service_connection_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineEmasArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/%s/pipelineRun/%s/emas/artifact/%s/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(emas_job_instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(md_5))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineEmasArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_emas_artifact_url(self, organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_emas_artifact_url_with_options(organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime)

    def get_pipeline_group_with_options(self, organization_id, group_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_group(self, organization_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    def get_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_scan_report_url_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_path):
            body['reportPath'] = request.report_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPipelineScanReportUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/getPipelineScanReportUrl' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineScanReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_scan_report_url(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_scan_report_url_with_options(organization_id, request, headers, runtime)

    def get_project_info_with_options(self, organization_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/project/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_info(self, organization_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_info_with_options(organization_id, project_id, headers, runtime)

    def get_project_member_with_options(self, repository_id, aliyun_pk, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/members/get/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(aliyun_pk))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_member(self, repository_id, aliyun_pk, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    def get_repository_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_with_options(request, headers, runtime)

    def get_repository_commit_with_options(self, repository_id, sha, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/commits/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sha))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_commit(self, repository_id, sha, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_commit_with_options(repository_id, sha, request, headers, runtime)

    def get_repository_tag_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['tagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/tag/info' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_tag(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_with_options(repository_id, request, headers, runtime)

    def get_search_code_preview_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.is_dsl):
            query['isDsl'] = request.is_dsl
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSearchCodePreview',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/search/code_preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSearchCodePreviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_search_code_preview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_search_code_preview_with_options(request, headers, runtime)

    def get_sprint_info_with_options(self, organization_id, sprint_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSprintInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sprints/%s/getSprintinfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sprint_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSprintInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sprint_info(self, organization_id, sprint_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sprint_info_with_options(organization_id, sprint_id, headers, runtime)

    def get_test_result_list_with_options(self, organization_id, test_plan_identifier, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestResultList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testplan/%s/testresults' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(test_plan_identifier))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestResultListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_test_result_list(self, organization_id, test_plan_identifier, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_test_result_list_with_options(organization_id, test_plan_identifier, request, headers, runtime)

    def get_testcase_list_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conditions):
            body['conditions'] = request.conditions
        if not UtilClient.is_unset(request.directory_identifier):
            body['directoryIdentifier'] = request.directory_identifier
        if not UtilClient.is_unset(request.max_result):
            body['maxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTestcaseList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testcases' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetTestcaseListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_testcase_list(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_testcase_list_with_options(organization_id, request, headers, runtime)

    def get_user_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/users/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_info_with_options(request, headers, runtime)

    def get_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def get_variable_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    def get_work_item_activity_with_options(self, organization_id, workitem_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemActivity',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s/getActivity' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemActivityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_work_item_activity(self, organization_id, workitem_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_activity_with_options(organization_id, workitem_id, headers, runtime)

    def get_work_item_info_with_options(self, organization_id, workitem_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_work_item_info(self, organization_id, workitem_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_info_with_options(organization_id, workitem_id, headers, runtime)

    def get_work_item_work_flow_info_with_options(self, organization_id, workitem_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration_id):
            query['configurationId'] = request.configuration_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkItemWorkFlowInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s/getWorkflowInfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemWorkFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_work_item_work_flow_info(self, organization_id, workitem_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_work_flow_info_with_options(organization_id, workitem_id, request, headers, runtime)

    def get_workitem_attachment_createmeta_with_options(self, organization_id, workitem_identifier, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemAttachmentCreatemeta',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitem/%s/attachment/createmeta' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_identifier))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemAttachmentCreatemetaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workitem_attachment_createmeta(self, organization_id, workitem_identifier, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_attachment_createmeta_with_options(organization_id, workitem_identifier, request, headers, runtime)

    def get_workitem_comment_list_with_options(self, organization_id, workitem_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemCommentList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s/commentList' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemCommentListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workitem_comment_list(self, organization_id, workitem_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_comment_list_with_options(organization_id, workitem_id, headers, runtime)

    def get_workitem_relations_with_options(self, organization_id, workitem_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s/getRelations' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workitem_relations(self, organization_id, workitem_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_relations_with_options(organization_id, workitem_id, request, headers, runtime)

    def get_workitem_time_type_list_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemTimeTypeList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/type/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemTimeTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workitem_time_type_list(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_time_type_list_with_options(organization_id, headers, runtime)

    def get_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    def join_pipeline_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups/join' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.JoinPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def join_pipeline_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.join_pipeline_group_with_options(organization_id, request, headers, runtime)

    def list_flow_tag_groups_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tagGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_flow_tag_groups(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_tag_groups_with_options(organization_id, headers, runtime)

    def list_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(group_id, request, headers, runtime)

    def list_group_repositories_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/projects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListGroupRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_repositories(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_repositories_with_options(group_id, request, headers, runtime)

    def list_host_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    def list_organization_members_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contains_extern_info):
            query['containsExternInfo'] = request.contains_extern_info
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organization_members(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(organization_id, request, headers, runtime)

    def list_organizations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level):
            query['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.min_access_level):
            query['minAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organizations/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organizations_with_options(request, headers, runtime)

    def list_pipeline_group_pipelines_with_options(self, organization_id, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.result_status_list):
            query['resultStatusList'] = request.result_status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroupPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups/%s/pipelines' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_group_pipelines(self, organization_id, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_group_pipelines_with_options(organization_id, group_id, request, headers, runtime)

    def list_pipeline_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_groups_with_options(organization_id, request, headers, runtime)

    def list_pipeline_job_historys_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobHistorys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/%s/job/historys' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_job_historys(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_job_historys_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_jobs_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/%s/jobs' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_jobs(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_jobs_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_relations_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rel_object_type):
            query['relObjectType'] = request.rel_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/pipelineRelations' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_relations(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_relations_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_runs(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipelines_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipelines(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    def list_project_members_with_options(self, organization_id, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/%s/listMembers' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_members(self, organization_id, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_members_with_options(organization_id, project_id, request, headers, runtime)

    def list_project_templates_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectTemplates',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/listTemplates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_templates(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_templates_with_options(organization_id, request, headers, runtime)

    def list_project_workitem_types_with_options(self, organization_id, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectWorkitemTypes',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/%s/getWorkitemType' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectWorkitemTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_workitem_types(self, organization_id, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_workitem_types_with_options(organization_id, project_id, request, headers, runtime)

    def list_projects_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/listProjects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(organization_id, request, headers, runtime)

    def list_protected_branches_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/protect_branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_protected_branches(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_protected_branches_with_options(repository_id, request, headers, runtime)

    def list_repositories_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.archived):
            query['archived'] = request.archived
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repositories(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    def list_repository_branches_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_branches(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_branches_with_options(repository_id, request, headers, runtime)

    def list_repository_commit_diff_with_options(self, repository_id, sha, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['contextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/commits/%s/diff' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sha))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitDiffResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_commit_diff(self, repository_id, sha, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commit_diff_with_options(repository_id, sha, request, headers, runtime)

    def list_repository_commits_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.show_comments_count):
            query['showCommentsCount'] = request.show_comments_count
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/commits' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_commits(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commits_with_options(repository_id, request, headers, runtime)

    def list_repository_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.include_personal):
            query['includePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/get/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_groups_with_options(request, headers, runtime)

    def list_repository_member_with_inherited_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/members/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryMemberWithInheritedResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_member_with_inherited(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_inherited_with_options(repository_id, request, headers, runtime)

    def list_repository_tags_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/tag/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_tags(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tags_with_options(repository_id, request, headers, runtime)

    def list_repository_tree_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files/tree' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_tree(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tree_with_options(repository_id, request, headers, runtime)

    def list_repository_webhook_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/webhooks/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_webhook(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_webhook_with_options(repository_id, request, headers, runtime)

    def list_resource_members_with_options(self, organization_id, resource_type, resource_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/%s/members' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_members(self, organization_id, resource_type, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    def list_search_commit_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/search/commit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def list_search_commit(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_commit_with_options(request, headers, runtime)

    def list_search_repository_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_pk):
            body['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/search/repo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_search_repository(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_repository_with_options(request, headers, runtime)

    def list_search_source_code_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['isCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.keyword):
            body['keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_path):
            body['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSearchSourceCode',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/search/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSearchSourceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_search_source_code(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_source_code_with_options(request, headers, runtime)

    def list_service_connections_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/serviceConnections' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_connections(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    def list_sprints_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSprints',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sprints/list' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSprintsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sprints(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sprints_with_options(organization_id, request, headers, runtime)

    def list_test_case_fields_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTestCaseFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testcase/fields' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListTestCaseFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_test_case_fields(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_test_case_fields_with_options(organization_id, request, headers, runtime)

    def list_user_keys_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserKeys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/v3/user/keys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListUserKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_keys(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_keys_with_options(request, headers, runtime)

    def list_variable_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_variable_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    def list_work_item_all_fields_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemAllFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/fields/listAll' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemAllFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_work_item_all_fields(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_all_fields_with_options(organization_id, request, headers, runtime)

    def list_work_item_work_flow_status_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_category_identifier):
            query['workitemCategoryIdentifier'] = request.workitem_category_identifier
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemWorkFlowStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/workflow/listWorkflowStatus' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemWorkFlowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_work_item_work_flow_status(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_work_flow_status_with_options(organization_id, request, headers, runtime)

    def list_workitem_time_with_options(self, organization_id, workitem_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemTime',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/%s/time/list' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workitem_time(self, organization_id, workitem_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitem_time_with_options(organization_id, workitem_id, headers, runtime)

    def list_workitems_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.group_condition):
            query['groupCondition'] = request.group_condition
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkitems',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/listWorkitems' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workitems(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitems_with_options(organization_id, request, headers, runtime)

    def list_workspaces_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    def log_pipeline_job_run_with_options(self, organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/%s/pipelineRun/%s/job/%s/logs' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def log_pipeline_job_run(self, organization_id, pipeline_id, job_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_pipeline_job_run_with_options(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    def log_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s/machine/%s/log' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(machine_sn))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def log_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def pass_pipeline_validate_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/pass' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    def pass_pipeline_validate(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pass_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def refuse_pipeline_validate_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/refuse' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    def refuse_pipeline_validate(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refuse_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def release_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s/release' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def release_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    def reset_ssh_key_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sshKey' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    def resume_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s/resume' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def retry_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s/machine/%s/retry' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(machine_sn))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def skip_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/skip' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s/machine/%s/skip' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(machine_sn))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def start_pipeline_run_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organizations/%s/pipelines/%s/run' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def start_pipeline_run(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    def stop_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/pipelineRuns/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_run_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/deploy/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_order_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def trigger_repository_mirror_sync_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/mirror' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TriggerRepositoryMirrorSyncResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_repository_mirror_sync(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_repository_mirror_sync_with_options(repository_id, request, headers, runtime)

    def update_file_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.new_path):
            body['newPath'] = request.new_path
        if not UtilClient.is_unset(request.old_path):
            body['oldPath'] = request.old_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/files/update' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_file(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(repository_id, request, headers, runtime)

    def update_flow_tag_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tags/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    def update_flow_tag(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_with_options(organization_id, id, request, headers, runtime)

    def update_flow_tag_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/flow/tagGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_flow_tag_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_group_with_options(organization_id, id, request, headers, runtime)

    def update_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.path_with_namespace):
            body['pathWithNamespace'] = request.path_with_namespace
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/groups/modify',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    def update_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.aliyun_pk):
            query['aliyunPk'] = request.aliyun_pk
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/groups/%s/members/update/aliyun_pk' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_member_with_options(group_id, request, headers, runtime)

    def update_host_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_host_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    def update_pipeline_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            body['pipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/update' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipeline(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(organization_id, request, headers, runtime)

    def update_pipeline_base_info_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/%s/baseInfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipeline_base_info(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_base_info_with_options(organization_id, pipeline_id, request, headers, runtime)

    def update_pipeline_group_with_options(self, organization_id, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelineGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipeline_group(self, organization_id, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_group_with_options(organization_id, group_id, request, headers, runtime)

    def update_project_member_with_options(self, organization_id, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_identifier):
            body['roleIdentifier'] = request.role_identifier
        if not UtilClient.is_unset(request.target_identifier):
            body['targetIdentifier'] = request.target_identifier
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identifier):
            body['userIdentifier'] = request.user_identifier
        if not UtilClient.is_unset(request.user_type):
            body['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/projects/%s/updateMember' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project_member(self, organization_id, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_member_with_options(organization_id, project_id, request, headers, runtime)

    def update_protected_branches_with_options(self, repository_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/%s/protect_branches/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_protected_branches(self, repository_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_protected_branches_with_options(repository_id, id, request, headers, runtime)

    def update_push_review_on_off_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.trunk_mode):
            query['trunkMode'] = request.trunk_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePushReviewOnOff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/settings/trunk_mode' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePushReviewOnOffResponse(),
            self.call_api(params, req, runtime)
        )

    def update_push_review_on_off(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_push_review_on_off_with_options(repository_id, request, headers, runtime)

    def update_repository_with_options(self, repository_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.admin_setting_language):
            body['adminSettingLanguage'] = request.admin_setting_language
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.builds_enabled):
            body['buildsEnabled'] = request.builds_enabled
        if not UtilClient.is_unset(request.check_email):
            body['checkEmail'] = request.check_email
        if not UtilClient.is_unset(request.default_branch):
            body['defaultBranch'] = request.default_branch
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.issues_enabled):
            body['issuesEnabled'] = request.issues_enabled
        if not UtilClient.is_unset(request.merge_requests_enabled):
            body['mergeRequestsEnabled'] = request.merge_requests_enabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.open_clone_download_control):
            body['openCloneDownloadControl'] = request.open_clone_download_control
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.project_clone_download_method_list):
            body['projectCloneDownloadMethodList'] = request.project_clone_download_method_list
        if not UtilClient.is_unset(request.project_clone_download_role_list):
            body['projectCloneDownloadRoleList'] = request.project_clone_download_role_list
        if not UtilClient.is_unset(request.snippets_enabled):
            body['snippetsEnabled'] = request.snippets_enabled
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        if not UtilClient.is_unset(request.wiki_enabled):
            body['wikiEnabled'] = request.wiki_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repository(self, repository_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_with_options(repository_id, request, headers, runtime)

    def update_repository_member_with_options(self, repository_id, aliyun_pk, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.expire_at):
            body['expireAt'] = request.expire_at
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.related_id):
            body['relatedId'] = request.related_id
        if not UtilClient.is_unset(request.related_infos):
            body['relatedInfos'] = request.related_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/repository/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(repository_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(aliyun_pk))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repository_member(self, repository_id, aliyun_pk, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    def update_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/%s/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(account_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_member(self, organization_id, resource_type, resource_id, account_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_test_case_with_options(self, organization_id, testcase_identifier, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestCase',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testcase/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(testcase_identifier))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    def update_test_case(self, organization_id, testcase_identifier, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_test_case_with_options(organization_id, testcase_identifier, request, headers, runtime)

    def update_test_result_with_options(self, organization_id, test_plan_identifier, testcase_identifier, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.executor):
            body['executor'] = request.executor
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTestResult',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/testhub/testplan/%s/testresult/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(test_plan_identifier)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(testcase_identifier))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    def update_test_result(self, organization_id, test_plan_identifier, testcase_identifier, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_test_result_with_options(organization_id, test_plan_identifier, testcase_identifier, request, headers, runtime)

    def update_variable_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_variable_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    def update_work_item_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_type):
            body['fieldType'] = request.field_type
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.property_key):
            body['propertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_value):
            body['propertyValue'] = request.property_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkItem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/update' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_work_item(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_work_item_with_options(organization_id, request, headers, runtime)

    def update_workitem_comment_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/commentUpdate' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workitem_comment(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workitem_comment_with_options(organization_id, request, headers, runtime)

    def update_workitem_field_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.update_workitem_property_request):
            body['updateWorkitemPropertyRequest'] = request.update_workitem_property_request
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemField',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitems/updateWorkitemField' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workitem_field(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workitem_field_with_options(organization_id, request, headers, runtime)

    def workitem_attachment_create_with_options(self, organization_id, workitem_identifier, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.original_filename):
            body['originalFilename'] = request.original_filename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WorkitemAttachmentCreate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/workitem/%s/attachment' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workitem_identifier))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.WorkitemAttachmentCreateResponse(),
            self.call_api(params, req, runtime)
        )

    def workitem_attachment_create(self, organization_id, workitem_identifier, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.workitem_attachment_create_with_options(organization_id, workitem_identifier, request, headers, runtime)
