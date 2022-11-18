# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pds.client import Client as GatewayClientClient
from alibabacloud_pds20220301 import models as pds_20220301_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client = None  # type: SPIClient

    def __init__(self, config):
        super(Client, self).__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''

    def authorize(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_with_options(request, headers, runtime)

    def authorize_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pds_20220301_models.AuthorizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not UtilClient.is_unset(request.login_type):
            query['login_type'] = request.login_type
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.response_type):
            query['response_type'] = request.response_type
        if not UtilClient.is_unset(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Authorize',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/oauth/authorize',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AuthorizeResponse(),
            self.execute(params, req, runtime)
        )

    def batch(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_with_options(request, headers, runtime)

    def batch_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.requests):
            body['requests'] = request.requests
        if not UtilClient.is_unset(request.resource):
            body['resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Batch',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.BatchResponse(),
            self.execute(params, req, runtime)
        )

    def cancel_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_share_link_with_options(request, headers, runtime)

    def cancel_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def clear_recyclebin(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clear_recyclebin_with_options(request, headers, runtime)

    def clear_recyclebin_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/recyclebin/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ClearRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    def complete_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.complete_file_with_options(request, headers, runtime)

    def complete_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/complete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CompleteFileResponse(),
            self.execute(params, req, runtime)
        )

    def copy_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copy_file_with_options(request, headers, runtime)

    def copy_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/copy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CopyFileResponse(),
            self.execute(params, req, runtime)
        )

    def create_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_drive_with_options(request, headers, runtime)

    def create_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.default):
            body['default'] = request.default
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.drive_type):
            body['drive_type'] = request.drive_type
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDriveResponse(),
            self.execute(params, req, runtime)
        )

    def create_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(request, headers, runtime)

    def create_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.content_hash):
            body['content_hash'] = request.content_hash
        if not UtilClient.is_unset(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not UtilClient.is_unset(request.content_type):
            body['content_type'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.image_media_metadata):
            body['image_media_metadata'] = request.image_media_metadata
        if not UtilClient.is_unset(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        if not UtilClient.is_unset(request.video_media_metadata):
            body['video_media_metadata'] = request.video_media_metadata
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateFileResponse(),
            self.execute(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    def create_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.is_root):
            body['is_root'] = request.is_root
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/group/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_share_link_with_options(request, headers, runtime)

    def create_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    def create_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateUserResponse(),
            self.execute(params, req, runtime)
        )

    def delete_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_drive_with_options(request, headers, runtime)

    def delete_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDriveResponse(),
            self.execute(params, req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(request, headers, runtime)

    def delete_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteFileResponse(),
            self.execute(params, req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(request, headers, runtime)

    def delete_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_revision(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_revision_with_options(request, headers, runtime)

    def delete_revision_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/revision/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteRevisionResponse(),
            self.execute(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    def delete_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteUserResponse(),
            self.execute(params, req, runtime)
        )

    def delta_get_last_cursor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delta_get_last_cursor_with_options(request, headers, runtime)

    def delta_get_last_cursor_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeltaGetLastCursor',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get_last_cursor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeltaGetLastCursorResponse(),
            self.execute(params, req, runtime)
        )

    def download_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.download_file_with_options(request, headers, runtime)

    def download_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.office_thumbnail_process):
            body['office_thumbnail_process'] = request.office_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/download',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DownloadFileResponse(),
            self.execute(params, req, runtime)
        )

    def file_add_permission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_add_permission_with_options(request, headers, runtime)

    def file_add_permission_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileAddPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/add_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileAddPermissionResponse(),
            self.execute(params, req, runtime)
        )

    def file_delete_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_delete_user_tags_with_options(request, headers, runtime)

    def file_delete_user_tags_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileDeleteUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/delete_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileDeleteUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    def file_list_permission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_list_permission_with_options(request, headers, runtime)

    def file_list_permission_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileListPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/list_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileListPermissionResponse(),
            self.execute(params, req, runtime)
        )

    def file_put_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_put_user_tags_with_options(request, headers, runtime)

    def file_put_user_tags_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FilePutUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/put_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FilePutUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    def file_remove_permission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_remove_permission_with_options(request, headers, runtime)

    def file_remove_permission_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileRemovePermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/remove_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileRemovePermissionResponse(),
            self.execute(params, req, runtime)
        )

    def get_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(request, headers, runtime)

    def get_async_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/async_task/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetAsyncTaskResponse(),
            self.execute(params, req, runtime)
        )

    def get_default_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_default_drive_with_options(request, headers, runtime)

    def get_default_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDefaultDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/get_default_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDefaultDriveResponse(),
            self.execute(params, req, runtime)
        )

    def get_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_download_url_with_options(request, headers, runtime)

    def get_download_url_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['file_name'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get_download_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDownloadUrlResponse(),
            self.execute(params, req, runtime)
        )

    def get_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_drive_with_options(request, headers, runtime)

    def get_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDriveResponse(),
            self.execute(params, req, runtime)
        )

    def get_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    def get_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetFileResponse(),
            self.execute(params, req, runtime)
        )

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(request, headers, runtime)

    def get_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/group/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetGroupResponse(),
            self.execute(params, req, runtime)
        )

    def get_link_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_with_options(request, headers, runtime)

    def get_link_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/account/get_link_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoResponse(),
            self.execute(params, req, runtime)
        )

    def get_link_info_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_by_user_id_with_options(request, headers, runtime)

    def get_link_info_by_user_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfoByUserId',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/account/get_link_info_by_user_id',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoByUserIdResponse(),
            self.execute(params, req, runtime)
        )

    def get_revision(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_revision_with_options(request, headers, runtime)

    def get_revision_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/revision/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetRevisionResponse(),
            self.execute(params, req, runtime)
        )

    def get_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_with_options(request, headers, runtime)

    def get_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def get_share_link_by_anonymous(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_by_anonymous_with_options(request, headers, runtime)

    def get_share_link_by_anonymous_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkByAnonymous',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/get_by_anonymous',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkByAnonymousResponse(),
            self.execute(params, req, runtime)
        )

    def get_share_link_token(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_token_with_options(request, headers, runtime)

    def get_share_link_token_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkToken',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/get_share_token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkTokenResponse(),
            self.execute(params, req, runtime)
        )

    def get_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upload_url_with_options(request, headers, runtime)

    def get_upload_url_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get_upload_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUploadUrlResponse(),
            self.execute(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    def get_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUserResponse(),
            self.execute(params, req, runtime)
        )

    def get_video_preview_play_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_info_with_options(request, headers, runtime)

    def get_video_preview_play_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.template_id):
            body['template_id'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get_video_preview_play_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayInfoResponse(),
            self.execute(params, req, runtime)
        )

    def get_video_preview_play_meta(self, domain_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_meta_with_options(domain_id, request, headers, runtime)

    def get_video_preview_play_meta_with_options(self, domain_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['domain_id'] = domain_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayMeta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/get_video_preview_play_meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayMetaResponse(),
            self.execute(params, req, runtime)
        )

    def import_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_user_with_options(request, headers, runtime)

    def import_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not UtilClient.is_unset(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not UtilClient.is_unset(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not UtilClient.is_unset(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ImportUserResponse(),
            self.execute(params, req, runtime)
        )

    def link_account(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.link_account_with_options(request, headers, runtime)

    def link_account_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/account/link',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.LinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    def list_address_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_address_groups_with_options(request, headers, runtime)

    def list_address_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/list_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    def list_delta(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_delta_with_options(request, headers, runtime)

    def list_delta_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/list_delta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDeltaResponse(),
            self.execute(params, req, runtime)
        )

    def list_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_drive_with_options(request, headers, runtime)

    def list_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDriveResponse(),
            self.execute(params, req, runtime)
        )

    def list_facegroups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_facegroups_with_options(request, headers, runtime)

    def list_facegroups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFacegroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/list_facegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFacegroupsResponse(),
            self.execute(params, req, runtime)
        )

    def list_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_file_with_options(request, headers, runtime)

    def list_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFileResponse(),
            self.execute(params, req, runtime)
        )

    def list_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    def list_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_my_drives(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_my_drives_with_options(request, headers, runtime)

    def list_my_drives_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyDrives',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/list_my_drives',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyDrivesResponse(),
            self.execute(params, req, runtime)
        )

    def list_recyclebin(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recyclebin_with_options(request, headers, runtime)

    def list_recyclebin_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/recyclebin/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    def list_revision(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_revision_with_options(request, headers, runtime)

    def list_revision_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/revision/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRevisionResponse(),
            self.execute(params, req, runtime)
        )

    def list_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_share_link_with_options(request, headers, runtime)

    def list_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    def list_tags_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/list_tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListTagsResponse(),
            self.execute(params, req, runtime)
        )

    def list_uploaded_parts(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_uploaded_parts_with_options(request, headers, runtime)

    def list_uploaded_parts_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUploadedParts',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/list_uploaded_parts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUploadedPartsResponse(),
            self.execute(params, req, runtime)
        )

    def list_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_with_options(request, headers, runtime)

    def list_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUserResponse(),
            self.execute(params, req, runtime)
        )

    def move_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_file_with_options(request, headers, runtime)

    def move_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/move',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.MoveFileResponse(),
            self.execute(params, req, runtime)
        )

    def parse_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.parse_keywords_with_options(request, headers, runtime)

    def parse_keywords_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['keywords'] = request.keywords
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ParseKeywords',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/parse_keywords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ParseKeywordsResponse(),
            self.execute(params, req, runtime)
        )

    def remove_face_group_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_face_group_file_with_options(request, headers, runtime)

    def remove_face_group_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveFaceGroupFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/albums/unassign_facegroup_item',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveFaceGroupFileResponse(),
            self.execute(params, req, runtime)
        )

    def restore_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_file_with_options(request, headers, runtime)

    def restore_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/recyclebin/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreFileResponse(),
            self.execute(params, req, runtime)
        )

    def restore_revision(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_revision_with_options(request, headers, runtime)

    def restore_revision_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/revision/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreRevisionResponse(),
            self.execute(params, req, runtime)
        )

    def scan_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_file_with_options(request, headers, runtime)

    def scan_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ScanFileResponse(),
            self.execute(params, req, runtime)
        )

    def search_address_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_address_groups_with_options(request, headers, runtime)

    def search_address_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_level):
            body['address_level'] = request.address_level
        if not UtilClient.is_unset(request.address_names):
            body['address_names'] = request.address_names
        if not UtilClient.is_unset(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/search_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    def search_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_drive_with_options(request, headers, runtime)

    def search_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDriveResponse(),
            self.execute(params, req, runtime)
        )

    def search_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_file_with_options(request, headers, runtime)

    def search_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchFileResponse(),
            self.execute(params, req, runtime)
        )

    def search_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_share_link_with_options(request, headers, runtime)

    def search_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creators):
            body['creators'] = request.creators
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def search_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_user_with_options(request, headers, runtime)

    def search_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchUserResponse(),
            self.execute(params, req, runtime)
        )

    def token(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.token_with_options(request, headers, runtime)

    def token_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assertion):
            body['assertion'] = request.assertion
        if not UtilClient.is_unset(request.client_id):
            body['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Token',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/oauth/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TokenResponse(),
            self.execute(params, req, runtime)
        )

    def trash_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trash_file_with_options(request, headers, runtime)

    def trash_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TrashFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/recyclebin/trash',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TrashFileResponse(),
            self.execute(params, req, runtime)
        )

    def update_drive(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_drive_with_options(request, headers, runtime)

    def update_drive_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/drive/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDriveResponse(),
            self.execute(params, req, runtime)
        )

    def update_facegroup(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_facegroup_with_options(request, headers, runtime)

    def update_facegroup_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFacegroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/image/update_facegroup_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFacegroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(request, headers, runtime)

    def update_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.starred):
            body['starred'] = request.starred
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFileResponse(),
            self.execute(params, req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    def update_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/group/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_revision(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_revision_with_options(request, headers, runtime)

    def update_revision_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not UtilClient.is_unset(request.revision_description):
            body['revision_description'] = request.revision_description
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/file/revision/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateRevisionResponse(),
            self.execute(params, req, runtime)
        )

    def update_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_share_link_with_options(request, headers, runtime)

    def update_share_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            body['download_count'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.preview_count):
            body['preview_count'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            body['report_count'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            body['save_count'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/share_link/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    def update_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname='/v2/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateUserResponse(),
            self.execute(params, req, runtime)
        )
