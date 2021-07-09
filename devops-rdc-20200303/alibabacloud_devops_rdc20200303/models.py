# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class InsertPipelineMemberRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, user_id=None, role_name=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.user_id = user_id  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertPipelineMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class InsertPipelineMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: bool
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertPipelineMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertPipelineMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertPipelineMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertPipelineMemberResponse, self).to_map()
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
            temp_model = InsertPipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskFlowRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsProjectTaskFlowResponseBodyObject(TeaModel):
    def __init__(self, type=None, name=None, id=None):
        self.type = type  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskFlowResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListDevopsProjectTaskFlowResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTaskFlowResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListDevopsProjectTaskFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectTaskFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowResponse, self).to_map()
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
            temp_model = ListDevopsProjectTaskFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectMembersRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, page_size=None, page_token=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.page_size = page_size  # type: int
        self.page_token = page_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        return self


class GetDevopsProjectMembersResponseBodyObject(TeaModel):
    def __init__(self, email=None, avatar_url=None, user_id=None, member_id=None, role=None, name=None, phone=None):
        self.email = email  # type: str
        self.avatar_url = avatar_url  # type: str
        self.user_id = user_id  # type: str
        self.member_id = member_id  # type: str
        self.role = role  # type: int
        self.name = name  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectMembersResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetDevopsProjectMembersResponseBody(TeaModel):
    def __init__(self, request_id=None, next_page_token=None, error_code=None, error_msg=None, successful=None,
                 total=None, object=None):
        self.request_id = request_id  # type: str
        self.next_page_token = next_page_token  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.successful = successful  # type: bool
        self.total = total  # type: int
        self.object = object  # type: list[GetDevopsProjectMembersResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDevopsProjectMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.total is not None:
            result['Total'] = self.total
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetDevopsProjectMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class GetDevopsProjectMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDevopsProjectMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDevopsProjectMembersResponse, self).to_map()
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
            temp_model = GetDevopsProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCodeupSourceToPipelineRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, code_path=None, code_branch=None):
        self.org_id = org_id  # type: str
        # 流水线ID
        self.pipeline_id = pipeline_id  # type: long
        # Codeup的代码库路径，比如 group1/repo1
        self.code_path = code_path  # type: str
        # 代码库分支
        self.code_branch = code_branch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCodeupSourceToPipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.code_path is not None:
            result['CodePath'] = self.code_path
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('CodePath') is not None:
            self.code_path = m.get('CodePath')
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        return self


class AddCodeupSourceToPipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, pipeline_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 流水线ID
        self.pipeline_id = pipeline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCodeupSourceToPipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class AddCodeupSourceToPipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddCodeupSourceToPipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCodeupSourceToPipelineResponse, self).to_map()
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
            temp_model = AddCodeupSourceToPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectSprintRequest(TeaModel):
    def __init__(self, org_id=None, sprint_id=None):
        self.org_id = org_id  # type: str
        self.sprint_id = sprint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectSprintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class DeleteDevopsProjectSprintResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectSprintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsProjectSprintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsProjectSprintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsProjectSprintResponse, self).to_map()
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
            temp_model = DeleteDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommonGroupRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, common_group_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.common_group_id = common_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommonGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.common_group_id is not None:
            result['CommonGroupId'] = self.common_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CommonGroupId') is not None:
            self.common_group_id = m.get('CommonGroupId')
        return self


