# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelArtifactBuildTaskRequest(TeaModel):
    def __init__(self, build_task_id=None, instance_id=None):
        # The ID of the artifact building task.
        self.build_task_id = build_task_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelArtifactBuildTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CancelArtifactBuildTaskResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelArtifactBuildTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelArtifactBuildTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelArtifactBuildTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelArtifactBuildTaskResponse, self).to_map()
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
            temp_model = CancelArtifactBuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRepoBuildRecordRequest(TeaModel):
    def __init__(self, build_record_id=None, instance_id=None, repo_id=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRepoBuildRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CancelRepoBuildRecordResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRepoBuildRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelRepoBuildRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelRepoBuildRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRepoBuildRecordResponse, self).to_map()
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
            temp_model = CancelRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None, resource_id=None, resource_region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        # Id of the request
        self.resource_id = resource_id  # type: str
        self.resource_region_id = resource_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactBuildRuleRequest(TeaModel):
    def __init__(self, artifact_type=None, instance_id=None, parameters=None, scope_id=None, scope_type=None):
        self.artifact_type = artifact_type  # type: str
        self.instance_id = instance_id  # type: str
        self.parameters = parameters  # type: dict[str, any]
        self.scope_id = scope_id  # type: str
        self.scope_type = scope_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class CreateArtifactBuildRuleShrinkRequest(TeaModel):
    def __init__(self, artifact_type=None, instance_id=None, parameters_shrink=None, scope_id=None, scope_type=None):
        self.artifact_type = artifact_type  # type: str
        self.instance_id = instance_id  # type: str
        self.parameters_shrink = parameters_shrink  # type: str
        self.scope_id = scope_id  # type: str
        self.scope_type = scope_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactBuildRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class CreateArtifactBuildRuleResponseBody(TeaModel):
    def __init__(self, build_rule_id=None, code=None, is_success=None, request_id=None):
        self.build_rule_id = build_rule_id  # type: str
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateArtifactBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateArtifactBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateArtifactBuildRuleResponse, self).to_map()
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
            temp_model = CreateArtifactBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRecordRequest(TeaModel):
    def __init__(self, build_record_id=None, instance_id=None, repo_id=None):
        self.build_record_id = build_record_id  # type: str
        self.instance_id = instance_id  # type: str
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBuildRecordByRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateBuildRecordByRecordResponseBody(TeaModel):
    def __init__(self, build_record_id=None, code=None, is_success=None, request_id=None):
        self.build_record_id = build_record_id  # type: str
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBuildRecordByRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBuildRecordByRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBuildRecordByRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBuildRecordByRecordResponse, self).to_map()
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
            temp_model = CreateBuildRecordByRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRuleRequest(TeaModel):
    def __init__(self, build_rule_id=None, instance_id=None, repo_id=None):
        # The ID of the image building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBuildRecordByRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateBuildRecordByRuleResponseBody(TeaModel):
    def __init__(self, build_record_id=None, code=None, is_success=None, request_id=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBuildRecordByRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBuildRecordByRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBuildRecordByRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBuildRecordByRuleResponse, self).to_map()
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
            temp_model = CreateBuildRecordByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChainRequest(TeaModel):
    def __init__(self, chain_config=None, description=None, instance_id=None, name=None, repo_name=None,
                 repo_namespace_name=None, scope_exclude=None):
        # The configuration of the delivery chain in the JSON format.
        self.chain_config = chain_config  # type: str
        # The description of the delivery chain.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the delivery chain.
        self.name = name  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # Repositories in which the delivery chain does not take effect.
        self.scope_exclude = scope_exclude  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            self.chain_config = m.get('ChainConfig')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        return self


class CreateChainResponseBody(TeaModel):
    def __init__(self, chain_id=None, code=None, is_success=None, request_id=None):
        # The ID of the delivery chain.
        self.chain_id = chain_id  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateChainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChainResponse, self).to_map()
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
            temp_model = CreateChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChartNamespaceRequest(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_name=None):
        # Specifies whether to automatically create repositories in the namespace. Valid values:
        # 
        # \-`  true `: automatically creates repositories in the namespace.
        # 
        # \-`  false `: does not automatically create repositories in the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChartNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateChartNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChartNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChartNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateChartNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChartNamespaceResponse, self).to_map()
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
            temp_model = CreateChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChartRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_name=None, repo_namespace_name=None, repo_type=None, summary=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        # 
        # You can specify the RepoType or Summary parameter. The RepoType parameter is optional.
        self.repo_type = repo_type  # type: str
        # The summary of the repository.
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChartRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class CreateChartRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, repo_id=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChartRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChartRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateChartRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChartRepositoryResponse, self).to_map()
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
            temp_model = CreateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(self, comment=None, endpoint_type=None, entry=None, instance_id=None, module_name=None):
        # The description.
        self.comment = comment  # type: str
        # The type of the endpoint. Set the value to Internet.
        self.endpoint_type = endpoint_type  # type: str
        # The CIDR block that is accessible.
        self.entry = entry  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceEndpointAclPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class CreateInstanceEndpointAclPolicyResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceEndpointAclPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceEndpointAclPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceEndpointAclPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceEndpointAclPolicyResponse, self).to_map()
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
            temp_model = CreateInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(self, enable_create_dnsrecord_in_pvzt=None, instance_id=None, module_name=None, vpc_id=None,
                 vswitch_id=None):
        self.enable_create_dnsrecord_in_pvzt = enable_create_dnsrecord_in_pvzt  # type: bool
        self.instance_id = instance_id  # type: str
        self.module_name = module_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceVpcEndpointLinkedVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_create_dnsrecord_in_pvzt is not None:
            result['EnableCreateDNSRecordInPvzt'] = self.enable_create_dnsrecord_in_pvzt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableCreateDNSRecordInPvzt') is not None:
            self.enable_create_dnsrecord_in_pvzt = m.get('EnableCreateDNSRecordInPvzt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateInstanceVpcEndpointLinkedVpcResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceVpcEndpointLinkedVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceVpcEndpointLinkedVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceVpcEndpointLinkedVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceVpcEndpointLinkedVpcResponse, self).to_map()
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
            temp_model = CreateInstanceVpcEndpointLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_name=None):
        # Specifies whether to automatically create an image repository in the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The default type of the repository that is automatically created. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace. The name must be 2 to 120 characters in length, and can contain lowercase letters, digits, and the following delimiters: underscores (\_), hyphens (-), and periods (.). The name cannot start or end with a delimiter.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoBuildRuleRequest(TeaModel):
    def __init__(self, build_args=None, dockerfile_location=None, dockerfile_name=None, image_tag=None,
                 instance_id=None, platforms=None, push_name=None, push_type=None, repo_id=None):
        # Building arguments.
        self.build_args = build_args  # type: list[str]
        # The path of the Dockerfile.
        self.dockerfile_location = dockerfile_location  # type: str
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name  # type: str
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Architecture for image building. Valid values:
        # 
        # *   `linux/amd64`
        # *   `linux/arm64`
        # *   `linux/386`
        # *   `linux/arm/v7`
        # *   `inux/arm/v6`
        # 
        # Default value: `linux/amd64`
        self.platforms = platforms  # type: list[str]
        # The name of the push that triggers the building rule.
        self.push_name = push_name  # type: str
        # The type of the push that triggers the building rule. Valid values:
        # 
        # *   `GIT_TAG`: tag push
        # *   `GIT_BRANCH`: branch push
        self.push_type = push_type  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateRepoBuildRuleResponseBody(TeaModel):
    def __init__(self, build_rule_id=None, code=None, is_success=None, request_id=None):
        # The ID of the building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoBuildRuleResponse, self).to_map()
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
            temp_model = CreateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(self, auto_build=None, code_repo_name=None, code_repo_namespace_name=None, code_repo_type=None,
                 disable_cache_build=None, instance_id=None, oversea_build=None, repo_id=None):
        # Specifies whether to trigger image building when source code is committed. Valid values:
        # 
        # *   `true`: triggers image building when source code is committed.
        # *   `false`: does not trigger image building when source code is committed.
        self.auto_build = auto_build  # type: bool
        # The name of the source code repository.
        self.code_repo_name = code_repo_name  # type: str
        # The namespace to which the source code repository belongs.
        self.code_repo_namespace_name = code_repo_namespace_name  # type: str
        # The type of the source code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        self.code_repo_type = code_repo_type  # type: str
        # Specifies whether to disable building caches. Valid values:
        # 
        # *   `true`: disables building caches.
        # *   `false`: enables building caches.
        self.disable_cache_build = disable_cache_build  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Specifies whether to enable Build With Servers Deployed Outside Chinese Mainland. Valid values:
        # 
        # *   `true`: enables Build With Servers Deployed Outside Chinese Mainland.
        # *   `false`: does not enable Build With Servers Deployed Outside Chinese Mainland.
        self.oversea_build = oversea_build  # type: bool
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSourceCodeRepoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSourceCodeRepoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoSourceCodeRepoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoSourceCodeRepoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoSourceCodeRepoResponse, self).to_map()
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
            temp_model = CreateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncRuleRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None, repo_name=None, sync_rule_name=None, sync_scope=None,
                 sync_trigger=None, tag_filter=None, target_instance_id=None, target_namespace_name=None, target_region_id=None,
                 target_repo_name=None, target_user_id=None):
        self.instance_id = instance_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.repo_name = repo_name  # type: str
        self.sync_rule_name = sync_rule_name  # type: str
        self.sync_scope = sync_scope  # type: str
        self.sync_trigger = sync_trigger  # type: str
        self.tag_filter = tag_filter  # type: str
        self.target_instance_id = target_instance_id  # type: str
        self.target_namespace_name = target_namespace_name  # type: str
        self.target_region_id = target_region_id  # type: str
        self.target_repo_name = target_repo_name  # type: str
        self.target_user_id = target_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class CreateRepoSyncRuleResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, sync_rule_id=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str
        self.sync_rule_id = sync_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        return self


class CreateRepoSyncRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoSyncRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoSyncRuleResponse, self).to_map()
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
            temp_model = CreateRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncTaskRequest(TeaModel):
    def __init__(self, instance_id=None, override=None, repo_id=None, tag=None, target_instance_id=None,
                 target_namespace=None, target_region_id=None, target_repo_name=None, target_tag=None, target_user_id=None):
        self.instance_id = instance_id  # type: str
        self.override = override  # type: bool
        self.repo_id = repo_id  # type: str
        self.tag = tag  # type: str
        self.target_instance_id = target_instance_id  # type: str
        self.target_namespace = target_namespace  # type: str
        self.target_region_id = target_region_id  # type: str
        self.target_repo_name = target_repo_name  # type: str
        self.target_tag = target_tag  # type: str
        self.target_user_id = target_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.override is not None:
            result['Override'] = self.override
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace is not None:
            result['TargetNamespace'] = self.target_namespace
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.target_tag is not None:
            result['TargetTag'] = self.target_tag
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespace') is not None:
            self.target_namespace = m.get('TargetNamespace')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('TargetTag') is not None:
            self.target_tag = m.get('TargetTag')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class CreateRepoSyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, sync_task_id=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str
        self.sync_task_id = sync_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        return self


class CreateRepoSyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoSyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoSyncTaskResponse, self).to_map()
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
            temp_model = CreateRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncTaskByRuleRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, sync_rule_id=None, tag=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id  # type: str
        # The version of the image to be synchronized.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncTaskByRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateRepoSyncTaskByRuleResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, sync_task_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoSyncTaskByRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        return self


class CreateRepoSyncTaskByRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoSyncTaskByRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoSyncTaskByRuleResponse, self).to_map()
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
            temp_model = CreateRepoSyncTaskByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagRequest(TeaModel):
    def __init__(self, from_tag=None, instance_id=None, namespace_name=None, repo_name=None, to_tag=None):
        # The source image tag.
        self.from_tag = from_tag  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The image tag that you want to create.
        self.to_tag = to_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_tag is not None:
            result['FromTag'] = self.from_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.to_tag is not None:
            result['ToTag'] = self.to_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromTag') is not None:
            self.from_tag = m.get('FromTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('ToTag') is not None:
            self.to_tag = m.get('ToTag')
        return self


class CreateRepoTagResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoTagResponse, self).to_map()
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
            temp_model = CreateRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagScanTaskRequest(TeaModel):
    def __init__(self, digest=None, instance_id=None, repo_id=None, scan_service=None, tag=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The type of the scanning engine.
        # 
        # *   `SAS_SCAN_SERVICE`: Security Center scan engine (paid service)
        # *   `ACR_SCAN_SERVICE`: Container Registry scan engine
        self.scan_service = scan_service  # type: str
        # The version of the image.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTagScanTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateRepoTagScanTaskResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTagScanTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoTagScanTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoTagScanTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoTagScanTaskResponse, self).to_map()
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
            temp_model = CreateRepoTagScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTriggerRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, trigger_name=None, trigger_tag=None, trigger_type=None,
                 trigger_url=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The name of the trigger.
        self.trigger_name = trigger_name  # type: str
        # The image tag based on which the trigger is set.
        # 
        # > 
        # 
        # *   If `TriggerType` is set to `ALL`, `TriggerTag` can be set to a string or an array, for example, `*`.
        # 
        # *   If `TriggerType` is set to `TAG_LIST`, `TriggerTag` must be set to an array, for example, `[1]`.
        # *   If `TriggerType` is set to `TAG_REG_EXP`, `TriggerTag` must be set to a string, for example, `*`.
        self.trigger_tag = trigger_tag  # type: str
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LIST`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type  # type: str
        # The URL of the trigger.
        self.trigger_url = trigger_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        return self


class CreateRepoTriggerResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, trigger_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the trigger.
        self.trigger_id = trigger_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepoTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        return self


class CreateRepoTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRepoTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepoTriggerResponse, self).to_map()
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
            temp_model = CreateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(self, detail=None, instance_id=None, repo_name=None, repo_namespace_name=None, repo_type=None,
                 summary=None, tag_immutability=None):
        # The description of the repository.
        self.detail = detail  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the image repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: The repository is a public repository.
        # *   `PRIVATE`: The repository is a private repository.
        self.repo_type = repo_type  # type: str
        # The summary about the repository.
        self.summary = summary  # type: str
        # Specifies whether to enable the feature of image tag immutability. Valid values:
        # 
        # *   `true`: enables the feature of image tag immutability.
        # *   `false`: disables the feature of image tag immutability.
        self.tag_immutability = tag_immutability  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, repo_id=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DeleteChainRequest(TeaModel):
    def __init__(self, chain_id=None, instance_id=None):
        # The ID of the delivery pipeline.
        self.chain_id = chain_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteChainResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChainResponse, self).to_map()
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
            temp_model = DeleteChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the chart namespace that you want to delete.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DeleteChartNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChartNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChartNamespaceResponse, self).to_map()
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
            temp_model = DeleteChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartReleaseRequest(TeaModel):
    def __init__(self, chart=None, instance_id=None, release=None, repo_name=None, repo_namespace_name=None):
        # The name of the chart.
        self.chart = chart  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The version of the chart that you want to delete.
        self.release = release  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartReleaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.release is not None:
            result['Release'] = self.release
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class DeleteChartReleaseResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartReleaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartReleaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChartReleaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChartReleaseResponse, self).to_map()
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
            temp_model = DeleteChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_name=None, repo_namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class DeleteChartRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChartRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChartRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChartRepositoryResponse, self).to_map()
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
            temp_model = DeleteChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventCenterRuleRequest(TeaModel):
    def __init__(self, instance_id=None, rule_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventCenterRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteEventCenterRuleResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventCenterRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEventCenterRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventCenterRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventCenterRuleResponse, self).to_map()
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
            temp_model = DeleteEventCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(self, endpoint_type=None, entry=None, instance_id=None, module_name=None):
        # The type of the endpoint. Set the value to Internet.
        self.endpoint_type = endpoint_type  # type: str
        # The CIDR block.
        self.entry = entry  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceEndpointAclPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class DeleteInstanceEndpointAclPolicyResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceEndpointAclPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceEndpointAclPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceEndpointAclPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceEndpointAclPolicyResponse, self).to_map()
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
            temp_model = DeleteInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(self, instance_id=None, module_name=None, vpc_id=None, vswitch_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceVpcEndpointLinkedVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DeleteInstanceVpcEndpointLinkedVpcResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceVpcEndpointLinkedVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceVpcEndpointLinkedVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceVpcEndpointLinkedVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceVpcEndpointLinkedVpcResponse, self).to_map()
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
            temp_model = DeleteInstanceVpcEndpointLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNamespaceResponse, self).to_map()
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoBuildRuleRequest(TeaModel):
    def __init__(self, build_rule_id=None, instance_id=None, repo_id=None):
        # The ID of the image building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class DeleteRepoBuildRuleResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepoBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepoBuildRuleResponse, self).to_map()
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
            temp_model = DeleteRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoSyncRuleRequest(TeaModel):
    def __init__(self, instance_id=None, sync_rule_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoSyncRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        return self


class DeleteRepoSyncRuleResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoSyncRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoSyncRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepoSyncRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepoSyncRuleResponse, self).to_map()
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
            temp_model = DeleteRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoTagRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, tag=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The tag of the image.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DeleteRepoTagResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepoTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepoTagResponse, self).to_map()
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
            temp_model = DeleteRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoTriggerRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, trigger_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The ID of the trigger.
        self.trigger_id = trigger_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        return self


class DeleteRepoTriggerResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepoTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRepoTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRepoTriggerResponse, self).to_map()
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
            temp_model = DeleteRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, repo_name=None, repo_namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class DeleteRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetArtifactBuildRuleRequest(TeaModel):
    def __init__(self, artifact_type=None, build_rule_id=None, instance_id=None, scope_id=None, scope_type=None):
        self.artifact_type = artifact_type  # type: str
        self.build_rule_id = build_rule_id  # type: str
        self.instance_id = instance_id  # type: str
        self.scope_id = scope_id  # type: str
        self.scope_type = scope_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetArtifactBuildRuleResponseBody(TeaModel):
    def __init__(self, artifact_type=None, build_rule_id=None, code=None, is_success=None, request_id=None,
                 scope_id=None, scope_type=None):
        self.artifact_type = artifact_type  # type: str
        self.build_rule_id = build_rule_id  # type: str
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str
        self.scope_id = scope_id  # type: str
        self.scope_type = scope_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetArtifactBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetArtifactBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetArtifactBuildRuleResponse, self).to_map()
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
            temp_model = GetArtifactBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactBuildTaskRequest(TeaModel):
    def __init__(self, build_task_id=None, instance_id=None):
        # The ID of the artifact building task.
        self.build_task_id = build_task_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactBuildTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetArtifactBuildTaskResponseBodySourceArtifact(TeaModel):
    def __init__(self, artifact_type=None, repo_id=None, version=None):
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type  # type: str
        # The ID of the repository to which the source artifact belongs. The repository can only be an image repository.
        self.repo_id = repo_id  # type: str
        # The version of the artifact. The artifact can only be an image.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactBuildTaskResponseBodySourceArtifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetArtifactBuildTaskResponseBodyTargetArtifact(TeaModel):
    def __init__(self, artifact_type=None, repo_id=None, version=None):
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type  # type: str
        # The ID of the repository to which the artifact that is built in the task belongs. The repository can only be an image repository. The value is the same as the ID of the repository to which the source artifact belongs.
        self.repo_id = repo_id  # type: str
        # The version of the artifact that is built in the task. The artifact can only be an image.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactBuildTaskResponseBodyTargetArtifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetArtifactBuildTaskResponseBody(TeaModel):
    def __init__(self, artifact_build_type=None, build_task_id=None, code=None, end_time=None, instructions=None,
                 is_success=None, request_id=None, source_artifact=None, start_time=None, target_artifact=None,
                 task_status=None):
        # The type of the artifact building task. Valid values:
        # 
        # *   `IMAGE_TO_ACCELERATED_IMAGE`: builds accelerated images for Container Service for Kubernetes (ACK) clusters.
        # *   `IMAGE_TO_ECI_ACCELERATED_IMAGE`: builds accelerated images for elastic container instances.
        self.artifact_build_type = artifact_build_type  # type: str
        # The ID of the artifact building task.
        self.build_task_id = build_task_id  # type: str
        # The return value.
        self.code = code  # type: str
        # The time when the artifact building task ends.
        self.end_time = end_time  # type: int
        self.instructions = instructions  # type: list[str]
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the source artifact.
        self.source_artifact = source_artifact  # type: GetArtifactBuildTaskResponseBodySourceArtifact
        # The time when the artifact building task starts.
        self.start_time = start_time  # type: int
        # The artifact that is built in the task.
        self.target_artifact = target_artifact  # type: GetArtifactBuildTaskResponseBodyTargetArtifact
        # The status of the artifact that is built in the task. Valid values:
        # 
        # *   `PENDING`: The artifact is being scheduled.
        # *   `BUILDING`: The artifact is being built.
        # *   `SUCCESS`: The artifact is built.
        # *   `FAILED`: The artifact fails to be built.
        self.task_status = task_status  # type: str

    def validate(self):
        if self.source_artifact:
            self.source_artifact.validate()
        if self.target_artifact:
            self.target_artifact.validate()

    def to_map(self):
        _map = super(GetArtifactBuildTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instructions is not None:
            result['Instructions'] = self.instructions
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_artifact is not None:
            result['SourceArtifact'] = self.source_artifact.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.target_artifact is not None:
            result['TargetArtifact'] = self.target_artifact.to_map()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodySourceArtifact()
            self.source_artifact = temp_model.from_map(m['SourceArtifact'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TargetArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodyTargetArtifact()
            self.target_artifact = temp_model.from_map(m['TargetArtifact'])
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetArtifactBuildTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetArtifactBuildTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetArtifactBuildTaskResponse, self).to_map()
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
            temp_model = GetArtifactBuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationTokenRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the request.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAuthorizationTokenResponseBody(TeaModel):
    def __init__(self, authorization_token=None, code=None, expire_time=None, is_success=None, request_id=None,
                 temp_username=None):
        # The temporary password returned after you call this API operation is a Security Token Service (STS) token whose validity period is 1 hour. Take note of the following items when you log on to Container Registry instances by using an STS token:
        # 
        # *   If the STS token belongs to an Alibaba Cloud account, you can use the STS token to log on to all Container Registry instances that belong to the Alibaba Cloud account.
        # *   If the STS token belongs to a Resource Access Management (RAM) user, you can use the STS token to log on to all Container Registry instances that belong to the RAM user.
        # *   You can use an STS token to access only Container Registry instances to which the STS token is scoped.
        self.authorization_token = authorization_token  # type: str
        # Indicates whether the API call is successful.
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.code = code  # type: str
        # The return value.
        self.expire_time = expire_time  # type: long
        # The username that is used to log on to the Container Registry instance.
        self.is_success = is_success  # type: bool
        # The timestamp when the temporary password expires. Unit: milliseconds.
        self.request_id = request_id  # type: str
        # The password that is used to log on to the Container Registry instance.
        self.temp_username = temp_username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_token is not None:
            result['AuthorizationToken'] = self.authorization_token
        if self.code is not None:
            result['Code'] = self.code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.temp_username is not None:
            result['TempUsername'] = self.temp_username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationToken') is not None:
            self.authorization_token = m.get('AuthorizationToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TempUsername') is not None:
            self.temp_username = m.get('TempUsername')
        return self


class GetAuthorizationTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuthorizationTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthorizationTokenResponse, self).to_map()
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
            temp_model = GetAuthorizationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChainRequest(TeaModel):
    def __init__(self, chain_id=None, instance_id=None):
        self.chain_id = chain_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy(TeaModel):
    def __init__(self, action=None, baseline_list=None, issue_count=None, issue_level=None, issue_list=None,
                 logic=None, malicious_list=None):
        self.action = action  # type: str
        self.baseline_list = baseline_list  # type: str
        self.issue_count = issue_count  # type: str
        self.issue_level = issue_level  # type: str
        self.issue_list = issue_list  # type: str
        self.logic = logic  # type: str
        self.malicious_list = malicious_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.baseline_list is not None:
            result['BaselineList'] = self.baseline_list
        if self.issue_count is not None:
            result['IssueCount'] = self.issue_count
        if self.issue_level is not None:
            result['IssueLevel'] = self.issue_level
        if self.issue_list is not None:
            result['IssueList'] = self.issue_list
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.malicious_list is not None:
            result['MaliciousList'] = self.malicious_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('BaselineList') is not None:
            self.baseline_list = m.get('BaselineList')
        if m.get('IssueCount') is not None:
            self.issue_count = m.get('IssueCount')
        if m.get('IssueLevel') is not None:
            self.issue_level = m.get('IssueLevel')
        if m.get('IssueList') is not None:
            self.issue_list = m.get('IssueList')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MaliciousList') is not None:
            self.malicious_list = m.get('MaliciousList')
        return self


class GetChainResponseBodyChainConfigNodesNodeConfig(TeaModel):
    def __init__(self, deny_policy=None, retry=None, scan_engine=None, timeout=None):
        self.deny_policy = deny_policy  # type: GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy
        self.retry = retry  # type: int
        self.scan_engine = scan_engine  # type: str
        self.timeout = timeout  # type: long

    def validate(self):
        if self.deny_policy:
            self.deny_policy.validate()

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigNodesNodeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny_policy is not None:
            result['DenyPolicy'] = self.deny_policy.to_map()
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.scan_engine is not None:
            result['ScanEngine'] = self.scan_engine
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DenyPolicy') is not None:
            temp_model = GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy()
            self.deny_policy = temp_model.from_map(m['DenyPolicy'])
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('ScanEngine') is not None:
            self.scan_engine = m.get('ScanEngine')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class GetChainResponseBodyChainConfigNodes(TeaModel):
    def __init__(self, enable=None, node_config=None, node_name=None):
        self.enable = enable  # type: bool
        self.node_config = node_config  # type: GetChainResponseBodyChainConfigNodesNodeConfig
        self.node_name = node_name  # type: str

    def validate(self):
        if self.node_config:
            self.node_config.validate()

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.node_config is not None:
            result['NodeConfig'] = self.node_config.to_map()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NodeConfig') is not None:
            temp_model = GetChainResponseBodyChainConfigNodesNodeConfig()
            self.node_config = temp_model.from_map(m['NodeConfig'])
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRoutersFrom(TeaModel):
    def __init__(self, node_name=None):
        self.node_name = node_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigRoutersFrom, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRoutersTo(TeaModel):
    def __init__(self, node_name=None):
        self.node_name = node_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigRoutersTo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRouters(TeaModel):
    def __init__(self, from_=None, to=None):
        self.from_ = from_  # type: GetChainResponseBodyChainConfigRoutersFrom
        self.to = to  # type: GetChainResponseBodyChainConfigRoutersTo

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfigRouters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_.to_map()
        if self.to is not None:
            result['To'] = self.to.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            temp_model = GetChainResponseBodyChainConfigRoutersFrom()
            self.from_ = temp_model.from_map(m['From'])
        if m.get('To') is not None:
            temp_model = GetChainResponseBodyChainConfigRoutersTo()
            self.to = temp_model.from_map(m['To'])
        return self


class GetChainResponseBodyChainConfig(TeaModel):
    def __init__(self, chain_config_id=None, is_active=None, nodes=None, routers=None, version=None):
        self.chain_config_id = chain_config_id  # type: str
        self.is_active = is_active  # type: bool
        self.nodes = nodes  # type: list[GetChainResponseBodyChainConfigNodes]
        self.routers = routers  # type: list[GetChainResponseBodyChainConfigRouters]
        self.version = version  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.routers:
            for k in self.routers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChainResponseBodyChainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config_id is not None:
            result['ChainConfigId'] = self.chain_config_id
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Routers'] = []
        if self.routers is not None:
            for k in self.routers:
                result['Routers'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainConfigId') is not None:
            self.chain_config_id = m.get('ChainConfigId')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetChainResponseBodyChainConfigNodes()
                self.nodes.append(temp_model.from_map(k))
        self.routers = []
        if m.get('Routers') is not None:
            for k in m.get('Routers'):
                temp_model = GetChainResponseBodyChainConfigRouters()
                self.routers.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetChainResponseBody(TeaModel):
    def __init__(self, chain_config=None, chain_id=None, code=None, create_time=None, description=None,
                 instance_id=None, is_success=None, modified_time=None, name=None, request_id=None, scope_exclude=None,
                 scope_id=None, scope_type=None):
        self.chain_config = chain_config  # type: GetChainResponseBodyChainConfig
        self.chain_id = chain_id  # type: str
        self.code = code  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.is_success = is_success  # type: bool
        self.modified_time = modified_time  # type: long
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.scope_exclude = scope_exclude  # type: list[str]
        self.scope_id = scope_id  # type: str
        self.scope_type = scope_type  # type: str

    def validate(self):
        if self.chain_config:
            self.chain_config.validate()

    def to_map(self):
        _map = super(GetChainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config.to_map()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            temp_model = GetChainResponseBodyChainConfig()
            self.chain_config = temp_model.from_map(m['ChainConfig'])
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetChainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChainResponse, self).to_map()
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
            temp_model = GetChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChartNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChartNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetChartNamespaceResponseBody(TeaModel):
    def __init__(self, auto_create_repo=None, code=None, default_repo_type=None, instance_id=None, is_success=None,
                 namespace_id=None, namespace_name=None, namespace_status=None, request_id=None, resource_group_id=None):
        # Indicates whether a repository was automatically created in the namespace. Valid values:
        # 
        # *   `true`: A repository was automatically created in the namespace.
        # *   `false`: No repository was automatically created in the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The return value.
        self.code = code  # type: str
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the namespace.
        self.namespace_id = namespace_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChartNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.code is not None:
            result['Code'] = self.code
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetChartNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChartNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChartNamespaceResponse, self).to_map()
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
            temp_model = GetChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChartRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_name=None, repo_namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChartRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetChartRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, create_time=None, instance_id=None, is_success=None, modified_time=None,
                 repo_id=None, repo_name=None, repo_namespace_name=None, repo_status=None, repo_type=None, request_id=None,
                 resource_group_id=None, summary=None):
        # The return value.
        self.code = code  # type: str
        # The time when the chart repository was created.
        self.create_time = create_time  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The time when the chart repository was last modified.
        self.modified_time = modified_time  # type: long
        # The ID of the chart repository.
        self.repo_id = repo_id  # type: str
        # The name of the chart repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the chart repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The status of the chart repository. Valid values:
        # 
        # *   `NORMAL`: The repository is normal.
        # *   `DELETING`: The repository is being deleted.
        self.repo_status = repo_status  # type: str
        # The type of the chart repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.repo_type = repo_type  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The summary about the chart repository.
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChartRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetChartRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChartRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChartRepositoryResponse, self).to_map()
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
            temp_model = GetChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, code=None, create_time=None, instance_id=None, instance_issue=None, instance_name=None,
                 instance_specification=None, instance_status=None, is_success=None, modified_time=None, request_id=None,
                 resource_group_id=None):
        self.code = code  # type: str
        self.create_time = create_time  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_issue = instance_issue  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_specification = instance_specification  # type: str
        self.instance_status = instance_status  # type: str
        self.is_success = is_success  # type: bool
        self.modified_time = modified_time  # type: long
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_issue is not None:
            result['InstanceIssue'] = self.instance_issue
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIssue') is not None:
            self.instance_issue = m.get('InstanceIssue')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceCountResponseBody(TeaModel):
    def __init__(self, code=None, count=None, is_success=None, request_id=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceCountResponse, self).to_map()
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
            temp_model = GetInstanceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceEndpointRequest(TeaModel):
    def __init__(self, endpoint_type=None, instance_id=None, module_name=None):
        # The type of the endpoint. Set the value to Internet.
        self.endpoint_type = endpoint_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class GetInstanceEndpointResponseBodyAclEntries(TeaModel):
    def __init__(self, comment=None, entry=None):
        # Remarks for public IP address whitelists.
        self.comment = comment  # type: str
        # The public IP address whitelist.
        self.entry = entry  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceEndpointResponseBodyAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class GetInstanceEndpointResponseBodyDomains(TeaModel):
    def __init__(self, domain=None, type=None):
        # The domain name that is used to access the Container Registry Enterprise Edition instance.
        self.domain = domain  # type: str
        # The type of the domain name. Valid values:
        # 
        # *   `SYSTEM`: a system domain name.
        # *   `USER`: a user domain name.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceEndpointResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceEndpointResponseBody(TeaModel):
    def __init__(self, acl_enable=None, acl_entries=None, code=None, domains=None, enable=None, is_success=None,
                 request_id=None, status=None):
        # Indicates whether the access control list (ACL) feature is enabled.
        self.acl_enable = acl_enable  # type: bool
        # The ACLs.
        self.acl_entries = acl_entries  # type: list[GetInstanceEndpointResponseBodyAclEntries]
        # The return value.
        self.code = code  # type: str
        # Domain names.
        self.domains = domains  # type: list[GetInstanceEndpointResponseBodyDomains]
        # Indicates whether the ACL feature is enabled.
        self.enable = enable  # type: bool
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the instance.
        self.status = status  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetInstanceEndpointResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = GetInstanceEndpointResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceEndpointResponse, self).to_map()
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
            temp_model = GetInstanceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceUsageRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceUsageResponseBody(TeaModel):
    def __init__(self, chart_namespace_quota=None, chart_namespace_usage=None, chart_repo_quota=None,
                 chart_repo_usage=None, code=None, is_success=None, namespace_quota=None, namespace_usage=None, repo_quota=None,
                 repo_usage=None, request_id=None):
        # The quota of chart namespaces.
        self.chart_namespace_quota = chart_namespace_quota  # type: str
        # The number of chart namespaces that are created in the instance.
        self.chart_namespace_usage = chart_namespace_usage  # type: str
        # The quota of chart repositories for the instance.
        self.chart_repo_quota = chart_repo_quota  # type: str
        # The number of chart repositories that are created.
        self.chart_repo_usage = chart_repo_usage  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The quota of image namespaces for the instance.
        self.namespace_quota = namespace_quota  # type: str
        # The number of image namespaces that are created in the instance.
        self.namespace_usage = namespace_usage  # type: str
        # The quota of image repositories for the instance.
        self.repo_quota = repo_quota  # type: str
        # The number of image repositories that are created in the instance.
        self.repo_usage = repo_usage  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_namespace_quota is not None:
            result['ChartNamespaceQuota'] = self.chart_namespace_quota
        if self.chart_namespace_usage is not None:
            result['ChartNamespaceUsage'] = self.chart_namespace_usage
        if self.chart_repo_quota is not None:
            result['ChartRepoQuota'] = self.chart_repo_quota
        if self.chart_repo_usage is not None:
            result['ChartRepoUsage'] = self.chart_repo_usage
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota
        if self.namespace_usage is not None:
            result['NamespaceUsage'] = self.namespace_usage
        if self.repo_quota is not None:
            result['RepoQuota'] = self.repo_quota
        if self.repo_usage is not None:
            result['RepoUsage'] = self.repo_usage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChartNamespaceQuota') is not None:
            self.chart_namespace_quota = m.get('ChartNamespaceQuota')
        if m.get('ChartNamespaceUsage') is not None:
            self.chart_namespace_usage = m.get('ChartNamespaceUsage')
        if m.get('ChartRepoQuota') is not None:
            self.chart_repo_quota = m.get('ChartRepoQuota')
        if m.get('ChartRepoUsage') is not None:
            self.chart_repo_usage = m.get('ChartRepoUsage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')
        if m.get('NamespaceUsage') is not None:
            self.namespace_usage = m.get('NamespaceUsage')
        if m.get('RepoQuota') is not None:
            self.repo_quota = m.get('RepoQuota')
        if m.get('RepoUsage') is not None:
            self.repo_usage = m.get('RepoUsage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceUsageResponse, self).to_map()
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
            temp_model = GetInstanceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceVpcEndpointRequest(TeaModel):
    def __init__(self, instance_id=None, module_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class GetInstanceVpcEndpointResponseBodyLinkedVpcs(TeaModel):
    def __init__(self, default_access=None, ip=None, status=None, vpc_id=None, vswitch_id=None):
        # Indicates whether the default ACL is used.
        self.default_access = default_access  # type: bool
        # IP address.
        self.ip = ip  # type: str
        # The status of the VPC. Valid values:
        # 
        # *   `CREATING`: The VPC is being created.
        # *   `RUNNING`: The VPC is running.
        self.status = status  # type: str
        # VPC ID
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceVpcEndpointResponseBodyLinkedVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_access is not None:
            result['DefaultAccess'] = self.default_access
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultAccess') is not None:
            self.default_access = m.get('DefaultAccess')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class GetInstanceVpcEndpointResponseBody(TeaModel):
    def __init__(self, code=None, domains=None, enable=None, is_success=None, linked_vpcs=None, module_name=None,
                 request_id=None):
        # The return value.
        self.code = code  # type: str
        self.domains = domains  # type: list[str]
        # Indicates whether the access control list (ACL) feature is enabled. Valid values:
        # 
        # *   `true`: The ACL feature is enabled.
        # *   `false`: The ACL feature is disabled.
        self.enable = enable  # type: bool
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The VPCs in which the instance is deployed.
        self.linked_vpcs = linked_vpcs  # type: list[GetInstanceVpcEndpointResponseBodyLinkedVpcs]
        self.module_name = module_name  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.linked_vpcs:
            for k in self.linked_vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceVpcEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = GetInstanceVpcEndpointResponseBodyLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceVpcEndpointResponse, self).to_map()
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
            temp_model = GetInstanceVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_id=None, namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the namespace.
        self.namespace_id = namespace_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetNamespaceResponseBody(TeaModel):
    def __init__(self, auto_create_repo=None, code=None, default_repo_type=None, instance_id=None, is_success=None,
                 namespace_id=None, namespace_name=None, namespace_status=None, request_id=None, resource_group_id=None):
        # Indicates whether a repository is automatically created when an image is pushed to the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The return value.
        self.code = code  # type: str
        # The default type of the repository. Valid values:
        # 
        # *   PUBLIC: The repository is a public repository.
        # *   PRIVATE: The repository is a private repository.
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the namespace.
        self.namespace_id = namespace_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The status of the namespace.
        self.namespace_status = namespace_status  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.code is not None:
            result['Code'] = self.code
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNamespaceResponse, self).to_map()
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
            temp_model = GetNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordRequest(TeaModel):
    def __init__(self, build_record_id=None, instance_id=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoBuildRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRepoBuildRecordResponseBodyImage(TeaModel):
    def __init__(self, image_tag=None, repo_name=None, repo_namespace_name=None):
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the image repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoBuildRecordResponseBodyImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoBuildRecordResponseBody(TeaModel):
    def __init__(self, build_record_id=None, code=None, end_time=None, image=None, is_success=None, request_id=None,
                 start_time=None, status=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The return value.
        self.code = code  # type: str
        # The time when the image building was completed.
        self.end_time = end_time  # type: long
        # The information about the image.
        self.image = image  # type: GetRepoBuildRecordResponseBodyImage
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The time when the image building started.
        self.start_time = start_time  # type: long
        # The status of the instance.
        self.status = status  # type: str

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super(GetRepoBuildRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Image') is not None:
            temp_model = GetRepoBuildRecordResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoBuildRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoBuildRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoBuildRecordResponse, self).to_map()
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
            temp_model = GetRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordStatusRequest(TeaModel):
    def __init__(self, build_record_id=None, instance_id=None, repo_id=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoBuildRecordStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class GetRepoBuildRecordStatusResponseBody(TeaModel):
    def __init__(self, build_status=None, code=None, is_success=None, request_id=None):
        # The status of the image building.
        self.build_status = build_status  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoBuildRecordStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoBuildRecordStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoBuildRecordStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoBuildRecordStatusResponse, self).to_map()
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
            temp_model = GetRepoBuildRecordStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoSourceCodeRepoRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None):
        # The ID of the Container Registry instance.
        self.instance_id = instance_id  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSourceCodeRepoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class GetRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(self, auto_build=None, code=None, code_repo_domain=None, code_repo_name=None,
                 code_repo_namespace_name=None, code_repo_type=None, disable_cache_build=None, is_success=None, oversea_build=None,
                 repo_id=None, request_id=None):
        # Indicates whether image building is automatically triggered when source code is committed. Valid values:
        # 
        # *   `true`: Image building is automatically triggered when source code is committed.
        # *   `false`: Image building is not triggered when source code is committed.
        self.auto_build = auto_build  # type: str
        # The response code.
        self.code = code  # type: str
        # The address of the source code repository.
        self.code_repo_domain = code_repo_domain  # type: str
        # The name of the source code repository.
        self.code_repo_name = code_repo_name  # type: str
        # The namespace to which the source code repository belongs.
        self.code_repo_namespace_name = code_repo_namespace_name  # type: str
        # The type of the code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        self.code_repo_type = code_repo_type  # type: str
        # Indicates whether build cache is disabled. Valid values:
        # 
        # *   `true`: Build cache is disabled.
        # *   `false`: Build cache is enabled.
        self.disable_cache_build = disable_cache_build  # type: str
        # Indicates whether the API call is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success  # type: bool
        # Indicates whether image building is accelerated for servers outside the Chinese mainland. Valid values:
        # 
        # *   `true`: Image building is accelerated for servers outside the Chinese mainland.
        # *   `false`: Image building is not accelerated for servers outside the Chinese mainland.
        self.oversea_build = oversea_build  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSourceCodeRepoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code is not None:
            result['Code'] = self.code
        if self.code_repo_domain is not None:
            result['CodeRepoDomain'] = self.code_repo_domain
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeRepoDomain') is not None:
            self.code_repo_domain = m.get('CodeRepoDomain')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoSourceCodeRepoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoSourceCodeRepoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoSourceCodeRepoResponse, self).to_map()
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
            temp_model = GetRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoSyncTaskRequest(TeaModel):
    def __init__(self, instance_id=None, sync_task_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        return self


class GetRepoSyncTaskResponseBodyImageFrom(TeaModel):
    def __init__(self, image_tag=None, instance_id=None, region_id=None, repo_name=None, repo_namespace_name=None):
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSyncTaskResponseBodyImageFrom, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoSyncTaskResponseBodyImageTo(TeaModel):
    def __init__(self, image_tag=None, instance_id=None, region_id=None, repo_name=None, repo_namespace_name=None):
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSyncTaskResponseBodyImageTo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoSyncTaskResponseBodyLayerTasks(TeaModel):
    def __init__(self, artifact_digest=None, digest=None, size=None, sync_layer_task_id=None, synced_size=None,
                 task_status=None):
        # The digest of the artifact.
        self.artifact_digest = artifact_digest  # type: str
        # The digest of the image layer.
        self.digest = digest  # type: str
        # The size of synchronized image layers.
        self.size = size  # type: long
        # The ID of the synchronization task for the image layer.
        self.sync_layer_task_id = sync_layer_task_id  # type: str
        # The size of the image layer that is synchronized.
        self.synced_size = synced_size  # type: long
        # The status of the synchronization task. Valid values:
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoSyncTaskResponseBodyLayerTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_digest is not None:
            result['ArtifactDigest'] = self.artifact_digest
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.size is not None:
            result['Size'] = self.size
        if self.sync_layer_task_id is not None:
            result['SyncLayerTaskId'] = self.sync_layer_task_id
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactDigest') is not None:
            self.artifact_digest = m.get('ArtifactDigest')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SyncLayerTaskId') is not None:
            self.sync_layer_task_id = m.get('SyncLayerTaskId')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetRepoSyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, cross_user=None, image_from=None, image_to=None, is_success=None, layer_tasks=None,
                 progress=None, request_id=None, sync_batch_task_id=None, sync_rule_id=None, sync_task_id=None,
                 sync_trans_accelerate=None, synced_size=None, task_status=None, task_trigger=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the synchronization task is performed across Alibaba Cloud accounts.
        self.cross_user = cross_user  # type: bool
        # The source address of the image.
        self.image_from = image_from  # type: GetRepoSyncTaskResponseBodyImageFrom
        # The destination address of the image.
        self.image_to = image_to  # type: GetRepoSyncTaskResponseBodyImageTo
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The synchronization tasks for the image layer.
        self.layer_tasks = layer_tasks  # type: list[GetRepoSyncTaskResponseBodyLayerTasks]
        # The synchronization progress. Valid values:
        # 
        # *   `0`: The synchronization starts or failed.
        # *   `1`: The synchronization is successful.
        self.progress = progress  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the synchronization task in which multiple images are synchronized at a time.
        self.sync_batch_task_id = sync_batch_task_id  # type: str
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id  # type: str
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id  # type: str
        # Indicates whether transfer acceleration is enabled in the synchronization process.
        self.sync_trans_accelerate = sync_trans_accelerate  # type: bool
        # The size of the image layer that is synchronized. Unit: bytes.
        self.synced_size = synced_size  # type: long
        # The status of the task. Valid values:
        self.task_status = task_status  # type: str
        # The policy that is used to trigger the synchronization task.
        self.task_trigger = task_trigger  # type: str

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()
        if self.layer_tasks:
            for k in self.layer_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRepoSyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['LayerTasks'] = []
        if self.layer_tasks is not None:
            for k in self.layer_tasks:
                result['LayerTasks'].append(k.to_map() if k else None)
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('ImageFrom') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.layer_tasks = []
        if m.get('LayerTasks') is not None:
            for k in m.get('LayerTasks'):
                temp_model = GetRepoSyncTaskResponseBodyLayerTasks()
                self.layer_tasks.append(temp_model.from_map(k))
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        return self


class GetRepoSyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoSyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoSyncTaskResponse, self).to_map()
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
            temp_model = GetRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, tag=None):
        # The return value of status code.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform. Set the value to **GetRepoTag**.
        self.repo_id = repo_id  # type: str
        # The number of milliseconds that have elapsed since the image was created.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagResponseBody(TeaModel):
    def __init__(self, code=None, digest=None, image_create=None, image_id=None, image_size=None, image_update=None,
                 is_success=None, request_id=None, status=None, tag=None):
        # The ID of the image.
        self.code = code  # type: str
        # The size of the image. Unit: Bytes.
        self.digest = digest  # type: str
        # crr-tquyps22md8p****\
        self.image_create = image_create  # type: long
        self.image_id = image_id  # type: str
        # The number of milliseconds that have elapsed since the image was last updated.
        self.image_size = image_size  # type: long
        # The ID of the request.
        self.image_update = image_update  # type: long
        # The status of the image. Valid values:
        # 
        # *   `NORMAL`: The image is normal.
        # *   `DELETING`: The image is being deleted.
        self.is_success = is_success  # type: bool
        # 1.0
        self.request_id = request_id  # type: str
        # The ID of the instance.
        self.status = status  # type: str
        # The version of the repository.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.image_create is not None:
            result['ImageCreate'] = self.image_create
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagResponse, self).to_map()
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
            temp_model = GetRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagLayersRequest(TeaModel):
    def __init__(self, digest=None, instance_id=None, repo_id=None, tag=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The tag of the image.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagLayersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagLayersResponseBodyLayers(TeaModel):
    def __init__(self, blob_digest=None, blob_size=None, layer_cmd=None, layer_index=None, layer_instruction=None):
        # The digest of a single image layer.
        self.blob_digest = blob_digest  # type: str
        # The size of the image layer.
        self.blob_size = blob_size  # type: long
        # Operation on the image layer.
        self.layer_cmd = layer_cmd  # type: str
        # The sequence number of the layer stack.
        self.layer_index = layer_index  # type: int
        # The command for the image layer.
        self.layer_instruction = layer_instruction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagLayersResponseBodyLayers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blob_digest is not None:
            result['BlobDigest'] = self.blob_digest
        if self.blob_size is not None:
            result['BlobSize'] = self.blob_size
        if self.layer_cmd is not None:
            result['LayerCMD'] = self.layer_cmd
        if self.layer_index is not None:
            result['LayerIndex'] = self.layer_index
        if self.layer_instruction is not None:
            result['LayerInstruction'] = self.layer_instruction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlobDigest') is not None:
            self.blob_digest = m.get('BlobDigest')
        if m.get('BlobSize') is not None:
            self.blob_size = m.get('BlobSize')
        if m.get('LayerCMD') is not None:
            self.layer_cmd = m.get('LayerCMD')
        if m.get('LayerIndex') is not None:
            self.layer_index = m.get('LayerIndex')
        if m.get('LayerInstruction') is not None:
            self.layer_instruction = m.get('LayerInstruction')
        return self


class GetRepoTagLayersResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, layers=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The queried image layers.
        self.layers = layers  # type: list[GetRepoTagLayersResponseBodyLayers]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRepoTagLayersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoTagLayersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoTagLayersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagLayersResponse, self).to_map()
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
            temp_model = GetRepoTagLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagManifestRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, schema_version=None, tag=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The schema version of the manifest. Valid values: 1 and 2.
        self.schema_version = schema_version  # type: int
        # The tag of the image.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagManifestResponseBodyManifestConfig(TeaModel):
    def __init__(self, digest=None, media_type=None, size=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The MIME type of the configuration file.
        self.media_type = media_type  # type: str
        # Size
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetRepoTagManifestResponseBodyManifestFsLayers(TeaModel):
    def __init__(self, blob_sum=None):
        # A list of filesystem layer blob sums contained in this image.
        self.blob_sum = blob_sum  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifestFsLayers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blob_sum is not None:
            result['BlobSum'] = self.blob_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlobSum') is not None:
            self.blob_sum = m.get('BlobSum')
        return self


class GetRepoTagManifestResponseBodyManifestHistory(TeaModel):
    def __init__(self, v_1compatibility=None):
        # The raw V1 compatibility information.
        self.v_1compatibility = v_1compatibility  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifestHistory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_1compatibility is not None:
            result['V1Compatibility'] = self.v_1compatibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('V1Compatibility') is not None:
            self.v_1compatibility = m.get('V1Compatibility')
        return self


class GetRepoTagManifestResponseBodyManifestLayers(TeaModel):
    def __init__(self, digest=None, media_type=None, size=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The MIME type of the configuration file.
        self.media_type = media_type  # type: str
        # Size.
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifestLayers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetRepoTagManifestResponseBodyManifestSignatures(TeaModel):
    def __init__(self, header=None, protected=None, signature=None):
        # The header information of the signature.
        self.header = header  # type: dict[str, any]
        # The signed protected header.
        self.protected = protected  # type: str
        # The signature for the image manifest.
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifestSignatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header
        if self.protected is not None:
            result['Protected'] = self.protected
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Protected') is not None:
            self.protected = m.get('Protected')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetRepoTagManifestResponseBodyManifest(TeaModel):
    def __init__(self, architecture=None, config=None, fs_layers=None, history=None, layers=None, media_type=None,
                 name=None, schema_version=None, signatures=None, tag=None):
        # Architecture.
        self.architecture = architecture  # type: str
        # The configuration information.
        self.config = config  # type: GetRepoTagManifestResponseBodyManifestConfig
        # The digest of the referenced filesystem image layer.
        self.fs_layers = fs_layers  # type: list[GetRepoTagManifestResponseBodyManifestFsLayers]
        # A list of unstructured historical data for V1 compatibility.
        self.history = history  # type: list[GetRepoTagManifestResponseBodyManifestHistory]
        # The information about image layers.
        self.layers = layers  # type: list[GetRepoTagManifestResponseBodyManifestLayers]
        # The type.
        self.media_type = media_type  # type: str
        # The name.
        self.name = name  # type: str
        # The schema version of the manifest.
        self.schema_version = schema_version  # type: int
        # The information about signatures.
        self.signatures = signatures  # type: list[GetRepoTagManifestResponseBodyManifestSignatures]
        # The tag of the image.
        self.tag = tag  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.fs_layers:
            for k in self.fs_layers:
                if k:
                    k.validate()
        if self.history:
            for k in self.history:
                if k:
                    k.validate()
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBodyManifest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.config is not None:
            result['Config'] = self.config.to_map()
        result['FsLayers'] = []
        if self.fs_layers is not None:
            for k in self.fs_layers:
                result['FsLayers'].append(k.to_map() if k else None)
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.name is not None:
            result['Name'] = self.name
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('Config') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifestConfig()
            self.config = temp_model.from_map(m['Config'])
        self.fs_layers = []
        if m.get('FsLayers') is not None:
            for k in m.get('FsLayers'):
                temp_model = GetRepoTagManifestResponseBodyManifestFsLayers()
                self.fs_layers.append(temp_model.from_map(k))
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = GetRepoTagManifestResponseBodyManifestHistory()
                self.history.append(temp_model.from_map(k))
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagManifestResponseBodyManifestLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = GetRepoTagManifestResponseBodyManifestSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagManifestResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, manifest=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The information about the image manifest.
        self.manifest = manifest  # type: GetRepoTagManifestResponseBodyManifest
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.manifest:
            self.manifest.validate()

    def to_map(self):
        _map = super(GetRepoTagManifestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.manifest is not None:
            result['Manifest'] = self.manifest.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Manifest') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifest()
            self.manifest = temp_model.from_map(m['Manifest'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoTagManifestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoTagManifestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagManifestResponse, self).to_map()
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
            temp_model = GetRepoTagManifestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanStatusRequest(TeaModel):
    def __init__(self, digest=None, instance_id=None, repo_id=None, scan_task_id=None, tag=None):
        self.digest = digest  # type: str
        self.instance_id = instance_id  # type: str
        self.repo_id = repo_id  # type: str
        self.scan_task_id = scan_task_id  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagScanStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagScanStatusResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, scan_service=None, status=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str
        self.scan_service = scan_service  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagScanStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoTagScanStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoTagScanStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagScanStatusResponse, self).to_map()
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
            temp_model = GetRepoTagScanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanSummaryRequest(TeaModel):
    def __init__(self, digest=None, instance_id=None, repo_id=None, scan_task_id=None, tag=None):
        # The number of unknown-severity vulnerabilities.
        self.digest = digest  # type: str
        # The ID of the image repository.
        self.instance_id = instance_id  # type: str
        # The name of the image tag.
        self.repo_id = repo_id  # type: str
        # The digest of the image.
        self.scan_task_id = scan_task_id  # type: str
        # The ID of the security scan task.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagScanSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagScanSummaryResponseBody(TeaModel):
    def __init__(self, code=None, high_severity=None, is_success=None, low_severity=None, medium_severity=None,
                 request_id=None, total_severity=None, unknown_severity=None):
        # The number of medium-severity vulnerabilities.
        self.code = code  # type: str
        # The number of low-severity vulnerabilities.
        self.high_severity = high_severity  # type: int
        # The number of high-severity vulnerabilities.
        self.is_success = is_success  # type: bool
        self.low_severity = low_severity  # type: int
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.medium_severity = medium_severity  # type: int
        # The total number of vulnerabilities detected on images.
        self.request_id = request_id  # type: str
        # The return value.
        self.total_severity = total_severity  # type: int
        # The ID of the request.
        self.unknown_severity = unknown_severity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepoTagScanSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.high_severity is not None:
            result['HighSeverity'] = self.high_severity
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.low_severity is not None:
            result['LowSeverity'] = self.low_severity
        if self.medium_severity is not None:
            result['MediumSeverity'] = self.medium_severity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_severity is not None:
            result['TotalSeverity'] = self.total_severity
        if self.unknown_severity is not None:
            result['UnknownSeverity'] = self.unknown_severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HighSeverity') is not None:
            self.high_severity = m.get('HighSeverity')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('LowSeverity') is not None:
            self.low_severity = m.get('LowSeverity')
        if m.get('MediumSeverity') is not None:
            self.medium_severity = m.get('MediumSeverity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalSeverity') is not None:
            self.total_severity = m.get('TotalSeverity')
        if m.get('UnknownSeverity') is not None:
            self.unknown_severity = m.get('UnknownSeverity')
        return self


class GetRepoTagScanSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepoTagScanSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepoTagScanSummaryResponse, self).to_map()
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
            temp_model = GetRepoTagScanSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, repo_name=None, repo_namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, create_time=None, detail=None, instance_id=None, is_success=None,
                 modified_time=None, repo_build_type=None, repo_id=None, repo_name=None, repo_namespace_name=None,
                 repo_status=None, repo_type=None, request_id=None, resource_group_id=None, summary=None, tag_immutability=None):
        # The return value.
        self.code = code  # type: str
        # The time when the repository was created.
        self.create_time = create_time  # type: long
        # The details of the repository.
        self.detail = detail  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The time when the repository was last modified.
        self.modified_time = modified_time  # type: long
        # Indicates how the repository was created. Valid values:
        # 
        # *   `MANUAL`: The repository was manually created.
        # *   `AUTO`: The repository was automatically created.
        self.repo_build_type = repo_build_type  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The status of the repository.
        self.repo_status = repo_status  # type: str
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: public repository.
        # *   `PRIVATE`: private repository.
        self.repo_type = repo_type  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The summary of the repository.
        self.summary = summary  # type: str
        # Indicates whether the feature of image tag immutability is enabled. Valid values:
        # 
        # *   `true`: The feature of image tag immutability is enabled.
        # *   `false`: The feature of image tag immutability is disabled.
        self.tag_immutability = tag_immutability  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class GetRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryResponse, self).to_map()
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
            temp_model = GetRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactBuildTaskLogRequest(TeaModel):
    def __init__(self, build_task_id=None, instance_id=None, page=None, page_size=None):
        # The ID of the artifact build task.
        self.build_task_id = build_task_id  # type: str
        # The ID of the Container Registry instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page = page  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactBuildTaskLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactBuildTaskLogResponseBodyBuildTaskLogs(TeaModel):
    def __init__(self, line_number=None, message=None):
        # The row number of the log entry.
        self.line_number = line_number  # type: int
        # The content of the log entry.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactBuildTaskLogResponseBodyBuildTaskLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_number is not None:
            result['LineNumber'] = self.line_number
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListArtifactBuildTaskLogResponseBody(TeaModel):
    def __init__(self, build_task_logs=None, code=None, is_success=None, request_id=None, total_count=None):
        # The log entries of the artifact build task.
        self.build_task_logs = build_task_logs  # type: list[ListArtifactBuildTaskLogResponseBodyBuildTaskLogs]
        # The response code.
        self.code = code  # type: str
        # Indicates whether the API call is successful.
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of log entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.build_task_logs:
            for k in self.build_task_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListArtifactBuildTaskLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BuildTaskLogs'] = []
        if self.build_task_logs is not None:
            for k in self.build_task_logs:
                result['BuildTaskLogs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.build_task_logs = []
        if m.get('BuildTaskLogs') is not None:
            for k in m.get('BuildTaskLogs'):
                temp_model = ListArtifactBuildTaskLogResponseBodyBuildTaskLogs()
                self.build_task_logs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactBuildTaskLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListArtifactBuildTaskLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListArtifactBuildTaskLogResponse, self).to_map()
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
            temp_model = ListArtifactBuildTaskLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChainRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_name=None, repo_namespace_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChainResponseBodyChains(TeaModel):
    def __init__(self, chain_id=None, create_time=None, description=None, instance_id=None, modified_time=None,
                 name=None, scope_exclude=None, scope_id=None, scope_type=None):
        # The ID of the delivery chain.
        self.chain_id = chain_id  # type: str
        # The time when the delivery chain was created.
        self.create_time = create_time  # type: long
        # The description of the delivery chain.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The time when the delivery chain was last modified.
        self.modified_time = modified_time  # type: long
        # The name of the delivery chain.
        self.name = name  # type: str
        # Repositories to which the delivery chain does not apply.
        self.scope_exclude = scope_exclude  # type: list[str]
        # The ID of the delivery chain scope.
        self.scope_id = scope_id  # type: str
        # The type of the delivery chain scope.
        self.scope_type = scope_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChainResponseBodyChains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class ListChainResponseBody(TeaModel):
    def __init__(self, chains=None, code=None, is_success=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        # The list of delivery chains.
        self.chains = chains  # type: list[ListChainResponseBodyChains]
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of delivery chains.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.chains:
            for k in self.chains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chains'] = []
        if self.chains is not None:
            for k in self.chains:
                result['Chains'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chains = []
        if m.get('Chains') is not None:
            for k in m.get('Chains'):
                temp_model = ListChainResponseBodyChains()
                self.chains.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChainResponse, self).to_map()
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
            temp_model = ListChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChainInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_name=None, repo_namespace_name=None):
        # The operation that you want to perform. Set this parameter to **ListChainInstance**.
        self.instance_id = instance_id  # type: str
        # The time when the delivery chain started.
        self.page_no = page_no  # type: int
        # The name of the image repository.
        self.page_size = page_size  # type: int
        # The time when the delivery chain is completed.
        self.repo_name = repo_name  # type: str
        # The name of the delivery chain.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChainInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChainInstanceResponseBodyChainInstancesChain(TeaModel):
    def __init__(self, chain_id=None, chain_name=None, version=None):
        # The name of the namespace.
        self.chain_id = chain_id  # type: str
        # The number of entries returned on each page.
        self.chain_name = chain_name  # type: str
        # The ID of the request.
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChainInstanceResponseBodyChainInstancesChain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListChainInstanceResponseBodyChainInstances(TeaModel):
    def __init__(self, chain=None, chain_instance_id=None, end_time=None, repo_name=None, repo_namespace_name=None,
                 result=None, start_time=None, status=None):
        # The name of the namespace.
        self.chain = chain  # type: ListChainInstanceResponseBodyChainInstancesChain
        # 1
        self.chain_instance_id = chain_instance_id  # type: str
        # The ID of the Container Registry instance.
        self.end_time = end_time  # type: long
        # The ID of the delivery chain.
        self.repo_name = repo_name  # type: str
        # The execution result of the delivery chain. Valid values:
        # 
        # *   `SUCCESS`
        # *   `FAILED`
        # *   `CANCELED`
        # *   `DENIED`
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The list of the execution records of delivery chains.
        self.result = result  # type: str
        # test-repo
        self.start_time = start_time  # type: long
        # The status of the delivery chain. Valid values:
        # 
        # *   `RUNNING`
        # *   `COMPLETE`
        # *   `CANCELING`
        # *   `CANCELED`
        self.status = status  # type: str

    def validate(self):
        if self.chain:
            self.chain.validate()

    def to_map(self):
        _map = super(ListChainInstanceResponseBodyChainInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain is not None:
            result['Chain'] = self.chain.to_map()
        if self.chain_instance_id is not None:
            result['ChainInstanceId'] = self.chain_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.result is not None:
            result['Result'] = self.result
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Chain') is not None:
            temp_model = ListChainInstanceResponseBodyChainInstancesChain()
            self.chain = temp_model.from_map(m['Chain'])
        if m.get('ChainInstanceId') is not None:
            self.chain_instance_id = m.get('ChainInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChainInstanceResponseBody(TeaModel):
    def __init__(self, chain_instances=None, code=None, instance_id=None, is_success=None, page_no=None,
                 page_size=None, request_id=None, total_count=None):
        # The number of entries to return on each page.
        self.chain_instances = chain_instances  # type: list[ListChainInstanceResponseBodyChainInstances]
        # The version of the delivery chain.
        self.code = code  # type: str
        # The page number of the page to return.
        self.instance_id = instance_id  # type: str
        # The execution record of the delivery chain.
        self.is_success = is_success  # type: bool
        # 30
        self.page_no = page_no  # type: int
        # Indicates whether the operation is successful.
        self.page_size = page_size  # type: int
        # The ID of the Container Registry instance.
        self.request_id = request_id  # type: str
        # The name of the repository.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.chain_instances:
            for k in self.chain_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChainInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChainInstances'] = []
        if self.chain_instances is not None:
            for k in self.chain_instances:
                result['ChainInstances'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chain_instances = []
        if m.get('ChainInstances') is not None:
            for k in m.get('ChainInstances'):
                temp_model = ListChainInstanceResponseBodyChainInstances()
                self.chain_instances.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChainInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChainInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChainInstanceResponse, self).to_map()
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
            temp_model = ListChainInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None, namespace_status=None, page_no=None, page_size=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChartNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_id=None,
                 namespace_name=None, namespace_status=None, resource_group_id=None):
        # Indicates whether a repository was automatically created when a chart is pushed to the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the namespace.
        self.namespace_id = namespace_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartNamespaceResponseBodyNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListChartNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, namespaces=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The namespaces.
        self.namespaces = namespaces  # type: list[ListChartNamespaceResponseBodyNamespaces]
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChartNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListChartNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChartNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChartNamespaceResponse, self).to_map()
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
            temp_model = ListChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartReleaseRequest(TeaModel):
    def __init__(self, chart=None, instance_id=None, page_no=None, page_size=None, repo_name=None,
                 repo_namespace_name=None):
        # The chart whose versions you want to query.
        self.chart = chart  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartReleaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChartReleaseResponseBodyChartReleases(TeaModel):
    def __init__(self, chart=None, instance_id=None, modified_time=None, release=None, repo_id=None, size=None,
                 status=None):
        # The name of the chart version.
        self.chart = chart  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The time when the chart was last modified.
        self.modified_time = modified_time  # type: long
        # The version number of the chart.
        self.release = release  # type: str
        # The ID of the chart repository.
        self.repo_id = repo_id  # type: str
        # The size of the chart of the version. Unit: bytes.
        self.size = size  # type: str
        # The status of the chart.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartReleaseResponseBodyChartReleases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.release is not None:
            result['Release'] = self.release
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChartReleaseResponseBody(TeaModel):
    def __init__(self, chart_releases=None, code=None, is_success=None, page_no=None, page_size=None,
                 request_id=None, total_count=None):
        # The list of chart versions.
        self.chart_releases = chart_releases  # type: list[ListChartReleaseResponseBodyChartReleases]
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.chart_releases:
            for k in self.chart_releases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChartReleaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChartReleases'] = []
        if self.chart_releases is not None:
            for k in self.chart_releases:
                result['ChartReleases'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chart_releases = []
        if m.get('ChartReleases') is not None:
            for k in m.get('ChartReleases'):
                temp_model = ListChartReleaseResponseBodyChartReleases()
                self.chart_releases.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartReleaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChartReleaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChartReleaseResponse, self).to_map()
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
            temp_model = ListChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_name=None, repo_namespace_name=None,
                 repo_status=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The status of the chart repositories that you want to query. Valid values:
        # 
        # *   `ALL`: query repositories of all status.
        # *   `NORMAL`: query normal repositories.
        # *   `DELETING`: query repositories that are being deleted.
        self.repo_status = repo_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        return self


class ListChartRepositoryResponseBodyRepositories(TeaModel):
    def __init__(self, create_time=None, instance_id=None, modified_time=None, repo_id=None, repo_name=None,
                 repo_namespace_name=None, repo_status=None, repo_type=None, resource_group_id=None, summary=None):
        # The time when the repository was created.
        self.create_time = create_time  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The time when the repository was last modified.
        self.modified_time = modified_time  # type: long
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The status of the repository. Valid values:
        # 
        # *   `NORMAL`: The repository is normal.
        # *   `DELETING`: The repository is being deleted.
        self.repo_status = repo_status  # type: str
        # The type of the repository. Valid values:
        # 
        # *   `PRIVATE`: a private repository
        # *   `PUBLIC`: a public repository
        self.repo_type = repo_type  # type: str
        # The ID of the resource group to which the repository belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The summary about the repository.
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartRepositoryResponseBodyRepositories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListChartRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, repositories=None, request_id=None,
                 total_count=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The queried repositories.
        self.repositories = repositories  # type: list[ListChartRepositoryResponseBodyRepositories]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.repositories:
            for k in self.repositories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChartRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListChartRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChartRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChartRepositoryResponse, self).to_map()
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
            temp_model = ListChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventCenterRecordRequest(TeaModel):
    def __init__(self, event_type=None, instance_id=None, page_no=None, page_size=None, rule_id=None):
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventCenterRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListEventCenterRecordResponseBodyRecords(TeaModel):
    def __init__(self, create_time=None, event_channel=None, event_notify_id=None, event_notify_method=None,
                 event_type=None, instance_id=None, namespace=None, record_id=None, repo_name=None, rule_id=None,
                 rule_name=None, tag=None, update_time=None):
        # The time when the event was created.
        self.create_time = create_time  # type: long
        # The event notification channel.
        self.event_channel = event_channel  # type: str
        # The ID of the event notification.
        self.event_notify_id = event_notify_id  # type: str
        # The notification method. Valid values:
        # 
        # *   `http`: The notification is sent over HTTP.
        # *   `https`: The notification is sent over HTTPS.
        # *   `dingding`: The notification is sent by using DingTalk.
        self.event_notify_method = event_notify_method  # type: str
        # The type of the event.
        self.event_type = event_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The namespace.
        self.namespace = namespace  # type: str
        # The ID of the event record.
        self.record_id = record_id  # type: str
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str
        # The name of the event notification rule.
        self.rule_name = rule_name  # type: str
        # The tags.
        self.tag = tag  # type: str
        # The time when the event was last updated.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventCenterRecordResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_notify_id is not None:
            result['EventNotifyId'] = self.event_notify_id
        if self.event_notify_method is not None:
            result['EventNotifyMethod'] = self.event_notify_method
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventNotifyId') is not None:
            self.event_notify_id = m.get('EventNotifyId')
        if m.get('EventNotifyMethod') is not None:
            self.event_notify_method = m.get('EventNotifyMethod')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEventCenterRecordResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, records=None, request_id=None,
                 total_count=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The list of historical events.
        self.records = records  # type: list[ListEventCenterRecordResponseBodyRecords]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total entries of historical events.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventCenterRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEventCenterRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEventCenterRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventCenterRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventCenterRecordResponse, self).to_map()
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
            temp_model = ListEventCenterRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventCenterRuleNameRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventCenterRuleNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListEventCenterRuleNameResponseBodyRuleNames(TeaModel):
    def __init__(self, rule_id=None, rule_name=None):
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str
        # The name of the event notification rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventCenterRuleNameResponseBodyRuleNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListEventCenterRuleNameResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, rule_names=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of names of event notification rules.
        self.rule_names = rule_names  # type: list[ListEventCenterRuleNameResponseBodyRuleNames]

    def validate(self):
        if self.rule_names:
            for k in self.rule_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventCenterRuleNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleNames'] = []
        if self.rule_names is not None:
            for k in self.rule_names:
                result['RuleNames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_names = []
        if m.get('RuleNames') is not None:
            for k in m.get('RuleNames'):
                temp_model = ListEventCenterRuleNameResponseBodyRuleNames()
                self.rule_names.append(temp_model.from_map(k))
        return self


class ListEventCenterRuleNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventCenterRuleNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventCenterRuleNameResponse, self).to_map()
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
            temp_model = ListEventCenterRuleNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, instance_status=None, page_no=None, page_size=None,
                 resource_group_id=None):
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(self, create_time=None, instance_id=None, instance_issue=None, instance_name=None,
                 instance_specification=None, instance_status=None, modified_time=None, region_id=None, resource_group_id=None):
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_issue = instance_issue  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_specification = instance_specification  # type: str
        self.instance_status = instance_status  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_issue is not None:
            result['InstanceIssue'] = self.instance_issue
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIssue') is not None:
            self.instance_issue = m.get('InstanceIssue')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, code=None, instances=None, is_success=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: str
        self.instances = instances  # type: list[ListInstanceResponseBodyInstances]
        self.is_success = is_success  # type: bool
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceEndpointRequest(TeaModel):
    def __init__(self, instance_id=None, module_name=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class ListInstanceEndpointResponseBodyEndpointsAclEntries(TeaModel):
    def __init__(self, entry=None):
        # Details about the ACL.
        self.entry = entry  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceEndpointResponseBodyEndpointsAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class ListInstanceEndpointResponseBodyEndpointsDomains(TeaModel):
    def __init__(self, domain=None, type=None):
        # The domain name.
        self.domain = domain  # type: str
        # Type
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceEndpointResponseBodyEndpointsDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstanceEndpointResponseBodyEndpointsLinkedVpcs(TeaModel):
    def __init__(self, vpc_id=None):
        # VPC ID
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceEndpointResponseBodyEndpointsLinkedVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstanceEndpointResponseBodyEndpoints(TeaModel):
    def __init__(self, acl_enable=None, acl_entries=None, domains=None, enable=None, endpoint_type=None,
                 linked_vpcs=None, status=None):
        # Indicates whether the access control list (ACL) feature is enabled.
        self.acl_enable = acl_enable  # type: bool
        # The ACL configured for the instance.
        self.acl_entries = acl_entries  # type: list[ListInstanceEndpointResponseBodyEndpointsAclEntries]
        # Domain names.
        self.domains = domains  # type: list[ListInstanceEndpointResponseBodyEndpointsDomains]
        # Indicates whether the ACL feature is enabled.
        self.enable = enable  # type: bool
        # The type of the endpoint.
        self.endpoint_type = endpoint_type  # type: str
        # The virtual private clouds (VPCs) that are associated with the instance.
        self.linked_vpcs = linked_vpcs  # type: list[ListInstanceEndpointResponseBodyEndpointsLinkedVpcs]
        # The status of the instance.
        self.status = status  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.linked_vpcs:
            for k in self.linked_vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceEndpointResponseBodyEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceEndpointResponseBody(TeaModel):
    def __init__(self, code=None, endpoints=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # The endpoints of the instance.
        self.endpoints = endpoints  # type: list[ListInstanceEndpointResponseBodyEndpoints]
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListInstanceEndpointResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceEndpointResponse, self).to_map()
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
            temp_model = ListInstanceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRegionRequest(TeaModel):
    def __init__(self, lang=None):
        # The language used for response parameters. Set this parameter to `zh-CN`.
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRegionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListInstanceRegionResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRegionResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstanceRegionResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, regions=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The list of regions.
        self.regions = regions  # type: list[ListInstanceRegionResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListInstanceRegionResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceRegionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceRegionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceRegionResponse, self).to_map()
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
            temp_model = ListInstanceRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None, namespace_status=None, page_no=None, page_size=None):
        # The number of the page to return.
        self.instance_id = instance_id  # type: str
        # The number of entries returned per page.
        self.namespace_name = namespace_name  # type: str
        # The ID of the namespace.
        self.namespace_status = namespace_status  # type: str
        # The list of namespaces.
        self.page_no = page_no  # type: int
        # The ID of the request.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_id=None,
                 namespace_name=None, namespace_status=None, resource_group_id=None):
        self.auto_create_repo = auto_create_repo  # type: bool
        self.default_repo_type = default_repo_type  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.namespace_status = namespace_status  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespaceResponseBodyNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, namespaces=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.namespaces = namespaces  # type: list[ListNamespaceResponseBodyNamespaces]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespaceResponse, self).to_map()
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
            temp_model = ListNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRecordResponseBodyBuildRecordsImage(TeaModel):
    def __init__(self, image_tag=None, repo_id=None, repo_name=None, repo_namespace_name=None):
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRecordResponseBodyBuildRecordsImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoBuildRecordResponseBodyBuildRecords(TeaModel):
    def __init__(self, build_record_id=None, build_status=None, end_time=None, image=None, start_time=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The status of the image building.
        self.build_status = build_status  # type: str
        # The time when the image building ended.
        self.end_time = end_time  # type: str
        # The information about the image.
        self.image = image  # type: ListRepoBuildRecordResponseBodyBuildRecordsImage
        # The time when the image building started.
        self.start_time = start_time  # type: str

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super(ListRepoBuildRecordResponseBodyBuildRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Image') is not None:
            temp_model = ListRepoBuildRecordResponseBodyBuildRecordsImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListRepoBuildRecordResponseBody(TeaModel):
    def __init__(self, build_records=None, code=None, is_success=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        # The list of image building records.
        self.build_records = build_records  # type: list[ListRepoBuildRecordResponseBodyBuildRecords]
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.build_records:
            for k in self.build_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoBuildRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BuildRecords'] = []
        if self.build_records is not None:
            for k in self.build_records:
                result['BuildRecords'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.build_records = []
        if m.get('BuildRecords') is not None:
            for k in m.get('BuildRecords'):
                temp_model = ListRepoBuildRecordResponseBodyBuildRecords()
                self.build_records.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoBuildRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoBuildRecordResponse, self).to_map()
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
            temp_model = ListRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordLogRequest(TeaModel):
    def __init__(self, build_record_id=None, instance_id=None, offset=None, repo_id=None):
        # The ID of the image building record.
        self.build_record_id = build_record_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The offset of log lines.
        self.offset = offset  # type: int
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRecordLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRecordLogResponseBodyBuildRecordLogs(TeaModel):
    def __init__(self, build_stage=None, line_number=None, message=None):
        # The stage of the building that is recorded in the log entry.
        self.build_stage = build_stage  # type: str
        # The line number of the log entry.
        self.line_number = line_number  # type: int
        # The content of the log.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRecordLogResponseBodyBuildRecordLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_stage is not None:
            result['BuildStage'] = self.build_stage
        if self.line_number is not None:
            result['LineNumber'] = self.line_number
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildStage') is not None:
            self.build_stage = m.get('BuildStage')
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListRepoBuildRecordLogResponseBody(TeaModel):
    def __init__(self, build_record_logs=None, code=None, is_success=None, page_no=None, page_size=None,
                 request_id=None, total_count=None):
        # The log content of the image building record.
        self.build_record_logs = build_record_logs  # type: list[ListRepoBuildRecordLogResponseBodyBuildRecordLogs]
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.build_record_logs:
            for k in self.build_record_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoBuildRecordLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BuildRecordLogs'] = []
        if self.build_record_logs is not None:
            for k in self.build_record_logs:
                result['BuildRecordLogs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.build_record_logs = []
        if m.get('BuildRecordLogs') is not None:
            for k in m.get('BuildRecordLogs'):
                temp_model = ListRepoBuildRecordLogResponseBodyBuildRecordLogs()
                self.build_record_logs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRecordLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoBuildRecordLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoBuildRecordLogResponse, self).to_map()
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
            temp_model = ListRepoBuildRecordLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRuleRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRuleResponseBodyBuildRules(TeaModel):
    def __init__(self, build_args=None, build_rule_id=None, dockerfile_location=None, dockerfile_name=None,
                 image_tag=None, platforms=None, push_name=None, push_type=None):
        self.build_args = build_args  # type: list[str]
        # The ID of the image building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The directory of the Dockerfile.
        self.dockerfile_location = dockerfile_location  # type: str
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name  # type: str
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        self.platforms = platforms  # type: list[str]
        # The name of the push that triggers the building rule.
        self.push_name = push_name  # type: str
        # The type of the push that triggers the image building rule. Valid values:
        # 
        # *   GIT_BRANCH: branch push
        # *   GIT_TAG: tag push
        self.push_type = push_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoBuildRuleResponseBodyBuildRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        return self


class ListRepoBuildRuleResponseBody(TeaModel):
    def __init__(self, build_rules=None, code=None, is_success=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        # The list of image building rules.
        self.build_rules = build_rules  # type: list[ListRepoBuildRuleResponseBodyBuildRules]
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.build_rules:
            for k in self.build_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BuildRules'] = []
        if self.build_rules is not None:
            for k in self.build_rules:
                result['BuildRules'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.build_rules = []
        if m.get('BuildRules') is not None:
            for k in m.get('BuildRules'):
                temp_model = ListRepoBuildRuleResponseBodyBuildRules()
                self.build_rules.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoBuildRuleResponse, self).to_map()
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
            temp_model = ListRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncRuleRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_name=None, page_no=None, page_size=None, repo_name=None,
                 target_instance_id=None, target_region_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the image repository.
        self.repo_name = repo_name  # type: str
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id  # type: str
        # The region ID of the destination instance.
        self.target_region_id = target_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoSyncRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class ListRepoSyncRuleResponseBodySyncRules(TeaModel):
    def __init__(self, create_time=None, cross_user=None, local_instance_id=None, local_namespace_name=None,
                 local_region_id=None, local_repo_name=None, modified_time=None, sync_direction=None, sync_rule_id=None,
                 sync_rule_name=None, sync_scope=None, sync_trigger=None, tag_filter=None, target_instance_id=None,
                 target_namespace_name=None, target_region_id=None, target_repo_name=None):
        # The time when the synchronization rule was created.
        self.create_time = create_time  # type: long
        # Indicates whether images are synchronized across Alibaba Cloud accounts. Valid values:
        # 
        # *   `true`: Images are synchronized across Alibaba Cloud accounts.
        # *   `false`: Images are synchronized within the same Alibaba Cloud account.
        # 
        # Default value: `false`
        self.cross_user = cross_user  # type: bool
        # The ID of the source instance.
        self.local_instance_id = local_instance_id  # type: str
        # The namespace name of the source instance.
        self.local_namespace_name = local_namespace_name  # type: str
        # The region ID of the source instance.
        self.local_region_id = local_region_id  # type: str
        # The image repository name of the source instance.
        self.local_repo_name = local_repo_name  # type: str
        # The time when the synchronization rule was last modified.
        self.modified_time = modified_time  # type: long
        # The synchronization direction. Valid values:
        # 
        # *   `FROM`: Images are synchronized from the source instance to the destination instance.
        # *   `TO`: Images are synchronized from the destination instance to the source instance.
        self.sync_direction = sync_direction  # type: str
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id  # type: str
        # The name of the synchronization rule.
        self.sync_rule_name = sync_rule_name  # type: str
        # The synchronization scope. Valid values:
        # 
        # *   `NAMESPACE`: synchronizes the image tags in a namespace that meet the synchronization rule.
        # *   `REPO`: synchronizes the image tags in an image repository that meet the synchronization rule.
        self.sync_scope = sync_scope  # type: str
        # The policy that is applied to trigger the synchronization rule. Valid values:
        # 
        # *   `INITIATIVE`: The synchronization rule is positively triggered.
        # *   `PASSIVE`: The synchronization rule is passively triggered.
        self.sync_trigger = sync_trigger  # type: str
        # The regular expression that is used to filter image tags.
        self.tag_filter = tag_filter  # type: str
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id  # type: str
        # The namespace name of the destination instance.
        self.target_namespace_name = target_namespace_name  # type: str
        # The region ID of the destination instance.
        self.target_region_id = target_region_id  # type: str
        # The image repository name of the destination instance.
        self.target_repo_name = target_repo_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoSyncRuleResponseBodySyncRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.local_instance_id is not None:
            result['LocalInstanceId'] = self.local_instance_id
        if self.local_namespace_name is not None:
            result['LocalNamespaceName'] = self.local_namespace_name
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.local_repo_name is not None:
            result['LocalRepoName'] = self.local_repo_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.sync_direction is not None:
            result['SyncDirection'] = self.sync_direction
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('LocalInstanceId') is not None:
            self.local_instance_id = m.get('LocalInstanceId')
        if m.get('LocalNamespaceName') is not None:
            self.local_namespace_name = m.get('LocalNamespaceName')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('LocalRepoName') is not None:
            self.local_repo_name = m.get('LocalRepoName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SyncDirection') is not None:
            self.sync_direction = m.get('SyncDirection')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        return self


class ListRepoSyncRuleResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, request_id=None, sync_rules=None,
                 total_count=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The synchronization rules.
        self.sync_rules = sync_rules  # type: list[ListRepoSyncRuleResponseBodySyncRules]
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.sync_rules:
            for k in self.sync_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoSyncRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SyncRules'] = []
        if self.sync_rules is not None:
            for k in self.sync_rules:
                result['SyncRules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sync_rules = []
        if m.get('SyncRules') is not None:
            for k in m.get('SyncRules'):
                temp_model = ListRepoSyncRuleResponseBodySyncRules()
                self.sync_rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoSyncRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoSyncRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoSyncRuleResponse, self).to_map()
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
            temp_model = ListRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncTaskRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_name=None, repo_namespace_name=None,
                 sync_record_id=None, tag=None):
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str
        self.sync_record_id = sync_record_id  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoSyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.sync_record_id is not None:
            result['SyncRecordId'] = self.sync_record_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('SyncRecordId') is not None:
            self.sync_record_id = m.get('SyncRecordId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageFrom(TeaModel):
    def __init__(self, image_tag=None, instance_id=None, region_id=None, repo_name=None, repo_namespace_name=None):
        self.image_tag = image_tag  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoSyncTaskResponseBodySyncTasksImageFrom, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageTo(TeaModel):
    def __init__(self, image_tag=None, instance_id=None, region_id=None, repo_name=None, repo_namespace_name=None):
        self.image_tag = image_tag  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoSyncTaskResponseBodySyncTasksImageTo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoSyncTaskResponseBodySyncTasks(TeaModel):
    def __init__(self, create_time=None, cross_user=None, custom_link=None, image_from=None, image_to=None,
                 modifed_time=None, sync_batch_task_id=None, sync_rule_id=None, sync_task_id=None, sync_trans_accelerate=None,
                 task_status=None, task_trigger=None):
        self.create_time = create_time  # type: long
        self.cross_user = cross_user  # type: bool
        self.custom_link = custom_link  # type: bool
        self.image_from = image_from  # type: ListRepoSyncTaskResponseBodySyncTasksImageFrom
        self.image_to = image_to  # type: ListRepoSyncTaskResponseBodySyncTasksImageTo
        self.modifed_time = modifed_time  # type: long
        self.sync_batch_task_id = sync_batch_task_id  # type: str
        self.sync_rule_id = sync_rule_id  # type: str
        self.sync_task_id = sync_task_id  # type: str
        self.sync_trans_accelerate = sync_trans_accelerate  # type: bool
        self.task_status = task_status  # type: str
        self.task_trigger = task_trigger  # type: str

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()

    def to_map(self):
        _map = super(ListRepoSyncTaskResponseBodySyncTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.custom_link is not None:
            result['CustomLink'] = self.custom_link
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        if self.modifed_time is not None:
            result['ModifedTime'] = self.modifed_time
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('CustomLink') is not None:
            self.custom_link = m.get('CustomLink')
        if m.get('ImageFrom') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        if m.get('ModifedTime') is not None:
            self.modifed_time = m.get('ModifedTime')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        return self


class ListRepoSyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, request_id=None, sync_tasks=None,
                 total_count=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.sync_tasks = sync_tasks  # type: list[ListRepoSyncTaskResponseBodySyncTasks]
        self.total_count = total_count  # type: str

    def validate(self):
        if self.sync_tasks:
            for k in self.sync_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoSyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SyncTasks'] = []
        if self.sync_tasks is not None:
            for k in self.sync_tasks:
                result['SyncTasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sync_tasks = []
        if m.get('SyncTasks') is not None:
            for k in m.get('SyncTasks'):
                temp_model = ListRepoSyncTaskResponseBodySyncTasks()
                self.sync_tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoSyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoSyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoSyncTaskResponse, self).to_map()
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
            temp_model = ListRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoTagResponseBodyImages(TeaModel):
    def __init__(self, digest=None, image_create=None, image_id=None, image_size=None, image_update=None,
                 status=None, tag=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The time when the image was created.
        self.image_create = image_create  # type: str
        # The ID of the image.
        self.image_id = image_id  # type: str
        # The size of the image.
        self.image_size = image_size  # type: long
        # The time when the image was last updated.
        self.image_update = image_update  # type: str
        # The status of the image.
        self.status = status  # type: str
        # The tag of the image.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTagResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.image_create is not None:
            result['ImageCreate'] = self.image_create
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListRepoTagResponseBody(TeaModel):
    def __init__(self, code=None, images=None, is_success=None, page_no=None, page_size=None, request_id=None,
                 total_count=None):
        # The return value.
        self.code = code  # type: str
        # The images.
        self.images = images  # type: list[ListRepoTagResponseBodyImages]
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The page number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListRepoTagResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoTagResponse, self).to_map()
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
            temp_model = ListRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagScanResultRequest(TeaModel):
    def __init__(self, digest=None, filter_value=None, instance_id=None, page_no=None, page_size=None, repo_id=None,
                 scan_task_id=None, scan_type=None, severity=None, tag=None, vul_query_key=None):
        # The digest of the image.
        self.digest = digest  # type: str
        # The parameter whose value that you want to query. Fox example, if the value is `FixCmd`, only the `FixCmd` parameter is returned.
        self.filter_value = filter_value  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The ID of the security scan task.
        self.scan_task_id = scan_task_id  # type: str
        # The type of the vulnerability. Valid values:
        # 
        # *   `cve`: image system vulnerability
        # *   `sca`: image application vulnerability
        self.scan_type = scan_type  # type: str
        # The severity of the vulnerability. Valid values:
        # 
        # *   `High`
        # *   `Medium`
        # *   `Low`
        # *   `Unknown`
        self.severity = severity  # type: str
        # The name of the image tag.
        self.tag = tag  # type: str
        # The keyword for fuzzy search used in scanning. The value can be a CVE name.
        self.vul_query_key = vul_query_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTagScanResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.vul_query_key is not None:
            result['VulQueryKey'] = self.vul_query_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('VulQueryKey') is not None:
            self.vul_query_key = m.get('VulQueryKey')
        return self


class ListRepoTagScanResultResponseBodyVulnerabilities(TeaModel):
    def __init__(self, added_by=None, alias_name=None, cve_link=None, cve_location=None, cve_name=None,
                 description=None, feature=None, fix_cmd=None, scan_type=None, severity=None, version=None, version_fixed=None,
                 version_format=None):
        # The ID of the image layer where the vulnerability was detected.
        self.added_by = added_by  # type: str
        # The name of the vulnerability.
        self.alias_name = alias_name  # type: str
        # The URL of the vulnerability.
        self.cve_link = cve_link  # type: str
        # The directory of the vulnerability.
        self.cve_location = cve_location  # type: str
        # The name of the vulnerability.
        self.cve_name = cve_name  # type: str
        # The description of the vulnerability.
        self.description = description  # type: str
        # The cause of the vulnerability.
        self.feature = feature  # type: str
        # The command used to fix the vulnerability.
        self.fix_cmd = fix_cmd  # type: str
        # The type of the vulnerability. Valid values:
        # 
        # *   `cve`: image system vulnerability
        # *   `sca`: image application vulnerability
        self.scan_type = scan_type  # type: str
        # The severity of the vulnerability.
        self.severity = severity  # type: str
        # The version of the vulnerability.
        self.version = version  # type: str
        # The version where the vulnerability was fixed.
        self.version_fixed = version_fixed  # type: str
        # The format of the vulnerability.
        self.version_format = version_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTagScanResultResponseBodyVulnerabilities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_by is not None:
            result['AddedBy'] = self.added_by
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.cve_link is not None:
            result['CveLink'] = self.cve_link
        if self.cve_location is not None:
            result['CveLocation'] = self.cve_location
        if self.cve_name is not None:
            result['CveName'] = self.cve_name
        if self.description is not None:
            result['Description'] = self.description
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.fix_cmd is not None:
            result['FixCmd'] = self.fix_cmd
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.version is not None:
            result['Version'] = self.version
        if self.version_fixed is not None:
            result['VersionFixed'] = self.version_fixed
        if self.version_format is not None:
            result['VersionFormat'] = self.version_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddedBy') is not None:
            self.added_by = m.get('AddedBy')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CveLink') is not None:
            self.cve_link = m.get('CveLink')
        if m.get('CveLocation') is not None:
            self.cve_location = m.get('CveLocation')
        if m.get('CveName') is not None:
            self.cve_name = m.get('CveName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('FixCmd') is not None:
            self.fix_cmd = m.get('FixCmd')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionFixed') is not None:
            self.version_fixed = m.get('VersionFixed')
        if m.get('VersionFormat') is not None:
            self.version_format = m.get('VersionFormat')
        return self


class ListRepoTagScanResultResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, request_id=None, total_count=None,
                 vulnerabilities=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request failed.
        self.is_success = is_success  # type: bool
        # The number of the returned page.
        self.page_no = page_no  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of vulnerabilities detected on images.
        self.total_count = total_count  # type: int
        # The details about the detected vulnerabilities.
        self.vulnerabilities = vulnerabilities  # type: list[ListRepoTagScanResultResponseBodyVulnerabilities]

    def validate(self):
        if self.vulnerabilities:
            for k in self.vulnerabilities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoTagScanResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vulnerabilities'] = []
        if self.vulnerabilities is not None:
            for k in self.vulnerabilities:
                result['Vulnerabilities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vulnerabilities = []
        if m.get('Vulnerabilities') is not None:
            for k in m.get('Vulnerabilities'):
                temp_model = ListRepoTagScanResultResponseBodyVulnerabilities()
                self.vulnerabilities.append(temp_model.from_map(k))
        return self


class ListRepoTagScanResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoTagScanResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoTagScanResultResponse, self).to_map()
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
            temp_model = ListRepoTagScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTriggerRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoTriggerResponseBodyTriggers(TeaModel):
    def __init__(self, repo_event=None, trigger_id=None, trigger_name=None, trigger_tag=None, trigger_type=None,
                 trigger_url=None):
        # The type of the event that activates the trigger. Valid values:
        # 
        # *   `BUILD_SUCCESS`: The trigger is activated when an image building task is successful.
        # *   `BUILD_Fail`: The trigger is activated when an image building task fails.
        self.repo_event = repo_event  # type: str
        # The ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger.
        self.trigger_name = trigger_name  # type: str
        # The image tag based on which the trigger is set.
        self.trigger_tag = trigger_tag  # type: str
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LISTTAG`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type  # type: str
        # The URL of the trigger.
        self.trigger_url = trigger_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepoTriggerResponseBodyTriggers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_event is not None:
            result['RepoEvent'] = self.repo_event
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RepoEvent') is not None:
            self.repo_event = m.get('RepoEvent')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        return self


class ListRepoTriggerResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None, triggers=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The triggers of the repository.
        self.triggers = triggers  # type: list[ListRepoTriggerResponseBodyTriggers]

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepoTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ListRepoTriggerResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListRepoTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepoTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepoTriggerResponse, self).to_map()
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
            temp_model = ListRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, repo_name=None, repo_namespace_name=None,
                 repo_status=None):
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str
        self.repo_status = repo_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        return self


