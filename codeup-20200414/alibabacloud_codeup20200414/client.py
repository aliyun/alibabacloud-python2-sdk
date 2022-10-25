# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_codeup20200414 import models as codeup_20200414_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('codeup', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_merge_request(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.accept_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    def accept_merge_request_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/merge_request/%s/accept' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def add_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(group_id, request, headers, runtime)

    def add_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/groups/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_repository_member(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_repository_member_with_options(project_id, request, headers, runtime)

    def add_repository_member_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_webhook(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_webhook_with_options(project_id, request, headers, runtime)

    def add_webhook_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/hooks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_branch(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_branch_with_options(project_id, request, headers, runtime)

    def create_branch_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
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
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(project_id, request, headers, runtime)

    def create_file_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/files' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_merge_request(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_merge_request_with_options(project_id, request, headers, runtime)

    def create_merge_request_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/merge_requests' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def create_merge_request_comment(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_merge_request_comment_with_options(project_id, merge_request_id, request, headers, runtime)

    def create_merge_request_comment_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/merge_request/%s/comments' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    def create_repository_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
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
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository_deploy_key(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_deploy_key_with_options(project_id, request, headers, runtime)

    def create_repository_deploy_key_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/keys' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_group_with_options(request, headers, runtime)

    def create_repository_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository_protected_branch(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_protected_branch_with_options(project_id, request, headers, runtime)

    def create_repository_protected_branch_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/protect_branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ssh_key(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(request, headers, runtime)

    def create_ssh_key_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/user/keys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(project_id, request, headers, runtime)

    def create_tag_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/tags' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_branch(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_branch_with_options(project_id, request, headers, runtime)

    def delete_branch_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/branches/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(project_id, request, headers, runtime)

    def delete_file_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/files' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_member(self, group_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_member_with_options(group_id, user_id, request, headers, runtime)

    def delete_group_member_with_options(self, group_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(project_id, request, headers, runtime)

    def delete_repository_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_group(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_group_with_options(group_id, request, headers, runtime)

    def delete_repository_group_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/%s/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_member(self, project_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_options(project_id, user_id, request, headers, runtime)

    def delete_repository_member_with_options(self, project_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_member_with_extern_uid(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_extern_uid_with_options(project_id, request, headers, runtime)

    def delete_repository_member_with_extern_uid_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.extern_user_id):
            query['ExternUserId'] = request.extern_user_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMemberWithExternUid',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/members/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_protected_branch(self, project_id, protected_branch_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_protected_branch_with_options(project_id, protected_branch_id, request, headers, runtime)

    def delete_repository_protected_branch_with_options(self, project_id, protected_branch_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/protect_branches/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(protected_branch_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_tag(self, project_id, tag_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_tag_with_options(project_id, tag_name, request, headers, runtime)

    def delete_repository_tag_with_options(self, project_id, tag_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/tags/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(tag_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_tag_v2(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_tag_v2with_options(project_id, request, headers, runtime)

    def delete_repository_tag_v2with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/tag/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            self.call_api(params, req, runtime)
        )

    def delete_repository_webhook(self, project_id, webhook_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_webhook_with_options(project_id, webhook_id, request, headers, runtime)

    def delete_repository_webhook_with_options(self, project_id, webhook_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/hooks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(webhook_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_repository_deploy_key(self, project_id, key_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_repository_deploy_key_with_options(project_id, key_id, request, headers, runtime)

    def enable_repository_deploy_key_with_options(self, project_id, key_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/keys/%s/enable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(key_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_branch_info(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_branch_info_with_options(project_id, request, headers, runtime)

    def get_branch_info_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/branches/detail' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_code_completion(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_completion_with_options(service_name, request, headers, runtime)

    def get_code_completion_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_keys):
            query['FetchKeys'] = request.fetch_keys
        if not UtilClient.is_unset(request.is_encrypted):
            query['IsEncrypted'] = request.is_encrypted
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeCompletion',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v2/service/invoke/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(service_name)),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_codeup_organization(self, organization_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_codeup_organization_with_options(organization_identity, request, headers, runtime)

    def get_codeup_organization_with_options(self, organization_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/organization/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organization_identity)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_blobs(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_blobs_with_options(project_id, request, headers, runtime)

    def get_file_blobs_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/blobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_last_commit(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_last_commit_with_options(project_id, request, headers, runtime)

    def get_file_last_commit_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/files/last_commit' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_detail_with_options(request, headers, runtime)

    def get_group_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_merge_request_approve_status(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_approve_status_with_options(project_id, merge_request_id, request, headers, runtime)

    def get_merge_request_approve_status_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequestApproveStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/merge_request/%s/approve_status' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_merge_request_detail(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_detail_with_options(project_id, merge_request_id, request, headers, runtime)

    def get_merge_request_detail_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequestDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/merge_request/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_merge_request_setting(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_setting_with_options(project_id, request, headers, runtime)

    def get_merge_request_setting_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/settings/merge_requests' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organization_repository_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_repository_setting_with_options(request, headers, runtime)

    def get_organization_repository_setting_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrganizationRepositorySetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/organization/settings/repo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationRepositorySettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organization_security_center_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_security_center_status_with_options(request, headers, runtime)

    def get_organization_security_center_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrganizationSecurityCenterStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/organization/security/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_member(self, project_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_member_with_options(project_id, user_id, request, headers, runtime)

    def get_project_member_with_options(self, project_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_commit(self, project_id, sha, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_commit_with_options(project_id, sha, request, headers, runtime)

    def get_repository_commit_with_options(self, project_id, sha, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/commits/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sha))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_info_with_options(request, headers, runtime)

    def get_repository_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['Identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_tag(self, project_id, tag_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_with_options(project_id, tag_name, request, headers, runtime)

    def get_repository_tag_with_options(self, project_id, tag_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/tags/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(tag_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository_tag_v2(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_v2with_options(project_id, request, headers, runtime)

    def get_repository_tag_v2with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/tag/info' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            self.call_api(params, req, runtime)
        )

    def get_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_info_with_options(request, headers, runtime)

    def get_user_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/user/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def is_sls_user_authrized_codeup(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.is_sls_user_authrized_codeup_with_options(request, headers, runtime)

    def is_sls_user_authrized_codeup_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_sub_user_id):
            body['aliyunSubUserId'] = request.aliyun_sub_user_id
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsSlsUserAuthrizedCodeup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/repository/is_codeup_authrized',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_member(self, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(group_id, request, headers, runtime)

    def list_group_member_with_options(self, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_repositories(self, identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_repositories_with_options(identity, request, headers, runtime)

    def list_group_repositories_with_options(self, identity, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/%s/projects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(identity)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    def list_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_merge_request_comments(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_comments_with_options(project_id, merge_request_id, request, headers, runtime)

    def list_merge_request_comments_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestComments',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/merge_request/%s/comments' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_merge_requests(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_requests_with_options(request, headers, runtime)

    def list_merge_requests_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequests',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/merge_requests/advanced_search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organization_security_scores(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_security_scores_with_options(request, headers, runtime)

    def list_organization_security_scores_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationSecurityScores',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/organization/security/scores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organizations_with_options(request, headers, runtime)

    def list_organizations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/organization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repositories(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    def list_repositories_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_branches(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_branches_with_options(project_id, request, headers, runtime)

    def list_repository_branches_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_code(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_code_with_options(request, headers, runtime)

    def list_repository_code_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['IsCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_path):
            body['RepositoryPath'] = request.repository_path
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRepositoryCode',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/search/v3/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_commit_diff(self, project_id, sha, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commit_diff_with_options(project_id, sha, request, headers, runtime)

    def list_repository_commit_diff_with_options(self, project_id, sha, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/repository/commits/%s/diff' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sha))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_commits(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commits_with_options(project_id, request, headers, runtime)

    def list_repository_commits_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/commits' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_member(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_options(project_id, request, headers, runtime)

    def list_repository_member_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_member_with_inherited(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_inherited_with_options(project_id, request, headers, runtime)

    def list_repository_member_with_inherited_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/all_members' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_protected_branch(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_protected_branch_with_options(project_id, request, headers, runtime)

    def list_repository_protected_branch_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/protect_branches' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_tags(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tags_with_options(project_id, request, headers, runtime)

    def list_repository_tags_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/tags' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_tree(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tree_with_options(project_id, request, headers, runtime)

    def list_repository_tree_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/tree' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository_webhook(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_webhook_with_options(project_id, request, headers, runtime)

    def list_repository_webhook_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/hooks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def merge_merge_request(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    def merge_merge_request_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MergeMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/merge_request/%s/merge' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sls_relation(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sls_relation_with_options(request, headers, runtime)

    def query_sls_relation_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySlsRelation',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/repository/query_sls_relation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.QuerySlsRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def related_sls_log_store(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.related_sls_log_store_with_options(request, headers, runtime)

    def related_sls_log_store_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.default_viewer):
            body['defaultViewer'] = request.default_viewer
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/repository/related_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.RelatedSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_repository_mirror_sync(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_repository_mirror_sync_with_options(project_id, request, headers, runtime)

    def trigger_repository_mirror_sync_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/mirror' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.TriggerRepositoryMirrorSyncResponse(),
            self.call_api(params, req, runtime)
        )

    def un_related_sls_log_store(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_related_sls_log_store_with_options(request, headers, runtime)

    def un_related_sls_log_store_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnRelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/repository/unrelated_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UnRelatedSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def update_file(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(project_id, request, headers, runtime)

    def update_file_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/repository/files' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_member(self, group_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_member_with_options(group_id, user_id, request, headers, runtime)

    def update_group_member_with_options(self, group_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/groups/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_merge_request(self, project_id, merge_request_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    def update_merge_request_with_options(self, project_id, merge_request_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/merge_request/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def update_merge_request_comment(self, project_id, merge_request_id, note_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_comment_with_options(project_id, merge_request_id, note_id, request, headers, runtime)

    def update_merge_request_comment_with_options(self, project_id, merge_request_id, note_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/merge_requests/%s/notes/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(merge_request_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(note_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_merge_request_setting(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_setting_with_options(project_id, request, headers, runtime)

    def update_merge_request_setting_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v4/projects/%s/settings/merge_requests' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repository(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_with_options(project_id, request, headers, runtime)

    def update_repository_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repository_member(self, project_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_member_with_options(project_id, user_id, request, headers, runtime)

    def update_repository_member_with_options(self, project_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname='/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )
