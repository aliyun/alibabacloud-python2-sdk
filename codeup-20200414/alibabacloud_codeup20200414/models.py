# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptMergeRequestRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptMergeRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class AcceptMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AcceptMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AcceptMergeRequestResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 merge_error=None, merge_status=None, merge_type=None, merged_revision=None, name_with_namespace=None,
                 project_id=None, source_branch=None, state=None, target_branch=None, title=None, updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: AcceptMergeRequestResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[AcceptMergeRequestResponseBodyResultAssigneeList]
        self.author = author  # type: AcceptMergeRequestResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = AcceptMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = AcceptMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class AcceptMergeRequestResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AcceptMergeRequestResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AcceptMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptMergeRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptMergeRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptMergeRequestResponse, self).to_map()
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
            temp_model = AcceptMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class AddGroupMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGroupMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class AddGroupMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[AddGroupMemberResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = AddGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGroupMemberResponse, self).to_map()
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
            temp_model = AddGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRepositoryMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRepositoryMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class AddRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRepositoryMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class AddRepositoryMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[AddRepositoryMemberResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddRepositoryMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = AddRepositoryMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRepositoryMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRepositoryMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRepositoryMemberResponse, self).to_map()
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
            temp_model = AddRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWebhookRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddWebhookResponseBodyResult(TeaModel):
    def __init__(self, build_events=None, created_at=None, description=None, enable_ssl_verification=None, id=None,
                 issues_events=None, last_test_result=None, merge_requests_events=None, note_events=None, project_id=None,
                 push_events=None, secret_token=None, tag_push_events=None, url=None):
        self.build_events = build_events  # type: bool
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        self.id = id  # type: long
        self.issues_events = issues_events  # type: bool
        self.last_test_result = last_test_result  # type: str
        self.merge_requests_events = merge_requests_events  # type: bool
        self.note_events = note_events  # type: bool
        self.project_id = project_id  # type: long
        self.push_events = push_events  # type: bool
        self.secret_token = secret_token  # type: str
        self.tag_push_events = tag_push_events  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWebhookResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_events is not None:
            result['BuildEvents'] = self.build_events
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['Id'] = self.id
        if self.issues_events is not None:
            result['IssuesEvents'] = self.issues_events
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildEvents') is not None:
            self.build_events = m.get('BuildEvents')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IssuesEvents') is not None:
            self.issues_events = m.get('IssuesEvents')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AddWebhookResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AddWebhookResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddWebhookResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWebhookResponse, self).to_map()
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
            temp_model = AddWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBranchRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None, branch_name=None, ref=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str
        self.branch_name = branch_name  # type: str
        self.ref = ref  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBranchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.branch_name is not None:
            result['branchName'] = self.branch_name
        if self.ref is not None:
            result['ref'] = self.ref
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('branchName') is not None:
            self.branch_name = m.get('branchName')
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        return self


class CreateBranchResponseBodyResultCommitInfo(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBranchResponseBodyResultCommitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateBranchResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, commit_info=None, protected_branch=None):
        self.branch_name = branch_name  # type: str
        self.commit_info = commit_info  # type: CreateBranchResponseBodyResultCommitInfo
        self.protected_branch = protected_branch  # type: bool

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super(CreateBranchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = CreateBranchResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        return self


class CreateBranchResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateBranchResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateBranchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBranchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBranchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBranchResponse, self).to_map()
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
            temp_model = CreateBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateFileResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, file_path=None):
        self.branch_name = branch_name  # type: str
        self.file_path = file_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateFileResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileResponse, self).to_map()
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeRequestRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class CreateMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMergeRequestResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 merge_error=None, merge_status=None, merge_type=None, merged_revision=None, name_with_namespace=None,
                 project_id=None, source_branch=None, state=None, target_branch=None, title=None, updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: CreateMergeRequestResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[CreateMergeRequestResponseBodyResultAssigneeList]
        self.author = author  # type: CreateMergeRequestResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = CreateMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = CreateMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = CreateMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class CreateMergeRequestResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateMergeRequestResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMergeRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMergeRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMergeRequestResponse, self).to_map()
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
            temp_model = CreateMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeRequestCommentRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateMergeRequestCommentResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, email=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeRequestCommentResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMergeRequestCommentResponseBodyResult(TeaModel):
    def __init__(self, author=None, closed=None, created_at=None, id=None, is_draft=None, line=None, note=None,
                 out_dated=None, parent_note_id=None, path=None, project_id=None, range_context=None, side=None,
                 updated_at=None):
        self.author = author  # type: CreateMergeRequestCommentResponseBodyResultAuthor
        self.closed = closed  # type: int
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.is_draft = is_draft  # type: bool
        self.line = line  # type: long
        self.note = note  # type: str
        self.out_dated = out_dated  # type: bool
        self.parent_note_id = parent_note_id  # type: long
        self.path = path  # type: str
        self.project_id = project_id  # type: long
        self.range_context = range_context  # type: str
        self.side = side  # type: str
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(CreateMergeRequestCommentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.is_draft is not None:
            result['IsDraft'] = self.is_draft
        if self.line is not None:
            result['Line'] = self.line
        if self.note is not None:
            result['Note'] = self.note
        if self.out_dated is not None:
            result['OutDated'] = self.out_dated
        if self.parent_note_id is not None:
            result['ParentNoteId'] = self.parent_note_id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.range_context is not None:
            result['RangeContext'] = self.range_context
        if self.side is not None:
            result['Side'] = self.side
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            temp_model = CreateMergeRequestCommentResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDraft') is not None:
            self.is_draft = m.get('IsDraft')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OutDated') is not None:
            self.out_dated = m.get('OutDated')
        if m.get('ParentNoteId') is not None:
            self.parent_note_id = m.get('ParentNoteId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RangeContext') is not None:
            self.range_context = m.get('RangeContext')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class CreateMergeRequestCommentResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateMergeRequestCommentResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateMergeRequestCommentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateMergeRequestCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMergeRequestCommentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMergeRequestCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMergeRequestCommentResponse, self).to_map()
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
            temp_model = CreateMergeRequestCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(self, access_token=None, create_parent_path=None, organization_id=None, sub_user_id=None,
                 sync=None, avatar_url=None, description=None, gitignore_type=None, import_account=None,
                 import_demo_project=None, import_repo_type=None, import_token=None, import_token_encrypted=None, import_url=None,
                 init_standard_service=None, is_crypto_enabled=None, local_import_url=None, name=None, namespace_id=None, path=None,
                 readme_type=None, visibility_level=None):
        self.access_token = access_token  # type: str
        self.create_parent_path = create_parent_path  # type: bool
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str
        self.sync = sync  # type: bool
        self.avatar_url = avatar_url  # type: str
        self.description = description  # type: str
        self.gitignore_type = gitignore_type  # type: str
        self.import_account = import_account  # type: str
        self.import_demo_project = import_demo_project  # type: bool
        self.import_repo_type = import_repo_type  # type: str
        self.import_token = import_token  # type: str
        self.import_token_encrypted = import_token_encrypted  # type: str
        self.import_url = import_url  # type: str
        self.init_standard_service = init_standard_service  # type: bool
        self.is_crypto_enabled = is_crypto_enabled  # type: bool
        self.local_import_url = local_import_url  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: long
        self.path = path  # type: str
        self.readme_type = readme_type  # type: str
        self.visibility_level = visibility_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.create_parent_path is not None:
            result['CreateParentPath'] = self.create_parent_path
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.description is not None:
            result['description'] = self.description
        if self.gitignore_type is not None:
            result['gitignoreType'] = self.gitignore_type
        if self.import_account is not None:
            result['importAccount'] = self.import_account
        if self.import_demo_project is not None:
            result['importDemoProject'] = self.import_demo_project
        if self.import_repo_type is not None:
            result['importRepoType'] = self.import_repo_type
        if self.import_token is not None:
            result['importToken'] = self.import_token
        if self.import_token_encrypted is not None:
            result['importTokenEncrypted'] = self.import_token_encrypted
        if self.import_url is not None:
            result['importUrl'] = self.import_url
        if self.init_standard_service is not None:
            result['initStandardService'] = self.init_standard_service
        if self.is_crypto_enabled is not None:
            result['isCryptoEnabled'] = self.is_crypto_enabled
        if self.local_import_url is not None:
            result['localImportUrl'] = self.local_import_url
        if self.name is not None:
            result['name'] = self.name
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id
        if self.path is not None:
            result['path'] = self.path
        if self.readme_type is not None:
            result['readmeType'] = self.readme_type
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CreateParentPath') is not None:
            self.create_parent_path = m.get('CreateParentPath')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gitignoreType') is not None:
            self.gitignore_type = m.get('gitignoreType')
        if m.get('importAccount') is not None:
            self.import_account = m.get('importAccount')
        if m.get('importDemoProject') is not None:
            self.import_demo_project = m.get('importDemoProject')
        if m.get('importRepoType') is not None:
            self.import_repo_type = m.get('importRepoType')
        if m.get('importToken') is not None:
            self.import_token = m.get('importToken')
        if m.get('importTokenEncrypted') is not None:
            self.import_token_encrypted = m.get('importTokenEncrypted')
        if m.get('importUrl') is not None:
            self.import_url = m.get('importUrl')
        if m.get('initStandardService') is not None:
            self.init_standard_service = m.get('initStandardService')
        if m.get('isCryptoEnabled') is not None:
            self.is_crypto_enabled = m.get('isCryptoEnabled')
        if m.get('localImportUrl') is not None:
            self.local_import_url = m.get('localImportUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('readmeType') is not None:
            self.readme_type = m.get('readmeType')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        return self


class CreateRepositoryResponseBodyResultNamespace(TeaModel):
    def __init__(self, avatar=None, created_at=None, description=None, id=None, name=None, owner_id=None, path=None,
                 public=None, state=None, updated_at=None, visibility_level=None):
        self.avatar = avatar  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.path = path  # type: str
        self.public = public  # type: bool
        self.state = state  # type: str
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryResponseBodyResultNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.public is not None:
            result['Public'] = self.public
        if self.state is not None:
            result['State'] = self.state
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        return self


class CreateRepositoryResponseBodyResult(TeaModel):
    def __init__(self, archive=None, avatar_url=None, builds_enable_status=None, created_at=None, creator_id=None,
                 default_branch=None, demo_project_status=None, description=None, http_url_to_repo=None, id=None,
                 issues_enable_status=None, last_activity_at=None, merge_request_enable_status=None, name=None,
                 name_with_namespace=None, namespace=None, path=None, path_with_namespace=None, public=None,
                 snippets_enable_status=None, ssh_url_to_repo=None, tag_list=None, visibility_level=None, web_url=None,
                 wiki_enable_status=None):
        self.archive = archive  # type: bool
        self.avatar_url = avatar_url  # type: str
        self.builds_enable_status = builds_enable_status  # type: bool
        self.created_at = created_at  # type: str
        self.creator_id = creator_id  # type: long
        self.default_branch = default_branch  # type: str
        self.demo_project_status = demo_project_status  # type: bool
        self.description = description  # type: str
        self.http_url_to_repo = http_url_to_repo  # type: str
        self.id = id  # type: long
        self.issues_enable_status = issues_enable_status  # type: bool
        self.last_activity_at = last_activity_at  # type: str
        self.merge_request_enable_status = merge_request_enable_status  # type: bool
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.namespace = namespace  # type: CreateRepositoryResponseBodyResultNamespace
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.public = public  # type: bool
        self.snippets_enable_status = snippets_enable_status  # type: bool
        self.ssh_url_to_repo = ssh_url_to_repo  # type: str
        self.tag_list = tag_list  # type: list[str]
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str
        self.wiki_enable_status = wiki_enable_status  # type: bool

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.builds_enable_status is not None:
            result['BuildsEnableStatus'] = self.builds_enable_status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.description is not None:
            result['Description'] = self.description
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.id is not None:
            result['Id'] = self.id
        if self.issues_enable_status is not None:
            result['IssuesEnableStatus'] = self.issues_enable_status
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.merge_request_enable_status is not None:
            result['MergeRequestEnableStatus'] = self.merge_request_enable_status
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.public is not None:
            result['Public'] = self.public
        if self.snippets_enable_status is not None:
            result['SnippetsEnableStatus'] = self.snippets_enable_status
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.wiki_enable_status is not None:
            result['WikiEnableStatus'] = self.wiki_enable_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('BuildsEnableStatus') is not None:
            self.builds_enable_status = m.get('BuildsEnableStatus')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IssuesEnableStatus') is not None:
            self.issues_enable_status = m.get('IssuesEnableStatus')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('MergeRequestEnableStatus') is not None:
            self.merge_request_enable_status = m.get('MergeRequestEnableStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Namespace') is not None:
            temp_model = CreateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('SnippetsEnableStatus') is not None:
            self.snippets_enable_status = m.get('SnippetsEnableStatus')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('WikiEnableStatus') is not None:
            self.wiki_enable_status = m.get('WikiEnableStatus')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRepositoryResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponse, self).to_map()
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryDeployKeyRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryDeployKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateRepositoryDeployKeyResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, finger_print=None, id=None, key=None, title=None):
        self.created_at = created_at  # type: str
        self.finger_print = finger_print  # type: str
        self.id = id  # type: long
        self.key = key  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryDeployKeyResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        if self.id is not None:
            result['Id'] = self.id
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateRepositoryDeployKeyResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRepositoryDeployKeyResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRepositoryDeployKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryDeployKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRepositoryDeployKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepositoryDeployKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepositoryDeployKeyResponse, self).to_map()
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
            temp_model = CreateRepositoryDeployKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryGroupRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateRepositoryGroupResponseBodyResult(TeaModel):
    def __init__(self, avatar_url=None, description=None, id=None, name=None, name_with_namespace=None,
                 owner_id=None, parent_id=None, path=None, path_with_namespace=None, type=None, visibility_level=None,
                 web_url=None):
        self.avatar_url = avatar_url  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_id = parent_id  # type: long
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.type = type  # type: str
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class CreateRepositoryGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRepositoryGroupResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRepositoryGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRepositoryGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepositoryGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepositoryGroupResponse, self).to_map()
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
            temp_model = CreateRepositoryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryProtectedBranchRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting(TeaModel):
    def __init__(self, allow_merge_request_roles=None, allow_self_approval=None, default_assignees=None,
                 is_require_discussion_processed=None, is_reset_approval_when_new_push=None, merge_request_mode=None, minimual_approval=None,
                 required=None):
        self.allow_merge_request_roles = allow_merge_request_roles  # type: list[int]
        self.allow_self_approval = allow_self_approval  # type: bool
        self.default_assignees = default_assignees  # type: list[str]
        self.is_require_discussion_processed = is_require_discussion_processed  # type: bool
        self.is_reset_approval_when_new_push = is_reset_approval_when_new_push  # type: bool
        self.merge_request_mode = merge_request_mode  # type: str
        self.minimual_approval = minimual_approval  # type: int
        self.required = required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_merge_request_roles is not None:
            result['AllowMergeRequestRoles'] = self.allow_merge_request_roles
        if self.allow_self_approval is not None:
            result['AllowSelfApproval'] = self.allow_self_approval
        if self.default_assignees is not None:
            result['DefaultAssignees'] = self.default_assignees
        if self.is_require_discussion_processed is not None:
            result['IsRequireDiscussionProcessed'] = self.is_require_discussion_processed
        if self.is_reset_approval_when_new_push is not None:
            result['IsResetApprovalWhenNewPush'] = self.is_reset_approval_when_new_push
        if self.merge_request_mode is not None:
            result['MergeRequestMode'] = self.merge_request_mode
        if self.minimual_approval is not None:
            result['MinimualApproval'] = self.minimual_approval
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowMergeRequestRoles') is not None:
            self.allow_merge_request_roles = m.get('AllowMergeRequestRoles')
        if m.get('AllowSelfApproval') is not None:
            self.allow_self_approval = m.get('AllowSelfApproval')
        if m.get('DefaultAssignees') is not None:
            self.default_assignees = m.get('DefaultAssignees')
        if m.get('IsRequireDiscussionProcessed') is not None:
            self.is_require_discussion_processed = m.get('IsRequireDiscussionProcessed')
        if m.get('IsResetApprovalWhenNewPush') is not None:
            self.is_reset_approval_when_new_push = m.get('IsResetApprovalWhenNewPush')
        if m.get('MergeRequestMode') is not None:
            self.merge_request_mode = m.get('MergeRequestMode')
        if m.get('MinimualApproval') is not None:
            self.minimual_approval = m.get('MinimualApproval')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig(TeaModel):
    def __init__(self, check_items=None):
        self.check_items = check_items  # type: list[CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems]

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems()
                self.check_items.append(temp_model.from_map(k))
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection(TeaModel):
    def __init__(self, enabled=None, message=None):
        self.enabled = enabled  # type: bool
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection(TeaModel):
    def __init__(self, enabled=None, message=None):
        self.enabled = enabled  # type: bool
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSetting(TeaModel):
    def __init__(self, check_config=None, coding_guidelines_detection=None, required=None,
                 sensitive_info_detection=None):
        self.check_config = check_config  # type: CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig
        self.coding_guidelines_detection = coding_guidelines_detection  # type: CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection
        self.required = required  # type: bool
        self.sensitive_info_detection = sensitive_info_detection  # type: CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection

    def validate(self):
        if self.check_config:
            self.check_config.validate()
        if self.coding_guidelines_detection:
            self.coding_guidelines_detection.validate()
        if self.sensitive_info_detection:
            self.sensitive_info_detection.validate()

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResultTestSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_config is not None:
            result['CheckConfig'] = self.check_config.to_map()
        if self.coding_guidelines_detection is not None:
            result['CodingGuidelinesDetection'] = self.coding_guidelines_detection.to_map()
        if self.required is not None:
            result['Required'] = self.required
        if self.sensitive_info_detection is not None:
            result['SensitiveInfoDetection'] = self.sensitive_info_detection.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckConfig') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig()
            self.check_config = temp_model.from_map(m['CheckConfig'])
        if m.get('CodingGuidelinesDetection') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection()
            self.coding_guidelines_detection = temp_model.from_map(m['CodingGuidelinesDetection'])
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('SensitiveInfoDetection') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection()
            self.sensitive_info_detection = temp_model.from_map(m['SensitiveInfoDetection'])
        return self


class CreateRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(self, allow_merge_roles=None, allow_push_roles=None, branch=None, id=None,
                 merge_request_setting=None, test_setting=None):
        self.allow_merge_roles = allow_merge_roles  # type: list[int]
        self.allow_push_roles = allow_push_roles  # type: list[int]
        self.branch = branch  # type: str
        self.id = id  # type: long
        self.merge_request_setting = merge_request_setting  # type: CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting
        self.test_setting = test_setting  # type: CreateRepositoryProtectedBranchResponseBodyResultTestSetting

    def validate(self):
        if self.merge_request_setting:
            self.merge_request_setting.validate()
        if self.test_setting:
            self.test_setting.validate()

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_merge_roles is not None:
            result['AllowMergeRoles'] = self.allow_merge_roles
        if self.allow_push_roles is not None:
            result['AllowPushRoles'] = self.allow_push_roles
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_request_setting is not None:
            result['MergeRequestSetting'] = self.merge_request_setting.to_map()
        if self.test_setting is not None:
            result['TestSetting'] = self.test_setting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowMergeRoles') is not None:
            self.allow_merge_roles = m.get('AllowMergeRoles')
        if m.get('AllowPushRoles') is not None:
            self.allow_push_roles = m.get('AllowPushRoles')
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeRequestSetting') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting()
            self.merge_request_setting = temp_model.from_map(m['MergeRequestSetting'])
        if m.get('TestSetting') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSetting()
            self.test_setting = temp_model.from_map(m['TestSetting'])
        return self


class CreateRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRepositoryProtectedBranchResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRepositoryProtectedBranchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepositoryProtectedBranchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepositoryProtectedBranchResponse, self).to_map()
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
            temp_model = CreateRepositoryProtectedBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSshKeyRequest(TeaModel):
    def __init__(self, access_token=None):
        self.access_token = access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSshKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class CreateSshKeyResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, finger_print=None, id=None, key=None, key_scope=None, title=None):
        self.created_at = created_at  # type: str
        self.finger_print = finger_print  # type: str
        self.id = id  # type: long
        self.key = key  # type: str
        self.key_scope = key_scope  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSshKeyResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        if self.id is not None:
            result['Id'] = self.id
        if self.key is not None:
            result['Key'] = self.key
        if self.key_scope is not None:
            result['KeyScope'] = self.key_scope
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyScope') is not None:
            self.key_scope = m.get('KeyScope')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateSshKeyResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateSshKeyResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateSshKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateSshKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSshKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSshKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSshKeyResponse, self).to_map()
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
            temp_model = CreateSshKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateTagResponseBodyResultCommitInfo(TeaModel):
    def __init__(self, author_email=None, author_name=None, authored_date=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 title=None):
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.authored_date = authored_date  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResponseBodyResultCommitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateTagResponseBodyResultRelease(TeaModel):
    def __init__(self, description=None, tag_name=None):
        self.description = description  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResponseBodyResultRelease, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class CreateTagResponseBodyResult(TeaModel):
    def __init__(self, commit_info=None, message=None, name=None, release=None):
        self.commit_info = commit_info  # type: CreateTagResponseBodyResultCommitInfo
        self.message = message  # type: str
        self.name = name  # type: str
        self.release = release  # type: CreateTagResponseBodyResultRelease

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()
        if self.release:
            self.release.validate()

    def to_map(self):
        _map = super(CreateTagResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.release is not None:
            result['Release'] = self.release.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitInfo') is not None:
            temp_model = CreateTagResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Release') is not None:
            temp_model = CreateTagResponseBodyResultRelease()
            self.release = temp_model.from_map(m['Release'])
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateTagResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagResponse, self).to_map()
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBranchRequest(TeaModel):
    def __init__(self, access_token=None, branch_name=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.branch_name = branch_name  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBranchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteBranchResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None):
        self.branch_name = branch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBranchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class DeleteBranchResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteBranchResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteBranchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBranchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBranchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBranchResponse, self).to_map()
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
            temp_model = DeleteBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, access_token=None, branch_name=None, commit_message=None, file_path=None,
                 organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.branch_name = branch_name  # type: str
        self.commit_message = commit_message  # type: str
        self.file_path = file_path  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_message is not None:
            result['CommitMessage'] = self.commit_message
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitMessage') is not None:
            self.commit_message = m.get('CommitMessage')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteFileResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, file_path=None):
        self.branch_name = branch_name  # type: str
        self.file_path = file_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteFileResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileResponse, self).to_map()
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteGroupMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DeleteGroupMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteGroupMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteGroupMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupMemberResponse, self).to_map()
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
            temp_model = DeleteGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryResponse, self).to_map()
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
            temp_model = DeleteRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryGroupRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryGroupResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryGroupResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryGroupResponse, self).to_map()
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
            temp_model = DeleteRepositoryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, created_at=None, id=None, message=None, notification_level=None,
                 source_id=None, source_type=None, updated_at=None, user_id=None):
        self.access_level = access_level  # type: int
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.message = message  # type: str
        self.notification_level = notification_level  # type: int
        self.source_id = source_id  # type: long
        self.source_type = source_type  # type: str
        self.updated_at = updated_at  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.notification_level is not None:
            result['NotificationLevel'] = self.notification_level
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotificationLevel') is not None:
            self.notification_level = m.get('NotificationLevel')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteRepositoryMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryMemberResponse, self).to_map()
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
            temp_model = DeleteRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryMemberWithExternUidRequest(TeaModel):
    def __init__(self, access_token=None, extern_user_id=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryMemberWithExternUidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryMemberWithExternUidResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, created_at=None, id=None, source_id=None, source_type=None,
                 updated_at=None, user_id=None):
        self.access_level = access_level  # type: int
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.source_id = source_id  # type: long
        self.source_type = source_type  # type: str
        self.updated_at = updated_at  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryMemberWithExternUidResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteRepositoryMemberWithExternUidResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryMemberWithExternUidResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryMemberWithExternUidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryMemberWithExternUidResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryMemberWithExternUidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryMemberWithExternUidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryMemberWithExternUidResponse, self).to_map()
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
            temp_model = DeleteRepositoryMemberWithExternUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryProtectedBranchRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryProtectedBranchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryProtectedBranchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryProtectedBranchResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryProtectedBranchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryProtectedBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryProtectedBranchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryProtectedBranchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryProtectedBranchResponse, self).to_map()
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
            temp_model = DeleteRepositoryProtectedBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryTagRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryTagResponseBodyResult(TeaModel):
    def __init__(self, tag_name=None):
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryTagResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryTagResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryTagResponse, self).to_map()
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
            temp_model = DeleteRepositoryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryTagV2Request(TeaModel):
    def __init__(self, access_token=None, organization_id=None, tag_name=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryTagV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagV2ResponseBodyResult(TeaModel):
    def __init__(self, tag_name=None):
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryTagV2ResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagV2ResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryTagV2ResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryTagV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryTagV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryTagV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryTagV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryTagV2Response, self).to_map()
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
            temp_model = DeleteRepositoryTagV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryWebhookRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryWebhookResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, description=None, enable_ssl_verification=None, id=None,
                 last_test_result=None, merge_requests_events=None, note_events=None, project_id=None, push_events=None,
                 secret_token=None, tag_push_events=None, url=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        self.id = id  # type: long
        self.last_test_result = last_test_result  # type: str
        self.merge_requests_events = merge_requests_events  # type: bool
        self.note_events = note_events  # type: bool
        self.project_id = project_id  # type: long
        self.push_events = push_events  # type: bool
        self.secret_token = secret_token  # type: str
        self.tag_push_events = tag_push_events  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryWebhookResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['Id'] = self.id
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DeleteRepositoryWebhookResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRepositoryWebhookResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRepositoryWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryWebhookResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRepositoryWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepositoryWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepositoryWebhookResponse, self).to_map()
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
            temp_model = DeleteRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRepositoryDeployKeyRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRepositoryDeployKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class EnableRepositoryDeployKeyResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRepositoryDeployKeyResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class EnableRepositoryDeployKeyResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: EnableRepositoryDeployKeyResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EnableRepositoryDeployKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EnableRepositoryDeployKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableRepositoryDeployKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableRepositoryDeployKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableRepositoryDeployKeyResponse, self).to_map()
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
            temp_model = EnableRepositoryDeployKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBranchInfoRequest(TeaModel):
    def __init__(self, access_token=None, branch_name=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.branch_name = branch_name  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBranchInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetBranchInfoResponseBodyResultCommitInfo(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBranchInfoResponseBodyResultCommitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetBranchInfoResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, commit_info=None, protected_branch=None):
        self.branch_name = branch_name  # type: str
        self.commit_info = commit_info  # type: GetBranchInfoResponseBodyResultCommitInfo
        self.protected_branch = protected_branch  # type: bool

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super(GetBranchInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = GetBranchInfoResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        return self


class GetBranchInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetBranchInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetBranchInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetBranchInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBranchInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBranchInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBranchInfoResponse, self).to_map()
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
            temp_model = GetBranchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeCompletionRequest(TeaModel):
    def __init__(self, fetch_keys=None, is_encrypted=None):
        self.fetch_keys = fetch_keys  # type: str
        self.is_encrypted = is_encrypted  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeCompletionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_keys is not None:
            result['FetchKeys'] = self.fetch_keys
        if self.is_encrypted is not None:
            result['IsEncrypted'] = self.is_encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchKeys') is not None:
            self.fetch_keys = m.get('FetchKeys')
        if m.get('IsEncrypted') is not None:
            self.is_encrypted = m.get('IsEncrypted')
        return self


class GetCodeCompletionResponseBodyResult(TeaModel):
    def __init__(self, body=None, client_timestamp=None, fetch_timestamp=None, invoke_timestamp=None,
                 receive_timestamp=None, rsp_timestamp=None):
        self.body = body  # type: str
        self.client_timestamp = client_timestamp  # type: str
        self.fetch_timestamp = fetch_timestamp  # type: str
        self.invoke_timestamp = invoke_timestamp  # type: str
        self.receive_timestamp = receive_timestamp  # type: str
        self.rsp_timestamp = rsp_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeCompletionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.client_timestamp is not None:
            result['ClientTimestamp'] = self.client_timestamp
        if self.fetch_timestamp is not None:
            result['FetchTimestamp'] = self.fetch_timestamp
        if self.invoke_timestamp is not None:
            result['InvokeTimestamp'] = self.invoke_timestamp
        if self.receive_timestamp is not None:
            result['ReceiveTimestamp'] = self.receive_timestamp
        if self.rsp_timestamp is not None:
            result['RspTimestamp'] = self.rsp_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ClientTimestamp') is not None:
            self.client_timestamp = m.get('ClientTimestamp')
        if m.get('FetchTimestamp') is not None:
            self.fetch_timestamp = m.get('FetchTimestamp')
        if m.get('InvokeTimestamp') is not None:
            self.invoke_timestamp = m.get('InvokeTimestamp')
        if m.get('ReceiveTimestamp') is not None:
            self.receive_timestamp = m.get('ReceiveTimestamp')
        if m.get('RspTimestamp') is not None:
            self.rsp_timestamp = m.get('RspTimestamp')
        return self


class GetCodeCompletionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetCodeCompletionResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCodeCompletionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCodeCompletionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCodeCompletionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCodeCompletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCodeCompletionResponse, self).to_map()
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
            temp_model = GetCodeCompletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeupOrganizationRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeupOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetCodeupOrganizationResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, id=None, namespace_id=None, organization_id=None, path=None, updated_at=None,
                 user_role=None):
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.namespace_id = namespace_id  # type: long
        self.organization_id = organization_id  # type: str
        self.path = path  # type: str
        self.updated_at = updated_at  # type: str
        self.user_role = user_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeupOrganizationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        return self


class GetCodeupOrganizationResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetCodeupOrganizationResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCodeupOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCodeupOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCodeupOrganizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCodeupOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCodeupOrganizationResponse, self).to_map()
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
            temp_model = GetCodeupOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileBlobsRequest(TeaModel):
    def __init__(self, access_token=None, file_path=None, from_=None, organization_id=None, ref=None,
                 sub_user_id=None, to=None):
        self.access_token = access_token  # type: str
        self.file_path = file_path  # type: str
        self.from_ = from_  # type: long
        self.organization_id = organization_id  # type: str
        self.ref = ref  # type: str
        self.sub_user_id = sub_user_id  # type: str
        self.to = to  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileBlobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.from_ is not None:
            result['From'] = self.from_
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.ref is not None:
            result['Ref'] = self.ref
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Ref') is not None:
            self.ref = m.get('Ref')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetFileBlobsResponseBodyResult(TeaModel):
    def __init__(self, content=None, total_lines=None):
        self.content = content  # type: str
        self.total_lines = total_lines  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileBlobsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.total_lines is not None:
            result['TotalLines'] = self.total_lines
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TotalLines') is not None:
            self.total_lines = m.get('TotalLines')
        return self


class GetFileBlobsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFileBlobsResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFileBlobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFileBlobsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileBlobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileBlobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileBlobsResponse, self).to_map()
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
            temp_model = GetFileBlobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileLastCommitRequest(TeaModel):
    def __init__(self, access_token=None, file_path=None, organization_id=None, sha=None):
        self.access_token = access_token  # type: str
        self.file_path = file_path  # type: str
        self.organization_id = organization_id  # type: str
        self.sha = sha  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileLastCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sha is not None:
            result['Sha'] = self.sha
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Sha') is not None:
            self.sha = m.get('Sha')
        return self


class GetFileLastCommitResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileLastCommitResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetFileLastCommitResponseBodyResult(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: GetFileLastCommitResponseBodyResultSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = GetFileLastCommitResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetFileLastCommitResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFileLastCommitResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFileLastCommitResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileLastCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileLastCommitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponse, self).to_map()
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
            temp_model = GetFileLastCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupDetailRequest(TeaModel):
    def __init__(self, access_token=None, group_id=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.group_id = group_id  # type: long
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetGroupDetailResponseBodyResult(TeaModel):
    def __init__(self, avatar_url=None, description=None, id=None, name=None, name_with_namespace=None,
                 owner_id=None, parent_id=None, path=None, path_with_namespace=None, type=None, visibility_level=None,
                 web_url=None):
        self.avatar_url = avatar_url  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_id = parent_id  # type: long
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.type = type  # type: str
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class GetGroupDetailResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetGroupDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetGroupDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupDetailResponse, self).to_map()
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
            temp_model = GetGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestApproveStatusRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestApproveStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetMergeRequestApproveStatusResponseBodyResult(TeaModel):
    def __init__(self, approve_status=None, message=None):
        self.approve_status = approve_status  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestApproveStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_status is not None:
            result['ApproveStatus'] = self.approve_status
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApproveStatus') is not None:
            self.approve_status = m.get('ApproveStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetMergeRequestApproveStatusResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetMergeRequestApproveStatusResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMergeRequestApproveStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestApproveStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMergeRequestApproveStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMergeRequestApproveStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMergeRequestApproveStatusResponse, self).to_map()
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
            temp_model = GetMergeRequestApproveStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestDetailRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class GetMergeRequestDetailResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, email=None, extern_user_id=None, id=None, name=None, status=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetMergeRequestDetailResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetMergeRequestDetailResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 is_support_merge=None, merge_error=None, merge_status=None, merge_type=None, merged_revision=None,
                 name_with_namespace=None, project_id=None, source_branch=None, state=None, target_branch=None, title=None,
                 updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: GetMergeRequestDetailResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[GetMergeRequestDetailResponseBodyResultAssigneeList]
        self.author = author  # type: GetMergeRequestDetailResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.is_support_merge = is_support_merge  # type: bool
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_support_merge is not None:
            result['IsSupportMerge'] = self.is_support_merge
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = GetMergeRequestDetailResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsSupportMerge') is not None:
            self.is_support_merge = m.get('IsSupportMerge')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class GetMergeRequestDetailResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetMergeRequestDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMergeRequestDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMergeRequestDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMergeRequestDetailResponse, self).to_map()
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
            temp_model = GetMergeRequestDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestSettingRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetMergeRequestSettingResponseBodyResult(TeaModel):
    def __init__(self, is_enable_smart_code_review=None, merge_types=None):
        self.is_enable_smart_code_review = is_enable_smart_code_review  # type: bool
        self.merge_types = merge_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMergeRequestSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enable_smart_code_review is not None:
            result['IsEnableSmartCodeReview'] = self.is_enable_smart_code_review
        if self.merge_types is not None:
            result['MergeTypes'] = self.merge_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsEnableSmartCodeReview') is not None:
            self.is_enable_smart_code_review = m.get('IsEnableSmartCodeReview')
        if m.get('MergeTypes') is not None:
            self.merge_types = m.get('MergeTypes')
        return self


class GetMergeRequestSettingResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetMergeRequestSettingResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetMergeRequestSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMergeRequestSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMergeRequestSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMergeRequestSettingResponse, self).to_map()
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
            temp_model = GetMergeRequestSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationRepositorySettingRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList(TeaModel):
    def __init__(self, allowed=None, permission_code=None):
        self.allowed = allowed  # type: bool
        self.permission_code = permission_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed is not None:
            result['Allowed'] = self.allowed
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Allowed') is not None:
            self.allowed = m.get('Allowed')
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        return self


class GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList(TeaModel):
    def __init__(self, allowed=None, role_code=None):
        self.allowed = allowed  # type: bool
        self.role_code = role_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed is not None:
            result['Allowed'] = self.allowed
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Allowed') is not None:
            self.allowed = m.get('Allowed')
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        return self


class GetOrganizationRepositorySettingResponseBodyResult(TeaModel):
    def __init__(self, force_push_forbidden=None, group_required=None, open_clone_download_control=None,
                 org_clone_download_method_list=None, org_clone_download_role_list=None, repo_admin_access_visibility_level=None,
                 repo_admin_operation=None, repo_creator_identity=None, repo_visibility_level=None):
        self.force_push_forbidden = force_push_forbidden  # type: bool
        self.group_required = group_required  # type: bool
        self.open_clone_download_control = open_clone_download_control  # type: bool
        self.org_clone_download_method_list = org_clone_download_method_list  # type: list[GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList]
        self.org_clone_download_role_list = org_clone_download_role_list  # type: list[GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList]
        self.repo_admin_access_visibility_level = repo_admin_access_visibility_level  # type: list[long]
        self.repo_admin_operation = repo_admin_operation  # type: list[long]
        self.repo_creator_identity = repo_creator_identity  # type: list[long]
        self.repo_visibility_level = repo_visibility_level  # type: list[long]

    def validate(self):
        if self.org_clone_download_method_list:
            for k in self.org_clone_download_method_list:
                if k:
                    k.validate()
        if self.org_clone_download_role_list:
            for k in self.org_clone_download_role_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_push_forbidden is not None:
            result['ForcePushForbidden'] = self.force_push_forbidden
        if self.group_required is not None:
            result['GroupRequired'] = self.group_required
        if self.open_clone_download_control is not None:
            result['OpenCloneDownloadControl'] = self.open_clone_download_control
        result['OrgCloneDownloadMethodList'] = []
        if self.org_clone_download_method_list is not None:
            for k in self.org_clone_download_method_list:
                result['OrgCloneDownloadMethodList'].append(k.to_map() if k else None)
        result['OrgCloneDownloadRoleList'] = []
        if self.org_clone_download_role_list is not None:
            for k in self.org_clone_download_role_list:
                result['OrgCloneDownloadRoleList'].append(k.to_map() if k else None)
        if self.repo_admin_access_visibility_level is not None:
            result['RepoAdminAccessVisibilityLevel'] = self.repo_admin_access_visibility_level
        if self.repo_admin_operation is not None:
            result['RepoAdminOperation'] = self.repo_admin_operation
        if self.repo_creator_identity is not None:
            result['RepoCreatorIdentity'] = self.repo_creator_identity
        if self.repo_visibility_level is not None:
            result['RepoVisibilityLevel'] = self.repo_visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForcePushForbidden') is not None:
            self.force_push_forbidden = m.get('ForcePushForbidden')
        if m.get('GroupRequired') is not None:
            self.group_required = m.get('GroupRequired')
        if m.get('OpenCloneDownloadControl') is not None:
            self.open_clone_download_control = m.get('OpenCloneDownloadControl')
        self.org_clone_download_method_list = []
        if m.get('OrgCloneDownloadMethodList') is not None:
            for k in m.get('OrgCloneDownloadMethodList'):
                temp_model = GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList()
                self.org_clone_download_method_list.append(temp_model.from_map(k))
        self.org_clone_download_role_list = []
        if m.get('OrgCloneDownloadRoleList') is not None:
            for k in m.get('OrgCloneDownloadRoleList'):
                temp_model = GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList()
                self.org_clone_download_role_list.append(temp_model.from_map(k))
        if m.get('RepoAdminAccessVisibilityLevel') is not None:
            self.repo_admin_access_visibility_level = m.get('RepoAdminAccessVisibilityLevel')
        if m.get('RepoAdminOperation') is not None:
            self.repo_admin_operation = m.get('RepoAdminOperation')
        if m.get('RepoCreatorIdentity') is not None:
            self.repo_creator_identity = m.get('RepoCreatorIdentity')
        if m.get('RepoVisibilityLevel') is not None:
            self.repo_visibility_level = m.get('RepoVisibilityLevel')
        return self


class GetOrganizationRepositorySettingResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetOrganizationRepositorySettingResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetOrganizationRepositorySettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrganizationRepositorySettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrganizationRepositorySettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrganizationRepositorySettingResponse, self).to_map()
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
            temp_model = GetOrganizationRepositorySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationSecurityCenterStatusRequest(TeaModel):
    def __init__(self, access_token=None):
        self.access_token = access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationSecurityCenterStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class GetOrganizationSecurityCenterStatusResponseBodyResult(TeaModel):
    def __init__(self, enable=None):
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationSecurityCenterStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class GetOrganizationSecurityCenterStatusResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetOrganizationSecurityCenterStatusResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetOrganizationSecurityCenterStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetOrganizationSecurityCenterStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrganizationSecurityCenterStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrganizationSecurityCenterStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrganizationSecurityCenterStatusResponse, self).to_map()
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
            temp_model = GetOrganizationSecurityCenterStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetProjectMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetProjectMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetProjectMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetProjectMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetProjectMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectMemberResponse, self).to_map()
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
            temp_model = GetProjectMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryCommitRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetRepositoryCommitResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryCommitResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryCommitResponseBodyResult(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: GetRepositoryCommitResponseBodyResultSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetRepositoryCommitResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryCommitResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetRepositoryCommitResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRepositoryCommitResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRepositoryCommitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRepositoryCommitResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRepositoryCommitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepositoryCommitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryCommitResponse, self).to_map()
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
            temp_model = GetRepositoryCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryInfoRequest(TeaModel):
    def __init__(self, access_token=None, identity=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.identity = identity  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetRepositoryInfoResponseBodyResultNamespace(TeaModel):
    def __init__(self, avatar=None, created_at=None, description=None, id=None, name=None, owner_id=None, path=None,
                 public=None, state=None, updated_at=None, visibility_level=None):
        self.avatar = avatar  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.path = path  # type: str
        self.public = public  # type: bool
        self.state = state  # type: str
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBodyResultNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.public is not None:
            result['Public'] = self.public
        if self.state is not None:
            result['State'] = self.state
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        return self


class GetRepositoryInfoResponseBodyResultPermissionsGroupAccess(TeaModel):
    def __init__(self, access_level=None):
        self.access_level = access_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBodyResultPermissionsGroupAccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        return self


class GetRepositoryInfoResponseBodyResultPermissionsProjectAccess(TeaModel):
    def __init__(self, access_level=None):
        self.access_level = access_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBodyResultPermissionsProjectAccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        return self


class GetRepositoryInfoResponseBodyResultPermissions(TeaModel):
    def __init__(self, group_access=None, project_access=None):
        self.group_access = group_access  # type: GetRepositoryInfoResponseBodyResultPermissionsGroupAccess
        self.project_access = project_access  # type: GetRepositoryInfoResponseBodyResultPermissionsProjectAccess

    def validate(self):
        if self.group_access:
            self.group_access.validate()
        if self.project_access:
            self.project_access.validate()

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBodyResultPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_access is not None:
            result['GroupAccess'] = self.group_access.to_map()
        if self.project_access is not None:
            result['ProjectAccess'] = self.project_access.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupAccess') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissionsGroupAccess()
            self.group_access = temp_model.from_map(m['GroupAccess'])
        if m.get('ProjectAccess') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissionsProjectAccess()
            self.project_access = temp_model.from_map(m['ProjectAccess'])
        return self


class GetRepositoryInfoResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, archive=None, avatar_url=None, created_at=None, creator_id=None,
                 default_branch=None, demo_project_status=None, description=None, http_url_to_repo=None, id=None,
                 import_from_subversion=None, import_status=None, import_url=None, last_activity_at=None, name=None,
                 name_with_namespace=None, namespace=None, path=None, path_with_namespace=None, permissions=None, public=None,
                 ssh_url_to_repo=None, tag_list=None, visibility_level=None, web_url=None):
        self.access_level = access_level  # type: int
        self.archive = archive  # type: bool
        self.avatar_url = avatar_url  # type: str
        self.created_at = created_at  # type: str
        self.creator_id = creator_id  # type: long
        self.default_branch = default_branch  # type: str
        self.demo_project_status = demo_project_status  # type: bool
        self.description = description  # type: str
        self.http_url_to_repo = http_url_to_repo  # type: str
        self.id = id  # type: long
        self.import_from_subversion = import_from_subversion  # type: bool
        self.import_status = import_status  # type: str
        self.import_url = import_url  # type: str
        self.last_activity_at = last_activity_at  # type: str
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.namespace = namespace  # type: GetRepositoryInfoResponseBodyResultNamespace
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.permissions = permissions  # type: GetRepositoryInfoResponseBodyResultPermissions
        self.public = public  # type: bool
        self.ssh_url_to_repo = ssh_url_to_repo  # type: str
        self.tag_list = tag_list  # type: list[str]
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.namespace:
            self.namespace.validate()
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.description is not None:
            result['Description'] = self.description
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.id is not None:
            result['Id'] = self.id
        if self.import_from_subversion is not None:
            result['ImportFromSubversion'] = self.import_from_subversion
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.import_url is not None:
            result['ImportUrl'] = self.import_url
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        if self.public is not None:
            result['Public'] = self.public
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImportFromSubversion') is not None:
            self.import_from_subversion = m.get('ImportFromSubversion')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('ImportUrl') is not None:
            self.import_url = m.get('ImportUrl')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Namespace') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Permissions') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissions()
            self.permissions = temp_model.from_map(m['Permissions'])
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class GetRepositoryInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRepositoryInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRepositoryInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRepositoryInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRepositoryInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepositoryInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryInfoResponse, self).to_map()
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
            temp_model = GetRepositoryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryTagRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetRepositoryTagResponseBodyResultCommitSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagResponseBodyResultCommitSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagResponseBodyResultCommit(TeaModel):
    def __init__(self, author_email=None, author_name=None, authored_date=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.authored_date = authored_date  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: GetRepositoryTagResponseBodyResultCommitSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetRepositoryTagResponseBodyResultCommit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetRepositoryTagResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagResponseBodyResult(TeaModel):
    def __init__(self, commit=None, id=None, message=None, name=None, signature=None):
        self.commit = commit  # type: GetRepositoryTagResponseBodyResultCommit
        self.id = id  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.signature = signature  # type: GetRepositoryTagResponseBodyResultSignature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetRepositoryTagResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Commit') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRepositoryTagResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRepositoryTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRepositoryTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRepositoryTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepositoryTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryTagResponse, self).to_map()
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
            temp_model = GetRepositoryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryTagV2Request(TeaModel):
    def __init__(self, access_token=None, organization_id=None, tag_name=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetRepositoryTagV2ResponseBodyResultCommitSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagV2ResponseBodyResultCommitSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagV2ResponseBodyResultCommit(TeaModel):
    def __init__(self, author_email=None, author_name=None, authored_date=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.authored_date = authored_date  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: GetRepositoryTagV2ResponseBodyResultCommitSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetRepositoryTagV2ResponseBodyResultCommit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetRepositoryTagV2ResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryTagV2ResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagV2ResponseBodyResult(TeaModel):
    def __init__(self, commit=None, id=None, message=None, name=None, signature=None):
        self.commit = commit  # type: GetRepositoryTagV2ResponseBodyResultCommit
        self.id = id  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.signature = signature  # type: GetRepositoryTagV2ResponseBodyResultSignature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetRepositoryTagV2ResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Commit') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagV2ResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRepositoryTagV2ResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRepositoryTagV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRepositoryTagV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepositoryTagV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryTagV2Response, self).to_map()
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
            temp_model = GetRepositoryTagV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetUserInfoResponseBodyResult(TeaModel):
    def __init__(self, avatar_url=None, email=None, external_user_id=None, id=None, name=None, username=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.external_user_id = external_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetUserInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserInfoResponse, self).to_map()
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
            temp_model = GetUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsSlsUserAuthrizedCodeupRequest(TeaModel):
    def __init__(self, organization_id=None, aliyun_sub_user_id=None, aliyun_user_id=None, codeup_project_id=None,
                 sls_log_store=None, sls_project=None):
        self.organization_id = organization_id  # type: str
        self.aliyun_sub_user_id = aliyun_sub_user_id  # type: str
        self.aliyun_user_id = aliyun_user_id  # type: str
        self.codeup_project_id = codeup_project_id  # type: long
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsSlsUserAuthrizedCodeupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.aliyun_sub_user_id is not None:
            result['aliyunSubUserId'] = self.aliyun_sub_user_id
        if self.aliyun_user_id is not None:
            result['aliyunUserId'] = self.aliyun_user_id
        if self.codeup_project_id is not None:
            result['codeupProjectId'] = self.codeup_project_id
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('aliyunSubUserId') is not None:
            self.aliyun_sub_user_id = m.get('aliyunSubUserId')
        if m.get('aliyunUserId') is not None:
            self.aliyun_user_id = m.get('aliyunUserId')
        if m.get('codeupProjectId') is not None:
            self.codeup_project_id = m.get('codeupProjectId')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class IsSlsUserAuthrizedCodeupResponseBodyResult(TeaModel):
    def __init__(self, authrized=None):
        self.authrized = authrized  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsSlsUserAuthrizedCodeupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authrized is not None:
            result['authrized'] = self.authrized
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authrized') is not None:
            self.authrized = m.get('authrized')
        return self


class IsSlsUserAuthrizedCodeupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: IsSlsUserAuthrizedCodeupResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(IsSlsUserAuthrizedCodeupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = IsSlsUserAuthrizedCodeupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IsSlsUserAuthrizedCodeupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IsSlsUserAuthrizedCodeupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IsSlsUserAuthrizedCodeupResponse, self).to_map()
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
            temp_model = IsSlsUserAuthrizedCodeupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListGroupMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListGroupMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListGroupMemberResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupMemberResponse, self).to_map()
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
            temp_model = ListGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRepositoriesRequest(TeaModel):
    def __init__(self, access_token=None, is_member=None, organization_id=None, page=None, page_size=None,
                 search=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.is_member = is_member  # type: bool
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.search = search  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupRepositoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.is_member is not None:
            result['IsMember'] = self.is_member
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('IsMember') is not None:
            self.is_member = m.get('IsMember')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListGroupRepositoriesResponseBodyResult(TeaModel):
    def __init__(self, archive=None, created_at=None, creator_id=None, http_clone_url=None, id=None,
                 import_status=None, last_activity_at=None, name=None, name_with_namespace=None, namespace_id=None, path=None,
                 path_with_namespace=None, ssh_clone_url=None, updated_at=None, visibility_level=None, web_url=None):
        self.archive = archive  # type: bool
        self.created_at = created_at  # type: str
        self.creator_id = creator_id  # type: long
        self.http_clone_url = http_clone_url  # type: str
        self.id = id  # type: long
        self.import_status = import_status  # type: str
        self.last_activity_at = last_activity_at  # type: str
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.namespace_id = namespace_id  # type: long
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.ssh_clone_url = ssh_clone_url  # type: str
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: int
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupRepositoriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.http_clone_url is not None:
            result['HttpCloneUrl'] = self.http_clone_url
        if self.id is not None:
            result['Id'] = self.id
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.ssh_clone_url is not None:
            result['SshCloneUrl'] = self.ssh_clone_url
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('HttpCloneUrl') is not None:
            self.http_clone_url = m.get('HttpCloneUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('SshCloneUrl') is not None:
            self.ssh_clone_url = m.get('SshCloneUrl')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class ListGroupRepositoriesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListGroupRepositoriesResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupRepositoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupRepositoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListGroupRepositoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupRepositoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupRepositoriesResponse, self).to_map()
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
            temp_model = ListGroupRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, access_token=None, include_personal=None, organization_id=None, page=None, page_size=None,
                 search=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.include_personal = include_personal  # type: bool
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.search = search  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.include_personal is not None:
            result['IncludePersonal'] = self.include_personal
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('IncludePersonal') is not None:
            self.include_personal = m.get('IncludePersonal')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListGroupsResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, created_at=None, description=None, id=None, name=None,
                 name_with_namespace=None, owner_id=None, parent_id=None, path=None, path_with_namespace=None, type=None,
                 updated_at=None, visibility_level=None, web_url=None):
        self.access_level = access_level  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_id = parent_id  # type: long
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.type = type  # type: str
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListGroupsResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsResponse, self).to_map()
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMergeRequestCommentsRequest(TeaModel):
    def __init__(self, access_token=None, from_commit=None, organization_id=None, to_commit=None):
        self.access_token = access_token  # type: str
        self.from_commit = from_commit  # type: str
        self.organization_id = organization_id  # type: str
        self.to_commit = to_commit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestCommentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.from_commit is not None:
            result['FromCommit'] = self.from_commit
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.to_commit is not None:
            result['ToCommit'] = self.to_commit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('FromCommit') is not None:
            self.from_commit = m.get('FromCommit')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ToCommit') is not None:
            self.to_commit = m.get('ToCommit')
        return self


class ListMergeRequestCommentsResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, email=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestCommentsResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMergeRequestCommentsResponseBodyResult(TeaModel):
    def __init__(self, author=None, closed=None, created_at=None, id=None, is_draft=None, line=None, note=None,
                 out_dated=None, parent_note_id=None, path=None, project_id=None, range_context=None, side=None,
                 updated_at=None):
        self.author = author  # type: ListMergeRequestCommentsResponseBodyResultAuthor
        self.closed = closed  # type: int
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.is_draft = is_draft  # type: bool
        self.line = line  # type: long
        self.note = note  # type: str
        self.out_dated = out_dated  # type: bool
        self.parent_note_id = parent_note_id  # type: long
        self.path = path  # type: str
        self.project_id = project_id  # type: long
        self.range_context = range_context  # type: str
        self.side = side  # type: str
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(ListMergeRequestCommentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.is_draft is not None:
            result['IsDraft'] = self.is_draft
        if self.line is not None:
            result['Line'] = self.line
        if self.note is not None:
            result['Note'] = self.note
        if self.out_dated is not None:
            result['OutDated'] = self.out_dated
        if self.parent_note_id is not None:
            result['ParentNoteId'] = self.parent_note_id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.range_context is not None:
            result['RangeContext'] = self.range_context
        if self.side is not None:
            result['Side'] = self.side
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            temp_model = ListMergeRequestCommentsResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDraft') is not None:
            self.is_draft = m.get('IsDraft')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OutDated') is not None:
            self.out_dated = m.get('OutDated')
        if m.get('ParentNoteId') is not None:
            self.parent_note_id = m.get('ParentNoteId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RangeContext') is not None:
            self.range_context = m.get('RangeContext')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListMergeRequestCommentsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListMergeRequestCommentsResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMergeRequestCommentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListMergeRequestCommentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMergeRequestCommentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMergeRequestCommentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMergeRequestCommentsResponse, self).to_map()
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
            temp_model = ListMergeRequestCommentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMergeRequestsRequest(TeaModel):
    def __init__(self, access_token=None, after_date=None, assignee_codeup_id_list=None, assignee_id_list=None,
                 author_codeup_id_list=None, author_id_list=None, before_date=None, group_id_list=None, order=None, organization_id=None,
                 page=None, page_size=None, project_id_list=None, search=None, state=None,
                 subscriber_codeup_id_list=None):
        self.access_token = access_token  # type: str
        self.after_date = after_date  # type: str
        self.assignee_codeup_id_list = assignee_codeup_id_list  # type: str
        self.assignee_id_list = assignee_id_list  # type: str
        self.author_codeup_id_list = author_codeup_id_list  # type: str
        self.author_id_list = author_id_list  # type: str
        self.before_date = before_date  # type: str
        self.group_id_list = group_id_list  # type: str
        self.order = order  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.project_id_list = project_id_list  # type: str
        self.search = search  # type: str
        self.state = state  # type: str
        self.subscriber_codeup_id_list = subscriber_codeup_id_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.assignee_codeup_id_list is not None:
            result['AssigneeCodeupIdList'] = self.assignee_codeup_id_list
        if self.assignee_id_list is not None:
            result['AssigneeIdList'] = self.assignee_id_list
        if self.author_codeup_id_list is not None:
            result['AuthorCodeupIdList'] = self.author_codeup_id_list
        if self.author_id_list is not None:
            result['AuthorIdList'] = self.author_id_list
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.order is not None:
            result['Order'] = self.order
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id_list is not None:
            result['ProjectIdList'] = self.project_id_list
        if self.search is not None:
            result['Search'] = self.search
        if self.state is not None:
            result['State'] = self.state
        if self.subscriber_codeup_id_list is not None:
            result['SubscriberCodeupIdList'] = self.subscriber_codeup_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('AssigneeCodeupIdList') is not None:
            self.assignee_codeup_id_list = m.get('AssigneeCodeupIdList')
        if m.get('AssigneeIdList') is not None:
            self.assignee_id_list = m.get('AssigneeIdList')
        if m.get('AuthorCodeupIdList') is not None:
            self.author_codeup_id_list = m.get('AuthorCodeupIdList')
        if m.get('AuthorIdList') is not None:
            self.author_id_list = m.get('AuthorIdList')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectIdList') is not None:
            self.project_id_list = m.get('ProjectIdList')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SubscriberCodeupIdList') is not None:
            self.subscriber_codeup_id_list = m.get('SubscriberCodeupIdList')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class ListMergeRequestsResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, email=None, extern_user_id=None, id=None, name=None, status=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMergeRequestsResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMergeRequestsResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 is_support_merge=None, merge_error=None, merge_status=None, merge_type=None, merged_revision=None,
                 name_with_namespace=None, project_id=None, source_branch=None, state=None, target_branch=None, title=None,
                 updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: ListMergeRequestsResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[ListMergeRequestsResponseBodyResultAssigneeList]
        self.author = author  # type: ListMergeRequestsResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.is_support_merge = is_support_merge  # type: bool
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_support_merge is not None:
            result['IsSupportMerge'] = self.is_support_merge
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = ListMergeRequestsResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = ListMergeRequestsResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = ListMergeRequestsResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsSupportMerge') is not None:
            self.is_support_merge = m.get('IsSupportMerge')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class ListMergeRequestsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListMergeRequestsResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListMergeRequestsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMergeRequestsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMergeRequestsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMergeRequestsResponse, self).to_map()
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
            temp_model = ListMergeRequestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationSecurityScoresRequest(TeaModel):
    def __init__(self, access_token=None):
        self.access_token = access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationSecurityScoresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore(TeaModel):
    def __init__(self, authority_control_score=None, code_content_score=None, level=None,
                 member_behavior_score=None):
        self.authority_control_score = authority_control_score  # type: int
        self.code_content_score = code_content_score  # type: int
        self.level = level  # type: str
        self.member_behavior_score = member_behavior_score  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_control_score is not None:
            result['AuthorityControlScore'] = self.authority_control_score
        if self.code_content_score is not None:
            result['CodeContentScore'] = self.code_content_score
        if self.level is not None:
            result['Level'] = self.level
        if self.member_behavior_score is not None:
            result['MemberBehaviorScore'] = self.member_behavior_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorityControlScore') is not None:
            self.authority_control_score = m.get('AuthorityControlScore')
        if m.get('CodeContentScore') is not None:
            self.code_content_score = m.get('CodeContentScore')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MemberBehaviorScore') is not None:
            self.member_behavior_score = m.get('MemberBehaviorScore')
        return self