class DeleteCommonGroupResponseBodyObject(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCommonGroupResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteCommonGroupResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: DeleteCommonGroupResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(DeleteCommonGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = DeleteCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class DeleteCommonGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCommonGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCommonGroupResponse, self).to_map()
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
            temp_model = DeleteCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectCustomFieldsRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectCustomFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListProjectCustomFieldsResponseBodyObjectValues(TeaModel):
    def __init__(self, value=None, id=None):
        self.value = value  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectCustomFieldsResponseBodyObjectValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListProjectCustomFieldsResponseBodyObject(TeaModel):
    def __init__(self, type=None, custom_field_id=None, subtype=None, name=None, values=None):
        self.type = type  # type: str
        self.custom_field_id = custom_field_id  # type: str
        self.subtype = subtype  # type: str
        self.name = name  # type: str
        self.values = values  # type: list[ListProjectCustomFieldsResponseBodyObjectValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectCustomFieldsResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.custom_field_id is not None:
            result['CustomFieldId'] = self.custom_field_id
        if self.subtype is not None:
            result['Subtype'] = self.subtype
        if self.name is not None:
            result['Name'] = self.name
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CustomFieldId') is not None:
            self.custom_field_id = m.get('CustomFieldId')
        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListProjectCustomFieldsResponseBodyObjectValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListProjectCustomFieldsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListProjectCustomFieldsResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectCustomFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListProjectCustomFieldsResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListProjectCustomFieldsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectCustomFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectCustomFieldsResponse, self).to_map()
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
            temp_model = ListProjectCustomFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertDevopsUserRequest(TeaModel):
    def __init__(self, user_pk=None, user_name=None, phone=None, email=None):
        self.user_pk = user_pk  # type: str
        self.user_name = user_name  # type: str
        self.phone = phone  # type: str
        self.email = email  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertDevopsUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class InsertDevopsUserResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, success=None, error_code=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertDevopsUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class InsertDevopsUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertDevopsUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertDevopsUserResponse, self).to_map()
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
            temp_model = InsertDevopsUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectRequest(TeaModel):
    def __init__(self, org_id=None, name=None, description=None, project_id=None):
        self.org_id = org_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateDevopsProjectResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateDevopsProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDevopsProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDevopsProjectResponse, self).to_map()
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
            temp_model = UpdateDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAliyunAccountExistsRequest(TeaModel):
    def __init__(self, user_pk=None):
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAliyunAccountExistsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CheckAliyunAccountExistsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAliyunAccountExistsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CheckAliyunAccountExistsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckAliyunAccountExistsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAliyunAccountExistsResponse, self).to_map()
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
            temp_model = CheckAliyunAccountExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceInfoRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, flow_instance_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.flow_instance_id = flow_instance_id  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipelineInstanceInfoResponseBodyObject(TeaModel):
    def __init__(self, employee_id=None, end_time=None, status=None, start_time=None, sources=None,
                 docker_images=None, package_download_urls=None):
        self.employee_id = employee_id  # type: str
        self.end_time = end_time  # type: long
        self.status = status  # type: str
        self.start_time = start_time  # type: long
        self.sources = sources  # type: str
        self.docker_images = docker_images  # type: list[str]
        self.package_download_urls = package_download_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceInfoResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.employee_id is not None:
            result['EmployeeId'] = self.employee_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.docker_images is not None:
            result['DockerImages'] = self.docker_images
        if self.package_download_urls is not None:
            result['PackageDownloadUrls'] = self.package_download_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmployeeId') is not None:
            self.employee_id = m.get('EmployeeId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('DockerImages') is not None:
            self.docker_images = m.get('DockerImages')
        if m.get('PackageDownloadUrls') is not None:
            self.package_download_urls = m.get('PackageDownloadUrls')
        return self


class GetPipelineInstanceInfoResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, success=None, error_code=None, object=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetPipelineInstanceInfoResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetPipelineInstanceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineInstanceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceInfoResponse, self).to_map()
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
            temp_model = GetPipelineInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchInsertMembersRequest(TeaModel):
    def __init__(self, org_id=None, members=None, real_pk=None):
        self.org_id = org_id  # type: str
        self.members = members  # type: str
        self.real_pk = real_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchInsertMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.members is not None:
            result['Members'] = self.members
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class BatchInsertMembersResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchInsertMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class BatchInsertMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchInsertMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchInsertMembersResponse, self).to_map()
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
            temp_model = BatchInsertMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceConnectionsRequest(TeaModel):
    def __init__(self, org_id=None, sc_type=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.sc_type = sc_type  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sc_type is not None:
            result['ScType'] = self.sc_type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ScType') is not None:
            self.sc_type = m.get('ScType')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListServiceConnectionsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceConnectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class ListServiceConnectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceConnectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceConnectionsResponse, self).to_map()
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
            temp_model = ListServiceConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserNameRequest(TeaModel):
    def __init__(self, org_id=None, user_id=None):
        self.org_id = org_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserNameResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class GetUserNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserNameResponse, self).to_map()
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
            temp_model = GetUserNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertProjectMembersRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, members=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.members = members  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertProjectMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class InsertProjectMembersResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertProjectMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class InsertProjectMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertProjectMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertProjectMembersResponse, self).to_map()
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
            temp_model = InsertProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskListRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsProjectTaskListResponseBodyObjectResult(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskListResponseBodyObjectResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskListResponseBodyObject(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: list[ListDevopsProjectTaskListResponseBodyObjectResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskListResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDevopsProjectTaskListResponseBodyObjectResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDevopsProjectTaskListResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: ListDevopsProjectTaskListResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = ListDevopsProjectTaskListResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class ListDevopsProjectTaskListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskListResponse, self).to_map()
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
            temp_model = ListDevopsProjectTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskDetailBaseRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, task_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskDetailBaseResponseBodyObjectCustomfieldsValue(TeaModel):
    def __init__(self, id=None, title=None):
        self.id = id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectCustomfieldsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTaskDetailBaseResponseBodyObjectCustomfields(TeaModel):
    def __init__(self, type=None, customfield_id=None, value=None, values=None):
        self.type = type  # type: str
        self.customfield_id = customfield_id  # type: str
        self.value = value  # type: list[GetTaskDetailBaseResponseBodyObjectCustomfieldsValue]
        self.values = values  # type: list[str]

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectCustomfields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.customfield_id is not None:
            result['CustomfieldId'] = self.customfield_id
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CustomfieldId') is not None:
            self.customfield_id = m.get('CustomfieldId')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = GetTaskDetailBaseResponseBodyObjectCustomfieldsValue()
                self.value.append(temp_model.from_map(k))
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetTaskDetailBaseResponseBodyObjectSubtasks(TeaModel):
    def __init__(self, content=None, id=None):
        self.content = content  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectSubtasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectInvolvers(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectInvolvers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectScenariofieldconfig(TeaModel):
    def __init__(self, icon=None, pro_template_config_type=None, name=None, id=None):
        self.icon = icon  # type: str
        self.pro_template_config_type = pro_template_config_type  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectScenariofieldconfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.pro_template_config_type is not None:
            result['ProTemplateConfigType'] = self.pro_template_config_type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('ProTemplateConfigType') is not None:
            self.pro_template_config_type = m.get('ProTemplateConfigType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectExecutor(TeaModel):
    def __init__(self, avatar_url=None, name=None, id=None):
        self.avatar_url = avatar_url  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectExecutor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectTasklist(TeaModel):
    def __init__(self, id=None, title=None):
        self.id = id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectTasklist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTaskDetailBaseResponseBodyObjectTaskflowstatus(TeaModel):
    def __init__(self, taskflow_id=None, name=None, id=None, kind=None):
        self.taskflow_id = taskflow_id  # type: str
        self.name = name  # type: str
        self.id = id  # type: str
        self.kind = kind  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectTaskflowstatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.taskflow_id is not None:
            result['TaskflowId'] = self.taskflow_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskflowId') is not None:
            self.taskflow_id = m.get('TaskflowId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class GetTaskDetailBaseResponseBodyObjectCreator(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectCreator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectReminder(TeaModel):
    def __init__(self, type=None, date=None, method=None, creator_id=None, member_roles=None, members=None,
                 rules=None):
        self.type = type  # type: str
        self.date = date  # type: str
        self.method = method  # type: str
        self.creator_id = creator_id  # type: str
        self.member_roles = member_roles  # type: list[str]
        self.members = members  # type: list[str]
        self.rules = rules  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectReminder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.date is not None:
            result['Date'] = self.date
        if self.method is not None:
            result['Method'] = self.method
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.member_roles is not None:
            result['MemberRoles'] = self.member_roles
        if self.members is not None:
            result['Members'] = self.members
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('MemberRoles') is not None:
            self.member_roles = m.get('MemberRoles')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class GetTaskDetailBaseResponseBodyObjectSubtaskCount(TeaModel):
    def __init__(self, done=None, total=None):
        self.done = done  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectSubtaskCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTaskDetailBaseResponseBodyObjectWorkTime(TeaModel):
    def __init__(self, used_time=None, total_time=None, unit=None):
        self.used_time = used_time  # type: int
        self.total_time = total_time  # type: int
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectWorkTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetTaskDetailBaseResponseBodyObjectBadges(TeaModel):
    def __init__(self, likes_count=None, objectlinks_count=None, attachments_count=None, comments_count=None):
        self.likes_count = likes_count  # type: int
        self.objectlinks_count = objectlinks_count  # type: int
        self.attachments_count = attachments_count  # type: int
        self.comments_count = comments_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectBadges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        return self


class GetTaskDetailBaseResponseBodyObjectStage(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObjectStage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObject(TeaModel):
    def __init__(self, is_favorite=None, organization=None, executor_id=None, scenariofieldconfig_id=None,
                 project_id=None, is_top_in_project=None, priority=None, share_status=None, accomplished=None,
                 taskflowstatus_id=None, note=None, updated=None, unique_id=None, is_archived=None, content=None, comments_count=None,
                 rating=None, recurrence=None, object_type=None, progress=None, until_date=None, start_date=None,
                 story_point=None, objectlinks_count=None, sprint=None, creator_id=None, source=None, source_id=None,
                 organization_id=None, source_date=None, likes_count=None, stage_id=None, visible=None, is_done=None, parent=None,
                 sprint_id=None, attachments_count=None, due_date=None, created=None, task_id=None, id=None, customfields=None,
                 subtasks=None, involvers=None, labels=None, divisions=None, ancestors=None, involve_members=None,
                 tag_ids=None, ancestor_ids=None, scenariofieldconfig=None, executor=None, tasklist=None,
                 taskflowstatus=None, creator=None, reminder=None, subtask_count=None, work_time=None, badges=None, stage=None):
        self.is_favorite = is_favorite  # type: bool
        self.organization = organization  # type: str
        self.executor_id = executor_id  # type: str
        self.scenariofieldconfig_id = scenariofieldconfig_id  # type: str
        self.project_id = project_id  # type: str
        self.is_top_in_project = is_top_in_project  # type: bool
        self.priority = priority  # type: int
        self.share_status = share_status  # type: int
        self.accomplished = accomplished  # type: str
        self.taskflowstatus_id = taskflowstatus_id  # type: str
        self.note = note  # type: str
        self.updated = updated  # type: str
        self.unique_id = unique_id  # type: int
        self.is_archived = is_archived  # type: bool
        self.content = content  # type: str
        self.comments_count = comments_count  # type: int
        self.rating = rating  # type: int
        self.recurrence = recurrence  # type: str
        self.object_type = object_type  # type: str
        self.progress = progress  # type: int
        self.until_date = until_date  # type: str
        self.start_date = start_date  # type: str
        self.story_point = story_point  # type: str
        self.objectlinks_count = objectlinks_count  # type: int
        self.sprint = sprint  # type: str
        self.creator_id = creator_id  # type: str
        self.source = source  # type: str
        self.source_id = source_id  # type: str
        self.organization_id = organization_id  # type: str
        self.source_date = source_date  # type: str
        self.likes_count = likes_count  # type: int
        self.stage_id = stage_id  # type: str
        self.visible = visible  # type: str
        self.is_done = is_done  # type: bool
        self.parent = parent  # type: str
        self.sprint_id = sprint_id  # type: str
        self.attachments_count = attachments_count  # type: int
        self.due_date = due_date  # type: str
        self.created = created  # type: str
        self.task_id = task_id  # type: str
        self.id = id  # type: str
        self.customfields = customfields  # type: list[GetTaskDetailBaseResponseBodyObjectCustomfields]
        self.subtasks = subtasks  # type: list[GetTaskDetailBaseResponseBodyObjectSubtasks]
        self.involvers = involvers  # type: list[GetTaskDetailBaseResponseBodyObjectInvolvers]
        self.labels = labels  # type: list[str]
        self.divisions = divisions  # type: list[str]
        self.ancestors = ancestors  # type: list[str]
        self.involve_members = involve_members  # type: list[str]
        self.tag_ids = tag_ids  # type: list[str]
        self.ancestor_ids = ancestor_ids  # type: list[str]
        self.scenariofieldconfig = scenariofieldconfig  # type: GetTaskDetailBaseResponseBodyObjectScenariofieldconfig
        self.executor = executor  # type: GetTaskDetailBaseResponseBodyObjectExecutor
        self.tasklist = tasklist  # type: GetTaskDetailBaseResponseBodyObjectTasklist
        self.taskflowstatus = taskflowstatus  # type: GetTaskDetailBaseResponseBodyObjectTaskflowstatus
        self.creator = creator  # type: GetTaskDetailBaseResponseBodyObjectCreator
        self.reminder = reminder  # type: GetTaskDetailBaseResponseBodyObjectReminder
        self.subtask_count = subtask_count  # type: GetTaskDetailBaseResponseBodyObjectSubtaskCount
        self.work_time = work_time  # type: GetTaskDetailBaseResponseBodyObjectWorkTime
        self.badges = badges  # type: GetTaskDetailBaseResponseBodyObjectBadges
        self.stage = stage  # type: GetTaskDetailBaseResponseBodyObjectStage

    def validate(self):
        if self.customfields:
            for k in self.customfields:
                if k:
                    k.validate()
        if self.subtasks:
            for k in self.subtasks:
                if k:
                    k.validate()
        if self.involvers:
            for k in self.involvers:
                if k:
                    k.validate()
        if self.scenariofieldconfig:
            self.scenariofieldconfig.validate()
        if self.executor:
            self.executor.validate()
        if self.tasklist:
            self.tasklist.validate()
        if self.taskflowstatus:
            self.taskflowstatus.validate()
        if self.creator:
            self.creator.validate()
        if self.reminder:
            self.reminder.validate()
        if self.subtask_count:
            self.subtask_count.validate()
        if self.work_time:
            self.work_time.validate()
        if self.badges:
            self.badges.validate()
        if self.stage:
            self.stage.validate()

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.scenariofieldconfig_id is not None:
            result['ScenariofieldconfigId'] = self.scenariofieldconfig_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.share_status is not None:
            result['ShareStatus'] = self.share_status
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.note is not None:
            result['Note'] = self.note
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.content is not None:
            result['Content'] = self.content
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.until_date is not None:
            result['UntilDate'] = self.until_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.sprint is not None:
            result['Sprint'] = self.sprint
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.source_date is not None:
            result['SourceDate'] = self.source_date
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.parent is not None:
            result['Parent'] = self.parent
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.id is not None:
            result['Id'] = self.id
        result['Customfields'] = []
        if self.customfields is not None:
            for k in self.customfields:
                result['Customfields'].append(k.to_map() if k else None)
        result['Subtasks'] = []
        if self.subtasks is not None:
            for k in self.subtasks:
                result['Subtasks'].append(k.to_map() if k else None)
        result['Involvers'] = []
        if self.involvers is not None:
            for k in self.involvers:
                result['Involvers'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.divisions is not None:
            result['Divisions'] = self.divisions
        if self.ancestors is not None:
            result['Ancestors'] = self.ancestors
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.scenariofieldconfig is not None:
            result['Scenariofieldconfig'] = self.scenariofieldconfig.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.tasklist is not None:
            result['Tasklist'] = self.tasklist.to_map()
        if self.taskflowstatus is not None:
            result['Taskflowstatus'] = self.taskflowstatus.to_map()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.reminder is not None:
            result['Reminder'] = self.reminder.to_map()
        if self.subtask_count is not None:
            result['SubtaskCount'] = self.subtask_count.to_map()
        if self.work_time is not None:
            result['WorkTime'] = self.work_time.to_map()
        if self.badges is not None:
            result['Badges'] = self.badges.to_map()
        if self.stage is not None:
            result['Stage'] = self.stage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ScenariofieldconfigId') is not None:
            self.scenariofieldconfig_id = m.get('ScenariofieldconfigId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ShareStatus') is not None:
            self.share_status = m.get('ShareStatus')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('UntilDate') is not None:
            self.until_date = m.get('UntilDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('Sprint') is not None:
            self.sprint = m.get('Sprint')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SourceDate') is not None:
            self.source_date = m.get('SourceDate')
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('Parent') is not None:
            self.parent = m.get('Parent')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.customfields = []
        if m.get('Customfields') is not None:
            for k in m.get('Customfields'):
                temp_model = GetTaskDetailBaseResponseBodyObjectCustomfields()
                self.customfields.append(temp_model.from_map(k))
        self.subtasks = []
        if m.get('Subtasks') is not None:
            for k in m.get('Subtasks'):
                temp_model = GetTaskDetailBaseResponseBodyObjectSubtasks()
                self.subtasks.append(temp_model.from_map(k))
        self.involvers = []
        if m.get('Involvers') is not None:
            for k in m.get('Involvers'):
                temp_model = GetTaskDetailBaseResponseBodyObjectInvolvers()
                self.involvers.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Divisions') is not None:
            self.divisions = m.get('Divisions')
        if m.get('Ancestors') is not None:
            self.ancestors = m.get('Ancestors')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('Scenariofieldconfig') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectScenariofieldconfig()
            self.scenariofieldconfig = temp_model.from_map(m['Scenariofieldconfig'])
        if m.get('Executor') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('Tasklist') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectTasklist()
            self.tasklist = temp_model.from_map(m['Tasklist'])
        if m.get('Taskflowstatus') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectTaskflowstatus()
            self.taskflowstatus = temp_model.from_map(m['Taskflowstatus'])
        if m.get('Creator') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Reminder') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectReminder()
            self.reminder = temp_model.from_map(m['Reminder'])
        if m.get('SubtaskCount') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectSubtaskCount()
            self.subtask_count = temp_model.from_map(m['SubtaskCount'])
        if m.get('WorkTime') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectWorkTime()
            self.work_time = temp_model.from_map(m['WorkTime'])
        if m.get('Badges') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectBadges()
            self.badges = temp_model.from_map(m['Badges'])
        if m.get('Stage') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectStage()
            self.stage = temp_model.from_map(m['Stage'])
        return self


class GetTaskDetailBaseResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetTaskDetailBaseResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetTaskDetailBaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetTaskDetailBaseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskDetailBaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskDetailBaseResponse, self).to_map()
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
            temp_model = GetTaskDetailBaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectMembersRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, user_ids=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class DeleteDevopsProjectMembersResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsProjectMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsProjectMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsProjectMembersResponse, self).to_map()
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
            temp_model = DeleteDevopsProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectSprintRequest(TeaModel):
    def __init__(self, org_id=None, name=None, description=None, project_id=None, executor_id=None, start_date=None,
                 due_date=None):
        self.org_id = org_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.project_id = project_id  # type: str
        self.executor_id = executor_id  # type: str
        self.start_date = start_date  # type: str
        self.due_date = due_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectSprintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        return self


class CreateDevopsProjectSprintResponseBodyObjectPlanToDo(TeaModel):
    def __init__(self, tasks=None, work_times=None, story_points=None):
        self.tasks = tasks  # type: int
        self.work_times = work_times  # type: int
        self.story_points = story_points  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectSprintResponseBodyObjectPlanToDo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class CreateDevopsProjectSprintResponseBodyObject(TeaModel):
    def __init__(self, status=None, project_id=None, start_date=None, creator_id=None, executor=None,
                 description=None, accomplished=None, is_deleted=None, updated=None, due_date=None, created=None, name=None,
                 id=None, plan_to_do=None):
        self.status = status  # type: str
        self.project_id = project_id  # type: str
        self.start_date = start_date  # type: str
        self.creator_id = creator_id  # type: str
        self.executor = executor  # type: str
        self.description = description  # type: str
        self.accomplished = accomplished  # type: str
        self.is_deleted = is_deleted  # type: bool
        self.updated = updated  # type: str
        self.due_date = due_date  # type: str
        self.created = created  # type: str
        self.name = name  # type: str
        self.id = id  # type: str
        self.plan_to_do = plan_to_do  # type: CreateDevopsProjectSprintResponseBodyObjectPlanToDo

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectSprintResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.description is not None:
            result['Description'] = self.description
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlanToDo') is not None:
            temp_model = CreateDevopsProjectSprintResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        return self


class CreateDevopsProjectSprintResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: CreateDevopsProjectSprintResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectSprintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = CreateDevopsProjectSprintResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class CreateDevopsProjectSprintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDevopsProjectSprintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectSprintResponse, self).to_map()
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
            temp_model = CreateDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectSprintRequest(TeaModel):
    def __init__(self, org_id=None, name=None, description=None, project_id=None, executor_id=None, start_date=None,
                 due_date=None, sprint_id=None):
        self.org_id = org_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.project_id = project_id  # type: str
        self.executor_id = executor_id  # type: str
        self.start_date = start_date  # type: str
        self.due_date = due_date  # type: str
        self.sprint_id = sprint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectSprintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class UpdateDevopsProjectSprintResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectSprintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateDevopsProjectSprintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDevopsProjectSprintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDevopsProjectSprintResponse, self).to_map()
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
            temp_model = UpdateDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsOrganizationRequest(TeaModel):
    def __init__(self, org_id=None):
        self.org_id = org_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DeleteDevopsOrganizationResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsOrganizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsOrganizationResponse, self).to_map()
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
            temp_model = DeleteDevopsOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPipelineRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, flow_instance_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.flow_instance_id = flow_instance_id  # type: long
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CancelPipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: bool
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelPipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelPipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelPipelineResponse, self).to_map()
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
            temp_model = CancelPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskFlowStatusRequest(TeaModel):
    def __init__(self, org_id=None, task_flow_id=None):
        self.org_id = org_id  # type: str
        self.task_flow_id = task_flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        return self


class ListDevopsProjectTaskFlowStatusResponseBodyObject(TeaModel):
    def __init__(self, taskflow_id=None, kind=None, pos=None, is_deleted=None, updated=None, creator_id=None,
                 name=None, created=None, reject_status_ids=None, id=None):
        self.taskflow_id = taskflow_id  # type: str
        self.kind = kind  # type: str
        self.pos = pos  # type: int
        self.is_deleted = is_deleted  # type: bool
        self.updated = updated  # type: str
        self.creator_id = creator_id  # type: str
        self.name = name  # type: str
        self.created = created  # type: str
        self.reject_status_ids = reject_status_ids  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowStatusResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.taskflow_id is not None:
            result['TaskflowId'] = self.taskflow_id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.reject_status_ids is not None:
            result['RejectStatusIds'] = self.reject_status_ids
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskflowId') is not None:
            self.taskflow_id = m.get('TaskflowId')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('RejectStatusIds') is not None:
            self.reject_status_ids = m.get('RejectStatusIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskFlowStatusResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListDevopsProjectTaskFlowStatusResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTaskFlowStatusResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListDevopsProjectTaskFlowStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectTaskFlowStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTaskFlowStatusResponse, self).to_map()
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
            temp_model = ListDevopsProjectTaskFlowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserOrganizationRequest(TeaModel):
    def __init__(self, real_pk=None):
        self.real_pk = real_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class ListUserOrganizationResponseBodyObject(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserOrganizationResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserOrganizationResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, success=None, error_code=None, object=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListUserOrganizationResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListUserOrganizationResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListUserOrganizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserOrganizationResponse, self).to_map()
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
            temp_model = ListUserOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineEnvVarsRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, env_vars=None):
        self.org_id = org_id  # type: str
        # 流水线id
        self.pipeline_id = pipeline_id  # type: long
        # 需要修改的环境变量和默认值，json形式
        self.env_vars = env_vars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineEnvVarsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.env_vars is not None:
            result['EnvVars'] = self.env_vars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('EnvVars') is not None:
            self.env_vars = m.get('EnvVars')
        return self


class UpdatePipelineEnvVarsResponseBody(TeaModel):
    def __init__(self, request_id=None, pipeline_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.pipeline_id = pipeline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineEnvVarsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class UpdatePipelineEnvVarsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePipelineEnvVarsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePipelineEnvVarsResponse, self).to_map()
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
            temp_model = UpdatePipelineEnvVarsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteDevopsProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, success=None, error_code=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsProjectResponse, self).to_map()
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
            temp_model = DeleteDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceStatusRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, flow_instance_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.flow_instance_id = flow_instance_id  # type: long
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipelineInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceStatusResponse, self).to_map()
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
            temp_model = GetPipelineInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineLogRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, job_id=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.job_id = job_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPipelineLogResponseBodyObjectBuildProcessNodes(TeaModel):
    def __init__(self, status=None, node_index=None, node_name=None):
        self.status = status  # type: str
        self.node_index = node_index  # type: int
        self.node_name = node_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineLogResponseBodyObjectBuildProcessNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.node_index is not None:
            result['NodeIndex'] = self.node_index
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NodeIndex') is not None:
            self.node_index = m.get('NodeIndex')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetPipelineLogResponseBodyObject(TeaModel):
    def __init__(self, action_name=None, start_time=None, job_id=None, build_process_nodes=None):
        self.action_name = action_name  # type: str
        self.start_time = start_time  # type: str
        self.job_id = job_id  # type: long
        self.build_process_nodes = build_process_nodes  # type: list[GetPipelineLogResponseBodyObjectBuildProcessNodes]

    def validate(self):
        if self.build_process_nodes:
            for k in self.build_process_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineLogResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['BuildProcessNodes'] = []
        if self.build_process_nodes is not None:
            for k in self.build_process_nodes:
                result['BuildProcessNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.build_process_nodes = []
        if m.get('BuildProcessNodes') is not None:
            for k in m.get('BuildProcessNodes'):
                temp_model = GetPipelineLogResponseBodyObjectBuildProcessNodes()
                self.build_process_nodes.append(temp_model.from_map(k))
        return self


class GetPipelineLogResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[GetPipelineLogResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetPipelineLogResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class GetPipelineLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineLogResponse, self).to_map()
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
            temp_model = GetPipelineLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByAliyunUidRequest(TeaModel):
    def __init__(self, org_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByAliyunUidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetUserByAliyunUidResponseBodyObject(TeaModel):
    def __init__(self, aliyun_pk=None, email=None, avatar_url=None, name=None, id=None, phone=None):
        self.aliyun_pk = aliyun_pk  # type: str
        self.email = email  # type: str
        self.avatar_url = avatar_url  # type: str
        self.name = name  # type: str
        self.id = id  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByAliyunUidResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetUserByAliyunUidResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetUserByAliyunUidResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetUserByAliyunUidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetUserByAliyunUidResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetUserByAliyunUidResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserByAliyunUidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserByAliyunUidResponse, self).to_map()
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
            temp_model = GetUserByAliyunUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineMemberRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, user_id=None, role_name=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.user_id = user_id  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdatePipelineMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: bool
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePipelineMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePipelineMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePipelineMemberResponse, self).to_map()
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
            temp_model = UpdatePipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectsRequest(TeaModel):
    def __init__(self, org_id=None, page_size=None, order_by=None, page_token=None, select_by=None):
        self.org_id = org_id  # type: str
        self.page_size = page_size  # type: int
        self.order_by = order_by  # type: str
        self.page_token = page_token  # type: str
        self.select_by = select_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.select_by is not None:
            result['SelectBy'] = self.select_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('SelectBy') is not None:
            self.select_by = m.get('SelectBy')
        return self


class ListDevopsProjectsResponseBodyObjectResult(TeaModel):
    def __init__(self, logo=None, is_star=None, creator_id=None, members_count=None, organization_id=None,
                 visibility=None, is_template=None, description=None, updated=None, created=None, is_archived=None, name=None,
                 is_public=None, tasks_count=None, role_id=None, id=None):
        self.logo = logo  # type: str
        self.is_star = is_star  # type: bool
        self.creator_id = creator_id  # type: str
        self.members_count = members_count  # type: int
        self.organization_id = organization_id  # type: str
        self.visibility = visibility  # type: str
        self.is_template = is_template  # type: bool
        self.description = description  # type: str
        self.updated = updated  # type: str
        self.created = created  # type: str
        self.is_archived = is_archived  # type: bool
        self.name = name  # type: str
        self.is_public = is_public  # type: bool
        self.tasks_count = tasks_count  # type: int
        self.role_id = role_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectsResponseBodyObjectResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.is_star is not None:
            result['IsStar'] = self.is_star
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.members_count is not None:
            result['MembersCount'] = self.members_count
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.description is not None:
            result['Description'] = self.description
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.created is not None:
            result['Created'] = self.created
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.name is not None:
            result['Name'] = self.name
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.tasks_count is not None:
            result['TasksCount'] = self.tasks_count
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('IsStar') is not None:
            self.is_star = m.get('IsStar')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('MembersCount') is not None:
            self.members_count = m.get('MembersCount')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('TasksCount') is not None:
            self.tasks_count = m.get('TasksCount')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectsResponseBodyObject(TeaModel):
    def __init__(self, next_page_token=None, result=None):
        self.next_page_token = next_page_token  # type: str
        self.result = result  # type: list[ListDevopsProjectsResponseBodyObjectResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectsResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDevopsProjectsResponseBodyObjectResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDevopsProjectsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: ListDevopsProjectsResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(ListDevopsProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = ListDevopsProjectsResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class ListDevopsProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectsResponse, self).to_map()
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
            temp_model = ListDevopsProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectTaskRequest(TeaModel):
    def __init__(self, org_id=None, content=None, project_id=None, executor_id=None, start_date=None, due_date=None,
                 scenario_field_config_id=None, task_flow_status_id=None, note=None, priority=None, visible=None, parent_task_id=None,
                 sprint_id=None, task_list_id=None):
        self.org_id = org_id  # type: str
        self.content = content  # type: str
        self.project_id = project_id  # type: str
        self.executor_id = executor_id  # type: str
        self.start_date = start_date  # type: str
        self.due_date = due_date  # type: str
        self.scenario_field_config_id = scenario_field_config_id  # type: str
        self.task_flow_status_id = task_flow_status_id  # type: str
        self.note = note  # type: str
        self.priority = priority  # type: int
        self.visible = visible  # type: str
        self.parent_task_id = parent_task_id  # type: str
        self.sprint_id = sprint_id  # type: str
        self.task_list_id = task_list_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_list_id is not None:
            result['TaskListId'] = self.task_list_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskListId') is not None:
            self.task_list_id = m.get('TaskListId')
        return self


