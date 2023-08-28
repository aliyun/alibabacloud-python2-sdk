# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class AddWorkspaceDocMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: AddWorkspaceDocMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(AddWorkspaceDocMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = AddWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class AddWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class AddWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None, role_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class AddWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class AddWorkspaceDocMembersRequest(TeaModel):
    def __init__(self, members=None, node_id=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[AddWorkspaceDocMembersRequestMembers]
        self.node_id = node_id  # type: str
        self.tenant_context = tenant_context  # type: AddWorkspaceDocMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(AddWorkspaceDocMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = AddWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, node_id=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.node_id = node_id  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceDocMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddWorkspaceDocMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddWorkspaceDocMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWorkspaceDocMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class AddWorkspaceMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: AddWorkspaceMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(AddWorkspaceMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = AddWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class AddWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class AddWorkspaceMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None, role_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class AddWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class AddWorkspaceMembersRequest(TeaModel):
    def __init__(self, members=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[AddWorkspaceMembersRequestMembers]
        self.tenant_context = tenant_context  # type: AddWorkspaceMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(AddWorkspaceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = AddWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceMembersResponseBody(TeaModel):
    def __init__(self, not_in_org_list=None, request_id=None):
        self.not_in_org_list = not_in_org_list  # type: list[str]
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkspaceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.not_in_org_list is not None:
            result['NotInOrgList'] = self.not_in_org_list
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotInOrgList') is not None:
            self.not_in_org_list = m.get('NotInOrgList')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddWorkspaceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddWorkspaceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWorkspaceMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSheetHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateSheetHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: CreateSheetHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(CreateSheetHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateSheetHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateSheetShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateSheetRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateSheetRequest(TeaModel):
    def __init__(self, name=None, tenant_context=None, workbook_id=None):
        self.name = name  # type: str
        self.tenant_context = tenant_context  # type: CreateSheetRequestTenantContext
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(CreateSheetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            temp_model = CreateSheetRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetShrinkRequest(TeaModel):
    def __init__(self, name=None, tenant_context_shrink=None, workbook_id=None):
        self.name = name  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetResponseBody(TeaModel):
    def __init__(self, id=None, name=None, request_id=None, visibility=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.visibility is not None:
            result['visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')
        return self


class CreateSheetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSheetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSheetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSheetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTodoTaskHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateTodoTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: CreateTodoTaskHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(CreateTodoTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateTodoTaskHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateTodoTaskShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateTodoTaskRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateTodoTaskRequestContentFieldList(TeaModel):
    def __init__(self, field_key=None, field_value=None):
        # fieldKey
        self.field_key = field_key  # type: str
        # fieldValue
        self.field_value = field_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskRequestContentFieldList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['fieldKey'] = self.field_key
        if self.field_value is not None:
            result['fieldValue'] = self.field_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')
        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')
        return self


class CreateTodoTaskRequestDetailUrl(TeaModel):
    def __init__(self, app_url=None, pc_url=None):
        self.app_url = app_url  # type: str
        self.pc_url = pc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskRequestDetailUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_url is not None:
            result['appUrl'] = self.app_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appUrl') is not None:
            self.app_url = m.get('appUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        return self


class CreateTodoTaskRequestNotifyConfigs(TeaModel):
    def __init__(self, ding_notify=None):
        self.ding_notify = ding_notify  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskRequestNotifyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_notify is not None:
            result['dingNotify'] = self.ding_notify
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dingNotify') is not None:
            self.ding_notify = m.get('dingNotify')
        return self


class CreateTodoTaskRequest(TeaModel):
    def __init__(self, tenant_context=None, content_field_list=None, creator_id=None, description=None,
                 detail_url=None, due_time=None, executor_ids=None, is_only_show_executor=None, notify_configs=None,
                 operator_id=None, participant_ids=None, priority=None, source_id=None, subject=None):
        self.tenant_context = tenant_context  # type: CreateTodoTaskRequestTenantContext
        self.content_field_list = content_field_list  # type: list[CreateTodoTaskRequestContentFieldList]
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.detail_url = detail_url  # type: CreateTodoTaskRequestDetailUrl
        self.due_time = due_time  # type: long
        self.executor_ids = executor_ids  # type: list[str]
        self.is_only_show_executor = is_only_show_executor  # type: bool
        self.notify_configs = notify_configs  # type: CreateTodoTaskRequestNotifyConfigs
        self.operator_id = operator_id  # type: str
        self.participant_ids = participant_ids  # type: list[str]
        self.priority = priority  # type: int
        self.source_id = source_id  # type: str
        self.subject = subject  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()
        if self.content_field_list:
            for k in self.content_field_list:
                if k:
                    k.validate()
        if self.detail_url:
            self.detail_url.validate()
        if self.notify_configs:
            self.notify_configs.validate()

    def to_map(self):
        _map = super(CreateTodoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        result['contentFieldList'] = []
        if self.content_field_list is not None:
            for k in self.content_field_list:
                result['contentFieldList'].append(k.to_map() if k else None)
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.description is not None:
            result['description'] = self.description
        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids
        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor
        if self.notify_configs is not None:
            result['notifyConfigs'] = self.notify_configs.to_map()
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids
        if self.priority is not None:
            result['priority'] = self.priority
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.subject is not None:
            result['subject'] = self.subject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = CreateTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        self.content_field_list = []
        if m.get('contentFieldList') is not None:
            for k in m.get('contentFieldList'):
                temp_model = CreateTodoTaskRequestContentFieldList()
                self.content_field_list.append(temp_model.from_map(k))
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('detailUrl') is not None:
            temp_model = CreateTodoTaskRequestDetailUrl()
            self.detail_url = temp_model.from_map(m['detailUrl'])
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')
        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')
        if m.get('notifyConfigs') is not None:
            temp_model = CreateTodoTaskRequestNotifyConfigs()
            self.notify_configs = temp_model.from_map(m['notifyConfigs'])
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        return self


class CreateTodoTaskShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, content_field_list_shrink=None, creator_id=None,
                 description=None, detail_url_shrink=None, due_time=None, executor_ids_shrink=None, is_only_show_executor=None,
                 notify_configs_shrink=None, operator_id=None, participant_ids_shrink=None, priority=None, source_id=None, subject=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.content_field_list_shrink = content_field_list_shrink  # type: str
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.detail_url_shrink = detail_url_shrink  # type: str
        self.due_time = due_time  # type: long
        self.executor_ids_shrink = executor_ids_shrink  # type: str
        self.is_only_show_executor = is_only_show_executor  # type: bool
        self.notify_configs_shrink = notify_configs_shrink  # type: str
        self.operator_id = operator_id  # type: str
        self.participant_ids_shrink = participant_ids_shrink  # type: str
        self.priority = priority  # type: int
        self.source_id = source_id  # type: str
        self.subject = subject  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.content_field_list_shrink is not None:
            result['contentFieldList'] = self.content_field_list_shrink
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.description is not None:
            result['description'] = self.description
        if self.detail_url_shrink is not None:
            result['detailUrl'] = self.detail_url_shrink
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.executor_ids_shrink is not None:
            result['executorIds'] = self.executor_ids_shrink
        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor
        if self.notify_configs_shrink is not None:
            result['notifyConfigs'] = self.notify_configs_shrink
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.participant_ids_shrink is not None:
            result['participantIds'] = self.participant_ids_shrink
        if self.priority is not None:
            result['priority'] = self.priority
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.subject is not None:
            result['subject'] = self.subject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('contentFieldList') is not None:
            self.content_field_list_shrink = m.get('contentFieldList')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('detailUrl') is not None:
            self.detail_url_shrink = m.get('detailUrl')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('executorIds') is not None:
            self.executor_ids_shrink = m.get('executorIds')
        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')
        if m.get('notifyConfigs') is not None:
            self.notify_configs_shrink = m.get('notifyConfigs')
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('participantIds') is not None:
            self.participant_ids_shrink = m.get('participantIds')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        return self


class CreateTodoTaskResponseBodyContentFieldList(TeaModel):
    def __init__(self, field_key=None, field_value=None):
        # fieldKey
        self.field_key = field_key  # type: str
        # fieldValue
        self.field_value = field_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskResponseBodyContentFieldList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['fieldKey'] = self.field_key
        if self.field_value is not None:
            result['fieldValue'] = self.field_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')
        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')
        return self


class CreateTodoTaskResponseBodyDetailUrl(TeaModel):
    def __init__(self, app_url=None, pc_url=None):
        self.app_url = app_url  # type: str
        self.pc_url = pc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskResponseBodyDetailUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_url is not None:
            result['appUrl'] = self.app_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appUrl') is not None:
            self.app_url = m.get('appUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        return self


class CreateTodoTaskResponseBodyNotifyConfigs(TeaModel):
    def __init__(self, ding_notify=None):
        self.ding_notify = ding_notify  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTodoTaskResponseBodyNotifyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_notify is not None:
            result['dingNotify'] = self.ding_notify
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dingNotify') is not None:
            self.ding_notify = m.get('dingNotify')
        return self


class CreateTodoTaskResponseBody(TeaModel):
    def __init__(self, biz_tag=None, content_field_list=None, created_time=None, creator_id=None, description=None,
                 detail_url=None, done=None, due_time=None, executor_ids=None, finish_time=None, id=None,
                 is_only_show_executor=None, modified_time=None, modifier_id=None, notify_configs=None, participant_ids=None,
                 priority=None, request_id=None, source=None, source_id=None, start_time=None, subject=None):
        self.biz_tag = biz_tag  # type: str
        self.content_field_list = content_field_list  # type: list[CreateTodoTaskResponseBodyContentFieldList]
        self.created_time = created_time  # type: long
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.detail_url = detail_url  # type: CreateTodoTaskResponseBodyDetailUrl
        self.done = done  # type: bool
        self.due_time = due_time  # type: long
        self.executor_ids = executor_ids  # type: list[str]
        self.finish_time = finish_time  # type: long
        self.id = id  # type: str
        self.is_only_show_executor = is_only_show_executor  # type: bool
        self.modified_time = modified_time  # type: long
        self.modifier_id = modifier_id  # type: str
        self.notify_configs = notify_configs  # type: CreateTodoTaskResponseBodyNotifyConfigs
        self.participant_ids = participant_ids  # type: list[str]
        self.priority = priority  # type: int
        # requestId
        self.request_id = request_id  # type: str
        self.source = source  # type: str
        self.source_id = source_id  # type: str
        self.start_time = start_time  # type: long
        self.subject = subject  # type: str

    def validate(self):
        if self.content_field_list:
            for k in self.content_field_list:
                if k:
                    k.validate()
        if self.detail_url:
            self.detail_url.validate()
        if self.notify_configs:
            self.notify_configs.validate()

    def to_map(self):
        _map = super(CreateTodoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_tag is not None:
            result['bizTag'] = self.biz_tag
        result['contentFieldList'] = []
        if self.content_field_list is not None:
            for k in self.content_field_list:
                result['contentFieldList'].append(k.to_map() if k else None)
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.description is not None:
            result['description'] = self.description
        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()
        if self.done is not None:
            result['done'] = self.done
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.id is not None:
            result['id'] = self.id
        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.modifier_id is not None:
            result['modifierId'] = self.modifier_id
        if self.notify_configs is not None:
            result['notifyConfigs'] = self.notify_configs.to_map()
        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids
        if self.priority is not None:
            result['priority'] = self.priority
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.source is not None:
            result['source'] = self.source
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.subject is not None:
            result['subject'] = self.subject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizTag') is not None:
            self.biz_tag = m.get('bizTag')
        self.content_field_list = []
        if m.get('contentFieldList') is not None:
            for k in m.get('contentFieldList'):
                temp_model = CreateTodoTaskResponseBodyContentFieldList()
                self.content_field_list.append(temp_model.from_map(k))
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('detailUrl') is not None:
            temp_model = CreateTodoTaskResponseBodyDetailUrl()
            self.detail_url = temp_model.from_map(m['detailUrl'])
        if m.get('done') is not None:
            self.done = m.get('done')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('modifierId') is not None:
            self.modifier_id = m.get('modifierId')
        if m.get('notifyConfigs') is not None:
            temp_model = CreateTodoTaskResponseBodyNotifyConfigs()
            self.notify_configs = temp_model.from_map(m['notifyConfigs'])
        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        return self


class CreateTodoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTodoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTodoTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTodoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateWorkspaceHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: CreateWorkspaceHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(CreateWorkspaceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateWorkspaceHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateWorkspaceShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateWorkspaceRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(self, description=None, name=None, tenant_context=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.tenant_context = tenant_context  # type: CreateWorkspaceRequestTenantContext

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(CreateWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            temp_model = CreateWorkspaceRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        return self


class CreateWorkspaceShrinkRequest(TeaModel):
    def __init__(self, description=None, name=None, tenant_context_shrink=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(self, description=None, name=None, request_id=None, url=None, workspace_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        # requestId
        self.request_id = request_id  # type: str
        self.url = url  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.url is not None:
            result['url'] = self.url
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWorkspaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceDocHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceDocHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateWorkspaceDocHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: CreateWorkspaceDocHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(CreateWorkspaceDocHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateWorkspaceDocHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateWorkspaceDocShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceDocShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateWorkspaceDocRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceDocRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateWorkspaceDocRequest(TeaModel):
    def __init__(self, doc_type=None, name=None, parent_node_id=None, template_id=None, template_type=None,
                 tenant_context=None, workspace_id=None):
        self.doc_type = doc_type  # type: str
        self.name = name  # type: str
        self.parent_node_id = parent_node_id  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.tenant_context = tenant_context  # type: CreateWorkspaceDocRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(CreateWorkspaceDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TenantContext') is not None:
            temp_model = CreateWorkspaceDocRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceDocShrinkRequest(TeaModel):
    def __init__(self, doc_type=None, name=None, parent_node_id=None, template_id=None, template_type=None,
                 tenant_context_shrink=None, workspace_id=None):
        self.doc_type = doc_type  # type: str
        self.name = name  # type: str
        self.parent_node_id = parent_node_id  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceDocShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceDocResponseBody(TeaModel):
    def __init__(self, doc_key=None, node_id=None, request_id=None, url=None, workspace_id=None):
        self.doc_key = doc_key  # type: str
        self.node_id = node_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        self.url = url  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_key is not None:
            result['docKey'] = self.doc_key
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.url is not None:
            result['url'] = self.url
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docKey') is not None:
            self.doc_key = m.get('docKey')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkspaceDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWorkspaceDocResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWorkspaceDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkspaceDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTodoTaskHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTodoTaskHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class DeleteTodoTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: DeleteTodoTaskHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(DeleteTodoTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = DeleteTodoTaskHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class DeleteTodoTaskShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTodoTaskShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class DeleteTodoTaskRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTodoTaskRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteTodoTaskRequest(TeaModel):
    def __init__(self, tenant_context=None, operator_id=None, task_id=None):
        self.tenant_context = tenant_context  # type: DeleteTodoTaskRequestTenantContext
        self.operator_id = operator_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(DeleteTodoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = DeleteTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteTodoTaskShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, operator_id=None, task_id=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.operator_id = operator_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTodoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteTodoTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # requestId
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTodoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteTodoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTodoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTodoTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTodoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class DeleteWorkspaceDocMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: DeleteWorkspaceDocMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = DeleteWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class DeleteWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class DeleteWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class DeleteWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteWorkspaceDocMembersRequest(TeaModel):
    def __init__(self, members=None, node_id=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[DeleteWorkspaceDocMembersRequestMembers]
        self.node_id = node_id  # type: str
        self.tenant_context = tenant_context  # type: DeleteWorkspaceDocMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DeleteWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = DeleteWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, node_id=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.node_id = node_id  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteWorkspaceDocMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWorkspaceDocMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceDocMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class DeleteWorkspaceMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: DeleteWorkspaceMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = DeleteWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class DeleteWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class DeleteWorkspaceMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class DeleteWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteWorkspaceMembersRequest(TeaModel):
    def __init__(self, members=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[DeleteWorkspaceMembersRequestMembers]
        self.tenant_context = tenant_context  # type: DeleteWorkspaceMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DeleteWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = DeleteWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteWorkspaceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWorkspaceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class GetUserHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: GetUserHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(GetUserHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = GetUserHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class GetUserShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class GetUserRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetUserRequest(TeaModel):
    def __init__(self, tenant_context=None, language=None):
        self.tenant_context = tenant_context  # type: GetUserRequestTenantContext
        self.language = language  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = GetUserRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class GetUserShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, language=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class GetUserResponseBodyDeptOrderList(TeaModel):
    def __init__(self, dept_id=None, order=None):
        self.dept_id = dept_id  # type: long
        self.order = order  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyDeptOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class GetUserResponseBodyLeaderInDept(TeaModel):
    def __init__(self, dept_id=None, leader=None):
        self.dept_id = dept_id  # type: long
        self.leader = leader  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyLeaderInDept, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.leader is not None:
            result['leader'] = self.leader
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('leader') is not None:
            self.leader = m.get('leader')
        return self


class GetUserResponseBodyRoleList(TeaModel):
    def __init__(self, group_name=None, id=None, name=None):
        self.group_name = group_name  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyRoleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetUserResponseBodyUnionEmpExtUnionEmpMapList(TeaModel):
    def __init__(self, crop_id=None, userid=None):
        self.crop_id = crop_id  # type: str
        self.userid = userid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUnionEmpExtUnionEmpMapList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop_id is not None:
            result['cropId'] = self.crop_id
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cropId') is not None:
            self.crop_id = m.get('cropId')
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class GetUserResponseBodyUnionEmpExt(TeaModel):
    def __init__(self, corp_id=None, union_emp_map_list=None, userid=None):
        self.corp_id = corp_id  # type: str
        self.union_emp_map_list = union_emp_map_list  # type: list[GetUserResponseBodyUnionEmpExtUnionEmpMapList]
        self.userid = userid  # type: str

    def validate(self):
        if self.union_emp_map_list:
            for k in self.union_emp_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserResponseBodyUnionEmpExt, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['unionEmpMapList'] = []
        if self.union_emp_map_list is not None:
            for k in self.union_emp_map_list:
                result['unionEmpMapList'].append(k.to_map() if k else None)
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.union_emp_map_list = []
        if m.get('unionEmpMapList') is not None:
            for k in m.get('unionEmpMapList'):
                temp_model = GetUserResponseBodyUnionEmpExtUnionEmpMapList()
                self.union_emp_map_list.append(temp_model.from_map(k))
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, active=None, admin=None, avatar=None, boss=None, dept_id_list=None, dept_order_list=None,
                 email=None, exclusive_account=None, exclusive_account_corp_id=None, exclusive_account_corp_name=None,
                 exclusive_account_type=None, extension=None, hide_mobile=None, hired_date=None, job_number=None, leader_in_dept=None,
                 login_id=None, manager_userid=None, mobile=None, name=None, nickname=None, org_email=None, real_authed=None,
                 remark=None, request_id=None, role_list=None, senior=None, state_code=None, telephone=None, title=None,
                 union_emp_ext=None, userid=None, work_place=None):
        self.active = active  # type: bool
        self.admin = admin  # type: bool
        self.avatar = avatar  # type: str
        self.boss = boss  # type: bool
        self.dept_id_list = dept_id_list  # type: list[long]
        self.dept_order_list = dept_order_list  # type: list[GetUserResponseBodyDeptOrderList]
        self.email = email  # type: str
        self.exclusive_account = exclusive_account  # type: bool
        self.exclusive_account_corp_id = exclusive_account_corp_id  # type: str
        self.exclusive_account_corp_name = exclusive_account_corp_name  # type: str
        self.exclusive_account_type = exclusive_account_type  # type: str
        self.extension = extension  # type: str
        self.hide_mobile = hide_mobile  # type: bool
        self.hired_date = hired_date  # type: long
        self.job_number = job_number  # type: str
        self.leader_in_dept = leader_in_dept  # type: list[GetUserResponseBodyLeaderInDept]
        self.login_id = login_id  # type: str
        self.manager_userid = manager_userid  # type: str
        self.mobile = mobile  # type: str
        self.name = name  # type: str
        self.nickname = nickname  # type: str
        self.org_email = org_email  # type: str
        self.real_authed = real_authed  # type: bool
        self.remark = remark  # type: str
        self.request_id = request_id  # type: str
        self.role_list = role_list  # type: list[GetUserResponseBodyRoleList]
        self.senior = senior  # type: bool
        self.state_code = state_code  # type: str
        self.telephone = telephone  # type: str
        self.title = title  # type: str
        self.union_emp_ext = union_emp_ext  # type: GetUserResponseBodyUnionEmpExt
        self.userid = userid  # type: str
        self.work_place = work_place  # type: str

    def validate(self):
        if self.dept_order_list:
            for k in self.dept_order_list:
                if k:
                    k.validate()
        if self.leader_in_dept:
            for k in self.leader_in_dept:
                if k:
                    k.validate()
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()
        if self.union_emp_ext:
            self.union_emp_ext.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.admin is not None:
            result['admin'] = self.admin
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.boss is not None:
            result['boss'] = self.boss
        if self.dept_id_list is not None:
            result['deptIdList'] = self.dept_id_list
        result['deptOrderList'] = []
        if self.dept_order_list is not None:
            for k in self.dept_order_list:
                result['deptOrderList'].append(k.to_map() if k else None)
        if self.email is not None:
            result['email'] = self.email
        if self.exclusive_account is not None:
            result['exclusiveAccount'] = self.exclusive_account
        if self.exclusive_account_corp_id is not None:
            result['exclusiveAccountCorpId'] = self.exclusive_account_corp_id
        if self.exclusive_account_corp_name is not None:
            result['exclusiveAccountCorpName'] = self.exclusive_account_corp_name
        if self.exclusive_account_type is not None:
            result['exclusiveAccountType'] = self.exclusive_account_type
        if self.extension is not None:
            result['extension'] = self.extension
        if self.hide_mobile is not None:
            result['hideMobile'] = self.hide_mobile
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.job_number is not None:
            result['jobNumber'] = self.job_number
        result['leaderInDept'] = []
        if self.leader_in_dept is not None:
            for k in self.leader_in_dept:
                result['leaderInDept'].append(k.to_map() if k else None)
        if self.login_id is not None:
            result['loginId'] = self.login_id
        if self.manager_userid is not None:
            result['managerUserid'] = self.manager_userid
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.org_email is not None:
            result['orgEmail'] = self.org_email
        if self.real_authed is not None:
            result['realAuthed'] = self.real_authed
        if self.remark is not None:
            result['remark'] = self.remark
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['roleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['roleList'].append(k.to_map() if k else None)
        if self.senior is not None:
            result['senior'] = self.senior
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.telephone is not None:
            result['telephone'] = self.telephone
        if self.title is not None:
            result['title'] = self.title
        if self.union_emp_ext is not None:
            result['unionEmpExt'] = self.union_emp_ext.to_map()
        if self.userid is not None:
            result['userid'] = self.userid
        if self.work_place is not None:
            result['workPlace'] = self.work_place
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('admin') is not None:
            self.admin = m.get('admin')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('boss') is not None:
            self.boss = m.get('boss')
        if m.get('deptIdList') is not None:
            self.dept_id_list = m.get('deptIdList')
        self.dept_order_list = []
        if m.get('deptOrderList') is not None:
            for k in m.get('deptOrderList'):
                temp_model = GetUserResponseBodyDeptOrderList()
                self.dept_order_list.append(temp_model.from_map(k))
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('exclusiveAccount') is not None:
            self.exclusive_account = m.get('exclusiveAccount')
        if m.get('exclusiveAccountCorpId') is not None:
            self.exclusive_account_corp_id = m.get('exclusiveAccountCorpId')
        if m.get('exclusiveAccountCorpName') is not None:
            self.exclusive_account_corp_name = m.get('exclusiveAccountCorpName')
        if m.get('exclusiveAccountType') is not None:
            self.exclusive_account_type = m.get('exclusiveAccountType')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('hideMobile') is not None:
            self.hide_mobile = m.get('hideMobile')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')
        self.leader_in_dept = []
        if m.get('leaderInDept') is not None:
            for k in m.get('leaderInDept'):
                temp_model = GetUserResponseBodyLeaderInDept()
                self.leader_in_dept.append(temp_model.from_map(k))
        if m.get('loginId') is not None:
            self.login_id = m.get('loginId')
        if m.get('managerUserid') is not None:
            self.manager_userid = m.get('managerUserid')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('orgEmail') is not None:
            self.org_email = m.get('orgEmail')
        if m.get('realAuthed') is not None:
            self.real_authed = m.get('realAuthed')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.role_list = []
        if m.get('roleList') is not None:
            for k in m.get('roleList'):
                temp_model = GetUserResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('senior') is not None:
            self.senior = m.get('senior')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('unionEmpExt') is not None:
            temp_model = GetUserResponseBodyUnionEmpExt()
            self.union_emp_ext = temp_model.from_map(m['unionEmpExt'])
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        if m.get('workPlace') is not None:
            self.work_place = m.get('workPlace')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRowsBeforeHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class InsertRowsBeforeHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: InsertRowsBeforeHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = InsertRowsBeforeHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class InsertRowsBeforeShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class InsertRowsBeforeRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class InsertRowsBeforeRequest(TeaModel):
    def __init__(self, row=None, row_count=None, sheet_id=None, tenant_context=None, workbook_id=None):
        self.row = row  # type: long
        self.row_count = row_count  # type: long
        self.sheet_id = sheet_id  # type: str
        self.tenant_context = tenant_context  # type: InsertRowsBeforeRequestTenantContext
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            temp_model = InsertRowsBeforeRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeShrinkRequest(TeaModel):
    def __init__(self, row=None, row_count=None, sheet_id=None, tenant_context_shrink=None, workbook_id=None):
        self.row = row  # type: long
        self.row_count = row_count  # type: long
        self.sheet_id = sheet_id  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class InsertRowsBeforeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertRowsBeforeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InsertRowsBeforeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrgTodoTasksHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrgTodoTasksHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class QueryOrgTodoTasksHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: QueryOrgTodoTasksHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(QueryOrgTodoTasksHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = QueryOrgTodoTasksHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class QueryOrgTodoTasksShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrgTodoTasksShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class QueryOrgTodoTasksRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrgTodoTasksRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class QueryOrgTodoTasksRequest(TeaModel):
    def __init__(self, tenant_context=None, is_done=None, next_token=None):
        self.tenant_context = tenant_context  # type: QueryOrgTodoTasksRequestTenantContext
        self.is_done = is_done  # type: bool
        self.next_token = next_token  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(QueryOrgTodoTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.is_done is not None:
            result['isDone'] = self.is_done
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = QueryOrgTodoTasksRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryOrgTodoTasksShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, is_done=None, next_token=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.is_done = is_done  # type: bool
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrgTodoTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.is_done is not None:
            result['isDone'] = self.is_done
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl(TeaModel):
    def __init__(self, app_url=None, pc_url=None):
        self.app_url = app_url  # type: str
        self.pc_url = pc_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_url is not None:
            result['appUrl'] = self.app_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appUrl') is not None:
            self.app_url = m.get('appUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        return self


class QueryOrgTodoTasksResponseBodyTodoCards(TeaModel):
    def __init__(self, biz_tag=None, created_time=None, creator_id=None, detail_url=None, due_time=None,
                 is_done=None, modified_time=None, priority=None, source_id=None, subject=None, task_id=None):
        self.biz_tag = biz_tag  # type: str
        self.created_time = created_time  # type: long
        self.creator_id = creator_id  # type: str
        self.detail_url = detail_url  # type: QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl
        self.due_time = due_time  # type: long
        self.is_done = is_done  # type: bool
        self.modified_time = modified_time  # type: long
        self.priority = priority  # type: int
        self.source_id = source_id  # type: str
        self.subject = subject  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.detail_url:
            self.detail_url.validate()

    def to_map(self):
        _map = super(QueryOrgTodoTasksResponseBodyTodoCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_tag is not None:
            result['bizTag'] = self.biz_tag
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.is_done is not None:
            result['isDone'] = self.is_done
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.priority is not None:
            result['priority'] = self.priority
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.subject is not None:
            result['subject'] = self.subject
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizTag') is not None:
            self.biz_tag = m.get('bizTag')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('detailUrl') is not None:
            temp_model = QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl()
            self.detail_url = temp_model.from_map(m['detailUrl'])
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class QueryOrgTodoTasksResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, todo_cards=None):
        self.next_token = next_token  # type: str
        # requestId
        self.request_id = request_id  # type: str
        self.todo_cards = todo_cards  # type: list[QueryOrgTodoTasksResponseBodyTodoCards]

    def validate(self):
        if self.todo_cards:
            for k in self.todo_cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrgTodoTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['todoCards'] = []
        if self.todo_cards is not None:
            for k in self.todo_cards:
                result['todoCards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.todo_cards = []
        if m.get('todoCards') is not None:
            for k in m.get('todoCards'):
                temp_model = QueryOrgTodoTasksResponseBodyTodoCards()
                self.todo_cards.append(temp_model.from_map(k))
        return self


class QueryOrgTodoTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOrgTodoTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrgTodoTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOrgTodoTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTodoTaskHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateTodoTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: UpdateTodoTaskHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateTodoTaskHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateTodoTaskShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateTodoTaskRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateTodoTaskRequest(TeaModel):
    def __init__(self, tenant_context=None, description=None, done=None, due_time=None, executor_ids=None,
                 participant_ids=None, subject=None, task_id=None):
        self.tenant_context = tenant_context  # type: UpdateTodoTaskRequestTenantContext
        self.description = description  # type: str
        self.done = done  # type: bool
        self.due_time = due_time  # type: long
        self.executor_ids = executor_ids  # type: list[str]
        self.participant_ids = participant_ids  # type: list[str]
        self.subject = subject  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.done is not None:
            result['done'] = self.done
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids
        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids
        if self.subject is not None:
            result['subject'] = self.subject
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = UpdateTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('done') is not None:
            self.done = m.get('done')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')
        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateTodoTaskShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, description=None, done=None, due_time=None,
                 executor_ids_shrink=None, participant_ids_shrink=None, subject=None, task_id=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.description = description  # type: str
        self.done = done  # type: bool
        self.due_time = due_time  # type: long
        self.executor_ids_shrink = executor_ids_shrink  # type: str
        self.participant_ids_shrink = participant_ids_shrink  # type: str
        self.subject = subject  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.description is not None:
            result['description'] = self.description
        if self.done is not None:
            result['done'] = self.done
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.executor_ids_shrink is not None:
            result['executorIds'] = self.executor_ids_shrink
        if self.participant_ids_shrink is not None:
            result['participantIds'] = self.participant_ids_shrink
        if self.subject is not None:
            result['subject'] = self.subject
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('done') is not None:
            self.done = m.get('done')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('executorIds') is not None:
            self.executor_ids_shrink = m.get('executorIds')
        if m.get('participantIds') is not None:
            self.participant_ids_shrink = m.get('participantIds')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateTodoTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # requestId
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateTodoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTodoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTodoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTodoTaskExecutorStatusHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateTodoTaskExecutorStatusHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: UpdateTodoTaskExecutorStatusHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateTodoTaskExecutorStatusHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateTodoTaskExecutorStatusShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateTodoTaskExecutorStatusRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateTodoTaskExecutorStatusRequestExecutorStatusList(TeaModel):
    def __init__(self, id=None, is_done=None):
        self.id = id  # type: str
        self.is_done = is_done  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusRequestExecutorStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.is_done is not None:
            result['isDone'] = self.is_done
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')
        return self


class UpdateTodoTaskExecutorStatusRequest(TeaModel):
    def __init__(self, tenant_context=None, executor_status_list=None, operator_id=None, task_id=None):
        self.tenant_context = tenant_context  # type: UpdateTodoTaskExecutorStatusRequestTenantContext
        self.executor_status_list = executor_status_list  # type: list[UpdateTodoTaskExecutorStatusRequestExecutorStatusList]
        self.operator_id = operator_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()
        if self.executor_status_list:
            for k in self.executor_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        result['executorStatusList'] = []
        if self.executor_status_list is not None:
            for k in self.executor_status_list:
                result['executorStatusList'].append(k.to_map() if k else None)
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = UpdateTodoTaskExecutorStatusRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        self.executor_status_list = []
        if m.get('executorStatusList') is not None:
            for k in m.get('executorStatusList'):
                temp_model = UpdateTodoTaskExecutorStatusRequestExecutorStatusList()
                self.executor_status_list.append(temp_model.from_map(k))
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateTodoTaskExecutorStatusShrinkRequest(TeaModel):
    def __init__(self, tenant_context_shrink=None, executor_status_list_shrink=None, operator_id=None,
                 task_id=None):
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.executor_status_list_shrink = executor_status_list_shrink  # type: str
        self.operator_id = operator_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.executor_status_list_shrink is not None:
            result['executorStatusList'] = self.executor_status_list_shrink
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('executorStatusList') is not None:
            self.executor_status_list_shrink = m.get('executorStatusList')
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateTodoTaskExecutorStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # requestId
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateTodoTaskExecutorStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTodoTaskExecutorStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTodoTaskExecutorStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTodoTaskExecutorStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateWorkspaceDocMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: UpdateWorkspaceDocMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None, role_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class UpdateWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateWorkspaceDocMembersRequest(TeaModel):
    def __init__(self, members=None, node_id=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[UpdateWorkspaceDocMembersRequestMembers]
        self.node_id = node_id  # type: str
        self.tenant_context = tenant_context  # type: UpdateWorkspaceDocMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = UpdateWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, node_id=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.node_id = node_id  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateWorkspaceDocMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWorkspaceDocMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceDocMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateWorkspaceMembersHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: UpdateWorkspaceMembersHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceMembersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateWorkspaceMembersRequestMembers(TeaModel):
    def __init__(self, member_id=None, member_type=None, role_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class UpdateWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateWorkspaceMembersRequest(TeaModel):
    def __init__(self, members=None, tenant_context=None, workspace_id=None):
        self.members = members  # type: list[UpdateWorkspaceMembersRequestMembers]
        self.tenant_context = tenant_context  # type: UpdateWorkspaceMembersRequestTenantContext
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = UpdateWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(self, members_shrink=None, tenant_context_shrink=None, workspace_id=None):
        self.members_shrink = members_shrink  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateWorkspaceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWorkspaceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