class ListOrganizationSecurityScoresResponseBodyResult(TeaModel):
    def __init__(self, enable=None, id=None, organization_id=None, organization_security_score=None):
        self.enable = enable  # type: bool
        self.id = id  # type: long
        self.organization_id = organization_id  # type: str
        self.organization_security_score = organization_security_score  # type: ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore

    def validate(self):
        if self.organization_security_score:
            self.organization_security_score.validate()

    def to_map(self):
        _map = super(ListOrganizationSecurityScoresResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_security_score is not None:
            result['OrganizationSecurityScore'] = self.organization_security_score.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationSecurityScore') is not None:
            temp_model = ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore()
            self.organization_security_score = temp_model.from_map(m['OrganizationSecurityScore'])
        return self


class ListOrganizationSecurityScoresResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListOrganizationSecurityScoresResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationSecurityScoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListOrganizationSecurityScoresResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrganizationSecurityScoresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrganizationSecurityScoresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationSecurityScoresResponse, self).to_map()
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
            temp_model = ListOrganizationSecurityScoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationsRequest(TeaModel):
    def __init__(self, access_level=None, access_token=None, min_access_level=None):
        self.access_level = access_level  # type: int
        self.access_token = access_token  # type: str
        self.min_access_level = min_access_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.min_access_level is not None:
            result['MinAccessLevel'] = self.min_access_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('MinAccessLevel') is not None:
            self.min_access_level = m.get('MinAccessLevel')
        return self


class ListOrganizationsResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, organization_id=None, organization_name=None, organization_role=None):
        self.access_level = access_level  # type: int
        self.organization_id = organization_id  # type: str
        self.organization_name = organization_name  # type: str
        self.organization_role = organization_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_role is not None:
            result['OrganizationRole'] = self.organization_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationRole') is not None:
            self.organization_role = m.get('OrganizationRole')
        return self


class ListOrganizationsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListOrganizationsResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrganizationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrganizationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationsResponse, self).to_map()
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
            temp_model = ListOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoriesRequest(TeaModel):
    def __init__(self, access_token=None, archive=None, order=None, organization_id=None, page=None, page_size=None,
                 search=None, sort=None):
        self.access_token = access_token  # type: str
        self.archive = archive  # type: bool
        self.order = order  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.search = search  # type: str
        self.sort = sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.order is not None:
            result['Order'] = self.order
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListRepositoriesResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, archive=None, avatar_url=None, created_at=None, demo_project_status=None,
                 description=None, id=None, import_status=None, last_activity_at=None, name=None, name_with_namespace=None,
                 namespace_id=None, path=None, path_with_namespace=None, star=None, star_count=None, updated_at=None,
                 visibility_level=None, web_url=None):
        self.access_level = access_level  # type: int
        self.archive = archive  # type: bool
        self.avatar_url = avatar_url  # type: str
        self.created_at = created_at  # type: str
        self.demo_project_status = demo_project_status  # type: bool
        self.description = description  # type: str
        self.id = id  # type: long
        self.import_status = import_status  # type: str
        self.last_activity_at = last_activity_at  # type: str
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.namespace_id = namespace_id  # type: long
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.star = star  # type: bool
        self.star_count = star_count  # type: long
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.star is not None:
            result['Star'] = self.star
        if self.star_count is not None:
            result['StarCount'] = self.star_count
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Star') is not None:
            self.star = m.get('Star')
        if m.get('StarCount') is not None:
            self.star_count = m.get('StarCount')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class ListRepositoriesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoriesResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponse, self).to_map()
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
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryBranchesRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None, search=None,
                 sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.search = search  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryBranchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListRepositoryBranchesResponseBodyResultCommitInfo(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryBranchesResponseBodyResultCommitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListRepositoryBranchesResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, commit_info=None, protected_branch=None):
        self.branch_name = branch_name  # type: str
        self.commit_info = commit_info  # type: ListRepositoryBranchesResponseBodyResultCommitInfo
        self.protected_branch = protected_branch  # type: bool

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super(ListRepositoryBranchesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = ListRepositoryBranchesResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        return self


class ListRepositoryBranchesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryBranchesResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryBranchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryBranchesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryBranchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryBranchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryBranchesResponse, self).to_map()
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
            temp_model = ListRepositoryBranchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryCodeRequestFilePath(TeaModel):
    def __init__(self, match_type=None, name=None, operator_type=None, value=None):
        self.match_type = match_type  # type: str
        self.name = name  # type: str
        self.operator_type = operator_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCodeRequestFilePath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListRepositoryCodeRequestRepositoryPath(TeaModel):
    def __init__(self, match_type=None, name=None, operator_type=None, value=None):
        self.match_type = match_type  # type: str
        self.name = name  # type: str
        self.operator_type = operator_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCodeRequestRepositoryPath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListRepositoryCodeRequest(TeaModel):
    def __init__(self, organization_id=None, file_path=None, is_code_block=None, key_word=None, language=None,
                 order=None, page=None, page_size=None, repository_path=None, scope=None, sort=None):
        self.organization_id = organization_id  # type: str
        self.file_path = file_path  # type: ListRepositoryCodeRequestFilePath
        self.is_code_block = is_code_block  # type: bool
        self.key_word = key_word  # type: str
        self.language = language  # type: str
        self.order = order  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.repository_path = repository_path  # type: ListRepositoryCodeRequestRepositoryPath
        self.scope = scope  # type: str
        self.sort = sort  # type: str

    def validate(self):
        if self.file_path:
            self.file_path.validate()
        if self.repository_path:
            self.repository_path.validate()

    def to_map(self):
        _map = super(ListRepositoryCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path.to_map()
        if self.is_code_block is not None:
            result['IsCodeBlock'] = self.is_code_block
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.language is not None:
            result['Language'] = self.language
        if self.order is not None:
            result['Order'] = self.order
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repository_path is not None:
            result['RepositoryPath'] = self.repository_path.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('FilePath') is not None:
            temp_model = ListRepositoryCodeRequestFilePath()
            self.file_path = temp_model.from_map(m['FilePath'])
        if m.get('IsCodeBlock') is not None:
            self.is_code_block = m.get('IsCodeBlock')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepositoryPath') is not None:
            temp_model = ListRepositoryCodeRequestRepositoryPath()
            self.repository_path = temp_model.from_map(m['RepositoryPath'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListRepositoryCodeResponseBodyResultSource(TeaModel):
    def __init__(self, branch=None, checkin_date=None, file_name=None, file_path=None, language=None,
                 organization_id=None, repo_path=None):
        self.branch = branch  # type: str
        self.checkin_date = checkin_date  # type: str
        self.file_name = file_name  # type: str
        self.file_path = file_path  # type: str
        self.language = language  # type: str
        self.organization_id = organization_id  # type: str
        self.repo_path = repo_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCodeResponseBodyResultSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.checkin_date is not None:
            result['CheckinDate'] = self.checkin_date
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.language is not None:
            result['Language'] = self.language
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.repo_path is not None:
            result['RepoPath'] = self.repo_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('CheckinDate') is not None:
            self.checkin_date = m.get('CheckinDate')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RepoPath') is not None:
            self.repo_path = m.get('RepoPath')
        return self


class ListRepositoryCodeResponseBodyResult(TeaModel):
    def __init__(self, doc_id=None, highlight_text_map=None, source=None):
        self.doc_id = doc_id  # type: str
        self.highlight_text_map = highlight_text_map  # type: dict[str, any]
        self.source = source  # type: ListRepositoryCodeResponseBodyResultSource

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(ListRepositoryCodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.highlight_text_map is not None:
            result['HighlightTextMap'] = self.highlight_text_map
        if self.source is not None:
            result['Source'] = self.source.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('HighlightTextMap') is not None:
            self.highlight_text_map = m.get('HighlightTextMap')
        if m.get('Source') is not None:
            temp_model = ListRepositoryCodeResponseBodyResultSource()
            self.source = temp_model.from_map(m['Source'])
        return self


class ListRepositoryCodeResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryCodeResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryCodeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryCodeResponse, self).to_map()
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
            temp_model = ListRepositoryCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryCommitDiffRequest(TeaModel):
    def __init__(self, access_token=None, context_line=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.context_line = context_line  # type: int
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCommitDiffRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.context_line is not None:
            result['ContextLine'] = self.context_line
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ContextLine') is not None:
            self.context_line = m.get('ContextLine')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRepositoryCommitDiffResponseBodyResult(TeaModel):
    def __init__(self, amode=None, bmode=None, deleted_file=None, diff=None, is_binary=None, is_new_lfs=None,
                 is_old_lfs=None, new_file=None, new_id=None, new_path=None, old_id=None, old_path=None, renamed_file=None):
        self.amode = amode  # type: str
        self.bmode = bmode  # type: str
        self.deleted_file = deleted_file  # type: bool
        self.diff = diff  # type: str
        self.is_binary = is_binary  # type: bool
        self.is_new_lfs = is_new_lfs  # type: bool
        self.is_old_lfs = is_old_lfs  # type: bool
        self.new_file = new_file  # type: bool
        self.new_id = new_id  # type: str
        self.new_path = new_path  # type: str
        self.old_id = old_id  # type: str
        self.old_path = old_path  # type: str
        self.renamed_file = renamed_file  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCommitDiffResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amode is not None:
            result['AMode'] = self.amode
        if self.bmode is not None:
            result['BMode'] = self.bmode
        if self.deleted_file is not None:
            result['DeletedFile'] = self.deleted_file
        if self.diff is not None:
            result['Diff'] = self.diff
        if self.is_binary is not None:
            result['IsBinary'] = self.is_binary
        if self.is_new_lfs is not None:
            result['IsNewLfs'] = self.is_new_lfs
        if self.is_old_lfs is not None:
            result['IsOldLfs'] = self.is_old_lfs
        if self.new_file is not None:
            result['NewFile'] = self.new_file
        if self.new_id is not None:
            result['NewId'] = self.new_id
        if self.new_path is not None:
            result['NewPath'] = self.new_path
        if self.old_id is not None:
            result['OldId'] = self.old_id
        if self.old_path is not None:
            result['OldPath'] = self.old_path
        if self.renamed_file is not None:
            result['RenamedFile'] = self.renamed_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AMode') is not None:
            self.amode = m.get('AMode')
        if m.get('BMode') is not None:
            self.bmode = m.get('BMode')
        if m.get('DeletedFile') is not None:
            self.deleted_file = m.get('DeletedFile')
        if m.get('Diff') is not None:
            self.diff = m.get('Diff')
        if m.get('IsBinary') is not None:
            self.is_binary = m.get('IsBinary')
        if m.get('IsNewLfs') is not None:
            self.is_new_lfs = m.get('IsNewLfs')
        if m.get('IsOldLfs') is not None:
            self.is_old_lfs = m.get('IsOldLfs')
        if m.get('NewFile') is not None:
            self.new_file = m.get('NewFile')
        if m.get('NewId') is not None:
            self.new_id = m.get('NewId')
        if m.get('NewPath') is not None:
            self.new_path = m.get('NewPath')
        if m.get('OldId') is not None:
            self.old_id = m.get('OldId')
        if m.get('OldPath') is not None:
            self.old_path = m.get('OldPath')
        if m.get('RenamedFile') is not None:
            self.renamed_file = m.get('RenamedFile')
        return self


class ListRepositoryCommitDiffResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryCommitDiffResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryCommitDiffResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryCommitDiffResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRepositoryCommitDiffResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryCommitDiffResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryCommitDiffResponse, self).to_map()
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
            temp_model = ListRepositoryCommitDiffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryCommitsRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None, path=None, ref_name=None,
                 search=None, show_signature=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.path = path  # type: str
        self.ref_name = ref_name  # type: str
        self.search = search  # type: str
        self.show_signature = show_signature  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCommitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        if self.ref_name is not None:
            result['RefName'] = self.ref_name
        if self.search is not None:
            result['Search'] = self.search
        if self.show_signature is not None:
            result['ShowSignature'] = self.show_signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RefName') is not None:
            self.ref_name = m.get('RefName')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('ShowSignature') is not None:
            self.show_signature = m.get('ShowSignature')
        return self


class ListRepositoryCommitsResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryCommitsResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListRepositoryCommitsResponseBodyResult(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_date = author_date  # type: str
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: ListRepositoryCommitsResponseBodyResultSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(ListRepositoryCommitsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryCommitsResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListRepositoryCommitsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryCommitsResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryCommitsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryCommitsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryCommitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryCommitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryCommitsResponse, self).to_map()
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
            temp_model = ListRepositoryCommitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None, query=None,
                 sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.query = query  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, name=None,
                 state=None, username=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.state = state  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListRepositoryMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryMemberResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberResponse, self).to_map()
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
            temp_model = ListRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryMemberWithInheritedRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRepositoryMemberWithInheritedResponseBodyResultInherited(TeaModel):
    def __init__(self, id=None, name=None, name_with_namespace=None, path=None, path_with_namespace=None, type=None,
                 visibility_level=None):
        self.id = id  # type: long
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.type = type  # type: str
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBodyResultInherited, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        return self


class ListRepositoryMemberWithInheritedResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, inherited=None,
                 name=None, state=None, username=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.inherited = inherited  # type: ListRepositoryMemberWithInheritedResponseBodyResultInherited
        self.name = name  # type: str
        self.state = state  # type: str
        self.username = username  # type: str

    def validate(self):
        if self.inherited:
            self.inherited.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.inherited is not None:
            result['Inherited'] = self.inherited.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Inherited') is not None:
            temp_model = ListRepositoryMemberWithInheritedResponseBodyResultInherited()
            self.inherited = temp_model.from_map(m['Inherited'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListRepositoryMemberWithInheritedResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryMemberWithInheritedResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryMemberWithInheritedResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRepositoryMemberWithInheritedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryMemberWithInheritedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponse, self).to_map()
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
            temp_model = ListRepositoryMemberWithInheritedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryProtectedBranchRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees(TeaModel):
    def __init__(self, avatar_url=None, email=None, extern_uid=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_uid = extern_uid  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_uid is not None:
            result['ExternUid'] = self.extern_uid
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUid') is not None:
            self.extern_uid = m.get('ExternUid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting(TeaModel):
    def __init__(self, allow_merge_request_roles=None, allow_self_approval=None, default_assignees=None,
                 is_require_discussion_processed=None, merge_request_mode=None, minimum_approval=None, required=None, white_list=None):
        self.allow_merge_request_roles = allow_merge_request_roles  # type: list[int]
        self.allow_self_approval = allow_self_approval  # type: bool
        self.default_assignees = default_assignees  # type: list[ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees]
        self.is_require_discussion_processed = is_require_discussion_processed  # type: bool
        self.merge_request_mode = merge_request_mode  # type: str
        self.minimum_approval = minimum_approval  # type: int
        self.required = required  # type: bool
        self.white_list = white_list  # type: str

    def validate(self):
        if self.default_assignees:
            for k in self.default_assignees:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_merge_request_roles is not None:
            result['AllowMergeRequestRoles'] = self.allow_merge_request_roles
        if self.allow_self_approval is not None:
            result['AllowSelfApproval'] = self.allow_self_approval
        result['DefaultAssignees'] = []
        if self.default_assignees is not None:
            for k in self.default_assignees:
                result['DefaultAssignees'].append(k.to_map() if k else None)
        if self.is_require_discussion_processed is not None:
            result['IsRequireDiscussionProcessed'] = self.is_require_discussion_processed
        if self.merge_request_mode is not None:
            result['MergeRequestMode'] = self.merge_request_mode
        if self.minimum_approval is not None:
            result['MinimumApproval'] = self.minimum_approval
        if self.required is not None:
            result['Required'] = self.required
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowMergeRequestRoles') is not None:
            self.allow_merge_request_roles = m.get('AllowMergeRequestRoles')
        if m.get('AllowSelfApproval') is not None:
            self.allow_self_approval = m.get('AllowSelfApproval')
        self.default_assignees = []
        if m.get('DefaultAssignees') is not None:
            for k in m.get('DefaultAssignees'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees()
                self.default_assignees.append(temp_model.from_map(k))
        if m.get('IsRequireDiscussionProcessed') is not None:
            self.is_require_discussion_processed = m.get('IsRequireDiscussionProcessed')
        if m.get('MergeRequestMode') is not None:
            self.merge_request_mode = m.get('MergeRequestMode')
        if m.get('MinimumApproval') is not None:
            self.minimum_approval = m.get('MinimumApproval')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig(TeaModel):
    def __init__(self, check_items=None):
        self.check_items = check_items  # type: list[ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems]

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems()
                self.check_items.append(temp_model.from_map(k))
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection(TeaModel):
    def __init__(self, enabled=None, message=None):
        self.enabled = enabled  # type: bool
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection(TeaModel):
    def __init__(self, enabled=None, message=None):
        self.enabled = enabled  # type: bool
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSetting(TeaModel):
    def __init__(self, check_config=None, coding_guidelines_detection=None, required=None,
                 sensitive_info_detection=None):
        self.check_config = check_config  # type: ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig
        self.coding_guidelines_detection = coding_guidelines_detection  # type: ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection
        self.required = required  # type: bool
        self.sensitive_info_detection = sensitive_info_detection  # type: ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection

    def validate(self):
        if self.check_config:
            self.check_config.validate()
        if self.coding_guidelines_detection:
            self.coding_guidelines_detection.validate()
        if self.sensitive_info_detection:
            self.sensitive_info_detection.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResultTestSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_config is not None:
            result['CheckConfig'] = self.check_config.to_map()
        if self.coding_guidelines_detection is not None:
            result['CodingGuidelinesDetection'] = self.coding_guidelines_detection.to_map()
        if self.required is not None:
            result['Required'] = self.required
        if self.sensitive_info_detection is not None:
            result['SensitiveInfoDetection'] = self.sensitive_info_detection.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckConfig') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig()
            self.check_config = temp_model.from_map(m['CheckConfig'])
        if m.get('CodingGuidelinesDetection') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection()
            self.coding_guidelines_detection = temp_model.from_map(m['CodingGuidelinesDetection'])
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('SensitiveInfoDetection') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection()
            self.sensitive_info_detection = temp_model.from_map(m['SensitiveInfoDetection'])
        return self


class ListRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(self, allow_merge_roles=None, allow_push_roles=None, branch=None, id=None,
                 merge_request_setting=None, test_setting=None):
        self.allow_merge_roles = allow_merge_roles  # type: list[int]
        self.allow_push_roles = allow_push_roles  # type: list[int]
        self.branch = branch  # type: str
        self.id = id  # type: long
        self.merge_request_setting = merge_request_setting  # type: ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting
        self.test_setting = test_setting  # type: ListRepositoryProtectedBranchResponseBodyResultTestSetting

    def validate(self):
        if self.merge_request_setting:
            self.merge_request_setting.validate()
        if self.test_setting:
            self.test_setting.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_merge_roles is not None:
            result['AllowMergeRoles'] = self.allow_merge_roles
        if self.allow_push_roles is not None:
            result['AllowPushRoles'] = self.allow_push_roles
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_request_setting is not None:
            result['MergeRequestSetting'] = self.merge_request_setting.to_map()
        if self.test_setting is not None:
            result['TestSetting'] = self.test_setting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowMergeRoles') is not None:
            self.allow_merge_roles = m.get('AllowMergeRoles')
        if m.get('AllowPushRoles') is not None:
            self.allow_push_roles = m.get('AllowPushRoles')
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeRequestSetting') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting()
            self.merge_request_setting = temp_model.from_map(m['MergeRequestSetting'])
        if m.get('TestSetting') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSetting()
            self.test_setting = temp_model.from_map(m['TestSetting'])
        return self


class ListRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryProtectedBranchResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRepositoryProtectedBranchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryProtectedBranchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryProtectedBranchResponse, self).to_map()
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
            temp_model = ListRepositoryProtectedBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryTagsRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None, search=None,
                 show_signature=None, sort=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.search = search  # type: str
        self.show_signature = show_signature  # type: bool
        self.sort = sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.show_signature is not None:
            result['ShowSignature'] = self.show_signature
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('ShowSignature') is not None:
            self.show_signature = m.get('ShowSignature')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListRepositoryTagsResponseBodyResultCommitSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryTagsResponseBodyResultCommitSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListRepositoryTagsResponseBodyResultCommit(TeaModel):
    def __init__(self, author_email=None, author_name=None, authored_date=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        self.author_email = author_email  # type: str
        self.author_name = author_name  # type: str
        self.authored_date = authored_date  # type: str
        self.committed_date = committed_date  # type: str
        self.committer_email = committer_email  # type: str
        self.committer_name = committer_name  # type: str
        self.created_at = created_at  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.parent_ids = parent_ids  # type: list[str]
        self.short_id = short_id  # type: str
        self.signature = signature  # type: ListRepositoryTagsResponseBodyResultCommitSignature
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(ListRepositoryTagsResponseBodyResultCommit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListRepositoryTagsResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        self.gpg_key_id = gpg_key_id  # type: str
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryTagsResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListRepositoryTagsResponseBodyResult(TeaModel):
    def __init__(self, commit=None, id=None, message=None, name=None, signature=None):
        self.commit = commit  # type: ListRepositoryTagsResponseBodyResultCommit
        self.id = id  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.signature = signature  # type: ListRepositoryTagsResponseBodyResultSignature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(ListRepositoryTagsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Commit') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class ListRepositoryTagsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryTagsResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryTagsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryTagsResponse, self).to_map()
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
            temp_model = ListRepositoryTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryTreeRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, path=None, ref_name=None, sub_user_id=None,
                 type=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.path = path  # type: str
        self.ref_name = ref_name  # type: str
        self.sub_user_id = sub_user_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryTreeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.path is not None:
            result['Path'] = self.path
        if self.ref_name is not None:
            result['RefName'] = self.ref_name
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RefName') is not None:
            self.ref_name = m.get('RefName')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRepositoryTreeResponseBodyResult(TeaModel):
    def __init__(self, id=None, mode=None, name=None, path=None, type=None):
        self.id = id  # type: str
        self.mode = mode  # type: str
        self.name = name  # type: str
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryTreeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRepositoryTreeResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryTreeResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryTreeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryTreeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRepositoryTreeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryTreeResponse, self).to_map()
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
            temp_model = ListRepositoryTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryWebhookRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepositoryWebhookResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, description=None, enable_ssl_verification=None, id=None,
                 last_test_result=None, merge_requests_events=None, note_events=None, project_id=None, push_events=None,
                 secret_token=None, tag_push_events=None, url=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        self.id = id  # type: long
        self.last_test_result = last_test_result  # type: str
        self.merge_requests_events = merge_requests_events  # type: bool
        self.note_events = note_events  # type: bool
        self.project_id = project_id  # type: long
        self.push_events = push_events  # type: bool
        self.secret_token = secret_token  # type: str
        self.tag_push_events = tag_push_events  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryWebhookResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['Id'] = self.id
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListRepositoryWebhookResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryWebhookResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryWebhookResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRepositoryWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryWebhookResponse, self).to_map()
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
            temp_model = ListRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeMergeRequestRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeMergeRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class MergeMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class MergeMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class MergeMergeRequestResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 merge_error=None, merge_status=None, merge_type=None, merged_revision=None, name_with_namespace=None,
                 project_id=None, source_branch=None, state=None, target_branch=None, title=None, updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: MergeMergeRequestResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[MergeMergeRequestResponseBodyResultAssigneeList]
        self.author = author  # type: MergeMergeRequestResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = MergeMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = MergeMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = MergeMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class MergeMergeRequestResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: MergeMergeRequestResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = MergeMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MergeMergeRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MergeMergeRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MergeMergeRequestResponse, self).to_map()
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
            temp_model = MergeMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySlsRelationRequest(TeaModel):
    def __init__(self, organization_id=None, aliyun_user_id=None, codeup_project_id=None, sls_log_store=None,
                 sls_project=None):
        self.organization_id = organization_id  # type: str
        self.aliyun_user_id = aliyun_user_id  # type: str
        self.codeup_project_id = codeup_project_id  # type: long
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlsRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.aliyun_user_id is not None:
            result['aliyunUserId'] = self.aliyun_user_id
        if self.codeup_project_id is not None:
            result['codeupProjectId'] = self.codeup_project_id
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('aliyunUserId') is not None:
            self.aliyun_user_id = m.get('aliyunUserId')
        if m.get('codeupProjectId') is not None:
            self.codeup_project_id = m.get('codeupProjectId')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class QuerySlsRelationResponseBodyResult(TeaModel):
    def __init__(self, aliyun_user_id=None, codeup_project_id=None, default_viewer=None, organization_id=None,
                 sls_log_store=None, sls_project=None):
        self.aliyun_user_id = aliyun_user_id  # type: str
        self.codeup_project_id = codeup_project_id  # type: long
        self.default_viewer = default_viewer  # type: bool
        self.organization_id = organization_id  # type: str
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlsRelationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_user_id is not None:
            result['aliyunUserId'] = self.aliyun_user_id
        if self.codeup_project_id is not None:
            result['codeupProjectId'] = self.codeup_project_id
        if self.default_viewer is not None:
            result['defaultViewer'] = self.default_viewer
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunUserId') is not None:
            self.aliyun_user_id = m.get('aliyunUserId')
        if m.get('codeupProjectId') is not None:
            self.codeup_project_id = m.get('codeupProjectId')
        if m.get('defaultViewer') is not None:
            self.default_viewer = m.get('defaultViewer')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class QuerySlsRelationResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QuerySlsRelationResponseBodyResult]
        self.success = success  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySlsRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QuerySlsRelationResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySlsRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySlsRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySlsRelationResponse, self).to_map()
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
            temp_model = QuerySlsRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RelatedSlsLogStoreRequest(TeaModel):
    def __init__(self, organization_id=None, aliyun_user_id=None, codeup_project_id=None, default_viewer=None,
                 sls_log_store=None, sls_project=None):
        self.organization_id = organization_id  # type: str
        self.aliyun_user_id = aliyun_user_id  # type: str
        self.codeup_project_id = codeup_project_id  # type: long
        self.default_viewer = default_viewer  # type: bool
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RelatedSlsLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.aliyun_user_id is not None:
            result['aliyunUserId'] = self.aliyun_user_id
        if self.codeup_project_id is not None:
            result['codeupProjectId'] = self.codeup_project_id
        if self.default_viewer is not None:
            result['defaultViewer'] = self.default_viewer
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('aliyunUserId') is not None:
            self.aliyun_user_id = m.get('aliyunUserId')
        if m.get('codeupProjectId') is not None:
            self.codeup_project_id = m.get('codeupProjectId')
        if m.get('defaultViewer') is not None:
            self.default_viewer = m.get('defaultViewer')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class RelatedSlsLogStoreResponseBodyResult(TeaModel):
    def __init__(self, related_result=None):
        self.related_result = related_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RelatedSlsLogStoreResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.related_result is not None:
            result['RelatedResult'] = self.related_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelatedResult') is not None:
            self.related_result = m.get('RelatedResult')
        return self


class RelatedSlsLogStoreResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: RelatedSlsLogStoreResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RelatedSlsLogStoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = RelatedSlsLogStoreResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RelatedSlsLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RelatedSlsLogStoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RelatedSlsLogStoreResponse, self).to_map()
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
            temp_model = RelatedSlsLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRepositoryMirrorSyncRequest(TeaModel):
    def __init__(self, access_token=None, account=None, organization_id=None, token=None):
        self.access_token = access_token  # type: str
        self.account = account  # type: str
        self.organization_id = organization_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.account is not None:
            result['Account'] = self.account
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class TriggerRepositoryMirrorSyncResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TriggerRepositoryMirrorSyncResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: TriggerRepositoryMirrorSyncResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = TriggerRepositoryMirrorSyncResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerRepositoryMirrorSyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerRepositoryMirrorSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponse, self).to_map()
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
            temp_model = TriggerRepositoryMirrorSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRelatedSlsLogStoreRequest(TeaModel):
    def __init__(self, organization_id=None, aliyun_user_id=None, codeup_project_id=None, sls_log_store=None,
                 sls_project=None):
        self.organization_id = organization_id  # type: str
        self.aliyun_user_id = aliyun_user_id  # type: str
        self.codeup_project_id = codeup_project_id  # type: long
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRelatedSlsLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.aliyun_user_id is not None:
            result['aliyunUserId'] = self.aliyun_user_id
        if self.codeup_project_id is not None:
            result['codeupProjectId'] = self.codeup_project_id
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('aliyunUserId') is not None:
            self.aliyun_user_id = m.get('aliyunUserId')
        if m.get('codeupProjectId') is not None:
            self.codeup_project_id = m.get('codeupProjectId')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class UnRelatedSlsLogStoreResponseBodyResult(TeaModel):
    def __init__(self, un_related_result=None):
        self.un_related_result = un_related_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRelatedSlsLogStoreResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_related_result is not None:
            result['UnRelatedResult'] = self.un_related_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnRelatedResult') is not None:
            self.un_related_result = m.get('UnRelatedResult')
        return self


class UnRelatedSlsLogStoreResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UnRelatedSlsLogStoreResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UnRelatedSlsLogStoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UnRelatedSlsLogStoreResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnRelatedSlsLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnRelatedSlsLogStoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnRelatedSlsLogStoreResponse, self).to_map()
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
            temp_model = UnRelatedSlsLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateFileResponseBodyResult(TeaModel):
    def __init__(self, branch_name=None, file_path=None):
        self.branch_name = branch_name  # type: str
        self.file_path = file_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class UpdateFileResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateFileResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFileResponse, self).to_map()
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
            temp_model = UpdateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateGroupMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class UpdateGroupMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateGroupMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateGroupMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateGroupMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGroupMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupMemberResponse, self).to_map()
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
            temp_model = UpdateGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(self, check_name=None, check_status=None, check_type=None, extra_users=None, satisfied_items=None,
                 unsatisfied_items=None):
        self.check_name = check_name  # type: str
        self.check_status = check_status  # type: str
        self.check_type = check_type  # type: str
        self.extra_users = extra_users  # type: list[UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers]
        self.satisfied_items = satisfied_items  # type: list[str]
        self.unsatisfied_items = unsatisfied_items  # type: list[str]

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(self, satisfied_check_results=None, total_check_result=None, unsatisfied_check_results=None):
        self.satisfied_check_results = satisfied_check_results  # type: list[UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults]
        self.total_check_result = total_check_result  # type: str
        self.unsatisfied_check_results = unsatisfied_check_results  # type: list[UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults]

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultApproveCheckResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class UpdateMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultAssigneeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(self, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResultAuthor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateMergeRequestResponseBodyResult(TeaModel):
    def __init__(self, accepted_revision=None, ahead_commit_count=None, approve_check_result=None,
                 assignee_list=None, author=None, behind_commit_count=None, created_at=None, description=None, id=None,
                 merge_error=None, merge_status=None, merge_type=None, merged_revision=None, name_with_namespace=None,
                 project_id=None, source_branch=None, state=None, target_branch=None, title=None, updated_at=None, web_url=None):
        self.accepted_revision = accepted_revision  # type: str
        self.ahead_commit_count = ahead_commit_count  # type: int
        self.approve_check_result = approve_check_result  # type: UpdateMergeRequestResponseBodyResultApproveCheckResult
        self.assignee_list = assignee_list  # type: list[UpdateMergeRequestResponseBodyResultAssigneeList]
        self.author = author  # type: UpdateMergeRequestResponseBodyResultAuthor
        self.behind_commit_count = behind_commit_count  # type: int
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.merge_error = merge_error  # type: str
        self.merge_status = merge_status  # type: str
        self.merge_type = merge_type  # type: str
        self.merged_revision = merged_revision  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.project_id = project_id  # type: long
        self.source_branch = source_branch  # type: str
        self.state = state  # type: str
        self.target_branch = target_branch  # type: str
        self.title = title  # type: str
        self.updated_at = updated_at  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.state is not None:
            result['State'] = self.state
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.title is not None:
            result['Title'] = self.title
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('ApproveCheckResult') is not None:
            temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = UpdateMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = UpdateMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class UpdateMergeRequestResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateMergeRequestResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMergeRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMergeRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestResponse, self).to_map()
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
            temp_model = UpdateMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestCommentRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateMergeRequestCommentResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestCommentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateMergeRequestCommentResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateMergeRequestCommentResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestCommentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMergeRequestCommentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMergeRequestCommentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestCommentResponse, self).to_map()
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
            temp_model = UpdateMergeRequestCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestSettingRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateMergeRequestSettingResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMergeRequestSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateMergeRequestSettingResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateMergeRequestSettingResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMergeRequestSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMergeRequestSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMergeRequestSettingResponse, self).to_map()
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
            temp_model = UpdateMergeRequestSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateRepositoryResponseBodyResultNamespace(TeaModel):
    def __init__(self, avatar=None, created_at=None, description=None, id=None, name=None, owner_id=None, path=None,
                 public=None, updated_at=None, visibility_level=None):
        self.avatar = avatar  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.path = path  # type: str
        self.public = public  # type: bool
        self.updated_at = updated_at  # type: str
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryResponseBodyResultNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.public is not None:
            result['Public'] = self.public
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        return self