class CreateDevopsProjectTaskResponseBodyObject(TeaModel):
    def __init__(self, executor_id=None, project_id=None, priority=None, scenario_field_config_id=None,
                 ancestor_ids=None, task_type=None, tasklist_id=None, taskflowstatus_id=None, note=None, updated=None,
                 unique_id=None, content=None, rating=None, pos=None, story_point=None, start_date=None, creator_id=None,
                 source=None, organization_id=None, visible=None, is_done=None, sprint_id=None, due_date=None, created=None,
                 id=None):
        self.executor_id = executor_id  # type: str
        self.project_id = project_id  # type: str
        self.priority = priority  # type: int
        self.scenario_field_config_id = scenario_field_config_id  # type: str
        self.ancestor_ids = ancestor_ids  # type: str
        self.task_type = task_type  # type: str
        self.tasklist_id = tasklist_id  # type: str
        self.taskflowstatus_id = taskflowstatus_id  # type: str
        self.note = note  # type: str
        self.updated = updated  # type: str
        self.unique_id = unique_id  # type: int
        self.content = content  # type: str
        self.rating = rating  # type: int
        self.pos = pos  # type: int
        self.story_point = story_point  # type: str
        self.start_date = start_date  # type: str
        self.creator_id = creator_id  # type: str
        self.source = source  # type: str
        self.organization_id = organization_id  # type: str
        self.visible = visible  # type: str
        self.is_done = is_done  # type: bool
        self.sprint_id = sprint_id  # type: str
        self.due_date = due_date  # type: str
        self.created = created  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectTaskResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.note is not None:
            result['Note'] = self.note
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.content is not None:
            result['Content'] = self.content
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source is not None:
            result['Source'] = self.source
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDevopsProjectTaskResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: CreateDevopsProjectTaskResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = CreateDevopsProjectTaskResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class CreateDevopsProjectTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDevopsProjectTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectTaskResponse, self).to_map()
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
            temp_model = CreateDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceBuildNumberStatusRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, build_num=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.build_num = build_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.build_num is not None:
            result['BuildNum'] = self.build_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('BuildNum') is not None:
            self.build_num = m.get('BuildNum')
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(self, status=None, name=None, job_id=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.job_id = job_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(self, status=None, sign=None, components=None):
        self.status = status  # type: str
        self.sign = sign  # type: str
        self.components = components  # type: list[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents]

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups(TeaModel):
    def __init__(self, status=None, name=None, stages=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.stages = stages  # type: list[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages]

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObject(TeaModel):
    def __init__(self, status=None, groups=None):
        self.status = status  # type: str
        self.groups = groups  # type: list[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups]

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceBuildNumberStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetPipelineInstanceBuildNumberStatusResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetPipelineInstanceBuildNumberStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineInstanceBuildNumberStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceBuildNumberStatusResponse, self).to_map()
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
            temp_model = GetPipelineInstanceBuildNumberStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectSprintsRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, page_size=None, page_token=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.page_size = page_size  # type: long
        self.page_token = page_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectSprintsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        return self


class ListDevopsProjectSprintsResponseBodyObjectPlanToDo(TeaModel):
    def __init__(self, tasks=None, work_times=None, story_points=None):
        self.tasks = tasks  # type: int
        self.work_times = work_times  # type: int
        self.story_points = story_points  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectSprintsResponseBodyObjectPlanToDo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class ListDevopsProjectSprintsResponseBodyObject(TeaModel):
    def __init__(self, status=None, accomplished=None, project_id=None, is_deleted=None, start_date=None,
                 updated=None, creator_id=None, due_date=None, name=None, created=None, id=None, plan_to_do=None):
        self.status = status  # type: str
        self.accomplished = accomplished  # type: str
        self.project_id = project_id  # type: str
        self.is_deleted = is_deleted  # type: bool
        self.start_date = start_date  # type: str
        self.updated = updated  # type: str
        self.creator_id = creator_id  # type: str
        self.due_date = due_date  # type: str
        self.name = name  # type: str
        self.created = created  # type: str
        self.id = id  # type: str
        self.plan_to_do = plan_to_do  # type: ListDevopsProjectSprintsResponseBodyObjectPlanToDo

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        _map = super(ListDevopsProjectSprintsResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlanToDo') is not None:
            temp_model = ListDevopsProjectSprintsResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        return self


class ListDevopsProjectSprintsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None,
                 next_page_token=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListDevopsProjectSprintsResponseBodyObject]
        self.next_page_token = next_page_token  # type: str

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectSprintsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectSprintsResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        return self


class ListDevopsProjectSprintsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectSprintsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectSprintsResponse, self).to_map()
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
            temp_model = ListDevopsProjectSprintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectInfoRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetDevopsProjectInfoResponseBodyObject(TeaModel):
    def __init__(self, sort_method=None, unique_id_prefix=None, normal_type=None, modifier_id=None,
                 source_type=None, is_template=None, description=None, default_role_id=None, root_collection_id=None,
                 is_deleted=None, updated=None, name=None, is_archived=None, end_date=None, logo=None, start_date=None,
                 pinyin=None, creator_id=None, source_id=None, default_collection_id=None, is_suspended=None,
                 organization_id=None, visibility=None, py=None, category=None, next_task_unique_id=None, customfields=None,
                 created=None, id=None):
        self.sort_method = sort_method  # type: str
        self.unique_id_prefix = unique_id_prefix  # type: str
        self.normal_type = normal_type  # type: str
        self.modifier_id = modifier_id  # type: str
        self.source_type = source_type  # type: str
        self.is_template = is_template  # type: bool
        self.description = description  # type: str
        self.default_role_id = default_role_id  # type: str
        self.root_collection_id = root_collection_id  # type: str
        self.is_deleted = is_deleted  # type: bool
        self.updated = updated  # type: str
        self.name = name  # type: str
        self.is_archived = is_archived  # type: bool
        self.end_date = end_date  # type: str
        self.logo = logo  # type: str
        self.start_date = start_date  # type: str
        self.pinyin = pinyin  # type: str
        self.creator_id = creator_id  # type: str
        self.source_id = source_id  # type: str
        self.default_collection_id = default_collection_id  # type: str
        self.is_suspended = is_suspended  # type: bool
        self.organization_id = organization_id  # type: str
        self.visibility = visibility  # type: str
        self.py = py  # type: str
        self.category = category  # type: str
        self.next_task_unique_id = next_task_unique_id  # type: int
        self.customfields = customfields  # type: str
        self.created = created  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectInfoResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_method is not None:
            result['SortMethod'] = self.sort_method
        if self.unique_id_prefix is not None:
            result['UniqueIdPrefix'] = self.unique_id_prefix
        if self.normal_type is not None:
            result['NormalType'] = self.normal_type
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.description is not None:
            result['Description'] = self.description
        if self.default_role_id is not None:
            result['DefaultRoleId'] = self.default_role_id
        if self.root_collection_id is not None:
            result['RootCollectionId'] = self.root_collection_id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.name is not None:
            result['Name'] = self.name
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.default_collection_id is not None:
            result['DefaultCollectionId'] = self.default_collection_id
        if self.is_suspended is not None:
            result['IsSuspended'] = self.is_suspended
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.py is not None:
            result['Py'] = self.py
        if self.category is not None:
            result['Category'] = self.category
        if self.next_task_unique_id is not None:
            result['NextTaskUniqueId'] = self.next_task_unique_id
        if self.customfields is not None:
            result['Customfields'] = self.customfields
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SortMethod') is not None:
            self.sort_method = m.get('SortMethod')
        if m.get('UniqueIdPrefix') is not None:
            self.unique_id_prefix = m.get('UniqueIdPrefix')
        if m.get('NormalType') is not None:
            self.normal_type = m.get('NormalType')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DefaultRoleId') is not None:
            self.default_role_id = m.get('DefaultRoleId')
        if m.get('RootCollectionId') is not None:
            self.root_collection_id = m.get('RootCollectionId')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('DefaultCollectionId') is not None:
            self.default_collection_id = m.get('DefaultCollectionId')
        if m.get('IsSuspended') is not None:
            self.is_suspended = m.get('IsSuspended')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('Py') is not None:
            self.py = m.get('Py')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('NextTaskUniqueId') is not None:
            self.next_task_unique_id = m.get('NextTaskUniqueId')
        if m.get('Customfields') is not None:
            self.customfields = m.get('Customfields')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDevopsProjectInfoResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetDevopsProjectInfoResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetDevopsProjectInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetDevopsProjectInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDevopsProjectInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDevopsProjectInfoResponse, self).to_map()
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
            temp_model = GetDevopsProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineMemberRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, user_id=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelineMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeletePipelineMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: bool
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelineMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePipelineMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePipelineMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePipelineMemberResponse, self).to_map()
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
            temp_model = DeletePipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectSprintInfoRequest(TeaModel):
    def __init__(self, org_id=None, sprint_id=None):
        self.org_id = org_id  # type: str
        self.sprint_id = sprint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectSprintInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo(TeaModel):
    def __init__(self, tasks=None, work_times=None, story_points=None):
        self.tasks = tasks  # type: int
        self.work_times = work_times  # type: int
        self.story_points = story_points  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class GetDevopsProjectSprintInfoResponseBodyObject(TeaModel):
    def __init__(self, status=None, accomplished=None, project_id=None, is_deleted=None, start_date=None,
                 updated=None, creator_id=None, due_date=None, name=None, created=None, id=None, plan_to_do=None):
        self.status = status  # type: str
        self.accomplished = accomplished  # type: str
        self.project_id = project_id  # type: str
        self.is_deleted = is_deleted  # type: bool
        self.start_date = start_date  # type: str
        self.updated = updated  # type: str
        self.creator_id = creator_id  # type: str
        self.due_date = due_date  # type: str
        self.name = name  # type: str
        self.created = created  # type: str
        self.id = id  # type: str
        self.plan_to_do = plan_to_do  # type: GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        _map = super(GetDevopsProjectSprintInfoResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlanToDo') is not None:
            temp_model = GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        return self


class GetDevopsProjectSprintInfoResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetDevopsProjectSprintInfoResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetDevopsProjectSprintInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectSprintInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetDevopsProjectSprintInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDevopsProjectSprintInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDevopsProjectSprintInfoResponse, self).to_map()
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
            temp_model = GetDevopsProjectSprintInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsOrganizationMembersRequest(TeaModel):
    def __init__(self, org_id=None, user_id=None, real_pk=None):
        self.org_id = org_id  # type: str
        self.user_id = user_id  # type: str
        self.real_pk = real_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsOrganizationMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class DeleteDevopsOrganizationMembersResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsOrganizationMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsOrganizationMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsOrganizationMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsOrganizationMembersResponse, self).to_map()
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
            temp_model = DeleteDevopsOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLastWorkspaceRequest(TeaModel):
    def __init__(self, org_id=None, real_pk=None):
        self.org_id = org_id  # type: str
        self.real_pk = real_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLastWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class GetLastWorkspaceResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLastWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class GetLastWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLastWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLastWorkspaceResponse, self).to_map()
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
            temp_model = GetLastWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCredentialRequest(TeaModel):
    def __init__(self, org_id=None, name=None, user_name=None, password=None, type=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.name = name  # type: str
        self.user_name = user_name  # type: str
        self.password = password  # type: str
        self.type = type  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.type is not None:
            result['Type'] = self.type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CreateCredentialResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: long
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CreateCredentialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCredentialResponse, self).to_map()
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
            temp_model = CreateCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCredentialsRequest(TeaModel):
    def __init__(self, org_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCredentialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListCredentialsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCredentialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class ListCredentialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCredentialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCredentialsResponse, self).to_map()
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
            temp_model = ListCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineRequest(TeaModel):
    def __init__(self, org_id=None, pipeline=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline = pipeline  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline is not None:
            result['Pipeline'] = self.pipeline
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Pipeline') is not None:
            self.pipeline = m.get('Pipeline')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CreatePipelineResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: long
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CreatePipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineResponse, self).to_map()
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
            temp_model = CreatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_name=None, creators=None, operators=None, result_status_list=None,
                 create_start_time=None, create_end_time=None, execute_start_time=None, execute_end_time=None, page_size=None,
                 page_start=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_name = pipeline_name  # type: str
        self.creators = creators  # type: str
        self.operators = operators  # type: str
        self.result_status_list = result_status_list  # type: str
        self.create_start_time = create_start_time  # type: str
        self.create_end_time = create_end_time  # type: str
        self.execute_start_time = execute_start_time  # type: str
        self.execute_end_time = execute_end_time  # type: str
        self.page_size = page_size  # type: int
        self.page_start = page_start  # type: int
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.creators is not None:
            result['Creators'] = self.creators
        if self.operators is not None:
            result['Operators'] = self.operators
        if self.result_status_list is not None:
            result['ResultStatusList'] = self.result_status_list
        if self.create_start_time is not None:
            result['CreateStartTime'] = self.create_start_time
        if self.create_end_time is not None:
            result['CreateEndTime'] = self.create_end_time
        if self.execute_start_time is not None:
            result['ExecuteStartTime'] = self.execute_start_time
        if self.execute_end_time is not None:
            result['ExecuteEndTime'] = self.execute_end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('Creators') is not None:
            self.creators = m.get('Creators')
        if m.get('Operators') is not None:
            self.operators = m.get('Operators')
        if m.get('ResultStatusList') is not None:
            self.result_status_list = m.get('ResultStatusList')
        if m.get('CreateStartTime') is not None:
            self.create_start_time = m.get('CreateStartTime')
        if m.get('CreateEndTime') is not None:
            self.create_end_time = m.get('CreateEndTime')
        if m.get('ExecuteStartTime') is not None:
            self.execute_start_time = m.get('ExecuteStartTime')
        if m.get('ExecuteEndTime') is not None:
            self.execute_end_time = m.get('ExecuteEndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListPipelinesResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: dict[str, any]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelinesResponse, self).to_map()
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
            temp_model = ListPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineFromTemplateRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_template_id=None, pipeline_name=None):
        self.org_id = org_id  # type: str
        # 流水线模板的ID，可通过GetPipelineTemplates获取到该信息
        self.pipeline_template_id = pipeline_template_id  # type: long
        # 流水线名称
        self.pipeline_name = pipeline_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelineFromTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_template_id is not None:
            result['PipelineTemplateId'] = self.pipeline_template_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineTemplateId') is not None:
            self.pipeline_template_id = m.get('PipelineTemplateId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        return self


class CreatePipelineFromTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, pipeline_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 流水线ID
        self.pipeline_id = pipeline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelineFromTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class CreatePipelineFromTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePipelineFromTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineFromTemplateResponse, self).to_map()
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
            temp_model = CreatePipelineFromTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmartGroupRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListSmartGroupResponseBodyObject(TeaModel):
    def __init__(self, type=None, id=None):
        self.type = type  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartGroupResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListSmartGroupResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListSmartGroupResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSmartGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListSmartGroupResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListSmartGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSmartGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSmartGroupResponse, self).to_map()
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
            temp_model = ListSmartGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferPipelineOwnerRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, new_owner_id=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.new_owner_id = new_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferPipelineOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.new_owner_id is not None:
            result['NewOwnerId'] = self.new_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('NewOwnerId') is not None:
            self.new_owner_id = m.get('NewOwnerId')
        return self


class TransferPipelineOwnerResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: dict[str, any]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferPipelineOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferPipelineOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransferPipelineOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferPipelineOwnerResponse, self).to_map()
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
            temp_model = TransferPipelineOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommonGroupRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, description=None, smart_group_id=None, name=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.description = description  # type: str
        self.smart_group_id = smart_group_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCommonGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.description is not None:
            result['Description'] = self.description
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCommonGroupResponseBodyObject(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCommonGroupResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateCommonGroupResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: CreateCommonGroupResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(CreateCommonGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = CreateCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class CreateCommonGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCommonGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCommonGroupResponse, self).to_map()
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
            temp_model = CreateCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsOrganizationRequest(TeaModel):
    def __init__(self, org_name=None, source=None, real_pk=None, desired_member_count=None):
        self.org_name = org_name  # type: str
        self.source = source  # type: str
        self.real_pk = real_pk  # type: str
        self.desired_member_count = desired_member_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.source is not None:
            result['Source'] = self.source
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        if self.desired_member_count is not None:
            result['DesiredMemberCount'] = self.desired_member_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        if m.get('DesiredMemberCount') is not None:
            self.desired_member_count = m.get('DesiredMemberCount')
        return self


class CreateDevopsOrganizationResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CreateDevopsOrganizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDevopsOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDevopsOrganizationResponse, self).to_map()
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
            temp_model = CreateDevopsOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsScenarioFieldConfigRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsScenarioFieldConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsScenarioFieldConfigResponseBodyObject(TeaModel):
    def __init__(self, type=None, name=None, id=None):
        self.type = type  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsScenarioFieldConfigResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsScenarioFieldConfigResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListDevopsScenarioFieldConfigResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsScenarioFieldConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsScenarioFieldConfigResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListDevopsScenarioFieldConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsScenarioFieldConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsScenarioFieldConfigResponse, self).to_map()
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
            temp_model = ListDevopsScenarioFieldConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineTemplatesRequest(TeaModel):
    def __init__(self, org_id=None, page_start=None, page_num=None):
        self.org_id = org_id  # type: str
        # 本次读取的最大数据记录数量
        self.page_start = page_start  # type: int
        # 本次读取的最大数据记录数量
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class ListPipelineTemplatesResponseBodyDataDataList(TeaModel):
    def __init__(self, template_name=None, id=None):
        self.template_name = template_name  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineTemplatesResponseBodyDataDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListPipelineTemplatesResponseBodyData(TeaModel):
    def __init__(self, total=None, data_list=None):
        self.total = total  # type: float
        self.data_list = data_list  # type: list[ListPipelineTemplatesResponseBodyDataDataList]

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListPipelineTemplatesResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class ListPipelineTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: ListPipelineTemplatesResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPipelineTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListPipelineTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListPipelineTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineTemplatesResponse, self).to_map()
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
            temp_model = ListPipelineTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectTaskRequest(TeaModel):
    def __init__(self, org_id=None, content=None, project_id=None, executor_id=None, start_date=None, due_date=None,
                 scenario_fiield_config_id=None, task_flow_status_id=None, note=None, priority=None, visible=None, parent_task_id=None,
                 sprint_id=None, task_id=None):
        self.org_id = org_id  # type: str
        self.content = content  # type: str
        self.project_id = project_id  # type: str
        self.executor_id = executor_id  # type: str
        self.start_date = start_date  # type: str
        self.due_date = due_date  # type: str
        self.scenario_fiield_config_id = scenario_fiield_config_id  # type: str
        self.task_flow_status_id = task_flow_status_id  # type: str
        self.note = note  # type: str
        self.priority = priority  # type: int
        self.visible = visible  # type: str
        self.parent_task_id = parent_task_id  # type: str
        self.sprint_id = sprint_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.scenario_fiield_config_id is not None:
            result['ScenarioFiieldConfigId'] = self.scenario_fiield_config_id
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('ScenarioFiieldConfigId') is not None:
            self.scenario_fiield_config_id = m.get('ScenarioFiieldConfigId')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDevopsProjectTaskResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDevopsProjectTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateDevopsProjectTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDevopsProjectTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDevopsProjectTaskResponse, self).to_map()
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
            temp_model = UpdateDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectTaskInfoRequest(TeaModel):
    def __init__(self, org_id=None, task_id=None):
        self.org_id = org_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectTaskInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDevopsProjectTaskInfoResponseBodyObject(TeaModel):
    def __init__(self, executor_id=None, project_id=None, start_date=None, story_point=None, priority=None,
                 is_top_in_project=None, creator_id=None, organization_id=None, task_type=None, visible=None, tasklist_id=None,
                 is_done=None, is_deleted=None, taskflowstatus_id=None, note=None, sprint_id=None, updated=None,
                 due_date=None, created=None, content=None, id=None, involve_members=None):
        self.executor_id = executor_id  # type: str
        self.project_id = project_id  # type: str
        self.start_date = start_date  # type: str
        self.story_point = story_point  # type: str
        self.priority = priority  # type: str
        self.is_top_in_project = is_top_in_project  # type: bool
        self.creator_id = creator_id  # type: str
        self.organization_id = organization_id  # type: str
        self.task_type = task_type  # type: str
        self.visible = visible  # type: str
        self.tasklist_id = tasklist_id  # type: str
        self.is_done = is_done  # type: bool
        self.is_deleted = is_deleted  # type: bool
        self.taskflowstatus_id = taskflowstatus_id  # type: str
        self.note = note  # type: str
        self.sprint_id = sprint_id  # type: str
        self.updated = updated  # type: str
        self.due_date = due_date  # type: str
        self.created = created  # type: str
        self.content = content  # type: str
        self.id = id  # type: str
        self.involve_members = involve_members  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsProjectTaskInfoResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.note is not None:
            result['Note'] = self.note
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        return self


class GetDevopsProjectTaskInfoResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetDevopsProjectTaskInfoResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetDevopsProjectTaskInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectTaskInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetDevopsProjectTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDevopsProjectTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDevopsProjectTaskInfoResponse, self).to_map()
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
            temp_model = GetDevopsProjectTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceGroupStatusRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, flow_instance_id=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.flow_instance_id = flow_instance_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(self, status=None, name=None, job_id=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(self, status=None, sign=None, components=None):
        self.status = status  # type: str
        self.sign = sign  # type: str
        self.components = components  # type: list[GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents]

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroups(TeaModel):
    def __init__(self, status=None, name=None, stages=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.stages = stages  # type: list[GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages]

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponseBodyObjectGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceGroupStatusResponseBodyObject(TeaModel):
    def __init__(self, status=None, groups=None):
        self.status = status  # type: str
        self.groups = groups  # type: list[GetPipelineInstanceGroupStatusResponseBodyObjectGroups]

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceGroupStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetPipelineInstanceGroupStatusResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceGroupStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetPipelineInstanceGroupStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineInstanceGroupStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineInstanceGroupStatusResponse, self).to_map()
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
            temp_model = GetPipelineInstanceGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskDetailRequest(TeaModel):
    def __init__(self, org_id=None, content=None, project_id=None, executor_id=None, start_date=None, due_date=None,
                 task_flow_status_id=None, note=None, priority=None, sprint_id=None, task_id=None, work_times=None, custom_field_id=None,
                 custom_field_values=None, story_point=None, tag_ids=None, del_involvers=None, add_involvers=None):
        self.org_id = org_id  # type: str
        self.content = content  # type: str
        self.project_id = project_id  # type: str
        self.executor_id = executor_id  # type: str
        self.start_date = start_date  # type: str
        self.due_date = due_date  # type: str
        self.task_flow_status_id = task_flow_status_id  # type: str
        self.note = note  # type: str
        self.priority = priority  # type: long
        self.sprint_id = sprint_id  # type: str
        self.task_id = task_id  # type: str
        self.work_times = work_times  # type: long
        self.custom_field_id = custom_field_id  # type: str
        self.custom_field_values = custom_field_values  # type: str
        self.story_point = story_point  # type: str
        self.tag_ids = tag_ids  # type: str
        self.del_involvers = del_involvers  # type: str
        self.add_involvers = add_involvers  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.custom_field_id is not None:
            result['CustomFieldId'] = self.custom_field_id
        if self.custom_field_values is not None:
            result['CustomFieldValues'] = self.custom_field_values
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.del_involvers is not None:
            result['DelInvolvers'] = self.del_involvers
        if self.add_involvers is not None:
            result['AddInvolvers'] = self.add_involvers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('CustomFieldId') is not None:
            self.custom_field_id = m.get('CustomFieldId')
        if m.get('CustomFieldValues') is not None:
            self.custom_field_values = m.get('CustomFieldValues')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('DelInvolvers') is not None:
            self.del_involvers = m.get('DelInvolvers')
        if m.get('AddInvolvers') is not None:
            self.add_involvers = m.get('AddInvolvers')
        return self


class UpdateTaskDetailResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskDetailResponse, self).to_map()
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
            temp_model = UpdateTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskListFilterRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, scenario_field_config_id=None, name=None, order_condition=None,
                 order=None, executor_id=None, tag_id=None, due_date_start=None, due_date_end=None, creator_id=None,
                 involve_members=None, is_done=None, priority=None, page_size=None, page_token=None, object_type=None,
                 task_flow_status_id=None, sprint_id=None, extra=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.scenario_field_config_id = scenario_field_config_id  # type: str
        self.name = name  # type: str
        self.order_condition = order_condition  # type: str
        self.order = order  # type: str
        self.executor_id = executor_id  # type: str
        self.tag_id = tag_id  # type: str
        self.due_date_start = due_date_start  # type: str
        self.due_date_end = due_date_end  # type: str
        self.creator_id = creator_id  # type: str
        self.involve_members = involve_members  # type: str
        self.is_done = is_done  # type: bool
        self.priority = priority  # type: str
        self.page_size = page_size  # type: int
        self.page_token = page_token  # type: str
        self.object_type = object_type  # type: str
        self.task_flow_status_id = task_flow_status_id  # type: str
        self.sprint_id = sprint_id  # type: str
        self.extra = extra  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_condition is not None:
            result['OrderCondition'] = self.order_condition
        if self.order is not None:
            result['Order'] = self.order
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.due_date_start is not None:
            result['DueDateStart'] = self.due_date_start
        if self.due_date_end is not None:
            result['DueDateEnd'] = self.due_date_end
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.extra is not None:
            result['Extra'] = self.extra
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderCondition') is not None:
            self.order_condition = m.get('OrderCondition')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('DueDateStart') is not None:
            self.due_date_start = m.get('DueDateStart')
        if m.get('DueDateEnd') is not None:
            self.due_date_end = m.get('DueDateEnd')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        return self


