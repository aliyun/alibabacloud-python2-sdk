# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('codeup', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            self.do_roarequest('DeleteRepositoryMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(user_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            self.do_roarequest('CreateRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/repository/protect_branches' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            self.do_roarequest('CreateMergeRequest', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/merge_requests' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.extern_user_id):
            query['ExternUserId'] = request.extern_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse(),
            self.do_roarequest('DeleteRepositoryMemberWithExternUid', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/members/remove' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            self.do_roarequest('DeleteRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/remove' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            self.do_roarequest('GetRepositoryTag', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/tags/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(tag_name)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            self.do_roarequest('UpdateMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s/merge_request/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            self.do_roarequest('UpdateRepository', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            self.do_roarequest('UpdateMergeRequestComment', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s/merge_requests/%s/notes/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id), TeaConverter.to_unicode(note_id)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.TriggerRepositoryMirrorSyncResponse(),
            self.do_roarequest('TriggerRepositoryMirrorSync', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/mirror' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            self.do_roarequest('DeleteBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/repository/branches/delete' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            self.do_roarequest('ListRepositoryCommitDiff', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/commits/%s/diff' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(sha)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            self.do_roarequest('GetRepositoryInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/info', 'json', req, runtime)
        )

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
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            self.do_roarequest('AcceptMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s/merge_request/%s/accept' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            self.do_roarequest('DeleteFile', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/repository/files' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            self.do_roarequest('DeleteRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v4/projects/%s/repository/protect_branches/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(protected_branch_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            self.do_roarequest('DeleteRepositoryTagV2', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/repository/tag/delete' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            self.do_roarequest('GetFileLastCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/files/last_commit' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            self.do_roarequest('UpdateFile', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v4/projects/%s/repository/files' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            self.do_roarequest('UpdateRepositoryMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(user_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            self.do_roarequest('AddRepositoryMember', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/members' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            self.do_roarequest('CreateSshKey', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/user/keys', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            self.do_roarequest('ListRepositoryTags', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/tags' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            self.do_roarequest('AddWebhook', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/hooks' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            self.do_roarequest('EnableRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/keys/%s/enable' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(key_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            self.do_roarequest('GetUserInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/user/current', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            self.do_roarequest('ListRepositoryTree', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/tree' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            self.do_roarequest('DeleteRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/groups/%s/remove' % TeaConverter.to_unicode(group_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            self.do_roarequest('DeleteRepositoryWebhook', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/hooks/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(webhook_id)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
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
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            self.do_roarequest('ListRepositoryMember', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/members' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            self.do_roarequest('CreateTag', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/repository/tags' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            self.do_roarequest('GetRepositoryCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/commits/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(sha)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            self.do_roarequest('AddGroupMember', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/groups/%s/members' % TeaConverter.to_unicode(group_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            self.do_roarequest('GetBranchInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/branches/detail' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            self.do_roarequest('ListMergeRequestComments', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/merge_request/%s/comments' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            self.do_roarequest('CreateRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/groups', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            self.do_roarequest('GetMergeRequestDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/merge_request/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            self.do_roarequest('ListGroups', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/groups/all', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            self.do_roarequest('ListRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/protect_branches' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
        )

    def list_organizations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organizations_with_options(request, headers, runtime)

    def list_organizations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            self.do_roarequest('ListOrganizations', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/organization', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            self.do_roarequest('GetProjectMember', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/members/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(user_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            self.do_roarequest('CreateFile', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/repository/files' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            self.do_roarequest('ListRepositoryCommits', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/commits' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            self.do_roarequest('GetMergeRequestApproveStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/merge_request/%s/approve_status' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            self.do_roarequest('ListRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/all', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            self.do_roarequest('UpdateMergeRequestSetting', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v4/projects/%s/settings/merge_requests' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            self.do_roarequest('ListGroupMember', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/groups/%s/members' % TeaConverter.to_unicode(group_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            self.do_roarequest('UpdateGroupMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/groups/%s/members/%s' % (TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(user_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            self.do_roarequest('CreateMergeRequestComment', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v4/projects/%s/merge_request/%s/comments' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            self.do_roarequest('CreateRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/keys' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            self.do_roarequest('DeleteRepositoryTag', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/projects/%s/repository/tags/%s' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(tag_name)), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            self.do_roarequest('CreateRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            self.do_roarequest('GetCodeCompletion', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v2/service/invoke/%s' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            self.do_roarequest('ListMergeRequests', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/merge_requests/advanced_search', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            self.do_roarequest('ListOrganizationSecurityScores', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/organization/security/scores', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            self.do_roarequest('GetFileBlobs', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/repository/blobs' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            self.do_roarequest('MergeMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', '/api/v3/projects/%s/merge_request/%s/merge' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(merge_request_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            self.do_roarequest('DeleteGroupMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', '/api/v3/groups/%s/members/%s' % (TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(user_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            self.do_roarequest('ListRepositoryMemberWithInherited', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/all_members' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            self.do_roarequest('GetGroupDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/groups/detail', 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            self.do_roarequest('GetCodeupOrganization', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/organization/%s' % TeaConverter.to_unicode(organization_identity), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            self.do_roarequest('GetOrganizationSecurityCenterStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/organization/security/status', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            self.do_roarequest('ListRepositoryBranches', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/branches' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            self.do_roarequest('CreateBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', '/api/v3/projects/%s/repository/branches' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationRepositorySettingResponse(),
            self.do_roarequest('GetOrganizationRepositorySetting', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/organization/settings/repo', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            self.do_roarequest('ListGroupRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/groups/%s/projects' % TeaConverter.to_unicode(identity), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            self.do_roarequest('GetRepositoryTagV2', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/repository/tag/info' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            self.do_roarequest('GetMergeRequestSetting', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v4/projects/%s/settings/merge_requests' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            self.do_roarequest('ListRepositoryWebhook', '2020-04-14', 'HTTPS', 'GET', 'AK', '/api/v3/projects/%s/hooks' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
        )