class ListRepositoryResponseBodyRepositories(TeaModel):
    def __init__(self, create_time=None, instance_id=None, modified_time=None, repo_build_type=None, repo_id=None,
                 repo_name=None, repo_namespace_name=None, repo_status=None, repo_type=None, resource_group_id=None,
                 summary=None, tag_immutability=None):
        self.create_time = create_time  # type: long
        self.instance_id = instance_id  # type: str
        self.modified_time = modified_time  # type: long
        self.repo_build_type = repo_build_type  # type: str
        self.repo_id = repo_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str
        self.repo_status = repo_status  # type: str
        self.repo_type = repo_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.summary = summary  # type: str
        self.tag_immutability = tag_immutability  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryResponseBodyRepositories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class ListRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, page_no=None, page_size=None, repositories=None, request_id=None,
                 total_count=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.repositories = repositories  # type: list[ListRepositoryResponseBodyRepositories]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.repositories:
            for k in self.repositories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryResponse, self).to_map()
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
            temp_model = ListRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetLoginPasswordRequest(TeaModel):
    def __init__(self, instance_id=None, password=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The new password that you specify to log on to the instance. The password must be 8 to 32 bits in length, and must contain at least two of the following character types: letters, special characters, and digits.
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetLoginPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ResetLoginPasswordResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetLoginPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetLoginPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetLoginPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetLoginPasswordResponse, self).to_map()
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
            temp_model = ResetLoginPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChainRequest(TeaModel):
    def __init__(self, chain_config=None, chain_id=None, description=None, instance_id=None, name=None,
                 scope_exclude=None):
        # The configuration of the delivery chain in the JSON format.
        self.chain_config = chain_config  # type: str
        # The ID of the delivery chain.
        self.chain_id = chain_id  # type: str
        # The description of the delivery chain.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the delivery chain.
        self.name = name  # type: str
        # Repositories in which the delivery chain does not take effect.
        self.scope_exclude = scope_exclude  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            self.chain_config = m.get('ChainConfig')
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        return self


class UpdateChainResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateChainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateChainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateChainResponse, self).to_map()
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
            temp_model = UpdateChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartNamespaceRequest(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_name=None):
        # Specifies whether to automatically create repositories in the namespace. Valid values:
        # 
        # *   `true`: automatically creates repositories in the namespace.
        # *   `false`: does not automatically create repositories in the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace to which the repository belongs.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChartNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateChartNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChartNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateChartNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateChartNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateChartNamespaceResponse, self).to_map()
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
            temp_model = UpdateChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartRepositoryRequest(TeaModel):
    def __init__(self, instance_id=None, repo_name=None, repo_namespace_name=None, repo_type=None, summary=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the repository.
        self.repo_name = repo_name  # type: str
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name  # type: str
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        self.repo_type = repo_type  # type: str
        # The summary of the repository.
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChartRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class UpdateChartRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateChartRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateChartRepositoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateChartRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateChartRepositoryResponse, self).to_map()
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
            temp_model = UpdateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventCenterRuleRequest(TeaModel):
    def __init__(self, event_channel=None, event_config=None, event_scope=None, event_type=None, instance_id=None,
                 namespaces=None, repo_names=None, repo_tag_filter_pattern=None, rule_id=None, rule_name=None):
        # The event notification channel.
        self.event_channel = event_channel  # type: str
        # The event configuration.
        self.event_config = event_config  # type: str
        # The event scope. Valid values:
        # 
        # *   `INSTANCE`
        # *   `NAMESPACE`
        # *   `REPO`
        # 
        # Default value: `INSTANCE`
        self.event_scope = event_scope  # type: str
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The namespaces to which the event notification rule applies.
        self.namespaces = namespaces  # type: list[str]
        # The names of the repositories to which the event notification rule applies.
        self.repo_names = repo_names  # type: list[str]
        # The regular expression for image tags.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern  # type: str
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str
        # The name of the event notification rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventCenterRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_config is not None:
            result['EventConfig'] = self.event_config
        if self.event_scope is not None:
            result['EventScope'] = self.event_scope
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.repo_names is not None:
            result['RepoNames'] = self.repo_names
        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventConfig') is not None:
            self.event_config = m.get('EventConfig')
        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('RepoNames') is not None:
            self.repo_names = m.get('RepoNames')
        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateEventCenterRuleShrinkRequest(TeaModel):
    def __init__(self, event_channel=None, event_config=None, event_scope=None, event_type=None, instance_id=None,
                 namespaces_shrink=None, repo_names_shrink=None, repo_tag_filter_pattern=None, rule_id=None, rule_name=None):
        # The event notification channel.
        self.event_channel = event_channel  # type: str
        # The event configuration.
        self.event_config = event_config  # type: str
        # The event scope. Valid values:
        # 
        # *   `INSTANCE`
        # *   `NAMESPACE`
        # *   `REPO`
        # 
        # Default value: `INSTANCE`
        self.event_scope = event_scope  # type: str
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The namespaces to which the event notification rule applies.
        self.namespaces_shrink = namespaces_shrink  # type: str
        # The names of the repositories to which the event notification rule applies.
        self.repo_names_shrink = repo_names_shrink  # type: str
        # The regular expression for image tags.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern  # type: str
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str
        # The name of the event notification rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventCenterRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_config is not None:
            result['EventConfig'] = self.event_config
        if self.event_scope is not None:
            result['EventScope'] = self.event_scope
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink
        if self.repo_names_shrink is not None:
            result['RepoNames'] = self.repo_names_shrink
        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventConfig') is not None:
            self.event_config = m.get('EventConfig')
        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')
        if m.get('RepoNames') is not None:
            self.repo_names_shrink = m.get('RepoNames')
        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateEventCenterRuleResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, rule_id=None):
        # The status code.
        self.code = code  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the event notification rule.
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventCenterRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UpdateEventCenterRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEventCenterRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEventCenterRuleResponse, self).to_map()
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
            temp_model = UpdateEventCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceEndpointStatusRequest(TeaModel):
    def __init__(self, enable=None, endpoint_type=None, instance_id=None, module_name=None):
        # Specifies whether to enable the instance endpoint. Valid values:
        # 
        # *   `true`: enables the instance endpoint.
        # *   `false`: disables the instance endpoint
        self.enable = enable  # type: bool
        # The type of the endpoint. Set the value to Internet.
        self.endpoint_type = endpoint_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceEndpointStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class UpdateInstanceEndpointStatusResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceEndpointStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceEndpointStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceEndpointStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceEndpointStatusResponse, self).to_map()
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
            temp_model = UpdateInstanceEndpointStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(self, auto_create_repo=None, default_repo_type=None, instance_id=None, namespace_name=None):
        # Specifies whether to automatically create a repository when an image is pushed to the namespace.
        self.auto_create_repo = auto_create_repo  # type: bool
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: The repository is a public repository.
        # *   `PRIVATE`: The repository is a private repository.
        self.default_repo_type = default_repo_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNamespaceResponse, self).to_map()
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
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoBuildRuleRequest(TeaModel):
    def __init__(self, build_args=None, build_rule_id=None, dockerfile_location=None, dockerfile_name=None,
                 image_tag=None, instance_id=None, platforms=None, push_name=None, push_type=None, repo_id=None):
        # Building arguments.
        self.build_args = build_args  # type: list[str]
        # The ID of the building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The path of the Dockerfile.
        self.dockerfile_location = dockerfile_location  # type: str
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name  # type: str
        # The tag of the image.
        self.image_tag = image_tag  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Architecture for image building. Valid values:
        # 
        # *   `linux/amd64`
        # *   `linux/arm64`
        # *   `linux/386`
        # *   `linux/arm/v7`
        # *   `linux/arm/v6`
        # 
        # Default value: `linux/amd64`
        self.platforms = platforms  # type: list[str]
        # The name of the push that triggers the building rule.
        self.push_name = push_name  # type: str
        # The type of the push that triggers the building rule. Valid values:
        # 
        # *   `GIT_TAG`: tag push
        # *   `GIT_BRANCH`: branch push
        self.push_type = push_type  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoBuildRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class UpdateRepoBuildRuleResponseBody(TeaModel):
    def __init__(self, build_rule_id=None, code=None, is_success=None, request_id=None):
        # The ID of the building rule.
        self.build_rule_id = build_rule_id  # type: str
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoBuildRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoBuildRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRepoBuildRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRepoBuildRuleResponse, self).to_map()
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
            temp_model = UpdateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(self, auto_build=None, code_repo_id=None, code_repo_name=None, code_repo_namespace_name=None,
                 code_repo_type=None, disable_cache_build=None, instance_id=None, oversea_build=None, repo_id=None):
        # Specifies whether to enable automatic image building when code is committed. Valid values:
        # 
        # *   `true`: enables automatic image building when code is committed.
        # *   `false`: disables automatic image building when code is committed.
        self.auto_build = auto_build  # type: str
        # The ID of the source code repository.
        self.code_repo_id = code_repo_id  # type: str
        # The name of the source code repository.
        self.code_repo_name = code_repo_name  # type: str
        # The namespace to which the source code repository belongs.
        self.code_repo_namespace_name = code_repo_namespace_name  # type: str
        # The type of the source code hosting platform. Valid values: GITHUB, GITLAB, GITEE, CODE, and CODEUP.
        self.code_repo_type = code_repo_type  # type: str
        # Specifies whether to disable building caches. Valid values:
        # 
        # *   `true`: disables building caches.
        # *   `false`: enables building caches.
        self.disable_cache_build = disable_cache_build  # type: str
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id  # type: str
        # Specifies whether to enable Build With Servers Deployed Outside Chinese Mainland. Valid values:
        # 
        # *   `true`: enables Build With Servers Deployed Outside Chinese Mainland.
        # *   `false`: disables Build With Servers Deployed Outside Chinese Mainland.
        self.oversea_build = oversea_build  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoSourceCodeRepoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code_repo_id is not None:
            result['CodeRepoId'] = self.code_repo_id
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('CodeRepoId') is not None:
            self.code_repo_id = m.get('CodeRepoId')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class UpdateRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoSourceCodeRepoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoSourceCodeRepoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRepoSourceCodeRepoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRepoSourceCodeRepoResponse, self).to_map()
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
            temp_model = UpdateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoTriggerRequest(TeaModel):
    def __init__(self, instance_id=None, repo_id=None, trigger_id=None, trigger_name=None, trigger_tag=None,
                 trigger_type=None, trigger_url=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the image repository.
        self.repo_id = repo_id  # type: str
        # The ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger.
        # 
        # You can specify the TriggerName or TriggerUrl parameter. The TriggerName parameter is optional.
        self.trigger_name = trigger_name  # type: str
        # The image tag based on which the trigger is set.
        self.trigger_tag = trigger_tag  # type: str
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LISTTAG`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type  # type: str
        # The URL of the trigger.
        self.trigger_url = trigger_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        return self


class UpdateRepoTriggerResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        # The return value.
        self.code = code  # type: str
        # Indicates whether the request is successful.
        self.is_success = is_success  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepoTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRepoTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRepoTriggerResponse, self).to_map()
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
            temp_model = UpdateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryRequest(TeaModel):
    def __init__(self, detail=None, instance_id=None, repo_id=None, repo_name=None, repo_namespace_name=None,
                 repo_type=None, summary=None, tag_immutability=None):
        self.detail = detail  # type: str
        self.instance_id = instance_id  # type: str
        self.repo_id = repo_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace_name = repo_namespace_name  # type: str
        self.repo_type = repo_type  # type: str
        self.summary = summary  # type: str
        self.tag_immutability = tag_immutability  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class UpdateRepositoryResponseBody(TeaModel):
    def __init__(self, code=None, is_success=None, request_id=None):
        self.code = code  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