class GetTaskListFilterResponseBodyObjectResultCustomfieldsValue(TeaModel):
    def __init__(self, id=None, title=None):
        self.id = id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultCustomfieldsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTaskListFilterResponseBodyObjectResultCustomfields(TeaModel):
    def __init__(self, type=None, customfield_id=None, values=None, value=None):
        self.type = type  # type: str
        self.customfield_id = customfield_id  # type: str
        self.values = values  # type: str
        self.value = value  # type: list[GetTaskListFilterResponseBodyObjectResultCustomfieldsValue]

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultCustomfields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.customfield_id is not None:
            result['CustomfieldId'] = self.customfield_id
        if self.values is not None:
            result['Values'] = self.values
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CustomfieldId') is not None:
            self.customfield_id = m.get('CustomfieldId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = GetTaskListFilterResponseBodyObjectResultCustomfieldsValue()
                self.value.append(temp_model.from_map(k))
        return self


class GetTaskListFilterResponseBodyObjectResultWorkTime(TeaModel):
    def __init__(self, used_time=None, total_time=None, unit=None):
        self.used_time = used_time  # type: int
        self.total_time = total_time  # type: int
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultWorkTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetTaskListFilterResponseBodyObjectResultBadges(TeaModel):
    def __init__(self, likes_count=None, objectlinks_count=None, attachments_count=None, comments_count=None):
        self.likes_count = likes_count  # type: int
        self.objectlinks_count = objectlinks_count  # type: int
        self.attachments_count = attachments_count  # type: int
        self.comments_count = comments_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultBadges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        return self


class GetTaskListFilterResponseBodyObjectResultSubtaskCount(TeaModel):
    def __init__(self, done=None, total=None):
        self.done = done  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultSubtaskCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTaskListFilterResponseBodyObjectResultReminder(TeaModel):
    def __init__(self, type=None, date=None, creator_id=None, members=None, rules=None):
        self.type = type  # type: str
        self.date = date  # type: str
        self.creator_id = creator_id  # type: str
        self.members = members  # type: list[str]
        self.rules = rules  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultReminder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.date is not None:
            result['Date'] = self.date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.members is not None:
            result['Members'] = self.members
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class GetTaskListFilterResponseBodyObjectResultCreator(TeaModel):
    def __init__(self, name=None, avatar_url=None, id=None):
        self.name = name  # type: str
        self.avatar_url = avatar_url  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultCreator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultStage(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultStage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultExecutor(TeaModel):
    def __init__(self, name=None, avatar_url=None, id=None):
        self.name = name  # type: str
        self.avatar_url = avatar_url  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultExecutor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultTaskFlowStatus(TeaModel):
    def __init__(self, task_flow_id=None, name=None, pos=None, kind=None, id=None):
        self.task_flow_id = task_flow_id  # type: str
        self.name = name  # type: str
        self.pos = pos  # type: int
        self.kind = kind  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResultTaskFlowStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.name is not None:
            result['Name'] = self.name
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResult(TeaModel):
    def __init__(self, is_favorite=None, executor_id=None, project_id=None, priority=None, is_top_in_project=None,
                 scenariof_feld_config_id=None, share_status=None, accomplished=None, task_list_id=None, note=None, updated=None,
                 unique_id=None, is_archived=None, content=None, rating=None, comments_count=None, task_flow_status_id=None,
                 recurrence=None, object_type=None, progress=None, until_date=None, story_point=None, objectlinks_count=None,
                 start_date=None, sprint=None, creator_id=None, source=None, source_id=None, source_date=None,
                 organization_id=None, likes_count=None, stage_id=None, visible=None, is_done=None, parent=None, sprint_id=None,
                 attachments_count=None, due_date=None, task_unique_id=None, created=None, task_id=None, id=None, customfields=None,
                 involve_members=None, tag_ids=None, labels=None, divisions=None, ancestor_ids=None, work_time=None, badges=None,
                 subtask_count=None, reminder=None, creator=None, stage=None, executor=None, task_flow_status=None):
        self.is_favorite = is_favorite  # type: bool
        self.executor_id = executor_id  # type: str
        self.project_id = project_id  # type: str
        self.priority = priority  # type: int
        self.is_top_in_project = is_top_in_project  # type: bool
        self.scenariof_feld_config_id = scenariof_feld_config_id  # type: str
        self.share_status = share_status  # type: int
        self.accomplished = accomplished  # type: str
        self.task_list_id = task_list_id  # type: str
        self.note = note  # type: str
        self.updated = updated  # type: str
        self.unique_id = unique_id  # type: int
        self.is_archived = is_archived  # type: bool
        self.content = content  # type: str
        self.rating = rating  # type: int
        self.comments_count = comments_count  # type: int
        self.task_flow_status_id = task_flow_status_id  # type: str
        self.recurrence = recurrence  # type: str
        self.object_type = object_type  # type: str
        self.progress = progress  # type: int
        self.until_date = until_date  # type: str
        self.story_point = story_point  # type: str
        self.objectlinks_count = objectlinks_count  # type: int
        self.start_date = start_date  # type: str
        self.sprint = sprint  # type: str
        self.creator_id = creator_id  # type: str
        self.source = source  # type: str
        self.source_id = source_id  # type: str
        self.source_date = source_date  # type: str
        self.organization_id = organization_id  # type: str
        self.likes_count = likes_count  # type: int
        self.stage_id = stage_id  # type: str
        self.visible = visible  # type: str
        self.is_done = is_done  # type: bool
        self.parent = parent  # type: str
        self.sprint_id = sprint_id  # type: str
        self.attachments_count = attachments_count  # type: int
        self.due_date = due_date  # type: str
        self.task_unique_id = task_unique_id  # type: str
        self.created = created  # type: str
        self.task_id = task_id  # type: str
        self.id = id  # type: str
        self.customfields = customfields  # type: list[GetTaskListFilterResponseBodyObjectResultCustomfields]
        self.involve_members = involve_members  # type: list[str]
        self.tag_ids = tag_ids  # type: list[str]
        self.labels = labels  # type: list[str]
        self.divisions = divisions  # type: list[str]
        self.ancestor_ids = ancestor_ids  # type: list[str]
        self.work_time = work_time  # type: GetTaskListFilterResponseBodyObjectResultWorkTime
        self.badges = badges  # type: GetTaskListFilterResponseBodyObjectResultBadges
        self.subtask_count = subtask_count  # type: GetTaskListFilterResponseBodyObjectResultSubtaskCount
        self.reminder = reminder  # type: GetTaskListFilterResponseBodyObjectResultReminder
        self.creator = creator  # type: GetTaskListFilterResponseBodyObjectResultCreator
        self.stage = stage  # type: GetTaskListFilterResponseBodyObjectResultStage
        self.executor = executor  # type: GetTaskListFilterResponseBodyObjectResultExecutor
        self.task_flow_status = task_flow_status  # type: GetTaskListFilterResponseBodyObjectResultTaskFlowStatus

    def validate(self):
        if self.customfields:
            for k in self.customfields:
                if k:
                    k.validate()
        if self.work_time:
            self.work_time.validate()
        if self.badges:
            self.badges.validate()
        if self.subtask_count:
            self.subtask_count.validate()
        if self.reminder:
            self.reminder.validate()
        if self.creator:
            self.creator.validate()
        if self.stage:
            self.stage.validate()
        if self.executor:
            self.executor.validate()
        if self.task_flow_status:
            self.task_flow_status.validate()

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObjectResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.scenariof_feld_config_id is not None:
            result['ScenariofFeldConfigId'] = self.scenariof_feld_config_id
        if self.share_status is not None:
            result['ShareStatus'] = self.share_status
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.task_list_id is not None:
            result['TaskListId'] = self.task_list_id
        if self.note is not None:
            result['Note'] = self.note
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.content is not None:
            result['Content'] = self.content
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.until_date is not None:
            result['UntilDate'] = self.until_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sprint is not None:
            result['Sprint'] = self.sprint
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_date is not None:
            result['SourceDate'] = self.source_date
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.parent is not None:
            result['Parent'] = self.parent
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.task_unique_id is not None:
            result['TaskUniqueId'] = self.task_unique_id
        if self.created is not None:
            result['Created'] = self.created
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.id is not None:
            result['Id'] = self.id
        result['Customfields'] = []
        if self.customfields is not None:
            for k in self.customfields:
                result['Customfields'].append(k.to_map() if k else None)
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.divisions is not None:
            result['Divisions'] = self.divisions
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.work_time is not None:
            result['WorkTime'] = self.work_time.to_map()
        if self.badges is not None:
            result['Badges'] = self.badges.to_map()
        if self.subtask_count is not None:
            result['SubtaskCount'] = self.subtask_count.to_map()
        if self.reminder is not None:
            result['Reminder'] = self.reminder.to_map()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.stage is not None:
            result['Stage'] = self.stage.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.task_flow_status is not None:
            result['TaskFlowStatus'] = self.task_flow_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('ScenariofFeldConfigId') is not None:
            self.scenariof_feld_config_id = m.get('ScenariofFeldConfigId')
        if m.get('ShareStatus') is not None:
            self.share_status = m.get('ShareStatus')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('TaskListId') is not None:
            self.task_list_id = m.get('TaskListId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('UntilDate') is not None:
            self.until_date = m.get('UntilDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Sprint') is not None:
            self.sprint = m.get('Sprint')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceDate') is not None:
            self.source_date = m.get('SourceDate')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('Parent') is not None:
            self.parent = m.get('Parent')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('TaskUniqueId') is not None:
            self.task_unique_id = m.get('TaskUniqueId')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.customfields = []
        if m.get('Customfields') is not None:
            for k in m.get('Customfields'):
                temp_model = GetTaskListFilterResponseBodyObjectResultCustomfields()
                self.customfields.append(temp_model.from_map(k))
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Divisions') is not None:
            self.divisions = m.get('Divisions')
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('WorkTime') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultWorkTime()
            self.work_time = temp_model.from_map(m['WorkTime'])
        if m.get('Badges') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultBadges()
            self.badges = temp_model.from_map(m['Badges'])
        if m.get('SubtaskCount') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultSubtaskCount()
            self.subtask_count = temp_model.from_map(m['SubtaskCount'])
        if m.get('Reminder') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultReminder()
            self.reminder = temp_model.from_map(m['Reminder'])
        if m.get('Creator') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Stage') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultStage()
            self.stage = temp_model.from_map(m['Stage'])
        if m.get('Executor') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('TaskFlowStatus') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultTaskFlowStatus()
            self.task_flow_status = temp_model.from_map(m['TaskFlowStatus'])
        return self


class GetTaskListFilterResponseBodyObject(TeaModel):
    def __init__(self, next_page_token=None, total_size=None, result=None):
        self.next_page_token = next_page_token  # type: str
        self.total_size = total_size  # type: int
        self.result = result  # type: list[GetTaskListFilterResponseBodyObjectResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskListFilterResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTaskListFilterResponseBodyObjectResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetTaskListFilterResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: str
        self.error_code = error_code  # type: str
        self.object = object  # type: GetTaskListFilterResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetTaskListFilterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetTaskListFilterResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetTaskListFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskListFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskListFilterResponse, self).to_map()
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
            temp_model = GetTaskListFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectOptionRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, type=None, query=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.type = type  # type: str
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class GetProjectOptionResponseBodyObject(TeaModel):
    def __init__(self, value=None, name=None, scope_name=None, kind=None):
        self.value = value  # type: str
        self.name = name  # type: str
        self.scope_name = scope_name  # type: str
        self.kind = kind  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectOptionResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.scope_name is not None:
            result['ScopeName'] = self.scope_name
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScopeName') is not None:
            self.scope_name = m.get('ScopeName')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class GetProjectOptionResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[GetProjectOptionResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetProjectOptionResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class GetProjectOptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProjectOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectOptionResponse, self).to_map()
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
            temp_model = GetProjectOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommonGroupRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, description=None, smart_group_id=None, common_group_id=None,
                 name=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.description = description  # type: str
        self.smart_group_id = smart_group_id  # type: str
        self.common_group_id = common_group_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCommonGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.description is not None:
            result['Description'] = self.description
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.common_group_id is not None:
            result['CommonGroupId'] = self.common_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('CommonGroupId') is not None:
            self.common_group_id = m.get('CommonGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCommonGroupResponseBodyObject(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCommonGroupResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateCommonGroupResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: UpdateCommonGroupResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(UpdateCommonGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = UpdateCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class UpdateCommonGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCommonGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCommonGroupResponse, self).to_map()
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
            temp_model = UpdateCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonGroupRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, smart_group_id=None, all=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.smart_group_id = smart_group_id  # type: str
        self.all = all  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class ListCommonGroupResponseBodyObject(TeaModel):
    def __init__(self, resource_count=None, smart_group_id=None, pos=None, project_id=None, is_root=None,
                 pinyin=None, creator_id=None, name=None, id=None):
        self.resource_count = resource_count  # type: int
        self.smart_group_id = smart_group_id  # type: str
        self.pos = pos  # type: int
        self.project_id = project_id  # type: str
        self.is_root = is_root  # type: bool
        self.pinyin = pinyin  # type: str
        self.creator_id = creator_id  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonGroupResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_root is not None:
            result['IsRoot'] = self.is_root
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListCommonGroupResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListCommonGroupResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommonGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListCommonGroupResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListCommonGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCommonGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommonGroupResponse, self).to_map()
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
            temp_model = ListCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectTaskRequest(TeaModel):
    def __init__(self, org_id=None, task_id=None):
        self.org_id = org_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteDevopsProjectTaskResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, object=None, successful=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: bool
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDevopsProjectTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteDevopsProjectTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDevopsProjectTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDevopsProjectTaskResponse, self).to_map()
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
            temp_model = DeleteDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsOrganizationMembersRequest(TeaModel):
    def __init__(self, org_id=None):
        self.org_id = org_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsOrganizationMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class GetDevopsOrganizationMembersResponseBodyObject(TeaModel):
    def __init__(self, email=None, avatar_url=None, user_id=None, member_id=None, role=None, name=None, phone=None):
        self.email = email  # type: str
        self.avatar_url = avatar_url  # type: str
        self.user_id = user_id  # type: str
        self.member_id = member_id  # type: str
        self.role = role  # type: int
        self.name = name  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDevopsOrganizationMembersResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetDevopsOrganizationMembersResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[GetDevopsOrganizationMembersResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDevopsOrganizationMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetDevopsOrganizationMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class GetDevopsOrganizationMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDevopsOrganizationMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDevopsOrganizationMembersResponse, self).to_map()
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
            temp_model = GetDevopsOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectRequest(TeaModel):
    def __init__(self, org_id=None, name=None, description=None):
        self.org_id = org_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDevopsProjectResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDevopsProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CreateDevopsProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDevopsProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDevopsProjectResponse, self).to_map()
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
            temp_model = CreateDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskDetailActivityRequest(TeaModel):
    def __init__(self, org_id=None, project_id=None, task_id=None):
        self.org_id = org_id  # type: str
        self.project_id = project_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailActivityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskDetailActivityResponseBodyObject(TeaModel):
    def __init__(self, updated=None, action=None, title=None, created=None, content=None):
        self.updated = updated  # type: str
        self.action = action  # type: str
        self.title = title  # type: str
        self.created = created  # type: str
        self.content = content  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskDetailActivityResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.action is not None:
            result['Action'] = self.action
        if self.title is not None:
            result['Title'] = self.title
        if self.created is not None:
            result['Created'] = self.created
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetTaskDetailActivityResponseBody(TeaModel):
    def __init__(self, http_status_code=None, error_msg=None, request_id=None, successful=None, error_code=None,
                 object=None):
        self.http_status_code = http_status_code  # type: int
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[GetTaskDetailActivityResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskDetailActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetTaskDetailActivityResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class GetTaskDetailActivityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskDetailActivityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskDetailActivityResponse, self).to_map()
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
            temp_model = GetTaskDetailActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecutePipelineRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, parameters=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.parameters = parameters  # type: str
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecutePipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ExecutePipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, object=None, success=None, error_code=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.object = object  # type: long
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecutePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ExecutePipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecutePipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecutePipelineResponse, self).to_map()
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
            temp_model = ExecutePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceConnectionRequest(TeaModel):
    def __init__(self, service_connection_type=None, user_pk=None, org_id=None):
        self.service_connection_type = service_connection_type  # type: str
        self.user_pk = user_pk  # type: str
        self.org_id = org_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_connection_type is not None:
            result['ServiceConnectionType'] = self.service_connection_type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceConnectionType') is not None:
            self.service_connection_type = m.get('ServiceConnectionType')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class CreateServiceConnectionResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, object=None, success=None, error_code=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.object = object  # type: long
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CreateServiceConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceConnectionResponse, self).to_map()
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
            temp_model = CreateServiceConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstHistoryRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, start_time=None, end_time=None, page_start=None,
                 page_size=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.page_start = page_start  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups(TeaModel):
    def __init__(self, status=None, create_time=None, delete_status=None, id_extent=None, creator=None,
                 end_time=None, start_time=None, modifier=None, result_status=None, flow_inst_id=None, name=None, id=None,
                 modify_time=None):
        self.status = status  # type: str
        self.create_time = create_time  # type: long
        self.delete_status = delete_status  # type: str
        self.id_extent = id_extent  # type: int
        self.creator = creator  # type: str
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.modifier = modifier  # type: str
        self.result_status = result_status  # type: str
        self.flow_inst_id = flow_inst_id  # type: int
        self.name = name  # type: str
        self.id = id  # type: int
        self.modify_time = modify_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delete_status is not None:
            result['DeleteStatus'] = self.delete_status
        if self.id_extent is not None:
            result['IdExtent'] = self.id_extent
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.result_status is not None:
            result['ResultStatus'] = self.result_status
        if self.flow_inst_id is not None:
            result['FlowInstId'] = self.flow_inst_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeleteStatus') is not None:
            self.delete_status = m.get('DeleteStatus')
        if m.get('IdExtent') is not None:
            self.id_extent = m.get('IdExtent')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ResultStatus') is not None:
            self.result_status = m.get('ResultStatus')
        if m.get('FlowInstId') is not None:
            self.flow_inst_id = m.get('FlowInstId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult(TeaModel):
    def __init__(self, engine_pipeline_number=None, mix_flow_inst_id=None, engine_pipeline_name=None,
                 engine_pipeline_id=None, engine_pipeline_inst_id=None, time_stamp=None, trigger_mode=None, sources=None, caches=None,
                 date_time=None):
        self.engine_pipeline_number = engine_pipeline_number  # type: int
        self.mix_flow_inst_id = mix_flow_inst_id  # type: str
        self.engine_pipeline_name = engine_pipeline_name  # type: str
        self.engine_pipeline_id = engine_pipeline_id  # type: int
        self.engine_pipeline_inst_id = engine_pipeline_inst_id  # type: int
        self.time_stamp = time_stamp  # type: str
        self.trigger_mode = trigger_mode  # type: str
        self.sources = sources  # type: str
        self.caches = caches  # type: str
        self.date_time = date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_pipeline_number is not None:
            result['EnginePipelineNumber'] = self.engine_pipeline_number
        if self.mix_flow_inst_id is not None:
            result['MixFlowInstId'] = self.mix_flow_inst_id
        if self.engine_pipeline_name is not None:
            result['EnginePipelineName'] = self.engine_pipeline_name
        if self.engine_pipeline_id is not None:
            result['EnginePipelineId'] = self.engine_pipeline_id
        if self.engine_pipeline_inst_id is not None:
            result['EnginePipelineInstId'] = self.engine_pipeline_inst_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.caches is not None:
            result['Caches'] = self.caches
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnginePipelineNumber') is not None:
            self.engine_pipeline_number = m.get('EnginePipelineNumber')
        if m.get('MixFlowInstId') is not None:
            self.mix_flow_inst_id = m.get('MixFlowInstId')
        if m.get('EnginePipelineName') is not None:
            self.engine_pipeline_name = m.get('EnginePipelineName')
        if m.get('EnginePipelineId') is not None:
            self.engine_pipeline_id = m.get('EnginePipelineId')
        if m.get('EnginePipelineInstId') is not None:
            self.engine_pipeline_inst_id = m.get('EnginePipelineInstId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('Caches') is not None:
            self.caches = m.get('Caches')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstance(TeaModel):
    def __init__(self, status=None, stages=None, create_time=None, status_name=None, running_status=None,
                 creator=None, stage_topo=None, modifier=None, auto_driven_status=None, result_status=None, id=None,
                 system_code=None, modify_time=None, system_id=None, groups=None, result=None):
        self.status = status  # type: str
        self.stages = stages  # type: dict[str, any]
        self.create_time = create_time  # type: long
        self.status_name = status_name  # type: str
        self.running_status = running_status  # type: str
        self.creator = creator  # type: str
        self.stage_topo = stage_topo  # type: str
        self.modifier = modifier  # type: str
        self.auto_driven_status = auto_driven_status  # type: bool
        self.result_status = result_status  # type: str
        self.id = id  # type: int
        self.system_code = system_code  # type: str
        self.modify_time = modify_time  # type: long
        self.system_id = system_id  # type: str
        self.groups = groups  # type: list[GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups]
        self.result = result  # type: GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBodyDataDataListFlowInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stages is not None:
            result['Stages'] = self.stages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.running_status is not None:
            result['RunningStatus'] = self.running_status
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.stage_topo is not None:
            result['StageTopo'] = self.stage_topo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.auto_driven_status is not None:
            result['AutoDrivenStatus'] = self.auto_driven_status
        if self.result_status is not None:
            result['ResultStatus'] = self.result_status
        if self.id is not None:
            result['Id'] = self.id
        if self.system_code is not None:
            result['SystemCode'] = self.system_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.system_id is not None:
            result['SystemId'] = self.system_id
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Stages') is not None:
            self.stages = m.get('Stages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('RunningStatus') is not None:
            self.running_status = m.get('RunningStatus')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('StageTopo') is not None:
            self.stage_topo = m.get('StageTopo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('AutoDrivenStatus') is not None:
            self.auto_driven_status = m.get('AutoDrivenStatus')
        if m.get('ResultStatus') is not None:
            self.result_status = m.get('ResultStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SystemCode') is not None:
            self.system_code = m.get('SystemCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SystemId') is not None:
            self.system_id = m.get('SystemId')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Result') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetPipelineInstHistoryResponseBodyDataDataList(TeaModel):
    def __init__(self, status=None, create_time=None, status_name=None, trigger_mode=None, pipeline_config_id=None,
                 deletion=None, creator=None, inst_number=None, modifier=None, packages=None, flow_inst_id=None,
                 pipeline_id=None, id=None, modify_time=None, flow_instance=None):
        self.status = status  # type: str
        self.create_time = create_time  # type: long
        self.status_name = status_name  # type: str
        self.trigger_mode = trigger_mode  # type: int
        self.pipeline_config_id = pipeline_config_id  # type: int
        self.deletion = deletion  # type: str
        self.creator = creator  # type: str
        self.inst_number = inst_number  # type: int
        self.modifier = modifier  # type: str
        self.packages = packages  # type: str
        self.flow_inst_id = flow_inst_id  # type: int
        self.pipeline_id = pipeline_id  # type: int
        self.id = id  # type: int
        self.modify_time = modify_time  # type: long
        self.flow_instance = flow_instance  # type: GetPipelineInstHistoryResponseBodyDataDataListFlowInstance

    def validate(self):
        if self.flow_instance:
            self.flow_instance.validate()

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBodyDataDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        if self.pipeline_config_id is not None:
            result['PipelineConfigId'] = self.pipeline_config_id
        if self.deletion is not None:
            result['Deletion'] = self.deletion
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.inst_number is not None:
            result['InstNumber'] = self.inst_number
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.packages is not None:
            result['Packages'] = self.packages
        if self.flow_inst_id is not None:
            result['FlowInstId'] = self.flow_inst_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.flow_instance is not None:
            result['FlowInstance'] = self.flow_instance.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        if m.get('PipelineConfigId') is not None:
            self.pipeline_config_id = m.get('PipelineConfigId')
        if m.get('Deletion') is not None:
            self.deletion = m.get('Deletion')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('InstNumber') is not None:
            self.inst_number = m.get('InstNumber')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('Packages') is not None:
            self.packages = m.get('Packages')
        if m.get('FlowInstId') is not None:
            self.flow_inst_id = m.get('FlowInstId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('FlowInstance') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstance()
            self.flow_instance = temp_model.from_map(m['FlowInstance'])
        return self


class GetPipelineInstHistoryResponseBodyData(TeaModel):
    def __init__(self, total=None, data_list=None):
        self.total = total  # type: int
        self.data_list = data_list  # type: list[GetPipelineInstHistoryResponseBodyDataDataList]

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = GetPipelineInstHistoryResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class GetPipelineInstHistoryResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, data=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.data = data  # type: GetPipelineInstHistoryResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Data') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetPipelineInstHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineInstHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineInstHistoryResponse, self).to_map()
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
            temp_model = GetPipelineInstHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineStepLogRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None, job_id=None, step_index=None, offset=None,
                 limit=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str
        self.job_id = job_id  # type: long
        self.step_index = step_index  # type: str
        self.offset = offset  # type: long
        self.limit = limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineStepLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.step_index is not None:
            result['StepIndex'] = self.step_index
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('StepIndex') is not None:
            self.step_index = m.get('StepIndex')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class GetPipelineStepLogResponseBodyObject(TeaModel):
    def __init__(self, last=None, more=None, logs=None):
        self.last = last  # type: int
        self.more = more  # type: bool
        self.logs = logs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineStepLogResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last is not None:
            result['Last'] = self.last
        if self.more is not None:
            result['More'] = self.more
        if self.logs is not None:
            result['Logs'] = self.logs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Last') is not None:
            self.last = m.get('Last')
        if m.get('More') is not None:
            self.more = m.get('More')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        return self


class GetPipelineStepLogResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetPipelineStepLogResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetPipelineStepLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetPipelineStepLogResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetPipelineStepLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineStepLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineStepLogResponse, self).to_map()
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
            temp_model = GetPipelineStepLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipleineLatestInstanceStatusRequest(TeaModel):
    def __init__(self, org_id=None, pipeline_id=None, user_pk=None):
        self.org_id = org_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.user_pk = user_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(self, status=None, name=None, job_id=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.job_id = job_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(self, status=None, sign=None, components=None):
        self.status = status  # type: str
        self.sign = sign  # type: str
        self.components = components  # type: list[GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents]

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroups(TeaModel):
    def __init__(self, status=None, name=None, stages=None):
        self.status = status  # type: str
        self.name = name  # type: str
        self.stages = stages  # type: list[GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages]

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponseBodyObjectGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        return self


class GetPipleineLatestInstanceStatusResponseBodyObject(TeaModel):
    def __init__(self, status=None, groups=None):
        self.status = status  # type: str
        self.groups = groups  # type: list[GetPipleineLatestInstanceStatusResponseBodyObjectGroups]

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipleineLatestInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, success=None, error_code=None, object=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: GetPipleineLatestInstanceStatusResponseBodyObject

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.object is not None:
            result['Object'] = self.object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Object') is not None:
            temp_model = GetPipleineLatestInstanceStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        return self


class GetPipleineLatestInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipleineLatestInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipleineLatestInstanceStatusResponse, self).to_map()
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
            temp_model = GetPipleineLatestInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTasksRequest(TeaModel):
    def __init__(self, org_id=None, project_ids=None):
        self.org_id = org_id  # type: str
        self.project_ids = project_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class ListDevopsProjectTasksResponseBodyObject(TeaModel):
    def __init__(self, taskgroup_id=None, tasklist_id=None, project_id=None, modifier_id=None, updated=None,
                 creator_id=None, created=None, name=None, id=None):
        self.taskgroup_id = taskgroup_id  # type: str
        self.tasklist_id = tasklist_id  # type: str
        self.project_id = project_id  # type: str
        self.modifier_id = modifier_id  # type: str
        self.updated = updated  # type: str
        self.creator_id = creator_id  # type: str
        self.created = created  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDevopsProjectTasksResponseBodyObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.taskgroup_id is not None:
            result['TaskgroupId'] = self.taskgroup_id
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.created is not None:
            result['Created'] = self.created
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskgroupId') is not None:
            self.taskgroup_id = m.get('TaskgroupId')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTasksResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, successful=None, error_code=None, object=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.successful = successful  # type: bool
        self.error_code = error_code  # type: str
        self.object = object  # type: list[ListDevopsProjectTasksResponseBodyObject]

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successful is not None:
            result['Successful'] = self.successful
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTasksResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        return self


class ListDevopsProjectTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDevopsProjectTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDevopsProjectTasksResponse, self).to_map()
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
            temp_model = ListDevopsProjectTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


