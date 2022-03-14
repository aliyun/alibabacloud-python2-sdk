# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDataLevelPermissionRuleUsersRequest(TeaModel):
    def __init__(self, add_user_model=None):
        self.add_user_model = add_user_model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataLevelPermissionRuleUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_user_model is not None:
            result['AddUserModel'] = self.add_user_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddUserModel') is not None:
            self.add_user_model = m.get('AddUserModel')
        return self


class AddDataLevelPermissionRuleUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataLevelPermissionRuleUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDataLevelPermissionRuleUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDataLevelPermissionRuleUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDataLevelPermissionRuleUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDataLevelPermissionRuleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(self, cube_id=None, operate_type=None, rule_type=None, target_ids=None, target_type=None):
        self.cube_id = cube_id  # type: str
        self.operate_type = operate_type  # type: str
        self.rule_type = rule_type  # type: str
        self.target_ids = target_ids  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataLevelPermissionWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AddDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataLevelPermissionWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDataLevelPermissionWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDataLevelPermissionWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddShareReportRequest(TeaModel):
    def __init__(self, auth_point=None, expire_date=None, share_to_id=None, share_to_type=None, works_id=None):
        self.auth_point = auth_point  # type: int
        self.expire_date = expire_date  # type: long
        self.share_to_id = share_to_id  # type: str
        self.share_to_type = share_to_type  # type: int
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShareReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class AddShareReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShareReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddShareReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddShareReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddShareReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddShareReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(self, account_name=None, admin_user=None, auth_admin_user=None, nick_name=None, user_type=None):
        self.account_name = account_name  # type: str
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.nick_name = nick_name  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AddUserResponseBodyResult(TeaModel):
    def __init__(self, account_name=None, admin_user=None, auth_admin_user=None, nick_name=None, user_id=None,
                 user_type=None):
        self.account_name = account_name  # type: str
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.nick_name = nick_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: AddUserResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddUserResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserGroupMemberRequest(TeaModel):
    def __init__(self, user_group_id=None, user_id_list=None):
        self.user_group_id = user_group_id  # type: str
        self.user_id_list = user_id_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class AddUserGroupMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserGroupMemberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserGroupMembersRequest(TeaModel):
    def __init__(self, user_group_ids=None, user_id=None):
        self.user_group_ids = user_group_ids  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        # 请求ID。
        self.request_id = request_id  # type: str
        # 接口执行结果。取值范围：true：请求成功false：请求失败
        self.result = result  # type: bool
        # 是否请求成功。取值范围：true：请求成功false：请求失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserGroupMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserTagMetaRequest(TeaModel):
    def __init__(self, tag_description=None, tag_name=None):
        self.tag_description = tag_description  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserTagMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class AddUserTagMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserTagMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserTagMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserTagMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserTagMetaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToWorkspaceRequest(TeaModel):
    def __init__(self, role_id=None, user_id=None, workspace_id=None):
        self.role_id = role_id  # type: long
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddUserToWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserToWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserToWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToWorkspaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWorkspaceUsersRequest(TeaModel):
    def __init__(self, role_id=None, user_ids=None, workspace_id=None):
        self.role_id = role_id  # type: long
        self.user_ids = user_ids  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceUsersResponseBodyResult(TeaModel):
    def __init__(self, failure=None, failure_detail=None, success=None, total=None):
        self.failure = failure  # type: int
        self.failure_detail = failure_detail  # type: dict[str, any]
        self.success = success  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceUsersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['Failure'] = self.failure
        if self.failure_detail is not None:
            result['FailureDetail'] = self.failure_detail
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Failure') is not None:
            self.failure = m.get('Failure')
        if m.get('FailureDetail') is not None:
            self.failure_detail = m.get('FailureDetail')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class AddWorkspaceUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: AddWorkspaceUsersResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddWorkspaceUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddWorkspaceUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWorkspaceUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddWorkspaceUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWorkspaceUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddWorkspaceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeMenuRequest(TeaModel):
    def __init__(self, auth_points_value=None, data_portal_id=None, menu_ids=None, user_group_ids=None,
                 user_ids=None):
        self.auth_points_value = auth_points_value  # type: int
        self.data_portal_id = data_portal_id  # type: str
        self.menu_ids = menu_ids  # type: str
        self.user_group_ids = user_group_ids  # type: str
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeMenuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_points_value is not None:
            result['AuthPointsValue'] = self.auth_points_value
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthPointsValue') is not None:
            self.auth_points_value = m.get('AuthPointsValue')
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AuthorizeMenuResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeMenuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeMenuResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AuthorizeMenuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeMenuResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeMenuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAuthorizationMenuRequest(TeaModel):
    def __init__(self, data_portal_id=None, menu_ids=None, user_group_ids=None, user_ids=None):
        self.data_portal_id = data_portal_id  # type: str
        self.menu_ids = menu_ids  # type: str
        self.user_group_ids = user_group_ids  # type: str
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAuthorizationMenuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class CancelAuthorizationMenuResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAuthorizationMenuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelAuthorizationMenuResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelAuthorizationMenuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelAuthorizationMenuResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelAuthorizationMenuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCollectionRequest(TeaModel):
    def __init__(self, user_id=None, works_id=None):
        self.user_id = user_id  # type: str
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CancelCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelCollectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelReportShareRequest(TeaModel):
    def __init__(self, report_id=None, share_to_ids=None, share_to_type=None):
        self.report_id = report_id  # type: str
        self.share_to_ids = share_to_ids  # type: str
        self.share_to_type = share_to_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelReportShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.share_to_ids is not None:
            result['ShareToIds'] = self.share_to_ids
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ShareToIds') is not None:
            self.share_to_ids = m.get('ShareToIds')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        return self


class CancelReportShareResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelReportShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelReportShareResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelReportShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelReportShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelReportShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeVisibilityModelRequest(TeaModel):
    def __init__(self, data_portal_id=None, menu_ids=None, show_only_with_access=None):
        self.data_portal_id = data_portal_id  # type: str
        self.menu_ids = menu_ids  # type: str
        self.show_only_with_access = show_only_with_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeVisibilityModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')
        return self


class ChangeVisibilityModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeVisibilityModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeVisibilityModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeVisibilityModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeVisibilityModelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeVisibilityModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckReadableRequest(TeaModel):
    def __init__(self, user_id=None, works_id=None):
        self.user_id = user_id  # type: str
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckReadableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CheckReadableResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckReadableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckReadableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckReadableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckReadableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckReadableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequest(TeaModel):
    def __init__(self, account_name=None, account_type=None, cmpt_id=None, expire_time=None, global_param=None,
                 ticket_num=None, user_id=None, watermark_param=None, works_id=None):
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: int
        self.cmpt_id = cmpt_id  # type: str
        self.expire_time = expire_time  # type: int
        self.global_param = global_param  # type: str
        self.ticket_num = ticket_num  # type: int
        self.user_id = user_id  # type: str
        self.watermark_param = watermark_param  # type: str
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.global_param is not None:
            result['GlobalParam'] = self.global_param
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTicketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(self, parent_user_group_id=None, user_group_description=None, user_group_id=None,
                 user_group_name=None):
        self.parent_user_group_id = parent_user_group_id  # type: str
        self.user_group_description = user_group_description  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelayTicketExpireTimeRequest(TeaModel):
    def __init__(self, expire_time=None, ticket=None):
        self.expire_time = expire_time  # type: int
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelayTicketExpireTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class DelayTicketExpireTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelayTicketExpireTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelayTicketExpireTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DelayTicketExpireTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DelayTicketExpireTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DelayTicketExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLevelPermissionRuleUsersRequest(TeaModel):
    def __init__(self, delete_user_model=None):
        self.delete_user_model = delete_user_model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLevelPermissionRuleUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_user_model is not None:
            result['DeleteUserModel'] = self.delete_user_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteUserModel') is not None:
            self.delete_user_model = m.get('DeleteUserModel')
        return self


class DeleteDataLevelPermissionRuleUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLevelPermissionRuleUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLevelPermissionRuleUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataLevelPermissionRuleUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataLevelPermissionRuleUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataLevelPermissionRuleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLevelRuleConfigRequest(TeaModel):
    def __init__(self, cube_id=None, rule_id=None):
        self.cube_id = cube_id  # type: str
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLevelRuleConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteDataLevelRuleConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLevelRuleConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLevelRuleConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataLevelRuleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataLevelRuleConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataLevelRuleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTicketRequest(TeaModel):
    def __init__(self, ticket=None):
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class DeleteTicketResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTicketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, transfer_user_id=None, user_id=None):
        self.transfer_user_id = transfer_user_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transfer_user_id is not None:
            result['TransferUserId'] = self.transfer_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransferUserId') is not None:
            self.transfer_user_id = m.get('TransferUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserFromWorkspaceRequest(TeaModel):
    def __init__(self, user_id=None, workspace_id=None):
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserFromWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteUserFromWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserFromWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserFromWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserFromWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserFromWorkspaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserFromWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(self, user_group_id=None):
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupMemberRequest(TeaModel):
    def __init__(self, user_group_id=None, user_id=None):
        self.user_group_id = user_group_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserGroupMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupMemberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupMembersRequest(TeaModel):
    def __init__(self, user_group_ids=None, user_id=None):
        self.user_group_ids = user_group_ids  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserTagMetaRequest(TeaModel):
    def __init__(self, tag_id=None):
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserTagMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeleteUserTagMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserTagMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserTagMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserTagMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserTagMetaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupInfoRequest(TeaModel):
    def __init__(self, keyword=None):
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class GetUserGroupInfoResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, create_user=None, identified_path=None, modified_time=None,
                 modify_user=None, parent_usergroup_id=None, usergroup_desc=None, usergroup_id=None, usergroup_name=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.identified_path = identified_path  # type: str
        self.modified_time = modified_time  # type: str
        self.modify_user = modify_user  # type: str
        self.parent_usergroup_id = parent_usergroup_id  # type: str
        self.usergroup_desc = usergroup_desc  # type: str
        self.usergroup_id = usergroup_id  # type: str
        self.usergroup_name = usergroup_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class GetUserGroupInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetUserGroupInfoResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserGroupInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetUserGroupInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserGroupInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserGroupInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserGroupInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListByUserGroupIdRequest(TeaModel):
    def __init__(self, user_group_ids=None):
        self.user_group_ids = user_group_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListByUserGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListByUserGroupIdResponseBodyResultUserGroupModels(TeaModel):
    def __init__(self, create_time=None, create_user=None, identified_path=None, modified_time=None,
                 modify_user=None, parent_usergroup_id=None, usergroup_desc=None, usergroup_id=None, usergroup_name=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.identified_path = identified_path  # type: str
        self.modified_time = modified_time  # type: str
        self.modify_user = modify_user  # type: str
        self.parent_usergroup_id = parent_usergroup_id  # type: str
        self.usergroup_desc = usergroup_desc  # type: str
        self.usergroup_id = usergroup_id  # type: str
        self.usergroup_name = usergroup_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListByUserGroupIdResponseBodyResultUserGroupModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class ListByUserGroupIdResponseBodyResult(TeaModel):
    def __init__(self, failed_user_group_ids=None, user_group_models=None):
        self.failed_user_group_ids = failed_user_group_ids  # type: list[str]
        self.user_group_models = user_group_models  # type: list[ListByUserGroupIdResponseBodyResultUserGroupModels]

    def validate(self):
        if self.user_group_models:
            for k in self.user_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListByUserGroupIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_user_group_ids is not None:
            result['FailedUserGroupIds'] = self.failed_user_group_ids
        result['UserGroupModels'] = []
        if self.user_group_models is not None:
            for k in self.user_group_models:
                result['UserGroupModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedUserGroupIds') is not None:
            self.failed_user_group_ids = m.get('FailedUserGroupIds')
        self.user_group_models = []
        if m.get('UserGroupModels') is not None:
            for k in m.get('UserGroupModels'):
                temp_model = ListByUserGroupIdResponseBodyResultUserGroupModels()
                self.user_group_models.append(temp_model.from_map(k))
        return self


class ListByUserGroupIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListByUserGroupIdResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListByUserGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListByUserGroupIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListByUserGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListByUserGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListByUserGroupIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListByUserGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionsRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListCollectionsResponseBodyResult(TeaModel):
    def __init__(self, favorite_id=None, owner_id=None, works_id=None, works_name=None, works_type=None,
                 workspace_id=None, workspace_name=None):
        self.favorite_id = favorite_id  # type: int
        self.owner_id = owner_id  # type: str
        self.works_id = works_id  # type: str
        self.works_name = works_name  # type: str
        self.works_type = works_type  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite_id is not None:
            result['FavoriteId'] = self.favorite_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.works_name is not None:
            result['WorksName'] = self.works_name
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FavoriteId') is not None:
            self.favorite_id = m.get('FavoriteId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorksName') is not None:
            self.works_name = m.get('WorksName')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListCollectionsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListCollectionsResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCollectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCollectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCollectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCollectionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCubeDataLevelPermissionConfigRequest(TeaModel):
    def __init__(self, cube_id=None, rule_type=None):
        self.cube_id = cube_id  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCubeDataLevelPermissionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListCubeDataLevelPermissionConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCubeDataLevelPermissionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCubeDataLevelPermissionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCubeDataLevelPermissionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCubeDataLevelPermissionConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCubeDataLevelPermissionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(self, cube_id=None, rule_type=None):
        self.cube_id = cube_id  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataLevelPermissionWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListDataLevelPermissionWhiteListResponseBodyResultUsersModel(TeaModel):
    def __init__(self, user_groups=None, users=None):
        self.user_groups = user_groups  # type: list[str]
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataLevelPermissionWhiteListResponseBodyResultUsersModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_groups is not None:
            result['UserGroups'] = self.user_groups
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroups') is not None:
            self.user_groups = m.get('UserGroups')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListDataLevelPermissionWhiteListResponseBodyResult(TeaModel):
    def __init__(self, cube_id=None, rule_type=None, users_model=None):
        self.cube_id = cube_id  # type: str
        self.rule_type = rule_type  # type: str
        self.users_model = users_model  # type: ListDataLevelPermissionWhiteListResponseBodyResultUsersModel

    def validate(self):
        if self.users_model:
            self.users_model.validate()

    def to_map(self):
        _map = super(ListDataLevelPermissionWhiteListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.users_model is not None:
            result['UsersModel'] = self.users_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('UsersModel') is not None:
            temp_model = ListDataLevelPermissionWhiteListResponseBodyResultUsersModel()
            self.users_model = temp_model.from_map(m['UsersModel'])
        return self


class ListDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListDataLevelPermissionWhiteListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListDataLevelPermissionWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListDataLevelPermissionWhiteListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataLevelPermissionWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataLevelPermissionWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFavoriteReportsRequest(TeaModel):
    def __init__(self, keyword=None, page_size=None, tree_type=None, user_id=None):
        self.keyword = keyword  # type: str
        self.page_size = page_size  # type: int
        self.tree_type = tree_type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFavoriteReportsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListFavoriteReportsResponseBodyResultData(TeaModel):
    def __init__(self, favorite=None, gmt_create=None, gmt_modified=None, has_edit_auth=None, has_view_auth=None,
                 name=None, owner_name=None, owner_num=None, publish_status=None, tree_id=None, type=None,
                 workspace_id=None, workspace_name=None):
        self.favorite = favorite  # type: bool
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_edit_auth = has_edit_auth  # type: bool
        self.has_view_auth = has_view_auth  # type: bool
        self.name = name  # type: str
        self.owner_name = owner_name  # type: str
        self.owner_num = owner_num  # type: str
        self.publish_status = publish_status  # type: int
        self.tree_id = tree_id  # type: str
        self.type = type  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFavoriteReportsResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListFavoriteReportsResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[ListFavoriteReportsResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFavoriteReportsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFavoriteReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListFavoriteReportsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListFavoriteReportsResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListFavoriteReportsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListFavoriteReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFavoriteReportsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFavoriteReportsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFavoriteReportsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFavoriteReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortalMenuAuthorizationRequest(TeaModel):
    def __init__(self, data_portal_id=None):
        self.data_portal_id = data_portal_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortalMenuAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        return self


class ListPortalMenuAuthorizationResponseBodyResultReceivers(TeaModel):
    def __init__(self, receiver_id=None, receiver_type=None):
        self.receiver_id = receiver_id  # type: str
        self.receiver_type = receiver_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortalMenuAuthorizationResponseBodyResultReceivers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        return self


class ListPortalMenuAuthorizationResponseBodyResult(TeaModel):
    def __init__(self, menu_id=None, receivers=None, show_only_with_access=None):
        self.menu_id = menu_id  # type: str
        self.receivers = receivers  # type: list[ListPortalMenuAuthorizationResponseBodyResultReceivers]
        self.show_only_with_access = show_only_with_access  # type: bool

    def validate(self):
        if self.receivers:
            for k in self.receivers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPortalMenuAuthorizationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.menu_id is not None:
            result['MenuId'] = self.menu_id
        result['Receivers'] = []
        if self.receivers is not None:
            for k in self.receivers:
                result['Receivers'].append(k.to_map() if k else None)
        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MenuId') is not None:
            self.menu_id = m.get('MenuId')
        self.receivers = []
        if m.get('Receivers') is not None:
            for k in m.get('Receivers'):
                temp_model = ListPortalMenuAuthorizationResponseBodyResultReceivers()
                self.receivers.append(temp_model.from_map(k))
        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')
        return self


class ListPortalMenuAuthorizationResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListPortalMenuAuthorizationResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPortalMenuAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPortalMenuAuthorizationResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPortalMenuAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPortalMenuAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPortalMenuAuthorizationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPortalMenuAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortalMenusRequest(TeaModel):
    def __init__(self, data_portal_id=None, user_id=None):
        self.data_portal_id = data_portal_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortalMenusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListPortalMenusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortalMenusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPortalMenusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPortalMenusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPortalMenusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPortalMenusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentViewReportsRequest(TeaModel):
    def __init__(self, keyword=None, offset_day=None, page_size=None, query_mode=None, tree_type=None, user_id=None):
        self.keyword = keyword  # type: str
        self.offset_day = offset_day  # type: int
        self.page_size = page_size  # type: int
        self.query_mode = query_mode  # type: str
        self.tree_type = tree_type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecentViewReportsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.offset_day is not None:
            result['OffsetDay'] = self.offset_day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OffsetDay') is not None:
            self.offset_day = m.get('OffsetDay')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRecentViewReportsResponseBodyResultData(TeaModel):
    def __init__(self, favorite=None, gmt_create=None, gmt_modified=None, has_edit_auth=None, has_view_auth=None,
                 latest_view_time=None, name=None, owner_name=None, owner_num=None, publish_status=None, tree_id=None, type=None,
                 view_count=None, workspace_id=None, workspace_name=None):
        self.favorite = favorite  # type: bool
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_edit_auth = has_edit_auth  # type: bool
        self.has_view_auth = has_view_auth  # type: bool
        self.latest_view_time = latest_view_time  # type: str
        self.name = name  # type: str
        self.owner_name = owner_name  # type: str
        self.owner_num = owner_num  # type: str
        self.publish_status = publish_status  # type: int
        self.tree_id = tree_id  # type: str
        self.type = type  # type: str
        self.view_count = view_count  # type: long
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecentViewReportsResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.latest_view_time is not None:
            result['LatestViewTime'] = self.latest_view_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.view_count is not None:
            result['ViewCount'] = self.view_count
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('LatestViewTime') is not None:
            self.latest_view_time = m.get('LatestViewTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListRecentViewReportsResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[ListRecentViewReportsResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecentViewReportsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRecentViewReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListRecentViewReportsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListRecentViewReportsResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListRecentViewReportsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRecentViewReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRecentViewReportsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRecentViewReportsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecentViewReportsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRecentViewReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedReportsRequest(TeaModel):
    def __init__(self, keyword=None, page_size=None, tree_type=None, user_id=None):
        self.keyword = keyword  # type: str
        self.page_size = page_size  # type: int
        self.tree_type = tree_type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedReportsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSharedReportsResponseBodyResultData(TeaModel):
    def __init__(self, favorite=None, gmt_create=None, gmt_modified=None, has_edit_auth=None, has_view_auth=None,
                 name=None, owner_name=None, owner_num=None, publish_status=None, tree_id=None, type=None,
                 workspace_id=None, workspace_name=None):
        self.favorite = favorite  # type: bool
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_edit_auth = has_edit_auth  # type: bool
        self.has_view_auth = has_view_auth  # type: bool
        self.name = name  # type: str
        self.owner_name = owner_name  # type: str
        self.owner_num = owner_num  # type: str
        self.publish_status = publish_status  # type: int
        self.tree_id = tree_id  # type: str
        self.type = type  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedReportsResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListSharedReportsResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[ListSharedReportsResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSharedReportsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSharedReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListSharedReportsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListSharedReportsResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSharedReportsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSharedReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSharedReportsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSharedReportsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSharedReportsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSharedReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsByUserIdRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserGroupsByUserIdResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, create_user=None, identified_path=None, modified_time=None,
                 modify_user=None, parent_usergroup_id=None, usergroup_desc=None, usergroup_id=None, usergroup_name=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.identified_path = identified_path  # type: str
        self.modified_time = modified_time  # type: str
        self.modify_user = modify_user  # type: str
        self.parent_usergroup_id = parent_usergroup_id  # type: str
        self.usergroup_desc = usergroup_desc  # type: str
        self.usergroup_id = usergroup_id  # type: str
        self.usergroup_name = usergroup_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsByUserIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class ListUserGroupsByUserIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListUserGroupsByUserIdResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListUserGroupsByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserGroupsByUserIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserGroupsByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsByUserIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserGroupsByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataServiceRequest(TeaModel):
    def __init__(self, api_id=None, conditions=None, return_fields=None):
        self.api_id = api_id  # type: str
        self.conditions = conditions  # type: str
        self.return_fields = return_fields  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.return_fields is not None:
            result['ReturnFields'] = self.return_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ReturnFields') is not None:
            self.return_fields = m.get('ReturnFields')
        return self


class QueryDataServiceResponseBodyResultHeaders(TeaModel):
    def __init__(self, aggregator=None, column=None, data_type=None, granularity=None, label=None, type=None):
        self.aggregator = aggregator  # type: str
        self.column = column  # type: str
        self.data_type = data_type  # type: str
        self.granularity = granularity  # type: str
        self.label = label  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataServiceResponseBodyResultHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.column is not None:
            result['Column'] = self.column
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataServiceResponseBodyResult(TeaModel):
    def __init__(self, headers=None, sql=None, values=None):
        self.headers = headers  # type: list[QueryDataServiceResponseBodyResultHeaders]
        self.sql = sql  # type: str
        self.values = values  # type: list[dict[str, any]]

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDataServiceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = QueryDataServiceResponseBodyResultHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class QueryDataServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryDataServiceResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryDataServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDataServiceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDataServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDataServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDataServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDataServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetDetailInfoRequest(TeaModel):
    def __init__(self, dataset_id=None):
        self.dataset_id = dataset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetDetailInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetDetailInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetDetailInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetDetailInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDatasetDetailInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDatasetDetailInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetInfoRequest(TeaModel):
    def __init__(self, dataset_id=None):
        self.dataset_id = dataset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetInfoResponseBodyResultCubeTableList(TeaModel):
    def __init__(self, caption=None, customsql=None, datasource_id=None, ds_type=None, fact_table=None, sql=None,
                 table_name=None, unique_id=None):
        self.caption = caption  # type: str
        self.customsql = customsql  # type: bool
        self.datasource_id = datasource_id  # type: str
        self.ds_type = ds_type  # type: str
        self.fact_table = fact_table  # type: bool
        self.sql = sql  # type: str
        self.table_name = table_name  # type: str
        self.unique_id = unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBodyResultCubeTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.customsql is not None:
            result['Customsql'] = self.customsql
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.fact_table is not None:
            result['FactTable'] = self.fact_table
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('Customsql') is not None:
            self.customsql = m.get('Customsql')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('FactTable') is not None:
            self.fact_table = m.get('FactTable')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class QueryDatasetInfoResponseBodyResultDimensionList(TeaModel):
    def __init__(self, caption=None, data_type=None, dimension_type=None, expression=None, fact_column=None,
                 granularity=None, ref_uid=None, table_unique_id=None, uid=None):
        self.caption = caption  # type: str
        self.data_type = data_type  # type: str
        self.dimension_type = dimension_type  # type: str
        self.expression = expression  # type: str
        self.fact_column = fact_column  # type: str
        self.granularity = granularity  # type: str
        self.ref_uid = ref_uid  # type: str
        self.table_unique_id = table_unique_id  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBodyResultDimensionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.ref_uid is not None:
            result['RefUid'] = self.ref_uid
        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('RefUid') is not None:
            self.ref_uid = m.get('RefUid')
        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryDatasetInfoResponseBodyResultDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBodyResultDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryDatasetInfoResponseBodyResultMeasureList(TeaModel):
    def __init__(self, caption=None, data_type=None, expression=None, fact_column=None, measure_type=None,
                 table_unique_id=None, uid=None):
        self.caption = caption  # type: str
        self.data_type = data_type  # type: str
        self.expression = expression  # type: str
        self.fact_column = fact_column  # type: str
        self.measure_type = measure_type  # type: str
        self.table_unique_id = table_unique_id  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBodyResultMeasureList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column
        if self.measure_type is not None:
            result['MeasureType'] = self.measure_type
        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')
        if m.get('MeasureType') is not None:
            self.measure_type = m.get('MeasureType')
        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryDatasetInfoResponseBodyResult(TeaModel):
    def __init__(self, cube_table_list=None, custimze_sql=None, dataset_id=None, dataset_name=None,
                 dimension_list=None, directory=None, ds_id=None, ds_name=None, ds_type=None, gmt_create=None, gmt_modify=None,
                 measure_list=None, owner_id=None, owner_name=None, row_level=None, workspace_id=None, workspace_name=None):
        self.cube_table_list = cube_table_list  # type: list[QueryDatasetInfoResponseBodyResultCubeTableList]
        self.custimze_sql = custimze_sql  # type: bool
        self.dataset_id = dataset_id  # type: str
        self.dataset_name = dataset_name  # type: str
        self.dimension_list = dimension_list  # type: list[QueryDatasetInfoResponseBodyResultDimensionList]
        self.directory = directory  # type: QueryDatasetInfoResponseBodyResultDirectory
        self.ds_id = ds_id  # type: str
        self.ds_name = ds_name  # type: str
        self.ds_type = ds_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.measure_list = measure_list  # type: list[QueryDatasetInfoResponseBodyResultMeasureList]
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.row_level = row_level  # type: bool
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.cube_table_list:
            for k in self.cube_table_list:
                if k:
                    k.validate()
        if self.dimension_list:
            for k in self.dimension_list:
                if k:
                    k.validate()
        if self.directory:
            self.directory.validate()
        if self.measure_list:
            for k in self.measure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CubeTableList'] = []
        if self.cube_table_list is not None:
            for k in self.cube_table_list:
                result['CubeTableList'].append(k.to_map() if k else None)
        if self.custimze_sql is not None:
            result['CustimzeSql'] = self.custimze_sql
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['DimensionList'] = []
        if self.dimension_list is not None:
            for k in self.dimension_list:
                result['DimensionList'].append(k.to_map() if k else None)
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_name is not None:
            result['DsName'] = self.ds_name
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['MeasureList'] = []
        if self.measure_list is not None:
            for k in self.measure_list:
                result['MeasureList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.row_level is not None:
            result['RowLevel'] = self.row_level
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cube_table_list = []
        if m.get('CubeTableList') is not None:
            for k in m.get('CubeTableList'):
                temp_model = QueryDatasetInfoResponseBodyResultCubeTableList()
                self.cube_table_list.append(temp_model.from_map(k))
        if m.get('CustimzeSql') is not None:
            self.custimze_sql = m.get('CustimzeSql')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.dimension_list = []
        if m.get('DimensionList') is not None:
            for k in m.get('DimensionList'):
                temp_model = QueryDatasetInfoResponseBodyResultDimensionList()
                self.dimension_list.append(temp_model.from_map(k))
        if m.get('Directory') is not None:
            temp_model = QueryDatasetInfoResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.measure_list = []
        if m.get('MeasureList') is not None:
            for k in m.get('MeasureList'):
                temp_model = QueryDatasetInfoResponseBodyResultMeasureList()
                self.measure_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryDatasetInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryDatasetInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryDatasetInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDatasetInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDatasetInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetListRequest(TeaModel):
    def __init__(self, directory_id=None, keyword=None, page_num=None, page_size=None, with_children=None,
                 workspace_id=None):
        self.directory_id = directory_id  # type: str
        self.keyword = keyword  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.with_children = with_children  # type: bool
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.with_children is not None:
            result['WithChildren'] = self.with_children
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WithChildren') is not None:
            self.with_children = m.get('WithChildren')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryDatasetListResponseBodyResultDataDataSource(TeaModel):
    def __init__(self, ds_id=None, ds_name=None, ds_type=None):
        self.ds_id = ds_id  # type: str
        self.ds_name = ds_name  # type: str
        self.ds_type = ds_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetListResponseBodyResultDataDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_name is not None:
            result['DsName'] = self.ds_name
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        return self


class QueryDatasetListResponseBodyResultDataDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetListResponseBodyResultDataDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryDatasetListResponseBodyResultData(TeaModel):
    def __init__(self, create_time=None, data_source=None, dataset_id=None, dataset_name=None, description=None,
                 directory=None, modify_time=None, owner_id=None, owner_name=None, row_level=None, workspace_id=None,
                 workspace_name=None):
        self.create_time = create_time  # type: str
        self.data_source = data_source  # type: QueryDatasetListResponseBodyResultDataDataSource
        self.dataset_id = dataset_id  # type: str
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.directory = directory  # type: QueryDatasetListResponseBodyResultDataDirectory
        self.modify_time = modify_time  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.row_level = row_level  # type: bool
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QueryDatasetListResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.row_level is not None:
            result['RowLevel'] = self.row_level
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryDatasetListResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryDatasetListResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDatasetListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDatasetListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryDatasetListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryDatasetListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryDatasetListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDatasetListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDatasetListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetSwitchInfoRequest(TeaModel):
    def __init__(self, cube_id=None):
        self.cube_id = cube_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetSwitchInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        return self


class QueryDatasetSwitchInfoResponseBodyResult(TeaModel):
    def __init__(self, cube_id=None, is_open_column_level_permission=None, is_open_row_level_permission=None):
        self.cube_id = cube_id  # type: str
        self.is_open_column_level_permission = is_open_column_level_permission  # type: int
        self.is_open_row_level_permission = is_open_row_level_permission  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetSwitchInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.is_open_column_level_permission is not None:
            result['IsOpenColumnLevelPermission'] = self.is_open_column_level_permission
        if self.is_open_row_level_permission is not None:
            result['IsOpenRowLevelPermission'] = self.is_open_row_level_permission
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('IsOpenColumnLevelPermission') is not None:
            self.is_open_column_level_permission = m.get('IsOpenColumnLevelPermission')
        if m.get('IsOpenRowLevelPermission') is not None:
            self.is_open_row_level_permission = m.get('IsOpenRowLevelPermission')
        return self


class QueryDatasetSwitchInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryDatasetSwitchInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryDatasetSwitchInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetSwitchInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetSwitchInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDatasetSwitchInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDatasetSwitchInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatasetSwitchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEmbeddedInfoResponseBodyResultDetail(TeaModel):
    def __init__(self, dashboard_offline_query=None, page=None, report=None):
        self.dashboard_offline_query = dashboard_offline_query  # type: int
        self.page = page  # type: int
        self.report = report  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEmbeddedInfoResponseBodyResultDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_offline_query is not None:
            result['DashboardOfflineQuery'] = self.dashboard_offline_query
        if self.page is not None:
            result['Page'] = self.page
        if self.report is not None:
            result['Report'] = self.report
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardOfflineQuery') is not None:
            self.dashboard_offline_query = m.get('DashboardOfflineQuery')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        return self


class QueryEmbeddedInfoResponseBodyResult(TeaModel):
    def __init__(self, detail=None, embedded_count=None, max_count=None):
        self.detail = detail  # type: QueryEmbeddedInfoResponseBodyResultDetail
        self.embedded_count = embedded_count  # type: int
        self.max_count = max_count  # type: int

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(QueryEmbeddedInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.embedded_count is not None:
            result['EmbeddedCount'] = self.embedded_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = QueryEmbeddedInfoResponseBodyResultDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('EmbeddedCount') is not None:
            self.embedded_count = m.get('EmbeddedCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class QueryEmbeddedInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryEmbeddedInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryEmbeddedInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryEmbeddedInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEmbeddedInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryEmbeddedInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEmbeddedInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEmbeddedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEmbeddedStausRequest(TeaModel):
    def __init__(self, works_id=None):
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEmbeddedStausRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryEmbeddedStausResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEmbeddedStausResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEmbeddedStausResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryEmbeddedStausResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEmbeddedStausResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEmbeddedStausResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrganizationWorkspaceListRequest(TeaModel):
    def __init__(self, keyword=None, page_num=None, page_size=None, user_id=None):
        self.keyword = keyword  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrganizationWorkspaceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryOrganizationWorkspaceListResponseBodyResultData(TeaModel):
    def __init__(self, allow_publish_operation=None, allow_share_operation=None, create_time=None,
                 create_user=None, create_user_account_name=None, modified_time=None, modify_user=None,
                 modify_user_account_name=None, organization_id=None, owner=None, owner_account_name=None, workspace_description=None,
                 workspace_id=None, workspace_name=None):
        self.allow_publish_operation = allow_publish_operation  # type: bool
        self.allow_share_operation = allow_share_operation  # type: bool
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.create_user_account_name = create_user_account_name  # type: str
        self.modified_time = modified_time  # type: str
        self.modify_user = modify_user  # type: str
        self.modify_user_account_name = modify_user_account_name  # type: str
        self.organization_id = organization_id  # type: str
        self.owner = owner  # type: str
        self.owner_account_name = owner_account_name  # type: str
        self.workspace_description = workspace_description  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrganizationWorkspaceListResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_publish_operation is not None:
            result['AllowPublishOperation'] = self.allow_publish_operation
        if self.allow_share_operation is not None:
            result['AllowShareOperation'] = self.allow_share_operation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.create_user_account_name is not None:
            result['CreateUserAccountName'] = self.create_user_account_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.modify_user_account_name is not None:
            result['ModifyUserAccountName'] = self.modify_user_account_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name
        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowPublishOperation') is not None:
            self.allow_publish_operation = m.get('AllowPublishOperation')
        if m.get('AllowShareOperation') is not None:
            self.allow_share_operation = m.get('AllowShareOperation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('CreateUserAccountName') is not None:
            self.create_user_account_name = m.get('CreateUserAccountName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ModifyUserAccountName') is not None:
            self.modify_user_account_name = m.get('ModifyUserAccountName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')
        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryOrganizationWorkspaceListResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryOrganizationWorkspaceListResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrganizationWorkspaceListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrganizationWorkspaceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryOrganizationWorkspaceListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryOrganizationWorkspaceListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryOrganizationWorkspaceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryOrganizationWorkspaceListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrganizationWorkspaceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOrganizationWorkspaceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrganizationWorkspaceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOrganizationWorkspaceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReadableResourcesListByUserIdRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReadableResourcesListByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryReadableResourcesListByUserIdResponseBodyResultDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReadableResourcesListByUserIdResponseBodyResultDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryReadableResourcesListByUserIdResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, description=None, directory=None, modify_name=None, modify_time=None,
                 owner_id=None, owner_name=None, security_level=None, status=None, third_part_auth_flag=None, work_name=None,
                 work_type=None, works_id=None, workspace_id=None, workspace_name=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.directory = directory  # type: QueryReadableResourcesListByUserIdResponseBodyResultDirectory
        self.modify_name = modify_name  # type: str
        self.modify_time = modify_time  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.security_level = security_level  # type: str
        self.status = status  # type: int
        self.third_part_auth_flag = third_part_auth_flag  # type: int
        self.work_name = work_name  # type: str
        self.work_type = work_type  # type: str
        self.works_id = works_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QueryReadableResourcesListByUserIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryReadableResourcesListByUserIdResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryReadableResourcesListByUserIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryReadableResourcesListByUserIdResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryReadableResourcesListByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryReadableResourcesListByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryReadableResourcesListByUserIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryReadableResourcesListByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryReadableResourcesListByUserIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryReadableResourcesListByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShareListRequest(TeaModel):
    def __init__(self, report_id=None):
        self.report_id = report_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryShareListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class QueryShareListResponseBodyResult(TeaModel):
    def __init__(self, auth_point=None, expire_date=None, report_id=None, share_id=None, share_to_id=None,
                 share_to_name=None, share_to_type=None, share_type=None):
        self.auth_point = auth_point  # type: int
        self.expire_date = expire_date  # type: long
        self.report_id = report_id  # type: str
        self.share_id = share_id  # type: str
        self.share_to_id = share_to_id  # type: str
        self.share_to_name = share_to_name  # type: str
        self.share_to_type = share_to_type  # type: int
        self.share_type = share_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryShareListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.share_id is not None:
            result['ShareId'] = self.share_id
        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id
        if self.share_to_name is not None:
            result['ShareToName'] = self.share_to_name
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')
        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')
        if m.get('ShareToName') is not None:
            self.share_to_name = m.get('ShareToName')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class QueryShareListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryShareListResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryShareListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryShareListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryShareListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryShareListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryShareListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryShareListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySharesToUserListRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySharesToUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuerySharesToUserListResponseBodyResultDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySharesToUserListResponseBodyResultDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QuerySharesToUserListResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, description=None, directory=None, modify_name=None, modify_time=None,
                 owner_id=None, owner_name=None, security_level=None, status=None, third_part_auth_flag=None, work_name=None,
                 work_type=None, works_id=None, workspace_id=None, workspace_name=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.directory = directory  # type: QuerySharesToUserListResponseBodyResultDirectory
        self.modify_name = modify_name  # type: str
        self.modify_time = modify_time  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.security_level = security_level  # type: str
        self.status = status  # type: int
        self.third_part_auth_flag = third_part_auth_flag  # type: int
        self.work_name = work_name  # type: str
        self.work_type = work_type  # type: str
        self.works_id = works_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QuerySharesToUserListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QuerySharesToUserListResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QuerySharesToUserListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QuerySharesToUserListResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySharesToUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QuerySharesToUserListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySharesToUserListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySharesToUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySharesToUserListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySharesToUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTicketInfoRequest(TeaModel):
    def __init__(self, ticket=None):
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTicketInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class QueryTicketInfoResponseBodyResult(TeaModel):
    def __init__(self, access_ticket=None, cmpt_id=None, global_param=None, invalid_time=None, max_ticket_num=None,
                 organization_id=None, register_time=None, used_ticket_num=None, user_id=None, watermark_param=None, works_id=None):
        self.access_ticket = access_ticket  # type: str
        self.cmpt_id = cmpt_id  # type: str
        self.global_param = global_param  # type: str
        self.invalid_time = invalid_time  # type: str
        self.max_ticket_num = max_ticket_num  # type: int
        self.organization_id = organization_id  # type: str
        self.register_time = register_time  # type: str
        self.used_ticket_num = used_ticket_num  # type: int
        self.user_id = user_id  # type: str
        self.watermark_param = watermark_param  # type: str
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTicketInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ticket is not None:
            result['AccessTicket'] = self.access_ticket
        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id
        if self.global_param is not None:
            result['GlobalParam'] = self.global_param
        if self.invalid_time is not None:
            result['InvalidTime'] = self.invalid_time
        if self.max_ticket_num is not None:
            result['MaxTicketNum'] = self.max_ticket_num
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.used_ticket_num is not None:
            result['UsedTicketNum'] = self.used_ticket_num
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTicket') is not None:
            self.access_ticket = m.get('AccessTicket')
        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')
        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')
        if m.get('InvalidTime') is not None:
            self.invalid_time = m.get('InvalidTime')
        if m.get('MaxTicketNum') is not None:
            self.max_ticket_num = m.get('MaxTicketNum')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('UsedTicketNum') is not None:
            self.used_ticket_num = m.get('UsedTicketNum')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryTicketInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryTicketInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryTicketInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryTicketInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTicketInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTicketInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTicketInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTicketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserGroupListByParentIdRequest(TeaModel):
    def __init__(self, parent_user_group_id=None):
        self.parent_user_group_id = parent_user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserGroupListByParentIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        return self


class QueryUserGroupListByParentIdResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, create_user=None, identified_path=None, modified_time=None,
                 modify_user=None, parent_user_group_id=None, user_group_description=None, user_group_id=None,
                 user_group_name=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.identified_path = identified_path  # type: str
        self.modified_time = modified_time  # type: str
        self.modify_user = modify_user  # type: str
        self.parent_user_group_id = parent_user_group_id  # type: str
        self.user_group_description = user_group_description  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserGroupListByParentIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryUserGroupListByParentIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryUserGroupListByParentIdResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserGroupListByParentIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserGroupListByParentIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserGroupListByParentIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserGroupListByParentIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserGroupListByParentIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserGroupListByParentIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserGroupMemberRequest(TeaModel):
    def __init__(self, keyword=None, user_group_id=None):
        self.keyword = keyword  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryUserGroupMemberResponseBodyResult(TeaModel):
    def __init__(self, id=None, is_user_group=None, name=None, parent_user_group_id=None,
                 parent_user_group_name=None):
        self.id = id  # type: str
        self.is_user_group = is_user_group  # type: bool
        self.name = name  # type: str
        self.parent_user_group_id = parent_user_group_id  # type: str
        self.parent_user_group_name = parent_user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserGroupMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_user_group is not None:
            result['IsUserGroup'] = self.is_user_group
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.parent_user_group_name is not None:
            result['ParentUserGroupName'] = self.parent_user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsUserGroup') is not None:
            self.is_user_group = m.get('IsUserGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('ParentUserGroupName') is not None:
            self.parent_user_group_name = m.get('ParentUserGroupName')
        return self


class QueryUserGroupMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryUserGroupMemberResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserGroupMemberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoByAccountRequest(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoByAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        return self


class QueryUserInfoByAccountResponseBodyResult(TeaModel):
    def __init__(self, account_id=None, account_name=None, admin_user=None, auth_admin_user=None, email=None,
                 nick_name=None, phone=None, user_id=None, user_type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.email = email  # type: str
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoByAccountResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.email is not None:
            result['Email'] = self.email
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserInfoByAccountResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryUserInfoByAccountResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryUserInfoByAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserInfoByAccountResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserInfoByAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserInfoByAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserInfoByAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserInfoByAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoByUserIdRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryUserInfoByUserIdResponseBodyResult(TeaModel):
    def __init__(self, account_id=None, account_name=None, admin_user=None, auth_admin_user=None, email=None,
                 nick_name=None, phone=None, user_id=None, user_type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.email = email  # type: str
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoByUserIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.email is not None:
            result['Email'] = self.email
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserInfoByUserIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryUserInfoByUserIdResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryUserInfoByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserInfoByUserIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserInfoByUserIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserInfoByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserInfoByUserIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserInfoByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserListRequest(TeaModel):
    def __init__(self, keyword=None, page_num=None, page_size=None):
        self.keyword = keyword  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryUserListResponseBodyResultData(TeaModel):
    def __init__(self, account_id=None, account_name=None, admin_user=None, auth_admin_user=None, nick_name=None,
                 user_id=None, user_type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.nick_name = nick_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserListResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserListResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryUserListResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryUserListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryUserListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryUserListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserRoleInfoInWorkspaceRequest(TeaModel):
    def __init__(self, user_id=None, workspace_id=None):
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserRoleInfoInWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryUserRoleInfoInWorkspaceResponseBodyResult(TeaModel):
    def __init__(self, role_code=None, role_id=None, role_name=None):
        self.role_code = role_code  # type: str
        self.role_id = role_id  # type: long
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserRoleInfoInWorkspaceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryUserRoleInfoInWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryUserRoleInfoInWorkspaceResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryUserRoleInfoInWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserRoleInfoInWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserRoleInfoInWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserRoleInfoInWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserRoleInfoInWorkspaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserRoleInfoInWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserTagMetaListResponseBodyResult(TeaModel):
    def __init__(self, tag_description=None, tag_id=None, tag_name=None):
        self.tag_description = tag_description  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserTagMetaListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryUserTagMetaListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryUserTagMetaListResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserTagMetaListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserTagMetaListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserTagMetaListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserTagMetaListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserTagMetaListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserTagMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserTagValueListRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserTagValueListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryUserTagValueListResponseBodyResult(TeaModel):
    def __init__(self, tag_id=None, tag_name=None, tag_value=None):
        self.tag_id = tag_id  # type: str
        self.tag_name = tag_name  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserTagValueListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class QueryUserTagValueListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryUserTagValueListResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserTagValueListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserTagValueListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserTagValueListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserTagValueListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserTagValueListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserTagValueListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksRequest(TeaModel):
    def __init__(self, works_id=None):
        # 报表ID
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryWorksResponseBodyResultDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        # 目录ID
        self.id = id  # type: str
        # 目录名称
        self.name = name  # type: str
        # 目录ID的路径，例如：aa/bb/cc/dd
        self.path_id = path_id  # type: str
        # 目录ID的路径名称，例如：一层目录/二层目录
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksResponseBodyResultDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksResponseBodyResult(TeaModel):
    def __init__(self, auth_3rd_flag=None, description=None, directory=None, gmt_create=None, gmt_modify=None,
                 modify_name=None, owner_id=None, owner_name=None, security_level=None, status=None, work_name=None,
                 work_type=None, works_id=None, workspace_id=None, workspace_name=None):
        # 第三方嵌入状态
        self.auth_3rd_flag = auth_3rd_flag  # type: int
        # 描述
        self.description = description  # type: str
        # 所属空间目录信息
        self.directory = directory  # type: QueryWorksResponseBodyResultDirectory
        # 创建时间d
        self.gmt_create = gmt_create  # type: str
        # 修改时间
        self.gmt_modify = gmt_modify  # type: str
        # 修改显示名称
        self.modify_name = modify_name  # type: str
        # 所有者Id
        self.owner_id = owner_id  # type: str
        # 所有者显示名称
        self.owner_name = owner_name  # type: str
        # 安全策略：0 私有 1 协同编辑。 （
        self.security_level = security_level  # type: str
        # 报表发布状态 @PublishStatusEnum
        self.status = status  # type: int
        # 作品名称
        self.work_name = work_name  # type: str
        # 作品类型
        self.work_type = work_type  # type: str
        # 作品ID
        self.works_id = works_id  # type: str
        # 所属工作空间
        self.workspace_id = workspace_id  # type: str
        # 所属空间名称
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QueryWorksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        # QueryWorksModel
        self.result = result  # type: QueryWorksResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryWorksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryWorksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWorksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryWorksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksBloodRelationshipRequest(TeaModel):
    def __init__(self, works_id=None):
        # 报表ID
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksBloodRelationshipRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryWorksBloodRelationshipResponseBodyResultQueryParams(TeaModel):
    def __init__(self, area_id=None, area_name=None, caption=None, data_type=None, is_measure=None, path_id=None,
                 uid=None):
        # 所属位置：
        self.area_id = area_id  # type: str
        self.area_name = area_name  # type: str
        # 字段显示名称
        self.caption = caption  # type: str
        # 字段类型
        self.data_type = data_type  # type: str
        # 是否是度量
        self.is_measure = is_measure  # type: bool
        # 全局唯一的PathId。位于cube的level中pathId
        self.path_id = path_id  # type: str
        # 字段唯一ID。即cube中的name
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksBloodRelationshipResponseBodyResultQueryParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.is_measure is not None:
            result['IsMeasure'] = self.is_measure
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('IsMeasure') is not None:
            self.is_measure = m.get('IsMeasure')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryWorksBloodRelationshipResponseBodyResult(TeaModel):
    def __init__(self, component_id=None, component_name=None, component_type=None, component_type_name=None,
                 dataset_id=None, query_params=None):
        # 组件ID or  sheetId
        self.component_id = component_id  # type: str
        self.component_name = component_name  # type: str
        # 组件类型
        self.component_type = component_type  # type: int
        self.component_type_name = component_type_name  # type: str
        # 数据集ID
        self.dataset_id = dataset_id  # type: str
        # 查询参数引用的列信息
        self.query_params = query_params  # type: list[QueryWorksBloodRelationshipResponseBodyResultQueryParams]

    def validate(self):
        if self.query_params:
            for k in self.query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWorksBloodRelationshipResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.component_type_name is not None:
            result['ComponentTypeName'] = self.component_type_name
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        result['QueryParams'] = []
        if self.query_params is not None:
            for k in self.query_params:
                result['QueryParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('ComponentTypeName') is not None:
            self.component_type_name = m.get('ComponentTypeName')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        self.query_params = []
        if m.get('QueryParams') is not None:
            for k in m.get('QueryParams'):
                temp_model = QueryWorksBloodRelationshipResponseBodyResultQueryParams()
                self.query_params.append(temp_model.from_map(k))
        return self


class QueryWorksBloodRelationshipResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryWorksBloodRelationshipResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWorksBloodRelationshipResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryWorksBloodRelationshipResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksBloodRelationshipResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryWorksBloodRelationshipResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWorksBloodRelationshipResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryWorksBloodRelationshipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksByOrganizationRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, status=None, third_part_auth_flag=None, works_type=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.third_part_auth_flag = third_part_auth_flag  # type: int
        self.works_type = works_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksByOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        return self


class QueryWorksByOrganizationResponseBodyResultDataDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksByOrganizationResponseBodyResultDataDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksByOrganizationResponseBodyResultData(TeaModel):
    def __init__(self, auth_3rd_flag=None, description=None, directory=None, gmt_create=None, gmt_modify=None,
                 modify_name=None, owner_id=None, owner_name=None, security_level=None, status=None, work_name=None,
                 work_type=None, works_id=None, workspace_id=None, workspace_name=None):
        self.auth_3rd_flag = auth_3rd_flag  # type: int
        self.description = description  # type: str
        self.directory = directory  # type: QueryWorksByOrganizationResponseBodyResultDataDirectory
        self.gmt_create = gmt_create  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.modify_name = modify_name  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.security_level = security_level  # type: str
        self.status = status  # type: int
        self.work_name = work_name  # type: str
        self.work_type = work_type  # type: str
        self.works_id = works_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QueryWorksByOrganizationResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksByOrganizationResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksByOrganizationResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryWorksByOrganizationResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWorksByOrganizationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorksByOrganizationResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorksByOrganizationResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryWorksByOrganizationResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryWorksByOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksByOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksByOrganizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryWorksByOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWorksByOrganizationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryWorksByOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksByWorkspaceRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, status=None, third_part_auth_flag=None, works_type=None,
                 workspace_id=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.third_part_auth_flag = third_part_auth_flag  # type: int
        self.works_type = works_type  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksByWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryWorksByWorkspaceResponseBodyResultDataDirectory(TeaModel):
    def __init__(self, id=None, name=None, path_id=None, path_name=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.path_id = path_id  # type: str
        self.path_name = path_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorksByWorkspaceResponseBodyResultDataDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksByWorkspaceResponseBodyResultData(TeaModel):
    def __init__(self, auth_3rd_flag=None, description=None, directory=None, gmt_create=None, gmt_modify=None,
                 modify_name=None, owner_id=None, owner_name=None, security_level=None, status=None, work_name=None,
                 work_type=None, works_id=None, workspace_id=None, workspace_name=None):
        self.auth_3rd_flag = auth_3rd_flag  # type: int
        self.description = description  # type: str
        self.directory = directory  # type: QueryWorksByWorkspaceResponseBodyResultDataDirectory
        self.gmt_create = gmt_create  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.modify_name = modify_name  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.security_level = security_level  # type: str
        self.status = status  # type: int
        self.work_name = work_name  # type: str
        self.work_type = work_type  # type: str
        self.works_id = works_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(QueryWorksByWorkspaceResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksByWorkspaceResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksByWorkspaceResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryWorksByWorkspaceResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWorksByWorkspaceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorksByWorkspaceResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorksByWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryWorksByWorkspaceResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryWorksByWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksByWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksByWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryWorksByWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWorksByWorkspaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryWorksByWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorkspaceUserListRequest(TeaModel):
    def __init__(self, keyword=None, page_num=None, page_size=None, workspace_id=None):
        self.keyword = keyword  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorkspaceUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryWorkspaceUserListResponseBodyResultDataRole(TeaModel):
    def __init__(self, role_code=None, role_id=None, role_name=None):
        self.role_code = role_code  # type: str
        self.role_id = role_id  # type: long
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWorkspaceUserListResponseBodyResultDataRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryWorkspaceUserListResponseBodyResultData(TeaModel):
    def __init__(self, account_id=None, account_name=None, nick_name=None, role=None, user_id=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.nick_name = nick_name  # type: str
        self.role = role  # type: QueryWorkspaceUserListResponseBodyResultDataRole
        self.user_id = user_id  # type: str

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(QueryWorkspaceUserListResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Role') is not None:
            temp_model = QueryWorkspaceUserListResponseBodyResultDataRole()
            self.role = temp_model.from_map(m['Role'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryWorkspaceUserListResponseBodyResult(TeaModel):
    def __init__(self, data=None, page_num=None, page_size=None, total_num=None, total_pages=None):
        self.data = data  # type: list[QueryWorkspaceUserListResponseBodyResultData]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWorkspaceUserListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorkspaceUserListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorkspaceUserListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryWorkspaceUserListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryWorkspaceUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorkspaceUserListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorkspaceUserListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryWorkspaceUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWorkspaceUserListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryWorkspaceUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResultCallbackRequest(TeaModel):
    def __init__(self, application_id=None, handle_reason=None, status=None):
        self.application_id = application_id  # type: str
        self.handle_reason = handle_reason  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.handle_reason is not None:
            result['HandleReason'] = self.handle_reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('HandleReason') is not None:
            self.handle_reason = m.get('HandleReason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResultCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResultCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResultCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResultCallbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResultCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveFavoritesRequest(TeaModel):
    def __init__(self, user_id=None, works_id=None):
        self.user_id = user_id  # type: str
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveFavoritesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class SaveFavoritesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveFavoritesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveFavoritesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveFavoritesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveFavoritesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveFavoritesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionExtraConfigRequest(TeaModel):
    def __init__(self, cube_id=None, miss_hit_policy=None, rule_type=None):
        self.cube_id = cube_id  # type: str
        self.miss_hit_policy = miss_hit_policy  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionExtraConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.miss_hit_policy is not None:
            result['MissHitPolicy'] = self.miss_hit_policy
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('MissHitPolicy') is not None:
            self.miss_hit_policy = m.get('MissHitPolicy')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class SetDataLevelPermissionExtraConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionExtraConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionExtraConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDataLevelPermissionExtraConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDataLevelPermissionExtraConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDataLevelPermissionExtraConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionRuleConfigRequest(TeaModel):
    def __init__(self, rule_model=None):
        self.rule_model = rule_model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionRuleConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_model is not None:
            result['RuleModel'] = self.rule_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleModel') is not None:
            self.rule_model = m.get('RuleModel')
        return self


class SetDataLevelPermissionRuleConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionRuleConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionRuleConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDataLevelPermissionRuleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDataLevelPermissionRuleConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDataLevelPermissionRuleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(self, white_list_model=None):
        self.white_list_model = white_list_model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_list_model is not None:
            result['WhiteListModel'] = self.white_list_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WhiteListModel') is not None:
            self.white_list_model = m.get('WhiteListModel')
        return self


class SetDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataLevelPermissionWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDataLevelPermissionWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDataLevelPermissionWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLevelPermissionStatusRequest(TeaModel):
    def __init__(self, cube_id=None, is_open=None, rule_type=None):
        self.cube_id = cube_id  # type: str
        self.is_open = is_open  # type: int
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataLevelPermissionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.is_open is not None:
            result['IsOpen'] = self.is_open
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class UpdateDataLevelPermissionStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataLevelPermissionStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataLevelPermissionStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDataLevelPermissionStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDataLevelPermissionStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDataLevelPermissionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEmbeddedStatusRequest(TeaModel):
    def __init__(self, third_part_auth_flag=None, works_id=None):
        self.third_part_auth_flag = third_part_auth_flag  # type: bool
        self.works_id = works_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEmbeddedStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class UpdateEmbeddedStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEmbeddedStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEmbeddedStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEmbeddedStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEmbeddedStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEmbeddedStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketNumRequest(TeaModel):
    def __init__(self, ticket=None, ticket_num=None):
        self.ticket = ticket  # type: str
        self.ticket_num = ticket_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTicketNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        return self


class UpdateTicketNumResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTicketNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTicketNumResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTicketNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTicketNumResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTicketNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, admin_user=None, auth_admin_user=None, nick_name=None, user_id=None, user_type=None):
        self.admin_user = admin_user  # type: bool
        self.auth_admin_user = auth_admin_user  # type: bool
        self.nick_name = nick_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(self, user_group_description=None, user_group_id=None, user_group_name=None):
        self.user_group_description = user_group_description  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserTagMetaRequest(TeaModel):
    def __init__(self, tag_description=None, tag_id=None, tag_name=None):
        self.tag_description = tag_description  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserTagMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UpdateUserTagMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserTagMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserTagMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserTagMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserTagMetaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserTagValueRequest(TeaModel):
    def __init__(self, tag_id=None, tag_value=None, user_id=None):
        self.tag_id = tag_id  # type: str
        self.tag_value = tag_value  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserTagValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserTagValueResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserTagValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserTagValueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserTagValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserTagValueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserTagValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceUserRoleRequest(TeaModel):
    def __init__(self, role_id=None, user_id=None, workspace_id=None):
        self.role_id = role_id  # type: long
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceUserRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceUserRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceUserRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkspaceUserRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWorkspaceUserRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceUserRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateWorkspaceUserRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceUsersRoleRequest(TeaModel):
    def __init__(self, role_id=None, user_ids=None, workspace_id=None):
        self.role_id = role_id  # type: long
        self.user_ids = user_ids  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceUsersRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceUsersRoleResponseBodyResult(TeaModel):
    def __init__(self, failure=None, failure_detail=None, success=None, total=None):
        self.failure = failure  # type: int
        self.failure_detail = failure_detail  # type: dict[str, any]
        self.success = success  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceUsersRoleResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['Failure'] = self.failure
        if self.failure_detail is not None:
            result['FailureDetail'] = self.failure_detail
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Failure') is not None:
            self.failure = m.get('Failure')
        if m.get('FailureDetail') is not None:
            self.failure_detail = m.get('FailureDetail')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class UpdateWorkspaceUsersRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateWorkspaceUsersRoleResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceUsersRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateWorkspaceUsersRoleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkspaceUsersRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWorkspaceUsersRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceUsersRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateWorkspaceUsersRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawAllUserGroupsRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawAllUserGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class WithdrawAllUserGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawAllUserGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WithdrawAllUserGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WithdrawAllUserGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WithdrawAllUserGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WithdrawAllUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