class UpdateRepositoryResponseBodyResult(TeaModel):
    def __init__(self, archive=None, avatar_url=None, created_at=None, creator_id=None, default_branch=None,
                 description=None, http_url_to_repo=None, id=None, last_activity_at=None, name=None, name_with_namespace=None,
                 namespace=None, path=None, path_with_namespace=None, ssh_url_to_repo=None, visibility_level=None,
                 web_url=None):
        self.archive = archive  # type: bool
        self.avatar_url = avatar_url  # type: str
        self.created_at = created_at  # type: str
        self.creator_id = creator_id  # type: long
        self.default_branch = default_branch  # type: str
        self.description = description  # type: str
        self.http_url_to_repo = http_url_to_repo  # type: str
        self.id = id  # type: long
        self.last_activity_at = last_activity_at  # type: str
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.namespace = namespace  # type: UpdateRepositoryResponseBodyResultNamespace
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.ssh_url_to_repo = ssh_url_to_repo  # type: str
        self.visibility_level = visibility_level  # type: str
        self.web_url = web_url  # type: str

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super(UpdateRepositoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.description is not None:
            result['Description'] = self.description
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.id is not None:
            result['Id'] = self.id
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['Name'] = self.name
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Namespace') is not None:
            temp_model = UpdateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        return self


class UpdateRepositoryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateRepositoryResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRepositoryResponse, self).to_map()
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
            temp_model = UpdateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, sub_user_id=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, state=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.email is not None:
            result['Email'] = self.email
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class UpdateRepositoryMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateRepositoryMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateRepositoryMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateRepositoryMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRepositoryMemberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRepositoryMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRepositoryMemberResponse, self).to_map()
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
            temp_model = UpdateRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


