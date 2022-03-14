# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quickbi_public20220101 import models as quickbi_public_20220101_models
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
        self._endpoint = self.get_endpoint('quickbi-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_data_level_permission_rule_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_user_model):
            query['AddUserModel'] = request.add_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_data_level_permission_rule_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_rule_users_with_options(request, runtime)

    def add_data_level_permission_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_data_level_permission_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_white_list_with_options(request, runtime)

    def add_share_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_point):
            query['AuthPoint'] = request.auth_point
        if not UtilClient.is_unset(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not UtilClient.is_unset(request.share_to_id):
            query['ShareToId'] = request.share_to_id
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShareReport',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddShareReportResponse(),
            self.call_api(params, req, runtime)
        )

    def add_share_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_share_report_with_options(request, runtime)

    def add_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    def add_user_group_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_group_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_member_with_options(request, runtime)

    def add_user_group_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_members_with_options(request, runtime)

    def add_user_tag_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_tag_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_tag_meta_with_options(request, runtime)

    def add_user_to_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserToWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_to_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_workspace_with_options(request, runtime)

    def add_workspace_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWorkspaceUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddWorkspaceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_workspace_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_workspace_users_with_options(request, runtime)

    def authorize_menu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AuthorizeMenuResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_menu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_menu_with_options(request, runtime)

    def cancel_authorization_menu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAuthorizationMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelAuthorizationMenuResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_authorization_menu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_authorization_menu_with_options(request, runtime)

    def cancel_collection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCollection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_collection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_collection_with_options(request, runtime)

    def cancel_report_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.share_to_ids):
            query['ShareToIds'] = request.share_to_ids
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelReportShare',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelReportShareResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_report_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_report_share_with_options(request, runtime)

    def change_visibility_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibilityModel',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ChangeVisibilityModelResponse(),
            self.call_api(params, req, runtime)
        )

    def change_visibility_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_visibility_model_with_options(request, runtime)

    def check_readable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReadable',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CheckReadableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_readable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_readable_with_options(request, runtime)

    def create_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.cmpt_id):
            query['CmptId'] = request.cmpt_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.global_param):
            query['GlobalParam'] = request.global_param
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.watermark_param):
            query['WatermarkParam'] = request.watermark_param
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    def create_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    def delay_ticket_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelayTicketExpireTime',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DelayTicketExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def delay_ticket_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delay_ticket_expire_time_with_options(request, runtime)

    def delete_data_level_permission_rule_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_user_model):
            query['DeleteUserModel'] = request.delete_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_level_permission_rule_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_permission_rule_users_with_options(request, runtime)

    def delete_data_level_rule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_level_rule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_rule_config_with_options(request, runtime)

    def delete_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ticket_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transfer_user_id):
            query['TransferUserId'] = request.transfer_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_user_from_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserFromWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_from_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_from_workspace_with_options(request, runtime)

    def delete_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    def delete_user_group_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_member_with_options(request, runtime)

    def delete_user_group_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_members_with_options(request, runtime)

    def delete_user_tag_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_tag_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_tag_meta_with_options(request, runtime)

    def get_user_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroupInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.GetUserGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_info_with_options(request, runtime)

    def list_by_user_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListByUserGroupId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListByUserGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_by_user_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_by_user_group_id_with_options(request, runtime)

    def list_collections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_collections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    def list_cube_data_level_permission_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCubeDataLevelPermissionConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cube_data_level_permission_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cube_data_level_permission_config_with_options(request, runtime)

    def list_data_level_permission_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_level_permission_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_level_permission_white_list_with_options(request, runtime)

    def list_favorite_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFavoriteReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListFavoriteReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_favorite_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_favorite_reports_with_options(request, runtime)

    def list_portal_menu_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenuAuthorization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_portal_menu_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menu_authorization_with_options(request, runtime)

    def list_portal_menus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_portal_menus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menus_with_options(request, runtime)

    def list_recent_view_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.offset_day):
            query['OffsetDay'] = request.offset_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentViewReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListRecentViewReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_recent_view_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recent_view_reports_with_options(request, runtime)

    def list_shared_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListSharedReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shared_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_shared_reports_with_options(request, runtime)

    def list_user_groups_by_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListUserGroupsByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_by_user_id_with_options(request, runtime)

    def query_data_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conditions):
            query['Conditions'] = request.conditions
        if not UtilClient.is_unset(request.return_fields):
            query['ReturnFields'] = request.return_fields
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataService',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_data_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_data_service_with_options(request, runtime)

    def query_dataset_detail_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetDetailInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dataset_detail_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_detail_info_with_options(request, runtime)

    def query_dataset_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dataset_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_info_with_options(request, runtime)

    def query_dataset_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.with_children):
            query['WithChildren'] = request.with_children
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dataset_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_list_with_options(request, runtime)

    def query_dataset_switch_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetSwitchInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dataset_switch_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_switch_info_with_options(request, runtime)

    def query_embedded_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryEmbeddedInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_embedded_info(self):
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_info_with_options(runtime)

    def query_embedded_staus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmbeddedStaus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedStausResponse(),
            self.call_api(params, req, runtime)
        )

    def query_embedded_staus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_staus_with_options(request, runtime)

    def query_organization_workspace_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrganizationWorkspaceList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_organization_workspace_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_organization_workspace_list_with_options(request, runtime)

    def query_readable_resources_list_by_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReadableResourcesListByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_readable_resources_list_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_readable_resources_list_by_user_id_with_options(request, runtime)

    def query_share_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShareList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryShareListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_share_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_share_list_with_options(request, runtime)

    def query_shares_to_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySharesToUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QuerySharesToUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_shares_to_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_shares_to_user_list_with_options(request, runtime)

    def query_ticket_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTicketInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryTicketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_ticket_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_ticket_info_with_options(request, runtime)

    def query_user_group_list_by_parent_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupListByParentId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_group_list_by_parent_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_list_by_parent_id_with_options(request, runtime)

    def query_user_group_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_group_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_member_with_options(request, runtime)

    def query_user_info_by_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_info_by_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_account_with_options(request, runtime)

    def query_user_info_by_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_info_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_user_id_with_options(request, runtime)

    def query_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_list_with_options(request, runtime)

    def query_user_role_info_in_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserRoleInfoInWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_role_info_in_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_role_info_in_workspace_with_options(request, runtime)

    def query_user_tag_meta_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUserTagMetaList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_tag_meta_list(self):
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_meta_list_with_options(runtime)

    def query_user_tag_value_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserTagValueList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_tag_value_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_value_list_with_options(request, runtime)

    def query_works_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorks',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksResponse(),
            self.call_api(params, req, runtime)
        )

    def query_works(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_works_with_options(request, runtime)

    def query_works_blood_relationship_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksBloodRelationship',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    def query_works_blood_relationship(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_works_blood_relationship_with_options(request, runtime)

    def query_works_by_organization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByOrganization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_works_by_organization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_organization_with_options(request, runtime)

    def query_works_by_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_works_by_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_workspace_with_options(request, runtime)

    def query_workspace_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkspaceUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorkspaceUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_workspace_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_workspace_user_list_with_options(request, runtime)

    def result_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.handle_reason):
            query['HandleReason'] = request.handle_reason
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResultCallback',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def result_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.result_callback_with_options(request, runtime)

    def save_favorites_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveFavorites',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SaveFavoritesResponse(),
            self.call_api(params, req, runtime)
        )

    def save_favorites(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_favorites_with_options(request, runtime)

    def set_data_level_permission_extra_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.miss_hit_policy):
            query['MissHitPolicy'] = request.miss_hit_policy
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionExtraConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_level_permission_extra_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_extra_config_with_options(request, runtime)

    def set_data_level_permission_rule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_model):
            query['RuleModel'] = request.rule_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_level_permission_rule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_rule_config_with_options(request, runtime)

    def set_data_level_permission_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.white_list_model):
            query['WhiteListModel'] = request.white_list_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_level_permission_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_white_list_with_options(request, runtime)

    def update_data_level_permission_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.is_open):
            query['IsOpen'] = request.is_open
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataLevelPermissionStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_level_permission_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_level_permission_status_with_options(request, runtime)

    def update_embedded_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEmbeddedStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateEmbeddedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_embedded_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_embedded_status_with_options(request, runtime)

    def update_ticket_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTicketNum',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateTicketNumResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ticket_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ticket_num_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    def update_user_tag_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_tag_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_meta_with_options(request, runtime)

    def update_user_tag_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagValue',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagValueResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_tag_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_value_with_options(request, runtime)

    def update_workspace_user_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUserRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workspace_user_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_user_role_with_options(request, runtime)

    def update_workspace_users_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUsersRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workspace_users_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_users_role_with_options(request, runtime)

    def withdraw_all_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawAllUserGroups',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.WithdrawAllUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def withdraw_all_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.withdraw_all_user_groups_with_options(request, runtime)
